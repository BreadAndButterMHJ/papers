# Optical RIS 辅助可见光隐蔽通信建模报告

## 1. 文献与报告目的

本文依据 Lei Qian、Fangqian Wu、Di Wang、Nuo Huang 和 Zhengyuan Xu 的论文 *Optical RIS-Aided Covert Visible Light Communications*（IEEE Transactions on Vehicular Technology, vol. 74, no. 7, 2025, pp. 11518-11523，DOI: 10.1109/TVT.2025.3545851）整理。报告的重点不是复述全文，而是回答：如何按照该文的思路，建立一个可计算、可优化、可扩展的可见光隐蔽通信模型。

论文的基本思想是：

1. 用镜面阵列 RIS（mRIS）调控反射路径，使反射光聚焦于合法用户 Bob；
2. 用液晶 RIS（LC-RIS）调控接收端的透射与放大增益；
3. 先让监测者 Willie 选择最有利于检测的 LC-RIS 参数，再在该最坏情形下优化 Alice、Bob 和 mRIS；
4. 用二元假设检验描述 Willie 的检测，用 KL 散度约束替代难以直接处理的检测错误概率约束。

因此，这是一种“最坏情形 Willie + RIS 信道重构 + 发射功率控制”的隐蔽通信建模框架。

## 2. 系统模型与参与者

室内 VLC 系统包含：

- Alice：安装于天花板的 LED 阵列，采用直流偏置强度调制/直接检测（IM/DD）；
- Bob：合法接收者，使用光电探测器（PD），其前方部署 LC-RIS；
- Willie：监测者，试图判断 Alice 是否正在向 Bob 发送信息，也使用带 LC-RIS 的 PD；
- mRIS：安装在墙面、由 $N_m$ 个可独立旋转镜面组成的二维镜面阵列。

每个镜面 $k$ 由滚转角 $\gamma_k$ 和偏航角 $\omega_k$ 控制：

$$
\boldsymbol\gamma=[\gamma_1,\ldots,\gamma_{N_m}]^{\mathsf T},\qquad
\boldsymbol\omega=[\omega_1,\ldots,\omega_{N_m}]^{\mathsf T}.
$$

在一个长度为 $N$ 的观测块内，Alice 发送光强序列 $\mathbf x=\{x[i]\}_{i=1}^{N}$。论文对光信号施加非负性、峰值光强和平均光强约束（论文式 (1)）：

$$
0\le x[i]\le A,\qquad \mathbb E[x[i]]=\xi P,
$$

其中 $A$ 是峰值光强，$P$ 是 Alice 的平均光强控制变量，$\xi\in[0,1]$ 是调光目标。这里的 $\xi$ 是调光系数，不应与文献中常用来表示“总检测错误概率”的符号混淆。

## 3. 光信道建模

### 3.1 统一的等效信道

对接收者 $j\in\{B,W\}$，定义论文中的等效电域信道增益

$$
g_j=h_j^{\mathrm{LC}}
\left(h_j^{\mathrm{LoS}}+\sum_{k=1}^{N_m}h_{j,k}^{\mathrm{mRIS}}\right).
$$

这个表达式把三部分物理机制串联起来：

- $h_j^{\mathrm{LoS}}$：Alice 到接收者的直射链路；
- $h_{j,k}^{\mathrm{mRIS}}$：Alice 经第 $k$ 个镜面反射到接收者的链路；
- $h_j^{\mathrm{LC}}$：接收者前端 LC-RIS 对入射光的透射/放大增益。

于是 Bob 和 Willie 的所有性能均可归结为 $g_B$ 与 $g_W$ 的对比。增强 $g_B$ 提升可靠通信速率，压低 $g_W$ 则提高隐蔽性。

### 3.2 LoS 信道

论文式 (6) 采用 Lambertian VLC 信道模型：

$$
h_j^{\mathrm{LoS}}=
\begin{cases}
\dfrac{(m+1)\varpi\mu T\vartheta a^2}
{2\pi d_j^2\sin^2(\psi_j^s)}
\cos^m(\phi_j^s)\cos(\psi_j^s),
&0\le \psi_j^s\le\psi_F,\\[6pt]
0,&\text{其他情形},
\end{cases}
$$

其中 $d_j$ 是 Alice 到接收端的距离，$m$ 是 Lambertian 阶数，$\phi_j^s$ 和 $\psi_j^s$ 分别为辐照角和入射角，$\psi_F$ 是 PD 的半视场角，$\mu$、$\varpi$、$T$、$\vartheta$ 和 $a$ 分别代表电光转换效率、PD 响应度、跨阻放大增益、PD 有效面积和透镜折射率。

### 3.3 mRIS 反射信道

论文把 mRIS 链路视为静态、频率平坦信道。第 $k$ 个镜面对接收者 $j$ 的贡献为（论文式 (7)）：

$$
h_{j,k}^{\mathrm{mRIS}}(\gamma_k,\omega_k)=
\begin{cases}
\dfrac{\rho(m+1)\varpi\mu T\vartheta a^2}
{2\pi(d_k^s)^2(d_j^k)^2\sin^2(\psi_j^k)}
dA_k\cos^m(\theta_k^s)\cos(\psi_k^s)
\cos(\theta_j^k)\cos(\psi_j^k),
&0\le\psi_j^k\le\psi_F,\\[6pt]
0,&\text{其他情形}.
\end{cases}
$$

其中 $\rho$ 为镜面反射系数，$d_k^s$ 和 $d_j^k$ 分别是 Alice-镜面和镜面-接收者距离，$dA_k$ 是镜面面积。镜面旋转角通过反射辐照角进入信道。例如论文式 (8) 给出

$$
\cos(\theta_j^k)=
\frac{x_k-x_j}{d_j^k}\sin\gamma_k\cos\omega_k+
\frac{y_k-y_j}{d_j^k}\cos\gamma_k\cos\omega_k+
\frac{z_k-z_j}{d_j^k}\sin\omega_k.
$$

这一步建立了“机械控制量 $\{\gamma_k,\omega_k\}$ - 光学几何 - 通信信道”的映射。

### 3.4 LC-RIS 接收增益

论文式 (9) 将 LC-RIS 增益分解为

$$
h_j^{\mathrm{LC}}=\zeta_j\delta_j,
$$

其中透射系数

$$
\zeta_j=\bigl(1-R_{\mathrm{in}}(\psi_j)\bigr)
\bigl(1-R_{\mathrm{out}}(\phi_j)\bigr)
$$

由进入和离开 LC-RIS 时的 Fresnel 反射率决定；放大系数为（论文式 (13)）

$$
\delta_j=\exp\!\left(
\frac{2\pi v_e\eta_j^3\Gamma}{\lambda\cos\psi_j}
\right).
$$

$\eta_j$ 是 LC-RIS 折射率，范围为 $\eta_1\le\eta_j\le\eta_2$；$v_e$ 是外加电压并由论文式 (14) 与 $\eta_j$ 关联；$\lambda$ 为波长，$\Gamma$ 为电光系数。实际复现时，应直接实现论文式 (10)-(14)，由 $\eta_j$ 计算 $v_e$、$R_{\mathrm{in}}$、$R_{\mathrm{out}}$，最终得到 $h_j^{\mathrm{LC}}$。

## 4. Bob 的通信模型

Bob 在第 $i$ 个信道使用上的接收信号为（论文式 (2)）

$$
y_B[i]=g_Bx[i]+n_B[i],\qquad
n_B[i]\sim\mathcal N(0,\sigma_B^2).
$$

论文采用 IM/DD 信道的一个可达速率下界（论文式 (20)）作为优化目标：

$$
R_B=\frac{1}{2}\log\!\left[
1+\frac{e\xi^2P^2(h_B^{\mathrm{LC}})^2}{2\pi\sigma_B^2}
\left(h_B^{\mathrm{LoS}}+
\sum_{k=1}^{N_m}h_{B,k}^{\mathrm{mRIS}}\right)^2
\right].
$$

若速率单位采用 bit/channel use，应明确实现为 $\log_2$；论文公式只写作 $\log$，复现代码应统一底数。该式说明 $R_B$ 随 $P$ 和 $g_B$ 单调增加。

## 5. Willie 的检测模型

### 5.1 二元假设检验

Willie 判断 Alice 是否发送信息：

$$
\begin{cases}
\mathcal H_0:y_W[i]=n_W[i],&\text{Alice 不发送};\\
\mathcal H_1:y_W[i]=g_Wx[i]+n_W[i],&\text{Alice 发送},
\end{cases}
$$

其中 $n_W[i]\sim\mathcal N(0,\sigma_W^2)$。论文用平均接收能量作为检测统计量（论文式 (4)）：

$$
\bar p_W=\frac{1}{N}\sum_{i=1}^{N}|y_W[i]|^2
\underset{\mathcal D_0}{\overset{\mathcal D_1}{\gtrless}}\Omega.
$$

假警概率和漏检概率分别为

$$
P_{\mathrm{FA}}=\Pr(\mathcal D_1|\mathcal H_0),\qquad
P_{\mathrm{MD}}=\Pr(\mathcal D_0|\mathcal H_1).
$$

论文假设 $\Pr(\mathcal H_0)=\Pr(\mathcal H_1)=1/2$，故贝叶斯检测错误概率为

$$
P_e=\frac12(P_{\mathrm{FA}}+P_{\mathrm{MD}}).
$$

隐蔽性要求定义为

$$
P_{\mathrm{FA}}+P_{\mathrm{MD}}\ge1-\epsilon,
$$

其中 $\epsilon$ 越小，要求越严格。注意：在该定义下，完全随机猜测时 $P_{\mathrm{FA}}+P_{\mathrm{MD}}=1$，而 $P_e=1/2$。

### 5.2 从检测错误概率到 KL 散度约束

直接求最优阈值 $\Omega$ 下的 $P_{\mathrm{FA}}$ 和 $P_{\mathrm{MD}}$ 较困难。论文利用

$$
P_e=\frac12\left[1-V_T(p_1(\mathbf y_W),p_0(\mathbf y_W))\right]
$$

以及 Pinsker 不等式，将隐蔽性转成一个充分条件。对 $N$ 个独立同分布观测，得到论文式 (21)：

$$
D\bigl(p_1(y_W)\Vert p_0(y_W)\bigr)
\le \frac{2\epsilon^2}{N\ln2}.
$$

这里的 $D(p_1\Vert p_0)$ 是单次观测在 $\mathcal H_1$ 与 $\mathcal H_0$ 下分布的 KL 散度。$N$ 出现在分母，体现了“Willie 观察得越久，Alice 必须发得越弱”的平方根律趋势。

论文进一步用相对熵链式法则和熵功率不等式给出 KL 散度上界（论文式 (18)）。令

$$
s_W=g_W\xi P,
$$

则

$$
D(p_1\Vert p_0)
\le
\frac{(4\pi-e)s_W^2}{4\pi\sigma_W^2\ln2}
+\frac{e^2s_W^4}{16\pi^2\sigma_W^4\ln2}.
$$

这是全文最关键的建模桥梁：隐蔽性最终只由 Willie 端的有效信号幅度 $g_W\xi P$、噪声 $\sigma_W^2$、观测长度 $N$ 和隐蔽参数 $\epsilon$ 决定。

## 6. 最坏情形 Willie 建模

Willie 会利用自己的 LC-RIS 增强检测。论文先求

$$
\min_{\eta_W}P_e,
\qquad \eta_1\le\eta_W\le\eta_2.
$$

由于 KL 上界随 $g_W$ 单调增加，上述问题等价为（论文 OP1-1）

$$
\max_{\eta_W}
h_W^{\mathrm{LC}}
\left(h_W^{\mathrm{LoS}}+
\sum_{k=1}^{N_m}h_{W,k}^{\mathrm{mRIS}}\right).
$$

论文假设 mRIS 完全由 Alice 控制并且不向 Willie 提供反射增益，即

$$
h_{W,k}^{\mathrm{mRIS}}=0,\quad \forall k.
$$

于是只需在 $[\eta_1,\eta_2]$ 内优化 $h_W^{\mathrm{LC}}h_W^{\mathrm{LoS}}$，得到 $\eta_W^*$ 和 $h_W^{\mathrm{LC},*}$。系统随后在这一最强检测配置下满足 KL 约束。这相当于一个“先攻击、后防御”的鲁棒/Stackelberg 建模思路。

## 7. 系统级联合优化

论文的系统问题 OP2 可写为

$$
\begin{aligned}
\max_{\eta_B,\boldsymbol\gamma,\boldsymbol\omega,P}\quad
&R_B(\eta_B,\boldsymbol\gamma,\boldsymbol\omega,P)\\
\text{s.t.}\quad
&D^*(p_1\Vert p_0)\le\frac{2\epsilon^2}{N\ln2},\\
&\eta_1\le\eta_B\le\eta_2,\\
&-\frac\pi2\le\gamma_k,\omega_k\le\frac\pi2,\quad \forall k.
\end{aligned}
$$

$D^*$ 表示 Willie 采用 $\eta_W^*$ 时的散度。论文采用分步解耦，而不是直接处理所有耦合变量。

### 7.1 mRIS 指向优化

论文把镜面角度改写为接收平面上的反射光斑位置 $\mathbf Q=[x_q,y_q,z_q]^{\mathsf T}$。依据反射定律，第 $k$ 个镜面朝向 $\mathbf Q$ 时的单位法向量为（论文式 (25)）

$$
\widehat{\mathbf N}_k(\mathbf Q)=
\frac{
\dfrac{\mathbf S-\mathbf R_k}{\|\mathbf S-\mathbf R_k\|_2}+
\dfrac{\mathbf Q-\mathbf R_k}{\|\mathbf Q-\mathbf R_k\|_2}}
{\left\|
\dfrac{\mathbf S-\mathbf R_k}{\|\mathbf S-\mathbf R_k\|_2}+
\dfrac{\mathbf Q-\mathbf R_k}{\|\mathbf Q-\mathbf R_k\|_2}
\right\|_2},
$$

其中 $\mathbf S$ 和 $\mathbf R_k$ 分别是 Alice 和镜面中心位置。再由论文式 (24) 将法向量映射为 $\omega_k$ 与 $\gamma_k$。在论文“mRIS 不照射 Willie”的假设下，最优光斑位置直接取 Bob 的位置：

$$
\mathbf Q^*=\mathbf q_B.
$$

### 7.2 发射功率优化

将 KL 上界代入隐蔽性约束，可得到平均光强上界（论文式 (29)）：

$$
P\le P^*=
\left[
\frac{
2\pi\sigma_W^2(4\pi-e)
\left(\sqrt{1+\dfrac{8\epsilon^2e^2}{N(4\pi-e)^2}}-1\right)}
{\xi^2e^2(h_W^{\mathrm{LC},*})^2
\left(h_W^{\mathrm{LoS}}+\sum_{k=1}^{N_m}h_{W,k}^{\mathrm{mRIS}}\right)^2}
\right]^{1/2}.
$$

由于 $R_B$ 随 $P$ 单调增加，论文取 $P=P^*$。从式中可以直接读出：

- Willie 信道越强，允许功率越小；
- Willie 噪声越大，允许功率越大；
- $\epsilon$ 越小或 $N$ 越大，允许功率越小；
- 在小 $\epsilon$ 区域，对根式作一阶展开可得 $P^*\propto\epsilon/\sqrt N$；在低信噪比下，论文的速率下界相应近似按 $1/N$ 缩放。

### 7.3 Bob 的 LC-RIS 优化

最后，在 $P^*$、$\boldsymbol\gamma^*$ 和 $\boldsymbol\omega^*$ 已知时求

$$
\max_{\eta_B\in[\eta_1,\eta_2]}h_B^{\mathrm{LC}}(\eta_B),
$$

等价于最大化 Bob 的有效信道增益。论文用梯度下降在约 10-30 次迭代内收敛。

## 8. 可直接复用的建模流程

针对新的 RIS-VLC 隐蔽通信课题，可以采用以下顺序：

1. **定义几何和控制变量**：给出 Alice、Bob、Willie、每个镜面的三维坐标；定义 $P$、$\eta_B$、$\eta_W$、$\gamma_k$、$\omega_k$。
2. **建立物理信道**：分别计算 LoS、每个 mRIS 反射链路和 LC-RIS 接收增益，再合成为 $g_B$、$g_W$。
3. **建立通信链路**：写出 $y_B=g_Bx+n_B$，选择适合 IM/DD 输入约束的速率下界或有限码长速率。
4. **建立检测链路**：写出 $\mathcal H_0$ 与 $\mathcal H_1$，明确 Willie 知道哪些参数、观测多少样本、采用何种检测器。
5. **选定隐蔽性指标**：可用 $P_{\mathrm{FA}}+P_{\mathrm{MD}}\ge1-\epsilon$；若难以直接求解，则用 KL 散度充分条件。
6. **先优化 Willie**：对 Willie 的位置、LC-RIS、阈值和可能的 CSI 误差求最强检测能力，形成最坏情形约束。
7. **再优化系统**：最大化 Bob 速率或隐蔽吞吐量，约束包括隐蔽性、非负光强、峰均光强、照明、RIS 角度/电压和 QoS。
8. **数值验证**：同时报告 Bob 速率、Willie 的实际最优检测错误率和 KL 上界，不能只验证代理约束。

对应的计算流程可概括为：

```text
输入几何、光学参数、N、epsilon
  -> 计算 hLoS_B 和 hLoS_W
  -> 在 [eta1, eta2] 搜索 Willie 的 etaW*，得到 hLC_W*
  -> 将每个镜面的光斑指向 Bob，得到 gamma*、omega*
  -> 由 KL 约束计算 P*
  -> 结合峰值/照明约束修正可用功率
  -> 在 [eta1, eta2] 搜索 Bob 的 etaB*
  -> 计算 RB，并用实际检测器复核 P_FA + P_MD
```

## 9. 论文结果给出的设计认识

论文在 $5\times5\times5\,\mathrm{m}^3$ 房间内仿真，Alice 位于天花板中心。主要参数包括：PD 视场角 $80^\circ$、$\xi=1$、峰值光强 $A=140\,\mathrm{mA}$、PD 面积 $1\,\mathrm{cm}^2$、LC-RIS 折射率范围 $[1.5,1.7]$、PD 响应度 $0.54\,\mathrm{A/W}$、镜面反射系数 $0.9$。

文章的主要数值结论是：

- Willie 配备优化 LC-RIS 后，检测能力增强，Alice 必须降低功率，因此速率可能低于无 RIS 基准；
- 仅有少量镜面（文中示例 $N_m=25$）时，mRIS 未必足以抵消 Willie 的 LC-RIS 优势；
- 增加镜面数量（文中示例 $N_m=225$）可改善 Bob 信道，但给 Bob 部署优化 LC-RIS 的收益更显著；
- 联合优化 mRIS 和 Bob 的 LC-RIS 性能最好；
- $\epsilon$ 越大，隐蔽约束越宽松，$R_B$ 越高；$N$ 越大，Willie 积累的检测证据越多，$R_B$ 越低；
- 波长增大时 LC-RIS 增益下降，但 Willie 增益的下降允许 Alice 提高隐蔽功率，论文场景下总体速率反而上升。

## 10. 复现与扩展时必须注意的问题

### 10.1 论文最关键、也最强的假设

论文直接令 $h_{W,k}^{\mathrm{mRIS}}=0$。这使 mRIS 角度不再影响隐蔽约束，光斑指向 Bob 就成为显然最优解。如果镜面存在旁瓣、有限光斑、表面散射、指向误差，或 Willie 靠近 Bob，则 $h_{W,k}^{\mathrm{mRIS}}>0$，此时必须联合优化 Bob 增益与 Willie 泄漏：

$$
\max_{\boldsymbol\gamma,\boldsymbol\omega} R_B
\quad\text{s.t.}\quad
D\bigl(g_W(\boldsymbol\gamma,\boldsymbol\omega),P\bigr)
\le\frac{2\epsilon^2}{N\ln2}.
$$

这比原论文更适合真实系统。

### 10.2 功率上界还应与峰值约束取交集

由 $0\le x[i]\le A$ 和 $\mathbb E[x[i]]=\xi P$ 至少有 $\xi P\le A$。因此工程实现不应只取论文的 $P^*$，而应使用

$$
P_{\mathrm{use}}=\min\left(P^*,\frac{A}{\xi},P_{\mathrm{illum}},P_{\mathrm{hardware}}\right),
$$

其中后两项可分别表示照明与硬件约束。论文 OP2 没有显式重列这一交集，复现时需要补上。

### 10.3 KL 约束是充分条件，不是实际检测性能本身

Pinsker 不等式和论文式 (18) 的 KL 上界都可能偏保守。建议仿真时另外实现 Willie 的似然比检验或能量检测，数值计算最优阈值，直接验证

$$
P_{\mathrm{FA}}+P_{\mathrm{MD}}\ge1-\epsilon.
$$

这样可以量化“理论保证”和“实际检测错误率”之间的松弛程度。

### 10.4 梯度算法的曲率需在代码中重新核验

论文称 OP1-1 与 OP2-5 为凸问题并用梯度下降求解。但标准凸优化中，最大化问题通常要求目标为凹函数；若目标确为凸函数，则最大化凸函数不属于标准凸优化。由于 $\eta_W$ 和 $\eta_B$ 都只是一维有界变量，最稳妥的复现方法是先用高密度网格或有界全局搜索得到基准，再核对二阶导数和梯度算法结果。

### 10.5 噪声与 CSI 模型较理想化

论文使用与信号无关的 AWGN。实际 VLC 常含背景光噪声和信号相关散粒噪声；若 $\mathcal H_0$、$\mathcal H_1$ 下方差不同，KL 散度、最优阈值和功率闭式解都需重推。此外，论文默认位置、入射角和信道状态已知。更稳健的模型可写成

$$
\max R_B\quad
\text{s.t.}\quad
\sup_{\mathbf q_W\in\mathcal W,\,\Delta\mathbf h\in\mathcal U}
D(p_1\Vert p_0)
\le\frac{2\epsilon^2}{N\ln2},
$$

其中 $\mathcal W$ 是 Willie 的可能位置区域，$\mathcal U$ 是 CSI 不确定集合。

### 10.6 隐蔽性不等于保密性

该模型主要保证 Willie 难以判断“是否存在通信”，但不自动保证消息在被发现后仍无法解码。若课题同时要求内容保密，应增加保密速率、加密或人工噪声等约束。

## 11. 推荐的后续研究模型

在忠实保留本文核心框架的基础上，一个更完整的研究问题可设置为：

$$
\begin{aligned}
\max_{P,\eta_B,\boldsymbol\gamma,\boldsymbol\omega}\quad
&R_B\\
\text{s.t.}\quad
&\sup_{\eta_W,\mathbf q_W,\Delta\mathbf h}
D(p_1\Vert p_0)\le\frac{2\epsilon^2}{N\ln2},\\
&0\le x[i]\le A,\quad \mathbb E[x[i]]=\xi P,\\
&E_{\min}\le E_{\mathrm{illum}}\le E_{\max},\\
&\eta_1\le\eta_B,\eta_W\le\eta_2,\\
&-\pi/2\le\gamma_k,\omega_k\le\pi/2.
\end{aligned}
$$

与原论文相比，这一模型增加了 Willie 位置/CSI 不确定性、峰均功率与照明约束，并允许 mRIS 对 Willie 存在非零泄漏。求解上可继续采用分块交替优化：外层更新 mRIS 和 Bob 的 LC-RIS，内层求最坏 Willie，功率块利用 KL 约束的一维单调性通过二分法求解。

## 12. 总结

这篇论文给出的隐蔽通信建模范式可以浓缩为：

> 先用光学几何得到 Bob/Willie 的等效信道，再把 Willie 的检测写成二元假设检验，用 KL 散度充分条件把不可检测性变成发射功率约束，最后在最强 Willie 条件下联合优化 RIS 与功率。

其中最值得直接借鉴的是“最坏情形监测者 + KL 散度约束 + 分步解耦”三层结构；最需要谨慎处理的是 mRIS 对 Willie 零泄漏、理想 AWGN、完美 CSI，以及论文闭式功率与原始峰值/照明约束之间的衔接。

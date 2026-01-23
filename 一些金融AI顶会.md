# AI & 金融交叉领域顶级会议清单

这份清单为算法团队梳理了“人工智能+金融科技”领域的核心会议，涵盖了从垂直应用到底层理论的重点关注对象。

## 1. 核心垂直顶会 (The Must-Attend)

最直接针对金融场景的跨学科会议，学术界与顶级金融机构（JPM, BlackRock等）的交汇点。

* **ICAIF (ACM International Conference on AI in Finance)**
* **简介**：目前全球最权威的 AI+金融 垂直会议。
* **关注点**：深度强化学习（做市/交易）、金融大模型（FinLLM）、合成数据、多智能体市场模拟。
* **备注**：**2025年将于11月在新加坡举办**，是近期最高价值的线下交流机会。

* **IEEE CIFEr (Conference on Computational Intelligence for Financial Engineering & Economics)**
* **简介**：侧重于计算智能在金融工程中的应用，IEEE 计算智能协会主办。
* **关注点**：演化计算、模糊系统在衍生品定价、风险管理中的应用。

## 2. 数据挖掘与应用顶会 (Industrial Applications)

金融业务（风控、营销、反欺诈）高度依赖结构化数据和图数据，此类会议实战价值极高。

* **KDD (ACM SIGKDD)**
* **简介**：数据挖掘领域的最高峰，工业界影响力极大。
* **关注点**：**ADS Track (应用赛道)** 是宝藏，常包含反欺诈（GNN）、信用评分、异常检测等落地案例。

* **ICDM (IEEE International Conference on Data Mining)**
* **简介**：仅次于 KDD 的数据挖掘顶会，偏重算法的实际效果。
* **关注点**：金融时序数据挖掘、高维稀疏数据处理。

## 3. 通用 AI 顶会 (General AI & Theory)

关注这些会议中的特定 Workshop 或 Track，寻找底层技术突破。

* **AAAI / IJCAI**
* **简介**：老牌综合性 AI 顶会。
* **关注点**：常设 **"AI for Financial Services"** 研讨会。重点关注可解释性 AI (XAI) 和因果推断（Causal Inference），解决金融合规黑盒问题。

* **NeurIPS / ICML / ICLR**
* **简介**：机器学习理论的三大顶会。
* **关注点**：关注 **Time Series**（时序预测 SOTA）和 **Reinforcement Learning**（离线强化学习）相关的 Workshop，用于量化交易策略开发。

## 4. NLP 领域顶会 (Financial Text Analysis)

适用于金融舆情监控、研报自动化处理等场景。

* **ACL / EMNLP**
* **简介**：自然语言处理领域的两大顶会。
* **关注点**：金融情感分析（Sentiment Analysis）、事件抽取、长文本（研报）摘要生成、领域知识图谱构建。

---

### 💡 调研建议 (For Algorithm Team)

* **落地找 KDD**：如果团队面临具体的工程落地问题（如反洗钱图谱构建），首选查阅 KDD 的论文。
* **前沿找 ICAIF**：如果需要了解同行（尤其是华尔街投行）在做什么，重点关注 ICAIF。
* **模型找 NeurIPS**：如果需要改进时序预测的基础架构（如 Transformer 变体），请深挖 NeurIPS/ICLR。

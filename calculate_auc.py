"""计算二分类 ROC-AUC，无需安装第三方库。"""

import math


def calculate_auc(y_true, y_score):
    """标签为 0/1，分数越高表示越可能是正样本；同分计 0.5。"""
    y_true, y_score = list(y_true), list(y_score)
    if len(y_true) != len(y_score):
        raise ValueError("标签和预测分数的数量必须一致")
    if any(label not in (0, 1) for label in y_true):
        raise ValueError("真实标签只能是 0 或 1")
    scores = [float(score) for score in y_score]
    if any(not math.isfinite(score) for score in scores):
        raise ValueError("预测分数不能包含 NaN 或无穷大")

    n_pos = sum(y_true)
    n_neg = len(y_true) - n_pos
    if n_pos == 0 or n_neg == 0:
        raise ValueError("计算 AUC 必须同时有正样本和负样本")

    # 从低分到高分排列，把分数相同的样本作为一组。
    samples = sorted(zip(scores, y_true))
    neg_before = 0
    correct_pairs = 0.0
    i = 0
    while i < len(samples):
        j = i
        group_pos = 0
        while j < len(samples) and samples[j][0] == samples[i][0]:
            group_pos += samples[j][1]
            j += 1
        group_neg = j - i - group_pos

        # 正样本胜过所有更低分的负样本，与同分负样本各计半次。
        correct_pairs += group_pos * (neg_before + 0.5 * group_neg)
        neg_before += group_neg
        i = j

    return correct_pairs / (n_pos * n_neg)


if __name__ == "__main__":
    labels = [1, 0, 1, 0]
    predictions = [0.8, 0.6, 0.4, 0.2]
    print(f"AUC = {calculate_auc(labels, predictions):.4f}")

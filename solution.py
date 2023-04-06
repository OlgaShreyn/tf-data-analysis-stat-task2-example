import pandas as pd
import numpy as np

from scipy.stats import norm, chi2


chat_id = 368780632 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    sum = (x**2).sum()
    left = np.sqrt(sum / (11 * chi2.ppf(1 - alpha / 2, n * 2)))
    right = np.sqrt(sum / (11 * chi2.ppf(alpha / 2, n * 2)))
    return left, right

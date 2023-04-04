import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 368780632 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    size = len(x)
    left = np.sqrt(size * (x ** 2).mean() / (11 * chi2.ppf(q=1 - alpha / 2, df=size)))
    right = np.sqrt(size * (x ** 2).mean() / (11 * chi2.ppf(q=alpha / 2, df=size)))
    return (left, right)

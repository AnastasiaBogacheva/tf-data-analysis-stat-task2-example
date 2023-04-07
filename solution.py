import pandas as pd
import numpy as np
from scipy.stats import gamma

chat_id = 694882183 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    n = len(x)
    c = 2/(n*44*44)
    l = np.sum(x)-n/2
    z1 = gamma.ppf(alpha/2,n, loc = l)
    z2 = gamma.ppf(1-alpha/2,n, loc = l)
    return (c*z1,c*z2)

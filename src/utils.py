from __future__ import annotations
import numpy as np
import pandas as pd

def softmax(v: np.ndarray, beta: float = 1.0) -> np.ndarray:
    z = beta * (v - np.max(v))
    e = np.exp(z)
    return e / e.sum()

def mnl_choice_probs(U: np.ndarray, beta: float = 1.0) -> np.ndarray:
    Uc = U - U.max(axis=1, keepdims=True)
    P = np.exp(beta * Uc)
    return P / P.sum(axis=1, keepdims=True)

def share(y: np.ndarray, J: int) -> np.ndarray:
    counts = np.bincount(y, minlength=J)
    return counts / counts.sum()

def standardize(df: pd.DataFrame, cols: list[str]) -> pd.DataFrame:
    out = df.copy()
    for c in cols:
        mu, sd = out[c].mean(), out[c].std(ddof=0)
        out[c + "_z"] = (out[c] - mu) / (sd if sd != 0 else 1.0)
    return out

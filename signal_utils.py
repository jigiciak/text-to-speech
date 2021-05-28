import numpy as np


def gen_impulse(fs, f0, duration=2):
    N = fs * duration  # sample count
    P = int(f0) * 2  # period
    D = 1  # width of pulse
    pulse = np.arange(N) % P < D

    return pulse


def klatt_filter(s, fs, f):
    T = 1 / fs
    BW = 100  # dobrane a priori
    C = -np.exp(-2 * np.pi * BW * T)
    B = 2 * np.exp(-np.pi * BW * T) * np.cos(2 * np.pi * f * T)
    A = 1 - B - C
    y = []

    sample_1 = 0
    sample_2 = 0
    for i, sample in enumerate(s):
        y.append(A * sample + B * sample_1 + C * sample_2)
        sample_2 = sample_1
        sample_1 = y[i]
    return y
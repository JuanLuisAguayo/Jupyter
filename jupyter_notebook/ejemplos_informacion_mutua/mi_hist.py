import numpy as np

def mutual_information_hist(x, y, bins=20):
    joint_hist = np.histogram2d(x, y, bins)[0]
    joint_prob = joint_hist / np.sum(joint_hist)

    px = np.sum(joint_prob, axis=1)
    py = np.sum(joint_prob, axis=0)

    nz = joint_prob > 0
    mi = np.sum(joint_prob[nz] * np.log(joint_prob[nz] / (px[:, None] * py)[nz]))
    return mi

np.random.seed(5)
x = np.random.randn(500)
y = 2 * x + np.random.randn(500)

print("MI (histogramas):", mutual_information_hist(x, y))

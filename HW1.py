from matplotlib import pyplot as plt
import numpy as np
from scipy.constants import R


Xb = np.linspace(0, 1, 100)
epsilon = 1e-10


def dS_mix(Xb):
    dS = -R * ((Xb + epsilon) * np.log(Xb + epsilon) + (1 - (Xb + epsilon)) * np.log(1 - (Xb - epsilon)))
    return dS


def dH_mix_regular(Xb, alpha):
    dH = alpha * Xb * (1 - Xb)
    return dH


def dH_mix_sub(Xb, alpha_1, alpha_2):
    dH = Xb * (1 - Xb) * (alpha_1 * Xb + alpha_2 * (1 - Xb))
    return dH

def plot1():
    alpha_n = -1000
    alpha_p = 1000
    T = 500 #K

    x = Xb

    H_n = dH_mix_regular(Xb, alpha_n)
    H_p = dH_mix_regular(Xb, alpha_p)
    S = dS_mix(Xb)
    G_n = H_n - T * S
    G_p = H_p - T * S

    fig, axes = plt.subplots(1, 1, figsize=(7, 8), facecolor='w')
    axes.plot(x, G_n, c='r', marker=',')
    axes.plot(x, G_p, c='b', marker=',')
    # axes.plot(x, H, c='g', marker=',')
    # axes.plot(x, S, c='b', marker=',')
    axes.set_title(r'$\Delta G_{mix}$ vs $X_B$ with different $\alpha$')
    plt.legend([fr'$\alpha $ < 0', fr'$\alpha $ > 0'], loc='upper right')
    plt.axis([-0, 1, -3500, 500])
    axes.set_xlabel("$X_B$")
    axes.set_ylabel("$\Delta G_{mix}$")
    # plt.show()
    filename = f'HW1_q4_a'
    plt.savefig(filename + ".jpg")


def plot2():
    alpha_p = 1000
    T1 = 500 #K
    T2 = T1 + 250
    T3 = T2 + 250

    x = Xb
    H_p = dH_mix_regular(Xb, alpha_p)
    S = dS_mix(Xb)
    G_500 = H_p - T1 * S
    G_750 = H_p - T2 * S
    G_1000 = H_p - T3 * S

    fig, axes = plt.subplots(1, 1, figsize=(7, 8), facecolor='w')
    axes.plot(x, G_500, c='r', marker=',')
    axes.plot(x, G_750, c='g', marker=',')
    axes.plot(x, G_1000, c='b', marker=',')
    # axes.plot(x, H, c='g', marker=',')
    # axes.plot(x, S, c='b', marker=',')
    axes.set_title(r'$\Delta G_{mix}$ vs $X_B$ with different Temperature')
    plt.legend([fr'T = {T1}K', fr'T = {T2}K', fr'T = {T3}K'], loc='upper right')
    plt.axis([-0, 1, -6000, 1000])
    axes.set_xlabel("$X_B$")
    axes.set_ylabel("$\Delta G_{mix}$")
    # plt.show()
    filename = f'HW1_q4_b'
    plt.savefig(filename + ".jpg")

def plot3():
    alpha_1 = 5000
    alpha_2 = 0
    alpha_3 = -5000
    T = 500 #K

    x = Xb

    H1 = dH_mix_sub(Xb, alpha_1, alpha_1)
    H2 = dH_mix_sub(Xb, alpha_1, alpha_3)
    H3 = dH_mix_sub(Xb, alpha_1, alpha_2)
    S = dS_mix(Xb)
    G1 = H1 - T * S
    G2 = H2 - T * S
    G3 = H3 - T * S

    fig, axes = plt.subplots(1, 1, figsize=(7, 8), facecolor='w')
    axes.plot(x, G1, c='r', marker=',')
    axes.plot(x, G2, c='g', marker=',')
    axes.plot(x, G3, c='b', marker=',')
    axes.set_title(r'$\Delta G_{mix}$ vs $X_B$ with different $\alpha_{1}$ and $\alpha_{2}$')
    plt.legend([r'$\alpha_{1} = \alpha_{2} = 5000$', r'$\alpha_{1} = 5000, \alpha_{2} = -5000$',r'$\alpha_{1} = 5000, \alpha_{2} = 0$'], loc='upper right')
    plt.axis([-0, 1, -3500, 500])
    axes.set_xlabel("$X_B$")
    axes.set_ylabel("$\Delta G_{mix}$")
    plt.show()
    filename = f'HW1_q5'
    plt.savefig(filename + ".jpg")


if __name__ == "__main__":
    plot1()
    plot2()
    plot3()
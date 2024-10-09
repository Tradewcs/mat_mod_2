import numpy as np
import os
import matplotlib.pyplot as plt

def F(N, a, b):
    return (a * N*N) / (b + N*N*N)

def FF(N, a, b):
    return F(F(N, a, b), a, b) - N


def plot(N_0, n, a, b):
    N = np.zeros(n)
    N[0] = N_0

    for t in range(1, n):
        N[t] = F(N[t-1], a, b)
    
    plt.plot(N, label=f'a={a}, b={b}')

    plt.xlabel('t')
    plt.ylabel('N_t')
    plt.legend()
    plt.grid(True)
    
    if not os.path.exists('static'):
        os.makedirs('static')

    plt.savefig('static/plot.png')
    plt.close()

def get_stationary_points(a, b):
    delta = b*b/4 - a*a*a/27
    if delta < 0:
        phi = np.arctan(np.sqrt(-delta) / (-b / 2)) + np.pi

        y1 = 2 * np.sqrt(a / 3) * np.cos(phi / 3)
        y2 = 2 * np.sqrt(a / 3) * np.cos(phi / 3 + 2 * np.pi / 3)
        y3 = 2 * np.sqrt(a / 3) * np.cos(phi / 3 + 4 * np.pi / 3)
    
        return [y for y in [y1, y2, y3] if y > 0]
    elif delta == 0:
        y1 = 2 * np.sqrt(a / 3) * np.cos(np.pi / 3)
    
        return [y1]

    return []

def is_stable(N, a, b):
    derivative = (a * N * ( 2*b - N*N*N )) / (b + N*N*N)**2

    return np.abs(derivative) < 1

if __name__ == "__main__":
    a = 3
    b = 2

    print(get_stationary_points(a, b))
    # print(is_stable(get_stationary_points(a, b)[1], a, b))
    # print(find_period_2(a, b))
    # plot(1.53209, 20, a, b)
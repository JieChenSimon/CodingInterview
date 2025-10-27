import numpy as np

def gradient_descent(f, bounds, lr = 0.01, max_iter=1000, eps_value=1e-6):
    (a, c), (b, d) = bounds
    x = np.array([(a + b) / 2, (c + d) / 2])
    for i in range(max_iter):
        y, grad = f(x)
        grad_norm = np.linalg.norm(grad)
        if grad_norm < eps_value:
            break
        x_new  = x - lr * grad
        x_new[0] = np.clip(x_new[0], a, b)
        x_new[1] = np.clip(x_new[1], c, d)

        if np.linalg.norm(x_new - x) < eps_value:
            break
        x = x_new
        y = f(x)
    return x, y



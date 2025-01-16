import mlx
import mlx.core as mx

num_features = 100
num_examples = 1_000
num_iters = 10_000  # iterations of SGD
lr = 0.01  # learning rate for SGD

w_star = mx.random.normal((num_features,))

# Input examples (design matrix)
X = mx.random.normal((num_examples, num_features))

# Noisy labels
eps = 1e-2 * mx.random.normal((num_examples,))
y = X @ w_star + eps

print(y)
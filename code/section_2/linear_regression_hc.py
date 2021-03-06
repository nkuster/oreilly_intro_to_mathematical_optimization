import pandas as pd
from random import uniform, normalvariate, randint
import numpy as np

# Generate random data around y = 4x + 50
def f(x):
    return 4 * x + 50

data = pd.DataFrame(columns=["x", "y"])

for i in range(1000):
    x = round(uniform(1, 20), 2)
    data = data.append(pd.DataFrame(columns=["x", "y"], data=[[x, round(f(x) + normalvariate(0, 50), 2)]]))

# Input data
X = data.iloc[:, 0]
Y = data.iloc[:, 1]

# Building the model
m = 0.0
b = 0.0


epochs = 200000  # The number of iterations to perform

n = float(len(X))  # Number of elements in X


best_loss = 10000000000000.0  # Initialize with a really large value

for i in range(epochs):

    # Randomly adjust "m" or "b"

    m_adjust = np.random.standard_t(3, 1)[0] #or use normalvariate(0, 1)
    b_adjust = np.random.standard_t(3, 1)[0] #or use normalvariate(0, 1)

    m += m_adjust
    b += b_adjust

    # Calculate loss, which is total mean squared error
    new_loss = (1 / n) * sum((Y - (m * X + b))**2 )

    # If loss has improved, keep new values. Otherwise revert.
    if new_loss < best_loss:
        best_loss = new_loss
    else:
        m -= m_adjust
        b -= b_adjust

    if i % 1000 == 0:
        print(m, b)

print(m, b)

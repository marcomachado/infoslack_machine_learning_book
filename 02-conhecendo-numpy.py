# %%
import numpy as np

# %%
a1 = np.array([1,2,3])

a2 = np.array([
    [4,5,6],
    [7,8,9]
])

a3 = np.array([
    [[1,2,3],
    [4,5,6],
    [7,8,9]],
    [[10,11,12],
     [13,14,15],
     [16,17,18]]
])
# %%
print(a1.shape)
print(a2.shape)
print(a3.shape)
# %%

print(a1.ndim, a2.ndim, a3.ndim)
# %%
print(a1.size, a2.size, a3.size)

# %%
print(type(a1), type(a2), type(a3))
# %%
array_simples = np.array([1, 2, 3])
array_simples

# %%
np.ones(10)

# %%
ones = np.ones((10,2))
ones
# %%
zeros = np.zeros((4, 4, 3))
zeros
# %%
# Start, Stop e Step
range_a1 = np.arange(0, 10, 2)
range_a1
# %%
random_1 = np.random.randint(10, size=(5,3))
random_1
# %%
np.random.randint(2, 10, size=(5,3))
# %%
np.random.seed(42)
random_2 = np.random.random((5, 3))
random_2
# %%
print(a1[0])
print(a2[0])
print(a3[0])
# %%
print(a2[0,0])
print(a3[:2, :2, :2])
# %%
print(a1)

ones = np.ones(3)
print(ones)
# %%
a1 + ones
# %%
a1 * ones
# %%
a1 / ones

# %%
a2 // a1

# %%
a2 / a1

# %%
a1 ** 2


# %%
np.square(a1)
# %%
print(a1 % 2)
print(np.log(a1))
print(np.exp(a1))

# %%
sum(a1)

# %%
grande_array = np.random.random(1000000)
grande_array.size

%timeit sum(grande_array)       # Python sum()
%timeit np.sum(grande_array)  # NumPy np.sum()
# %%
# Reshaping e Transpose
print(a2)
print('\n------')
print(a3)
print('\n------')
print(a2.reshape(2,3,1))
print('\n------')
a2.reshape(2, 3, 1) + a3

# %%
print(a2)
print('\n------')
print(a2.T)
print('\n------')
print(a2.shape)
print('\n------')
print(a2.T.shape)
# %%
a1 > a2

# %%
a1 <= a2

# %%
a1 > 5

# %%
a1 == a2

# %%
print(random_1)
print('\n------')
print(np.sort(random_1))
# %%

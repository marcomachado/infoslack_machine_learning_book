# %%
import numpy as np
# %%
vetor = np.array([4,5,6])
matrix = np.array([
    [1,2,3],
    [3,2,1],
    [2,2,2]
])
matrix_3d = np.array([[
    [[1,2,3],
    [4,5,6],
    [4,5,6]],
    [[1,1,1],
    [2,2,2],
    [3,3,3]],
    [[9,9,9],
    [4,4,4],
    [8,5,2]]
]])
# %%
print(vetor, matrix, matrix_3d)
print('\n ------')
print(vetor.ndim, matrix.ndim, matrix_3d.ndim)
print('\n ------')
print(type(vetor), type(matrix), type(matrix_3d))
print('\n ------')
print(vetor.size, matrix.size, matrix_3d.size)
# %%
np.ones(shape=(10,2))
# %%
np.ones(shape=(5,4,3))
# %%
np.random.randint(0, 10, 3)
# %%
np.random.randint(0, 10, size=(7,2))
# %%
np.random.seed(42)
np.random.random(size=(5,3))
# %%
print(matrix_3d)
print('\n ----')
print(matrix_3d[0][0][0][0])
print(matrix_3d[0][0][0])
print(matrix_3d[0][0][0][:2])
# %%
ones = np.ones(shape=(3,5))
print(ones)
print('\n ----')
new_matrix = np.random.randint(0, 10, 5) - ones
print(new_matrix)
# %%
print(np.mean(new_matrix))
# %%
print(new_matrix)
print('\n ----')
print(new_matrix.T)
print('\n ----')
print(new_matrix.shape)
print('\n ----')
print(new_matrix.T.shape)
# %%

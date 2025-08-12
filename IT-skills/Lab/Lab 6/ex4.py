import numpy as np

#print(np.__version__)


arr = np.array([1,2,3.8,4])

# print(arry)

# print(type(arry))

matrix = np.array([[1,2,3,4],[10,10,10,10],[10,10,10,10]])
# print(matrix) 

# just like range function
# rangeArray = np.arange(1, 10)
# print(rangeArray)
# rangeArrayWithNeg = np.arange(-5,0,1)
# print(rangeArrayWithNeg)


# print("\n ----------------")

# arrLinspace = np.linspace(0,1,5)
# print(arrLinspace)

# print("\n ----------------")

# zeroMatrix = np.zeros((2,3))
# oneMatrix = np.ones((4,4))
# constMatrix = np.full((3,3),7)
# identity = np.eye(3)
# emptyMatrix = np.empty((2,2)) #empty matrix


# print("Zeros: \n", zeroMatrix)
# print("\nOnes: \n", oneMatrix)
# print("\nConstent: \n", constMatrix)
# print("\nidentity: \n", identity)
# print("\nemptyMatrix: \n", emptyMatrix)


# print("\n", zeroMatrix.shape)
# print("\n", zeroMatrix.dtype)
# print("\n", oneMatrix.ndim)

# print(arr)
# new_arr = arr.astype('int32')
# print(new_arr)

# print(arr.dtype == np.float64)

# print(matrix)
# print(matrix.size)
# print(matrix.shape)
# print(matrix.ndim)

# print(matrix.itemsize)
# print(matrix.dtype)
# print(matrix.nbytes) # print(8*12)


randArry = np.random.r
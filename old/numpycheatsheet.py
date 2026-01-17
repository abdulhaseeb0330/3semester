import numpy as np
# 🔹 NumPy Cheatsheet (Most Important Functions by Category)
# 1. Array Creation
np.array([1,2,3])              # from list/tuple
np.zeros((2,3))                # all zeros
np.ones((3,3))                 # all ones
np.empty((2,2))                # uninitialized
np.arange(0,10,2)              # range with step
np.linspace(0,1,5)             # evenly spaced values
np.identity(3)                 # identity matrix
np.eye(3, k=1)                 # diag matrix
np.full((2,2), 7)              # constant filled
np.random.rand(2,3)            # random floats [0,1)
np.random.randint(0,10,(2,2))  # random ints
arr=np.array([[1,2,3],[4,5,6]])  # 2D array
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
# 2. Array Inspection
arr.shape        # dimensions
arr.ndim         # number of dimensions
arr.size         # total elements
arr.dtype        # data type
arr.itemsize     # bytes per element
arr.nbytes       # total memory

# 3. Array Manipulation
arr.reshape(2,3)       # change shape
arr.ravel()            # flatten
arr.flatten()          # flatten (copy)
arr.transpose()        # swap axes
np.concatenate([a,b])  # join arrays
np.vstack([a,b])       # stack vertically
np.hstack([a,b])       # stack horizontally
np.split(arr,2)        # split into parts

# 4. Indexing & Slicing
arr[0,1]        # element access
arr[:,0]        # first column
arr[1,:]        # second row
arr[::2]        # step slicing
arr[arr > 5]    # boolean indexing

# 5. Math / Statistics
np.min(arr), np.max(arr)
np.mean(arr), np.median(arr)
np.std(arr), np.var(arr)
np.sum(arr), np.cumsum(arr)
np.prod(arr), np.cumprod(arr)
np.argmax(arr), np.argmin(arr)
np.percentile(arr, 75)

# 6. Linear Algebra
np.dot(a,b)           # dot product
np.matmul(a,b)        # matrix multiply
np.linalg.inv(a)      # inverse
np.linalg.det(a)      # determinant
np.linalg.eig(a)      # eigenvalues/vectors
np.linalg.solve(a,b)  # solve linear eqns

# 7. Sorting & Searching
np.sort(arr)              # sort copy
arr.sort(axis=0)          # in-place
np.argsort(arr)           # indices
np.unique(arr)            # unique values
np.where(arr>5)           # condition indices
np.nonzero(arr)           # non-zero indices
np.in1d(a,b)              # test membership
np.intersect1d(a,b)       # intersection

# 8. Random Module
np.random.seed(0)          # reproducibility
np.random.rand(3,2)        # uniform [0,1)
np.random.randn(3,2)       # normal dist
np.random.randint(1,10,5)  # random ints
np.random.choice(arr,3)    # random sample
np.random.shuffle(arr)     # shuffle inplace

# 9. Trigonometric & Log/Exp
np.sin(arr), np.cos(arr), np.tan(arr)
np.exp(arr), np.log(arr), np.log10(arr)
np.deg2rad(arr), np.rad2deg(arr)

# 10. Set Operations
np.union1d(a,b)
np.intersect1d(a,b)
np.setdiff1d(a,b)
np.setxor1d(a,b)

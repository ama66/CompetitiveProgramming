def create_array(a, text):
    print(text)
    print(a)
    
create_array(np.arange(20).reshape(4,5),"using arange") 
create_array(np.zeros((2,4)) , "using zeros") 
create_array(np.ones((3,4)) , "using ones") 
create_array(np.empty((2,3)), "using empty array initialized with random content")
create_array(np.full((2,2), 3) , "using constant value to fill array")
create_array(np.eye(3,3), "diagonal array")
create_array(np.linspace(0, 10, num=4), "Linear space with number of elements")
create_array(np.array([4,5,6]), "passing a list")
create_array(np.array([(1,2,3), (4,5,6)]), "pass list of tuples for 2D array")
create_array(np.random.random((2,2)), "using random numbers with specificed size array")
create_array(np.empty_like(np.zeros((2,4))), "empty array same size as passed array")
create_array(np.zeros_like(np.zeros((2,4))), "zero array same size as passed array")
create_array(np.ones_like(np.zeros((2,4))), "ones array same size as passed array")
create_array(np.full_like(np.array([4,5,6], dtype=np.double), 50.1),"uniform value in an array with size similar to passed array")



using arange
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]]
using zeros
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
using ones
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]
 [1. 1. 1. 1.]]
using empty array initialized with random content
[[4.9e-324 9.9e-324 1.5e-323]
 [2.0e-323 2.5e-323 3.0e-323]]
using constant value to fill array
[[3 3]
 [3 3]]
diagonal array
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
Linear space with number of elements
[ 0.          3.33333333  6.66666667 10.        ]
passing a list
[4 5 6]
pass list of tuples for 2D array
[[1 2 3]
 [4 5 6]]
using random numbers with specificed size array
[[0.86110614 0.23845203]
 [0.64635758 0.6316998 ]]
empty array same size as passed array
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
zero array same size as passed array
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]]
ones array same size as passed array
[[1. 1. 1. 1.]
 [1. 1. 1. 1.]]
uniform value in an array with size similar to passed array
[50.1 50.1 50.1]

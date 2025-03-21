import numpy as np

#1.Creating Arrays:
"""
import numpy as np
a=np.array([1,2,3,4,5,6])
print(a)

import numpy as np
matrix=np.array([[1,2,3],[4,5,6]])
print(matrix)
"""
# 2.Generating Arrays:
"""
import numpy as np
zeros=np.zeros((2,3))
ones=np.ones((3,2))

print("Zero Array:")
print(zeros)
print("One Array:")
print(ones)
"""
#3.Generating a random Array:
"""
import numpy as np
import random
random_array=np.random.rand(3,3)
print(random_array)
"""
#4.Element-wise Operations:
"""
import numpy as np

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

print("addition:",arr1+arr2)
print("subtraction:",arr1-arr2)
print("multiplication:",arr1*arr2)
print("division:",arr1**2)
"""
# 5.Matrix multiplication:
"""
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
result=np.dot(a,b)
print(result)
"""
# 6.Indexing and slicing:
"""
import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[1])
print(arr[1:4])
print(arr[-1])
"""
#7.Statistical Operations:
"""
import statistics
data=[10,20,30,40,50]
mean_value=statistics.mean(data)
print("mean",mean_value)
"""
#shortcut method for standrd deviation(SD):
"""
import numpy as np

data=np.array([10,20,30,40,50])
n=len(data)
sum_x=np.sum(data)
sum_x2=np.sum(data**2)

std_shortcut=np.sqrt((sum_x2/n))-((sum_x/n)**2)
print("standerd deviation (shortcut method):",std_shortcut)
"""
#(MEAN,MEDIAN,S.D):

import numpy as np
arr=np.array([10,20,30,40,50,60])

print("mean:",np.mean(arr))
print("median:",np.median(arr))
print("standard deviation:",np.std(arr))
print("sum:",np.sum(arr))
print("min:",np.min(arr))
print("max:",np.max(arr))


#8.Reshaping and Transposing:
"""
arr=np.array([1,2,3,4,5,6])
reshaped=arr.reshape(2,3)
print("Reshaped Array:")
print(reshaped)
matrix=np.array([[1,2,3],[4,5,6]])
transposed=matrix.T
print("\nTransposed Matrix:")
print(transposed)

"""
#9.Boolean Indexing (Filtering Elenment):
 # -> Boolean indexing uses conditions iside[]
  #->Use & for AND,| for OR(must be inside parantheses)
#Multiple conditions using & (AND) and (OR)
"""
import numpy as np
arr=np.array([1,20,30,40,50])
#find values between 20 and 40
Filtered_arr=arr[(arr>=20)&(arr<=40)]
print(Filtered_arr)"
"""


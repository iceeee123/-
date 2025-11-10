import numpy as np

#生成数组(以一维数组为例)
x=np.array([1,2,3])
y=np.array([4,5,6])
print(x,y)
print(type(x),type(y))

#数组算数运算
##如果元素个数不同，程序就会报错
x = np.array([11,22,33])
y = np.array([44,55,66])

print(x + y)
print(x - y)
print(x * y)
print(x / y)

##数组与标量运算...
x=np.array([1,2,3])
print(x*2)

#N维数组
'''一维数组---向量
   二维数组---矩阵
   三维数组---张量
'''
A=np.array([[1,2],[3,4]])
B=np.array([[3,0],[0,6]])

print(A.shape)
print(A.dtype,end='\n\n')

print(A+B,end="\n\n")

# 逐元素相乘的规则
# 两个数组中对应位置的元素相乘。这就要求参与运算的两个数组必须具有完全相同的形状（即相同的维度和各维度大小一致）
print(A * B) #矩阵相乘为@ 运算符

#广播
##NumPy中，形状不同的数组之间也可以进行运算
A=np.array([[1,2],[3,4]])
B=np.array([10,20])
print(A * B)

# 除了常规的索引操作，NumPy还可以使用数组访问各个元素
X=np.array([[1,2],[3,4],[5,6]])
X=X.flatten()
print(X)

'''
运用这个标记法，可以获取满足一定条件的元素
对NumPy数组使用不等号运算符等,结果会得到一个布尔型的数组
'''
print(X[np.array([0, 2, 4])])
print(X>3)
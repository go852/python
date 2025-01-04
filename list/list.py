# 空列表
empty_list = []
print(empty_list)
# 包含不同类型元素的列表
mixed_list = [1, 3.14, "Hello", True]
print(mixed_list)
# 嵌套列表
nested_list = [1, [2, 3], 4]
print(nested_list)

my_list = [10, 20, 30, 40, 50]
# 访问第一个元素
print(my_list[0])  # 输出 10

# 访问最后一个元素
print(my_list[-1])  # 输出 50

# 访问子列表（切片）
print(my_list[1:4])  # 输出 [20, 30, 40]

my_list = [10, 20, 30, 40, 50]

# 使用 map 对每个元素执行平方操作
squared_list = map(lambda x: x**2, my_list)

# 将 map 转化为列表并打印
print(list(squared_list))  # 输出 [100, 400, 900, 1600, 2500]

# 定义一个函数
def square(x):
    return x ** 2

# 创建一个列表
numbers = [1, 2, 3, 4, 5]

# 使用 map 将 square 函数应用到列表中的每个元素
squared_numbers = map(square, numbers)

# 将返回的迭代器转为列表并打印
print(list(squared_numbers))  # 输出 [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6]

# 使用 filter 先过滤出偶数，再用 map 平方
even_numbers_squared = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))

# 将返回的迭代器转为列表并打印
print(list(even_numbers_squared))  # 输出 [4, 16, 36]

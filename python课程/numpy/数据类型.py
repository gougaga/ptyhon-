"""
# 数据类型

| 名称   | 描述 | 名称   | 描述 |
| ------    |:------ |------    |:------ |
| bool_  | 布尔型数据类型（True 或者 False） |float_  | float64 类型的简写 |
|int_   | 默认的整数类型（类似于 C 语言中的 long，int32 或 int64） |float16/32/64  | 半精度浮点数:1 个符号位，5 个指数位，10个尾数位<br/>单精度浮点数:1 个符号位，8 个指数位，23个尾数位<br/>双精度浮点数,包括：1 个符号位，11 个指数位，52个尾数位|
| intc    | 和 C 语言的 int 类型一样，一般是 int32 或 int 64 |complex_  | 复数类型，与 complex128 类型相同 |
| intp    | 用于索引的整数类型（类似于 C 的 ssize_t，通常为 int32 或 int64） |complex64/128  | 复数，表示双 32 位浮点数（实数部分和虚数部分）<br/>复数，表示双 64 位浮点数（实数部分和虚数部分） |
| int8/16/32/64  |   代表与1字节相同的8位整数<br/>代表与2字节相同的16位整数<br/>代表与4字节相同的32位整数<br/>代表与8字节相同的64位整数 |str_  | 表示字符串类型 |
| uint8/16/32/64  | 代表1字节（8位）无符号整数<br/>代表与2字节相同的16位整数<br/>代表与4字节相同的32位整数<br/>代表与8字节相同的64位整数 |string_  | 表示字节串类型,也就是bytes类型 |
"""
import numpy as np
a = np.array([1, 2, 3, 4])
print(a)
# 浮点型 astype dtype
b = a.astype(dtype='float_')
print('浮点', b)

c = np.array([1, 2, 3, 4], dtype=np.float_)
print('浮点:', c)

# 布尔型
d = np.array([1, 2, 3, 4], dtype=np.bool_)
print('字符串:', d)

# 字符串
e = np.array([0, 1, 2, 3, 4], dtype=np.str_)
f = np.array([0, 1, 2, 3, 4], dtype=np.string_)
print('字符串:', e, f, e.dtype)
str1 = np.array(['你好:', 0, 1], dtype=np.str_)
print("///", str1)
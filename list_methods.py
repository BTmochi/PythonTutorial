# ===============================================================================
# map()
# -------------------------------------------------------------------------------
# map() はリストの各要素に対して処理を行い、行った結果を返します。
# ===============================================================================
# 下記の例では各要素を2倍にする処理を行います。
from functools import reduce

a = [1, 2, 3]


def double(x): return x * 2


print(map(double, a))  # => [2, 4, 6] : 関数方式
print(map(lambda x: x * 2, a))  # => [2, 4, 6] : lambda方式
print([x * 2 for x in a])  # => [2, 4, 6] : 内包表記(後述)

# ===============================================================================
# filter()
# -------------------------------------------------------------------------------
# filter() はリストの各要素に対して処理を行い、処理結果が真となる要素のみを取り出します。
# ===============================================================================
# 下記の例では各要素から奇数のみを取り出します。
a = [1, 2, 3]


def isodd(x): return x % 2


print(filter(isodd, a))  # => [1, 3] : 関数方式
print(filter(lambda x: x % 2, a))  # => [1, 3] : lambda方式
print([x for x in a if x % 2])  # => [1, 3] : 内包表記(後述)

# ===============================================================================
# reduce()
# -------------------------------------------------------------------------------
# reduce() はリストの最初の2要素を引数に処理を呼び出し、結果と次の要素を引数に処理の呼び出しを繰り返し、
# 単一の結果を返します
# ===============================================================================
# 下記の例では、各要素の合計を計算しています。
a = [1, 2, 3, 4, 5]


def add(x, y): return x + y


print(reduce(add, a))  # => 15 : 関数方式
print(reduce(lambda x, y: x + y, a))  # => 15 : lambda方式


"""
関数を定義してみる
"""

# まずはスタンダードに文字列だけ返す関数
def hoge():
    return "defining-function!"

print(hoge())

# 引数を渡せるようにする（この場合引数は必須）
def hoge_age(n):
    return "n = %s" % (n)

print(hoge_age(10))
print(hoge_age('ABC'))
#print(hoge_age()) # 引数を渡していないと"TypeError"


# 引数にデフォルト値を与える
def hoge_age_default(m = 'default_value'):
    return "m = %s" % (m)

print(hoge_age_default(100))
print(hoge_age_default('abc'))
print(hoge_age_default())

#
# デフォルト値の注意点　その１
# 関数が定義された時点で関数を定義している側のスコープが評価される
#
num = 100
def func_scope1(arg=num):
  return arg

# 関数の定義は終わっているので引数の評価は済んでいる。
# そのため200を入れても表示は100のままです。
num = 200
print(func_scope1())

#
# デフォルト値の注意点　その２
# デフォルト値は一度だけしか評価されない。
# そのため引数がリスト、辞書の場合は続けて使用した場合
# 初期化されずに値を追加してしまう
#
def func_scope2(n, val=[]):
    val.append(n)
    return val

print(func_scope2(1))
print(func_scope2(2))
print(func_scope2(3))

#
# 定義された関数を呼び出す度に引数を初期化する方法
#
def func_scope3(n, val=None):
    val = [] if val is None else val
    val.append(n)
    return val

print(func_scope3(1))
print(func_scope3(2))
result = func_scope3(3)
print(result)
print(func_scope3(4, result))







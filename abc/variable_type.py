#
# 変数の型について
#

import sys

doc = """
Pythonの変数の型をいくつか確認してみます。
""".strip()

print(doc)

"""
https://docs.python.jp/3/library/stdtypes.html
"""

"""
数値型 ... 整数, 浮動小数点, 複素数
Numeric Types ... int, float, complex
浮動小数点型の精度と内部表現はsys.float_info
複素数の実部、虚部はz.realおよびz.imagを使用する
"""
a = 100
print("a = %d" % (a,))

b = 0.25
print("b = %0.2f" % (b,))
print("float_info", sys.float_info)

comp = 1 + 5j
print(comp)
print("real = %0.2f" % comp.real)
print("imag = %0.2f" % comp.imag)

"""
2進数、8進数、16進数
"""
a = 0b0111
print("0b0111: %02d" % a)

b = 0o12
print("0o12: %d" % b)

c = 0x1a
print("0x1a: %d" % c)

print("string")
a = "Let's Python!"
print("a = %s" % (a,))

b = 'Let\'s Python!'
print("b = %s" % (b,))

c = '"Python" is cool!'
print("c = %s" % (c,))

d = "abcdefghijk"
print("d = %s" % (d,))
print("d[0] = %c" % (d[0],))
print("d[2] = %c" % (d[2],))
print("d[4] = %c" % (d[4],))
print("d[0:3] = %s" % (d[0:3]))
print("d[2:6] = %s" % (d[2:6]))
print("d[3:] = %s" % (d[3:]))
print("d[:3] = %s" % (d[:3]))
print("d[-3:] = %s" % (d[-3:]))
print("d[:-3] = %s" % (d[:-3]))
# d[1] = 'B' 書き換えは出来ない

e = "str" + "ing"
print('"str" + "ing" = %s' % (e, ))

print("list")
squares = [1, 4, 9, 16, 25, 32, 44, 56]
print("squares = ", squares)
print("squares[0] = %d" % (squares[0],))
print("squares[-1] = %d" % (squares[-1],))
print("squares[-3] = %d" % (squares[-3],))
print("squares[2:5] = ", squares[2:5])
print("squares[3:] = ", squares[3:])
print("squares[:3] = ", squares[:3])
print("squares[-3:] = ", squares[-3:])
print("squares[:-3] = ", squares[:-3])



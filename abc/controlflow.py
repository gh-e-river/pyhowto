"""
制御文のサンプルになります。
"""
#
# 条件分岐（if文）
# ある条件を満たしている又は満たしていないを判定する。
#
num = 10
if num == 10:
    print("num == %d" % (num,))

#
# 'else'の使い方
#
if num == 11:
    print("num == 11")
else:
    print("num != 10")

#
# 'elif'の使い方
#
if num < 8:
    print("num < 8")
elif num < 9:
    print("num < 9")
elif num < 10:
    print("num < 10")
else:
    print("num = %d" % (num))

#
# 1行でif文を書く
#
result = "num = 10" if num == 10 else 'num != 10'
print(result)

#
# 上限を指定
# 0, 1, 2, 3, 4
#
for num in range(5):
    print(num, end=" " if (num+1) % 5 else "\n")

#
# 開始、上限を指定
# 2, 3, 4
#
for num in range(2, 5):
    print(num, end=" " if (num+1) % 5 else "\n")

#
# 開始、上限、カウント数を指定
# 1, 3, 5, 7, 9
#
for num in range(1, 10, 2):
    print(num, end=" " if (num+1) % 5 else "\n")

#
# リストのループ
#
data = ['C', 'C++', 'Perl', 'Python', 'PHP', 'Ruby']
for lang in data:
    print("%s" % (lang, ))

#
# リストのループ
# ※enumerate使用時
#
data = ['C', 'C++', 'Perl', 'Python', 'PHP', 'Ruby']
for idx, lang in enumerate(data):
    print("data[%d] = %s" % (idx, lang))

#
# 辞書型のループ
#
data = {
    'C': 'c',
    'C++': 'c++',
    'Perl': 'perl',
    'Python': 'python',
    'PHP': 'php',
    'Ruby': 'ruby'
}
for k, v in data.items():
    print("data[%s] = %s" % (k, v))

#
# 空文字列の除き型
#
data = ['a', '', 'c', 'd', '', 'f', 'g']
data = [x for x in data if x != '']
print(data)


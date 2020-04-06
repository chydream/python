# 正则表达式 字符和特殊符号组成的字符串
# [a-z] 表示26个小写英文字母
# [A-Z] 表示26个大写英文字母
# literal 字面值
# re1|re2  或者
# . 任何字符 （除了\n）
# ^ 匹配字符串的起始部分
# $ 匹配字符串的 终止部分
# * 匹配次数 0次或者多次  前面一位
# + 匹配次数 至少一次   前面一位
# ？ 匹配次数 0次或者1次
# {N} [0-9]{3} 匹配次数 前面字符串出现次数
#{M,N} [0-9]{5,9} 匹配次数 前面字符串出现m - n次 最大化优先
# [] 匹配来自字符集的任意单一字符
# [x-y] 匹配 x-y中的任意单一字符
# [^...] 不匹配范围中的任意字符
# (...) 匹配封闭的正则表达式，然后另存为子组([0-9]{3})?
# (*|+|?|{})? 用于匹配上面频繁出现/重复出现符号的非贪婪版本(*、+、？、{})
# \d 数字 \D 非数字 \w 字母数字字符 \W 非字母 \s 空格字符 \S 非空格字符  \b 任何单词边界 \N 匹配已保存的子组N
# \c 逐字匹配任何特殊字符 c   \A(\Z) 匹配字符串的起始(结束)
# 需要用 '\'进行转义 默认都匹配一个字符，通过次数元字符控制次数

# 2.正则表达式分组
# 重复一个字符串时 使用()进行分组，使用(?<word>\w+)指定组名
#使用 \1 、\2 反向引用

# He loves her lover.
# He likes her liker.
# He (l..e)s her \1r.  \1反向引用
# He (?<name>l..e)s her \k<name>r.  名称引用

# 3.贪婪模式vs非贪婪模式
# 贪婪匹配：在整个表达式匹配成功的前提下，尽可能多的匹配
# 非贪婪匹配：：在整个表达式匹配成功的前提下，以最少的匹配。只需在匹配的pattern中加上"?"
# 默认是贪婪模式

# 4.常用的正则表达式
# 身份证号：
# 430656  1996 1001 5493
# 430656  1996 1001 548X
# \d{17}([0-9]|X)
#  (\d{6})(\d{4})((\d{2})(\d{2}))\d{2}\d{1}([0-9]|X)

# 电子邮箱：  123456@qq.com  123456@vip.qq.com
# \w+@(\w+\.)+\w+
# [a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9-]+)*(\.[a-zA-Z]{2,5})

# 5.正则进阶
# re模块  findall() 返回列表  search() 返回对象  group() 返回字符串  groups() 返回元组 groupdict() 返回字典  split() 返回列表 sub() 返回字符串 compile() 返回对象  match() 返回对象
# compile(pattern, flags = 0) 返回正则表达式对象
# match(pattern, string, flags=0)
import re
pattern = re.compile(r'hello', re.I)
#rest = re.match(pattern, 'hello world')
rest = pattern.match('world hello ')
# print(rest)


content = 'one1two2Three33four444five5six698'
# findall(pattern, string, flags=0)
p = re.compile(r'[a-z]+',re.I)
rest1 =p.findall(content)
rest2 = re.findall(r'[a-z]+', content, re.I) #返回列表
# print(rest2)


# search(pattern, string, flags=0)
p1 = re.compile(r'two', re.I)
rest3 = p1.search(content) #返回对象
# print(rest3)


# group(num) num特定子组
# groups() 返回一个包含所有匹配子组的元组，没成功匹配返回空元组
def test_group():
    content1 = 'hello, world!'
    p3 = re.compile(r'world')
    rest4 = p3.search(content1)
    # print(rest4)
    if rest4:
        print(rest4.group())
        print(rest4.groups())

def test_id_card():
    p = re.compile(r'(?P<dist>\d{6})(\d{4})((\d{2})(\d{2}))\d{2}\d{1}([0-9]|X)')
    id1 = '430656199610015493'
    id2 = '43065619961001548X'
    rest1 = p.search(id1)
    print(rest1.group())
    print(rest1.groups())
    print(rest1.groupdict())

# split()  sub()
# split(pattern, string, max=0)
s = 'one1two2Three33four444five5six698'
p4 = re.compile(r'\d+')
rest4 = p4.split(s,2)
# print(rest4)
# sub(pattern, repl, string, max=0)
s1 = 'one1two2Three33four444five5six698'
p5 = re.compile(r'\d+')
rest5 = p4.sub('#', s1)
# print(rest5)
str = 'hello world'
p_str = re.compile(r'(\w+) (\w+)')
rs = p_str.sub(r'\2 \1',str)
# print(rs)
def f(m):
    return m.group(2).upper() + ' ' + m.group(1)
rs2 = p_str.sub(lambda x:x.group(2).upper() + ' ' + x.group(1), str)
print(rs2)



# if __name__ == '__main__':
    # test_group()
    # test_id_card()
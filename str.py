#二.字符串
#1.拼接 +， str.lower() str.upper() str.title() str.capitalize() str.swapcase() str.format()
mo = 1234.568
str = "{} {} you {:0,.2f}"
strNew = str.format("i", "love", mo)
print(strNew)
# format(1234.567,0.2f)  保留2位小数
# format(1234.567,',') 千分位分隔符
# format(1234.568,0,.3f)  千分位 保留2位小数
name = "张三"
age = 25
weight = 83.5
print(" %s years old %d %.1f"%(name,age,weight))
# 特殊字符 \t 制表符 \n 换行符  str.lstrip()  str.rstrip()  str.strip()  删除空格  len()长度
# str.find(字符串,开始位置，结束位置）  bool =  str in str
# str.replace(old,new，替换次数）
# python -m pip install --upgrade pip  在C盘需要管理员身份
# pip install colorama https://pypi.tuna.tsinghua.edu.cn/simple
from colorama import Back, Fore, Style
print(Fore.LIGHTBLUE_EX, "HelloWorld") #字体颜色
print(Back.LIGHTGREEN_EX, "HelloWorld") #背景颜色
print(Style.RESET_ALL, "HelloWorld") #重置



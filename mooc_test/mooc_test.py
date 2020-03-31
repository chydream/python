import random
import sys
from datetime import datetime

def guide_page(guide_word):
    print("{0}{1}{2}".format('*'*10, guide_word, '*'*10))

def all_num(n):
    if n.isdigit():
        return True
    else:
        return False

def num_legal(start, end):
    if start == end:
        print("您输入的区间数字相同！！请重新启动程序")
        sys.exit()
    elif start > end:
        print("您输入的区间数字大小有误！！请重新启动程序")
        sys.exit()
    else:
        return 1

def set_final_num(num1,num2):
    ran = random.randint(num1, num2)
    return ran

def check_num_legal(num, ls):
    if num in ls:
        return True
    else:
        return False

def write_record(times,value):
    file_name = 'record.txt'
    with open(file_name, 'a+', encoding='utf-8') as f:
        t = datetime.now()
        f.write("{0}:第{1}次您猜测的数字为{2}".format(t, times, value))
        f.write("\n")

def main():
    guide_page('欢迎进入数字猜猜猜小游戏')
    start = input("请输入数字区间起始位置：")
    end = input("请输入数字区间终止位置：")
    if all_num(start) and all_num(end):
        start = int(start)
        end = int(end)
        if num_legal(start, end) == 1:
            ran = set_final_num(start, end)
            print("数字区间起始值：{0}".format(start))
            print("数字区间终止值：{0}".format(end))
            print("所产生的随机数字区间：[{0},{1}]".format(start, end))
            i = 1
            while True:
                guess = input("请继续输入您猜测的数字：")
                if all_num(guess):
                    guess = int(guess)
                    ls = list(range(start, end+1))
                    if check_num_legal(guess, ls):
                        write_record(i, guess)
                        if guess > ran:
                            print("higher than the answer")
                            i = i + 1
                            continue
                        elif guess < ran:
                            i = i + 1
                            print("lower than the answer")
                            continue
                        else:
                            print("恭喜您！只用了{0}次就赢得了游戏".format(i))
                            break
                    else:
                        print("输入数字超出区间,请重新输入")
                        continue
                else:
                    print("您所输入的为非数字字符，请重新启动")
                    break
    else:
        print("您所输入的为非数字字符，请重新启动")

if __name__ == '__main__':
    main()
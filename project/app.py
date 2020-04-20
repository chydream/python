import time
from colorama import Fore, Style
import os
import sys
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService

__user_service = UserService()
__news_service = NewsService()
while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t======================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t======================")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("输入操作编号：")
    if opt == "1":
        username = input("\n\t用户名：")
        password = getpass("\n\t密码：")
        result = __user_service.login(username, password)
        if result:
            while True:
                os.system("cls")
                print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                print(Style.RESET_ALL)
                opt = input("输入操作编号：")
                if opt == '1':
                    page = 1
                    while True:
                        os.system("cls")
                        result = __news_service.search_unreview_list(page)
                        count_page = __news_service.search_unreview_count_page()
                        for index in range(len(result)):
                            print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s" % (index+1, result[index][1], result[index][2], result[index][3]))
                        print(Fore.LIGHTBLUE_EX, "\n\t----------------------")
                        print(Fore.LIGHTGREEN_EX, "\n\t%d/%d" % (page, count_page))
                        print(Fore.LIGHTBLUE_EX, "\n\t----------------------")
                        print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                        print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                        print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                        print(Style.RESET_ALL)
                        opt = input("输入操作编号：")
                        if opt == 'back':
                            break
                        elif opt == 'prev' and page > 1:
                            page -= 1
                        elif opt == 'next' and page < count_page:
                            page += 1
                        elif int(opt) >= 1 and int(opt) <= 10:
                            news_id = result[int(opt) -1][0]
                            __news_service.update(news_id)
                elif opt == '2':
                    page = 1
                    while True:
                        os.system("cls")
                        result = __news_service.search_list(page)
                        count_page = __news_service.search_count_page()
                        for index in range(len(result)):
                            print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s" % (
                            index + 1, result[index][1], result[index][2], result[index][3]))
                        print(Fore.LIGHTBLUE_EX, "\n\t----------------------")
                        print(Fore.LIGHTGREEN_EX, "\n\t%d/%d" % (page, count_page))
                        print(Fore.LIGHTBLUE_EX, "\n\t----------------------")
                        print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                        print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                        print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                        print(Style.RESET_ALL)
                        opt = input("输入操作编号：")
                        if opt == 'back':
                            break
                        elif opt == 'prev' and page > 1:
                            page -= 1
                        elif opt == 'next' and page < count_page:
                            page += 1
                        elif int(opt) >= 1 and int(opt) <= 10:
                            news_id = result[int(opt) - 1][0]
                            __news_service.delete(news_id)
                else:
                    break
        else:
            print("\n\t登录失败(3s自动返回)")
            time.sleep(3)
            continue
    elif opt == "2":
        sys.exit(0)
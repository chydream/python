import time
from colorama import Fore, Style
import os
import sys
from getpass import getpass
from service.user_service import UserService
from service.news_service import NewsService
from service.type_service import TypeService

__user_service = UserService()
__news_service = NewsService()
__type_service = TypeService()
while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t======================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用新闻管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t======================")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出系统")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号：")
    if opt == "1":
        username = input("\n\t用户名：")
        password = getpass("\n\t密码：")
        result = __user_service.login(username, password)
        if result:
            role = __user_service.search_user_role(username)
            while True:
                os.system("cls")
                if role == '新闻编辑':
                    os.system("cls")
                    print(Fore.LIGHTGREEN_EX, "\n\t1.发表新闻")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.编辑新闻")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt == "back":
                        break
                    elif opt == "exit":
                        sys.exit(0)
                    elif opt == "1":
                        title = input("\n\t输入新闻标题：")
                        user_id = __user_service.get_userid(username)
                        result = __type_service.search_list()
                        for index in range(len(result)):
                            print(Fore.LIGHTBLUE_EX,"\n\t%d\t%s" % (index + 1, result[index][1]))
                        opt = input("\n\t输入类型编号：")
                        type_id = result[int(opt)-1][0]
                        content_id = 100
                        is_top = input("\n\t输入置顶级别(0-5)：")
                        is_commite = input("\n\t输入Y/N：")
                        if is_commite == "Y" or is_commite == "y":
                            __news_service.insert(title, user_id, type_id, content_id, is_top)
                            print("\n\t保存成功(3秒自动返回)")
                            time.sleep(3)
                    elif opt == "2":
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
                            opt = input("\n\t输入操作编号：")
                            if opt == 'back':
                                break
                            elif opt == 'prev' and page > 1:
                                page -= 1
                            elif opt == 'next' and page < count_page:
                                page += 1
                            elif opt.isdigit() and int(opt) >= 1 and int(opt) <= 10:
                                news_id = result[int(opt) - 1][0]
                                result = __news_service.search_news_by_id(news_id)
                                title = result[0]
                                type = result[2]
                                is_top = result[4]
                                print("\n\t原标题：{0}".format(title))
                                new_title = input("\n\t新标题：")
                                print("\n\t原类型编号：{0}".format(type))
                                result = __type_service.search_list()
                                for index in range(len(result)):
                                    print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s" % (index + 1, result[index][1]))
                                opt = input("\n\t输入类型编号：")
                                new_type_id = result[int(opt) - 1][0]
                                content_id = 100
                                print("\n\t原置顶级别：{0}".format(is_top))
                                new_is_top = input("\n\t输入置顶级别(0-5)：")
                                is_commite = input("\n\t输入Y/N：")
                                if is_commite == "Y" or is_commite == "y":
                                    __news_service.update_news_by_id(news_id, new_title, new_type_id, content_id, new_is_top)
                                    __news_service.delete_cache(news_id)
                                    print("\n\t保存成功(3秒自动返回)")
                                    time.sleep(3)
                elif role == '管理员':
                    print(Fore.LIGHTGREEN_EX, "\n\t1.新闻管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt == "back":
                        break
                    elif opt == 'exit':
                        sys.exit(0)
                    elif opt == '1':
                        while True:
                            os.system("cls")
                            print(Fore.LIGHTGREEN_EX, "\n\t1.审批新闻")
                            print(Fore.LIGHTGREEN_EX, "\n\t2.删除新闻")
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号：")
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
                                    opt = input("\n\t输入操作编号：")
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif opt.isdigit() and int(opt) >= 1 and int(opt) <= 10:
                                        news_id = result[int(opt) -1][0]
                                        __news_service.update(news_id)
                                        result = __news_service.search_news_by_id(news_id)
                                        title = result[0]
                                        username = result[1]
                                        type = result[2]
                                        content_id = result[3]
                                        is_top = result[4]
                                        create_time = str(result[5])
                                        __news_service.insert_cache(news_id, title, username, type, content_id, is_top, create_time)

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
                                    opt = input("\n\t输入操作编号：")
                                    if opt == 'back':
                                        break
                                    elif opt == 'prev' and page > 1:
                                        page -= 1
                                    elif opt == 'next' and page < count_page:
                                        page += 1
                                    elif opt.isdigit() and int(opt) >= 1 and int(opt) <= 10:
                                        news_id = result[int(opt) - 1][0]
                                        __news_service.delete(news_id)
                            else:
                                print(111)
                                break
        else:
            print("\n\t登录失败(3s自动返回)")
            time.sleep(3)
            continue
    elif opt == "2":
        sys.exit(0)
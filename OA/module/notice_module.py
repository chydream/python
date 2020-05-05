from colorama import Fore, Style
from service.notice_service import NoticeService
import os
import sys
import time


class  NoticeModule:
    __notice_service = NoticeService()

    def notice_init(self, username, role):
        while True:
            os.system("cls")
            if role == "普通用户":
                print(Fore.LIGHTGREEN_EX, "\n\t4.查看通知公告")
            elif role == "管理员":
                print(Fore.LIGHTGREEN_EX, "\n\t1.添加通知公告")
                print(Fore.LIGHTGREEN_EX, "\n\t2.修改通知公告")
                print(Fore.LIGHTGREEN_EX, "\n\t3.删除通知公告")
                print(Fore.LIGHTGREEN_EX, "\n\t4.查看通知公告")
            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
            print(Style.RESET_ALL)
            opt = input("\n\t输入操作编号：")
            if opt == 'back':
                break
            elif opt == '1':
                if role == "管理员":
                    os.system("cls")
                    title = input("\n\t公告标题：")
                    content = input("\n\t公告内容：")
                    self.__notice_service.notice_add(username, title, content)
                    print("\n\t保存成功(3s自动返回)")
                    time.sleep(3)
            elif opt == '2':
                if role == "管理员":
                    page = 1
                    while True:
                        os.system("cls")
                        count_page = self.__notice_service.get_total_page()
                        result = self.__notice_service.get_list(page, username)
                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTBLUE_EX,
                                  "\n\t%d\t%s\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3], one[4]))
                        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
                        print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
                        print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                        print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                        print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                        print(Style.RESET_ALL)
                        opt = input("\n\t输入操作编号：")
                        if opt == "back":
                            break
                        elif opt == "prev" and page > 1:
                            page -= 1
                        elif opt == "next" and page < count_page:
                            page += 1
                        elif opt.isdigit() and int(opt) >= 1 and int(opt) <= 10:
                            os.system("cls")
                            id = result[int(opt) - 1][0]
                            title = input("\n\t新公告标题：")
                            content = input("\n\t新公告内容：")
                            opt = input("\n\t是否保存(Y/N)")
                            if opt == 'Y' or opt == 'y':
                                self.__notice_service.notice_update(username, title, content, id)
                            print("\n\t保存成功(3s自动返回)")
                            time.sleep(3)
            elif opt == '3':
                if role == "管理员":
                    page = 1
                    while True:
                        os.system("cls")
                        count_page = self.__notice_service.get_total_page()
                        result = self.__notice_service.get_list(page, username)
                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTBLUE_EX,
                                  "\n\t%d\t%s\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3], one[4]))
                        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
                        print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                        print(Fore.LIGHTBLUE_EX, "\n\t=====================")
                        print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                        print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                        print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                        print(Style.RESET_ALL)
                        opt = input("\n\t输入操作编号：")
                        if opt == "back":
                            break
                        elif opt == "prev" and page > 1:
                            page -= 1
                        elif opt == "next" and page < count_page:
                            page += 1
                        elif opt.isdigit() and int(opt) >= 1 and int(opt) <= 10:
                            os.system("cls")
                            notice_id = result[int(opt) - 1][0]
                            self.__notice_service.notice_delete(notice_id)
                            print("\n\t删除成功(3s自动返回)")
                            time.sleep(3)
            elif opt == '4':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__notice_service.get_total_page()
                    result = self.__notice_service.get_list(page, username)
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTBLUE_EX,
                              "\n\t%d\t%s\t%s\t%s\t%s" % (index + 1, one[1], one[2], one[3], one[4]))
                    print(Fore.LIGHTBLUE_EX, "\n\t=====================")
                    print(Fore.LIGHTBLUE_EX, "\n\t%d/%d" % (page, count_page))
                    print(Fore.LIGHTBLUE_EX, "\n\t=====================")
                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                    print(Fore.LIGHTRED_EX, "\n\tprev.上一页")
                    print(Fore.LIGHTRED_EX, "\n\tnext.下一页")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt == "back":
                        break
                    elif opt == "prev" and page > 1:
                        page -= 1
                    elif opt == "next" and page < count_page:
                        page += 1
                    elif opt.isdigit() and int(opt) >= 1 and int(opt) <= 10:
                        while True:
                            os.system("cls")
                            notice_id = result[int(opt) - 1][0]
                            one = self.__notice_service.notice_view(notice_id)
                            print(Fore.LIGHTBLUE_EX, "\n\t%s\t%s\t%s\t%s" % (one[0], one[1], one[2], one[3]))
                            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                            print(Style.RESET_ALL)
                            opt = input("\n\t输入操作编号：")
                            if opt == "back":
                                break

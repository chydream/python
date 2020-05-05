from colorama import Fore, Style
from service.user_service import UserService
import os
import sys
import time
from service.role_service import RoleService


class UserModule:
    __user_service = UserService()
    __role_service = RoleService()
    def user_init(self):
        while True:
            os.system("cls")
            print(Fore.LIGHTGREEN_EX, "\n\t1.添加用户")
            print(Fore.LIGHTGREEN_EX, "\n\t2.修改用户")
            print(Fore.LIGHTGREEN_EX, "\n\t3.删除用户")
            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
            print(Style.RESET_ALL)
            opt = input("\n\t输入操作编号：")
            if opt == 'back':
                break
            elif opt == '1':
                os.system("cls")
                username = input("\n\t用户名：")
                password = input("\n\t密码：")
                repassword = input("\n\t重复密码：")
                if password != repassword:
                    print("\n\t两次密码不一致(3s自动返回)")
                    time.sleep(3)
                    continue
                email = input("\n\t邮箱：")
                result = self.__role_service.search_list()
                for index in range(len(result)):
                    one = result[index]
                    print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                # print(Style.RESET_ALL)
                opt = input("\n\t角色编号：")
                role_id = result[int(opt) - 1][0]
                self.__user_service.insert(username, password, email, role_id)
                print("\n\t保存成功(3s自动返回)")
                time.sleep(3)
            elif opt == '2':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__user_service.search_count_page()
                    result = self.__user_service.search_list(page)
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTBLUE_EX,
                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
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
                        user_id = result[int(opt) - 1][0]
                        username = input("\n\t新用户名：")
                        password = input("\n\t新密码：")
                        repassword = input("\n\t再次输入密码：")
                        if password != repassword:
                            print("\n\t两次密码不一致(3s自动返回)")
                            print(Style.RESET_ALL)
                            time.sleep(3)
                            break
                        email = input("\n\t邮箱：")
                        result = self.__role_service.search_list()
                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                        print(Style.RESET_ALL)
                        opt = input("\n\t角色编号：")
                        role_id = result[int(opt) - 1][0]
                        opt = input("\n\t是否保存(Y/N)")
                        if opt == 'Y' or opt == 'y':
                            self.__user_service.update(user_id, username, password, email, role_id)
                        print("\n\t保存成功(3s自动返回)")
                        time.sleep(3)
            elif opt == '3':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__user_service.search_count_page()
                    result = self.__user_service.search_list(page)
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTBLUE_EX,
                              "\n\t%d\t%s\t%s" % (index + 1, one[1], one[2]))
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
                        user_id = result[int(opt) - 1][0]
                        self.__user_service.delete_by_id(user_id)
                        print("\n\t删除成功(3s自动返回)")
                        time.sleep(3)
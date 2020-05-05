from colorama import Fore, Style
from service.staff_service import StaffService
import os
import sys
import time
from service.dept_service import DeptService

class StaffModule:
    __staff_service = StaffService()
    __dept_service = DeptService()
    def staff_view(self, email):
        while True:
            one = self.__staff_service.staff_view(email)
            print(Fore.LIGHTBLUE_EX, "\n\t%s\t%s\t%s\t%s" % (one[1], one[2], one[3], one[4]))
            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
            print(Style.RESET_ALL)
            opt = input("\n\t输入操作编号：")
            if opt == 'back':
                break


    def staff_init(self):
        while True:
            os.system("cls")
            print(Fore.LIGHTGREEN_EX, "\n\t1.添加职工信息")
            print(Fore.LIGHTGREEN_EX, "\n\t2.修改职工信息")
            print(Fore.LIGHTGREEN_EX, "\n\t3.删除职工信息")
            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
            print(Style.RESET_ALL)
            opt = input("\n\t输入操作编号：")
            if opt == 'back':
                break
            elif opt == '1':
                os.system("cls")
                truename = input("\n\t姓名：")
                email = input("\n\t邮箱：")
                sex = input("\n\t性别：")
                result = self.__dept_service.get_list()
                for index in range(len(result)):
                    one = result[index]
                    print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                opt = input("\n\t部门编号：")
                deptno = result[int(opt) - 1][0]
                job = input("\n\t职务：")
                phone = input("\n\t手机号码：")
                address = input("\n\t地址：")
                self.__staff_service.staff_add(truename, email, sex, deptno, job, phone, address)
                print("\n\t保存成功(3s自动返回)")
                time.sleep(3)
            elif opt == '2':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__staff_service.get_total_page()
                    result = self.__staff_service.get_list(page)
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
                        staff_id = result[int(opt) - 1][0]
                        result = self.__dept_service.get_list()
                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTBLUE_EX, "\n\t%d.%s" % (index + 1, one[1]))
                        opt = input("\n\t新部门编号：")
                        deptno = result[int(opt) - 1][0]
                        job = input("\n\t新职务：")
                        phone = input("\n\t新手机号码：")
                        address = input("\n\t新地址：")
                        opt = input("\n\t是否保存(Y/N)")
                        if opt == 'Y' or opt == 'y':
                            self.__staff_service.staff_update(deptno, job, phone, address, staff_id)
                        print("\n\t保存成功(3s自动返回)")
                        time.sleep(3)
            elif opt == '3':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__staff_service.get_total_page()
                    result = self.__staff_service.get_list(page)
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
                        staff_id = result[int(opt) - 1][0]
                        self.__staff_service.staff_delete(staff_id)
                        print("\n\t删除成功(3s自动返回)")
                        time.sleep(3)
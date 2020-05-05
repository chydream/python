from colorama import Fore, Style
from service.schedule_service import SchedulService
import os
import sys
import time


class  ScheduleModule:
    __schedule_service = SchedulService()
    def schedule_view(self, username, role):
        page = 1
        while True:
            os.system("cls")
            count_page = self.__schedule_service.get_total_page()
            result = self.__schedule_service.get_list(page, username, role)
            for index in range(len(result)):
                one = result[index]
                print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s\t%s" % (
                index + 1, str(one[1]) + '年', str(one[2]) + '月', str(one[3]) + '日', one[4]))
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
                    schedule_id = result[int(opt) - 1][0]
                    one = self.__schedule_service.schedule_view(schedule_id)
                    print(Fore.LIGHTBLUE_EX, "\n\t%s\t%s\t%s\t%s" % (one[0], one[1], one[2], one[3]))
                    print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
                    opt = input("\n\t输入操作编号：")
                    if opt == "back":
                        break

    def schedule_init(self, username, role):
        while True:
            os.system("cls")
            print(Fore.LIGHTGREEN_EX, "\n\t1.添加日程安排")
            print(Fore.LIGHTGREEN_EX, "\n\t2.修改日程安排")
            print(Fore.LIGHTGREEN_EX, "\n\t3.删除日程安排")
            print(Fore.LIGHTGREEN_EX, "\n\t4.查看日程安排")
            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
            print(Style.RESET_ALL)
            opt = input("\n\t输入操作编号：")
            if opt == 'back':
                break
            elif opt == '1':
                os.system("cls")
                year = input("\n\t年份：")
                month = input("\n\t月份：")
                day = input("\n\t日期：")
                plan = input("\n\t计划：")
                self.__schedule_service.schedule_add(username, int(year), int(month), int(day), plan)
                print("\n\t保存成功(3s自动返回)")
                time.sleep(3)
            elif opt == '2':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__schedule_service.get_total_page()
                    result = self.__schedule_service.get_list(page, username, role)
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s\t%s" % (index + 1, str(one[1])+'年', str(one[2]) + '月', str(one[3]) + '日', one[4]))
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
                        year = input("\n\t新年份：")
                        month = input("\n\t新月份：")
                        day = input("\n\t新日期：")
                        plan = input("\n\t新计划：")
                        id = result[int(opt)-1][0]
                        opt = input("\n\t是否保存(Y/N)")
                        if opt == 'Y' or opt == 'y':
                            self.__schedule_service.schedule_update(int(year), int(month), int(day), plan, id)
                        print("\n\t保存成功(3s自动返回)")
                        time.sleep(3)
            elif opt == '3':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__schedule_service.get_total_page()
                    result = self.__schedule_service.get_list(page, username, role)
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTBLUE_EX, "\n\t%d\t%s\t%s\t%s\t%s" % (index + 1, str(one[1])+'年', str(one[2]) + '月', str(one[3]) + '日', one[4]))
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
                        schedule_id = result[int(opt) - 1][0]
                        self.__schedule_service.schedule_delete(schedule_id)
                        print("\n\t删除成功(3s自动返回)")
                        time.sleep(3)
            elif opt == '4':
                self.schedule_view(username, role)
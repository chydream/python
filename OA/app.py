from colorama import Fore, Style
from getpass import getpass
from service.user_service import UserService
import os
import sys
import time
from service.role_service import RoleService
from module.user_module import UserModule
from module.staff_module import StaffModule
from module.schedule_module import ScheduleModule
from module.notice_module import NoticeModule
from module.file_module import FileModule

__user_service = UserService()
__role_service = RoleService()
__user_module = UserModule()
__staff_module = StaffModule()
__schedule_module = ScheduleModule()
__notice_module = NoticeModule()
__file_module = FileModule()
while True:
    os.system("cls")
    print(Fore.LIGHTBLUE_EX, "\n\t=====================")
    print(Fore.LIGHTBLUE_EX, "\n\t欢迎使用OA管理系统")
    print(Fore.LIGHTBLUE_EX, "\n\t=====================")
    print(Fore.LIGHTGREEN_EX, "\n\t1.登录系统")
    print(Fore.LIGHTGREEN_EX, "\n\t2.退出登录")
    print(Style.RESET_ALL)
    opt = input("\n\t输入操作编号：")
    if opt == "1":
        username = input("\n\t用户名：")
        password = input("\n\t密码：")
        result = __user_service.login(username, password)
        if result == True:
            role = __user_service.search_user_role(username)
            while True:
                os.system("cls")
                if role == '普通用户':
                    print(Fore.LIGHTGREEN_EX, "\n\t1.查看当前用户")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.日程安排管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t3.通知公告管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t4.文件管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt == "back":
                        break
                    elif opt == 'exit':
                        sys.exit(0)
                    elif opt == '1':
                        email = __user_service.get_email(username)
                        __staff_module.staff_view(email)
                    elif opt == '2':
                        __schedule_module.schedule_init(username, role)
                    elif opt == '3':
                        __notice_module.notice_init(username, role)
                    elif opt == '4':
                        __file_module.file_init(username, role)

                elif role == "管理员":
                    print(Fore.LIGHTGREEN_EX, "\n\t1.用户管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t2.职工信息管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t3.日程安排管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t4.通知公告管理")
                    print(Fore.LIGHTGREEN_EX, "\n\t5.文件管理")
                    print(Fore.LIGHTRED_EX, "\n\tback.退出登录")
                    print(Fore.LIGHTRED_EX, "\n\texit.退出系统")
                    print(Style.RESET_ALL)
                    opt = input("\n\t输入操作编号：")
                    if opt == "back":
                        break
                    elif opt == 'exit':
                        sys.exit(0)
                    elif opt == '1':
                        __user_module.user_init()
                    elif opt == '2':
                        __staff_module.staff_init()
                    elif opt == '3':
                        __schedule_module.schedule_init(username, role)
                    elif opt == '4':
                        __notice_module.notice_init(username, role)
                    elif opt == '5':
                        __file_module.file_init(username, role)

        else:
            print("\n\t登录失败(3s自动返回)")
            time.sleep(3)
    elif opt == "2":
        sys.exit(0)  # 安全退出
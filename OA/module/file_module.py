from colorama import Fore, Style
from service.file_service import FileService
from service.mongo_file_service import MongoFileService
import os
import sys
import time


class FileModule:
    __file_service = FileService()
    __mongo_file_service = MongoFileService()
    def file_init(self, username, role):
        while True:
            os.system("cls")
            print(Fore.LIGHTGREEN_EX, "\n\t1.上传文件")
            print(Fore.LIGHTGREEN_EX, "\n\t2.下载文件")
            if role == '管理员':
                print(Fore.LIGHTGREEN_EX, "\n\t3.删除文件")
            print(Fore.LIGHTGREEN_EX, "\n\t4.查看文件信息")
            print(Fore.LIGHTRED_EX, "\n\tback.返回上一层")
            print(Style.RESET_ALL)
            opt = input("\n\t输入操作编号：")
            if opt == 'back':
                break
            elif opt == '1':
                os.system("cls")
                filePath = input("\n\t文件绝对路径：")
                filename = os.path.basename(filePath)
                filesize = round((os.path.getsize(filePath)/1024/1024), 4) #单位兆
                fileinfo = {"filePath": filePath, "filename": filename, "filesize": filesize, "type": os.path.splitext(filePath)[1]}
                args = {"type": os.path.splitext(filePath)[1]}
                self.__mongo_file_service.add_file(fileinfo)
                file_id = self.__mongo_file_service.get_file_id(fileinfo)
                self.__file_service.file_add(username, filename, filesize, fileinfo, str(file_id))
                print("\n\t保存成功(3s自动返回)")
                time.sleep(3)
            elif opt == '2':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__file_service.get_total_page()
                    result = self.__file_service.get_list(page, username, role)
                    for index in range(len(result)):
                        one = result[index]
                        print(Fore.LIGHTBLUE_EX,
                              "\n\t%d\t%s\t%s\t%s\t%s" % (index + 1,  one[1], one[2], one[3], one[4]))
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
                        file_id = str(result[int(opt) - 1][1])
                        # print(file_id)
                        self.__mongo_file_service.download_file(file_id, './download/')
                        print("\n\t保存成功(3s自动返回)")
                        time.sleep(3)
            elif opt == '3':
                if role == '管理员':
                    page = 1
                    while True:
                        os.system("cls")
                        count_page = self.__file_service.get_total_page()
                        result = self.__file_service.get_list(page, username, role)
                        for index in range(len(result)):
                            one = result[index]
                            print(Fore.LIGHTBLUE_EX,
                                  "\n\t%d\t%s\t%s\t%s\t%s" % (index + 1,  one[1], one[2], one[3], one[4]))
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
                            file_id = result[int(opt) - 1][1]
                            self.__file_service.file_delete(id)
                            self.__mongo_file_service.delete_file(file_id)
                            print("\n\t删除成功(3s自动返回)")
                            time.sleep(3)
            elif opt == '4':
                page = 1
                while True:
                    os.system("cls")
                    count_page = self.__file_service.get_total_page()
                    result = self.__file_service.get_list(page, username, role)
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
                        one = self.__file_service.file_view(id)
                        print(Fore.LIGHTBLUE_EX, "\n\t%s\t%s\t%s\t%s" % (one[0], one[1], one[2], one[4]))
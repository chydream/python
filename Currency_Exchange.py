service_menu = {
    1: "人民币转换美元",
    2: "美元转换人民币",
    3: "人民币转换欧元",
    0: "结束程序"
}
print("************欢迎使用货币转换服务系统************")
items = service_menu.items()
for key,value in items:
    print(str(key)+'、'+value)
bool = True
while bool:
    Your_Choice  = input("请选择你需要的服务：")
    Your_Choice  = int(Your_Choice)
    if Your_Choice  == 1:
        print("欢迎使用人民币兑换美元服务")
        your_money = input("请输入您需要转换的人民币金额：")
        your_money = int(your_money)
        print("您需要转换的人民币为：{}元".format(your_money))
        RMB_to_US = format(your_money/6.27, '0.2f')
        print("兑换为美元为：{}$".format(RMB_to_US))
        continue
    elif Your_Choice  == 2:
        print("欢迎使用美元兑换人民币服务")
        your_money = input("请输入您需要转换的美元金额：")
        your_money = int(your_money)
        print("您需要转换的美元为：{}$".format(your_money))
        US_to_RMB = format(your_money * 6.27, '0.2f')
        print("兑换为人民币为：{}元".format(US_to_RMB))
        continue
    elif Your_Choice  == 3:
        print("欢迎使用人民币兑换欧元服务")
        your_money = input("请输入您需要转换的人民币金额：")
        your_money = int(your_money)
        print("您需要转换的人民币为：{}元".format(your_money))
        RMB_to_EUR = format(your_money * 0.13, '0.2f')
        print("兑换为欧元为：{}欧元".format(RMB_to_EUR))
        continue
    elif Your_Choice  == 0:
        print("感谢您的使用，祝您生活愉快，再见！")
        break
    else:
        print("输出信息有误！")
        continue

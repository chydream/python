# 1.异常处理 异常类 Exception
def test_divide():
    try:
        5/0
    except:
        print("报错了,除数不能为0")

def test_div(num1,num2):
    return num1 / num2

# 2.自定义异常
class ApiException(Exception):
    err_code = ''
    err_msg = ''
    def __init__(self, err_code = None,err_msg = None):
        self.err_code = self.err_code if self.err_code else err_code
        self.err_msg = self.err_msg if self.err_msg else err_msg

    def __str__(self):
        return 'Error:{0} - {1}'.format(self.err_code, self.err_msg)

class InvalidCtrlExec(ApiException):
    err_code = '40001'
    err_msg = '不合法的调用凭证'

class BadPramsException(ApiException):
    err_code = '40002'
    err_msg = '2个参数必须都是整数'

def divide(num1,num2):
    if not isinstance(num1,int) or not isinstance(num2, int):
        raise BadPramsException()
    if num2 == 0:
        print(3)
        raise ApiException('400000', '除数不能为0!!!')
    return num1 / num2

# 抛出异常及异常的传递，如果在异常产生的地方不捕获，那么它会一层一层的往上传递
def my_for():
    for x in range(1,10):
        print(x)
        if x == 5:
            raise ApiException('1', '我故意的') # 抛出异常

def do_sth():
    print('开始do_sth')
    my_for()
    print('结束do_sth')

def test_trans():
    print('开始测试')
    try:
        do_sth()
    except ApiException as e:  # 捕获异常
        print('我在最外层捕获到了：{0}'.format(e))
    print('结束测试')


if __name__ == '__main__':
    test_trans()

    # try:
    #     divide(5, 1)
    # except BadPramsException as e:
    #     print(1)
    #     print(e)
    # except ApiException as a:
    #     print(2)
    #     print(a)
    # else:
    #     print('没有异常发声')

    # test_divide()
    # try:
    #     f = open('demo.py', 'r', encoding='utf-8')
    #     res = f.read()
    #     # rest = test_div(5/'s')
    #     # print(rest)
    # except (ZeroDivisionError, TypeError) as e:
    #     print(e)
    # finally:
    #     try:
    #         f.close()
    #         print('文件关闭')
    #     except:
    #         pass
    # except TypeError:
    #     print("请输入数字类型")

    # rest = test_div(5 / 's')
    # print(rest)


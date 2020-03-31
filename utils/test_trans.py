from datetime import datetime

from utils.trans.tools import gen_trans_id
from utils.work.tools import get_file_type

def test_trans_tool():
    id1 = gen_trans_id()
    print(id1)
    date = datetime(2015, 10, 2, 12, 30, 45)
    id2 = gen_trans_id(date)
    print(id2)

def test_work_tool():
    rest = get_file_type('G:\\python\\python\\demo.py')
    print(rest)


if __name__ == '__main__':
    test_trans_tool()
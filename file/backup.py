import os


class FileBackup(object)
    """
    文本文件备份
    """
    def __init__(self, src, dist):
        self.src = src
        self.dist = dist

    def read_files(self):
        ls = os.listdir(self.src)
        print(ls)
        for l in ls:
            self.backup_file(l)

    def backup_file(self,file_name):
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)
            print('指定的目录不存在，创建完成')
        full_src_path = os.path.join(self.src,file_name)
        full_dist_path = os.path.join(self.dist, file_name)
        if os.path.isfile(full_src_path) and os.path.splitext(full_src_path)[-1].lower() == '.txt':
            with open(full_dist_path, 'w', encoding='utf-8') as f_dist:
                print("开始备份{0}".format(file_name))
                with open(full_src_path,'r',encoding='utf-8') as f_src:
                    while True:
                        rest = f_src.read(100)
                        if not rest:
                            break
                        f_dist.write(rest)
                    f_dist.flush()
                print("备份完成{0}".format(file_name))
        else:
            print("文件类型不符合备份要求，跳过>>")

if __name__ == '__main__':
    base_path = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_path,'src')
    dist_path =  os.path.join(base_path,'dist')
    bak = FileBackup()

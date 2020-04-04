from done.example import Student, Teacher, Course

# 提示
def introduction(str):
    print("{0}{1}{2}".format('*'*20, str, '*'*20))

#返回课程列表
def prepare_course():
    course = {
        "01": "网络爬虫",
        "02": "数据分析",
        "03": "人工智能",
        "04": "机器学习",
        "05": "云计算",
        "06": "大数据",
        "07": "图像识别",
        "08": "Web开发"
    }
    ls = []
    for k,v in course.items():
        cs = Course(k, v)
        ls.append(cs)
    return ls

#返回教师列表
def create_teacher():
    teachers = [
        ["T1", "张亮", "13301122001"],
        ["T2", "王朋", "13301122002"],
        ["T3", "李旭", "13301122003"],
        ["T4", "黄国发", "13301122004"],
        ["T5", "周勤", "13301122005"],
        ["T6", "谢富顺", "13301122006"],
        ["T7", "贾教师", "13301122007"],
        ["T8", "杨教师", "13301122008"]
    ]
    ls = []
    for x in teachers:
        ts = Teacher(x[0], x[1], x[2])
        ls.append(ts)
    return ls

#课程与教师逐一绑定
def course_to_teacher():
    ls = []
    ls_course = prepare_course()
    ls_teacher = create_teacher()
    for x in range(0,len(ls_course)):
        v = ls_course[x].binding(ls_teacher[-1-x])
        ls.append(v)
    return ls

# 创建学生列表
def create_student():
    ls_student = ["小亮", "小明", "李红", "小丽", "Jone", "小彤", "小K", "慕慕"]
    rg = list(range(1000, 1008))
    ls = []
    lenth = len(ls_student)
    for x in range(0,lenth):
        s = Student(rg[x], ls_student[-1-x])
        ls.append(s)
    return ls

if __name__ == '__main__':
    cts = course_to_teacher()
    students = create_student()
    introduction("慕课学院（1）班学生信息")
    for x in students:
        print(x.__str__())
    introduction("慕课学院（1）班选课结果")
    for y in range(0, len(cts)):
        students[y].add_course(cts[y])
    for z in students:
        print("Name：{0}, Selected：{1}".format(z.name, z.course_detail()))
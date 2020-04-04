class Student(object):
    """学生类"""
    def __init__(self, s_number, name, select_course = []):
        self.s_number = s_number
        self.name = name
        self.__select_course = select_course

    """课程详情"""
    def course_detail(self):
        return self.__select_course

    """添加课程信息"""
    def add_course(self, cour_info):
        ls = []
        ls.append(cour_info)
        self.__select_course = ls

    def __str__(self):
        return "name:{0},s_number:{1}".format(self.name, self.s_number)

class Teacher(object):
    """
    教师类
    """
    def __init__(self, t_number, name, phone):
        self.t_number = t_number
        self.name = name
        self.phone = phone

    def __str__(self):
        return "name:{0},t_number:{1}".format(self.name, self.t_number)

class Course(object):
    """
    课程类
    """

    def __init__(self, c_number, name, teacher=None):
        self.c_number = c_number
        self.name = name
        self.teacher = teacher

    """
    绑定授课教师功能
    """
    def binding(self, teacher):
        if isinstance(teacher, Teacher):
            return {'课程名称': self.name, '教师名称':  teacher.name}
        else:
            return None


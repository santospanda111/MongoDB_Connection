from models import *

class ClassRoom:
    student = StudentData()
    teacher = TeacherData()

    def insert_data_student(self, id,name,age,grade,date):
        """[This method will insert data]

        Args:
            value ([data])

        Returns:
            [count]: [No of data.]
        """
        self.student.delete()
        self.student.id = id
        self.student.name = name
        self.student.age = age
        self.student.grade = grade
        self.student.date_added_on = date
        self.student.save()
        return StudentData.objects.count()

    def update_data_student(self, value):
        """
        :param value: value to be inserted to update
        :return: count of rows after update
        """
        self.student.update(name= value)
        for student in StudentData.objects:
            name_is = student.name
        return name_is

    def read_data_student(self):
        count = 0
        """
        :return: count of rows after read the data
        """
        for student in StudentData.objects:
            print(student)
            count+=1
        return count

    def delete_data_student(self):
        """
        :return: count of rows after delete
        """
        self.student.delete()
        return StudentData.objects.count()

    def insert_data_teacher(self, id,name,subject,date):
        """[This method will insert data]

        Args:
            value ([data])

        Returns:
            [count]: [No of data.]
        """
        self.teacher.delete()
        self.teacher.id = id
        self.teacher.teacher_name = name
        self.teacher.subject = subject
        self.teacher.date_added_on = date
        self.teacher.save()
        return TeacherData.objects.count()

    def update_data_teacher(self, value):
        """
        :param value: value to be inserted to update
        :return: value after update
        """
        self.teacher.update(teacher_name= value)
        for teacher in TeacherData.objects:
            name_is = teacher.teacher_name
        return name_is

    def read_data_teacher(self):
        count = 0
        """
        :return: count of rows after read the data
        """
        for teacher in TeacherData.objects:
            print(teacher)
            count+=1
        return count

    def delete_data_teacher(self):
        """
        :return: count of rows after delete
        """
        self.teacher.delete()
        return TeacherData.objects.count()
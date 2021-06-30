
from input_data import ClassRoom
from datetime import date

from input_data import *

class TestInputData:
    input_object = ClassRoom()

    def test_insert_data_student(self):
        """[This method will insert data]

        Args:
            value ([data])

        Returns:
            [count]: [No of data.]
        """
        id = 1
        name = "Santosh kumar panda"
        age = 26
        grade = "Twelveth"
        date1 = date.today()
        count = self.input_object.insert_data_student(id,name,age,grade,date1)
        assert count == 1, "Insertion unsuccessful"

    def test_update_data_student(self):
        """
        :param value: value to be inserted to update
        :return: count of rows after update
        """
        value = "Soumya"
        result = self.input_object.update_data_student(value)
        assert value == result, "Updation unsuccessful"

    def test_read_data_student(self):
        """
        :return: count of rows after read the data
        """
        count = self.input_object.read_data_student()
        assert count == 1, "Couldn't Read data"

    def test_delete_data_student(self):
        """
        :return: count of rows after delete
        """
        count = self.input_object.delete_data_student()
        assert count == 0, "Couldn't delete data"


    def test_insert_data_teacher(self):
        """[This method will insert data]

        Args:
            value ([data])

        Returns:
            [count]: [No of data.]
        """
        id = 1
        name = "Ashis"
        subject = "Python"
        date1 = date.today()
        count = self.input_object.insert_data_teacher(id,name,subject,date1)
        assert count == 1, "Insertion unsuccessful"

    def test_update_data_teacher(self):
        """
        :param value: value to be inserted to update
        :return: count of rows after update
        """
        value = "Ashis Ogale"
        result = self.input_object.update_data_teacher(value)
        assert value == result, "Updation unsuccessful"

    def test_read_data_teacher(self):
        """
        :return: count of rows after read the data
        """
        count = self.input_object.read_data_teacher()
        assert count == 1, "Couldn't Read data"

    def test_delete_data_teacher(self):
        """
        :return: count of rows after delete
        """
        count = self.input_object.delete_data_teacher()
        assert count == 0, "Couldn't delete data"

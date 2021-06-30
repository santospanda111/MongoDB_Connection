from mongoengine import connect,Document,StringField,IntField,DateTimeField,ReferenceField
"""
-Imported mongoengine module.
-To get connection with database i have used connect()
-Through client i have created School database.
"""
connect(db='SchoolProject')

class StudentData(Document):
    id = IntField(primary_key = True)
    name = StringField(max_length=50)
    age = IntField()
    grade = StringField(max_length=50)
    date_added_on = DateTimeField()

class TeacherData(Document):
    id = IntField(primary_key = True)
    student_id = ReferenceField(StudentData)
    teacher_name = StringField(max_length=50)
    subject = StringField(max_length=50)
    date_added_on = DateTimeField()
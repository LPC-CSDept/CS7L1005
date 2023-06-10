
class Student:
    numofStudent = 0

    def __init__(self, sid, name):
        self._id = sid
        self._name = name
        Student.numofStudent += 1

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def __del__(self):
        Student.numofStudent -= 1
        del self

    def __str__(self):
        return (f'Student id: {self.id:>10} \t name: {self.name:>10}')


def makeStudent(student_dict_list):
    slist = []
    for student in student_dict_list:
        sid = student['id']
        name = student['name']
        s = Student(sid, name)
        slist.append(s)
    return slist


def deleteOneStudent(slist, did):
    for i, student in enumerate(slist):
        if student.id == did:
            print('-->Deleted', student)
            del student
            del slist[i]
            # Student.numofStudent -= 1


def main():

    student_dict_list = [{'id': 1001, 'name': 'John'},
                         {'id': 1002, 'name': 'James'},
                         {'id': 1003, 'name': 'Mark'},
                         {'id': 1004, 'name': 'Matthew'},
                         {'id': 1005, 'name': 'Arnold'}]
    slist = makeStudent(student_dict_list)
    print(f'\n**** Total number of students: {Student.numofStudent}')
    for s in slist:
        print(s)

    # Delete one object
    did = 1003
    deleteOneStudent(slist, did)
    print(f'\n**** Total number of students: {Student.numofStudent}')
    for s in slist:
        print(s)


if __name__ == '__main__':
    main()

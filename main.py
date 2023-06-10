
class Student:
    numofStudent = 0

    def __str__(self):
        return (f'Student id: {self.id:>10} \t name: {self.name:>10}')
    """
    ########################################
    Code Your Program here
    ########################################
    """


def makeStudent(student_dict_list):
    """
    ########################################
    Code Your Program here
    ########################################
    """


def deleteOneStudent(slist, did):
    """
    ########################################
    Code Your Program here
    ########################################
    """


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

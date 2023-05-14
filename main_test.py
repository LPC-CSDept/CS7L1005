import main
import io
import sys
import re
import math
import types


def test_main_1():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    student_dict_list = [{'id': 1001, 'name': 'John'},
                         {'id': 1002, 'name': 'James'},
                         {'id': 1003, 'name': 'Mark'},
                         {'id': 1004, 'name': 'Matthew'},
                         {'id': 1005, 'name': 'Arnold'}]
    slist = main.makeStudent(student_dict_list)
    print(f'\n**** Total number of students: {main.Student.numofStudent}')
    for s in slist:
        print(s)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    assert len(slist) == 5, "Length must be 5"
    assert main.Student.numofStudent == 5, 'Class variable numofStudent must be 5'
    assert slist[0].id == 1001
    assert slist[4].id == 1005

    main.deleteOneStudent(slist, 1003)
    assert len(slist) == 4, 'Length must be 4'
    assert main.Student.numofStudent == 4, 'Class variable numofStudent must be 4'
    assert slist[2].id == 1004

    print(f'\n**** Total number of students: {main.Student.numofStudent}')
    for s in slist:
        print(s)

    # regex_string = r'[\w,\W]*Elapsed'
    # regex_string += r'[\w,\W]*time'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())

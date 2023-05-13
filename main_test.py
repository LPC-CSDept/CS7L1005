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

    ret = main.factorial(10)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*Elapsed'
    # regex_string += r'[\w,\W]*time'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())

    assert ret == 362880


def test_main_2():
    captureOut = io.StringIO()
    sys.stdout = captureOut
    # datastr = 'Kim \n 100 80 70 60\n Bill \n 100 90 80 60 \n Mary \n 90 80 70 100'
    # sys.stdin = io.StringIO(datastr)

    fact = main.deco_fact(main.factorial)
    ret = fact(10)

    sys.stdout = sys.__stdout__
    print('Captured ', captureOut.getvalue())
    lines = captureOut.getvalue().split('\n')
    print(lines)

    # regex_string = r'[\w,\W]*Elapsed'
    # regex_string += r'[\w,\W]*time'
    # regex_string += r'[\w,\W]*'
    # print(regex_string)
    # res = re.search(regex_string, lines[1])
    # assert res != None
    # print(res.group())

    assert ret == 362880

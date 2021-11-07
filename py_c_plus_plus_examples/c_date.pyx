# distutils: language = c++

cdef extern from "c_date/c_src/date.cpp":
    pass

'''
except + mean if the C++ code or the initial memory allocation raises an exception due to a failure, this will let
Cython safely raise an appropriate Python exception
'''

cdef extern from "c_date/c_src/date.h":
    cdef cppclass Date:
        Date(int, int, int) except +
        int year, month, day
        int getYear()
        int getMonth()
        int getDay()
        void print_all()
        void SetDate(int, int, int)
        char* getCurrentDate()


cdef class PyDate:
    # if your class have constructor you must set `*` after class name and `new` in `__init__`
    cdef Date* c_date

    def __init__(self, year, month, day):
        self.c_date = new Date(year, month, day)

    def __cinit__(self, int year, int month, int day):
        self.c_date = new Date(year, month, day)

    def getYear(self):
        return self.c_date.getYear()

    def getMonth(self):
        return self.c_date.getMonth()

    def getDay(self):
        return self.c_date.getDay()

    def print_all(self):
        self.c_date.print_all()

    def SetDate(self, year, month, day):
        self.c_date.SetDate(year, month, day)

    def getCurrentDate(self):
        return self.c_date.getCurrentDate().decode()

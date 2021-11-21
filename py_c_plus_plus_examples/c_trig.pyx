###################################################
###################################################
###################################################
##### imports from trig.h and trig.cpp ############
###################################################
###################################################
###################################################

# if you defined functions in `.cpp` and `.h` etc

# just added to incl the .cpp in the build
cdef extern from "c_trig/c_src/trig.cpp":
    pass

# Redeclare the trig.h in cython space
# You can remove `namespace "trig"`, but don't forget remove it from `.cpp` and `.h` file
cdef extern from "c_trig/c_src/trig.h" namespace "trig":
    double sinh_impl(double x);
    double cosh_impl(double x);
    double tanh_impl(double x);


###################################################
###################################################
###################################################
###################################################
###################################################
###################################################



###################################################
###################################################
###################################################
###################################################
##### without using a cython Class ################
###################################################
###################################################
###################################################


'''
simple pure python wrapping
use normal def if your cython code dont need to do anything else but wrapping it
returns double as python object float
'''

# after can be imported after build
def py_sinh_impl(double x):
    return sinh_impl(x)  # sinh_impl - c++ func

def py_cosh_impl(double x):
    return cosh_impl(x) # cosh_impl - c++ func

def py_tanh_impl(double x):
    return tanh_impl(x) # tanh_impl - c++ func

'''
cython based functions (no call overhead)
can only be used from cython
use when u need to write your own cython functions and dont want python overhead,
but also want it to be **private from normal python space**
'''

cdef double c_sinh_impl(double x):
    return sinh_impl(x) * 2.0
    
cdef double c_cosh_impl(double x):
    return cosh_impl(x) * 2.0

cdef double c_tanh_impl(double x):
    return tanh_impl(x) * 2.0



# no overhead inside the python function and finally returns as python object float
def mixed_test(double x):
    cdef double s_impl = sinh_impl(x)
    cdef double c_impl = cosh_impl(x)
    cdef double t_impl = tanh_impl(x)

    return s_impl + c_impl + t_impl


# same as mixed_test but using the cdef functions instead, still no overhead inside the function
def mixed_test2(double x):

    cdef double s_impl = c_sinh_impl(x) + 2.0
    cdef double c_impl = c_cosh_impl(x) + 3.0
    cdef double t_impl = c_tanh_impl(x) + 4.0

    return (s_impl + c_impl + t_impl) * 2.0


###################################################
###################################################
###################################################
############ using a cython Class #################
### imported as normal python class afterwards ####
###################################################
###################################################
###################################################


cdef class PyTrig:

    cdef double value  # define double value

    def __init__(self, value):
        self.value = value

    '''
    simple pure python wrapping
    use normal def if your cython code don't need to do anything else but wrapping it
    returns double as python object float
    '''

    def sinh_impl(self):
        return sinh_impl(self.value)

    def cosh_impl(self):
        return cosh_impl(self.value)

    def tanh_impl(self):
        return tanh_impl(self.value)


    # no overhead inside the python function and finally returns as python object float
    def mixed_test(self):
        cdef double x = self.value

        cdef double s_impl = tanh_impl(x)
        cdef double c_impl = cosh_impl(x)
        cdef double t_impl = tanh_impl(x)

        return s_impl + c_impl + t_impl

    # no overhead inside the python function using the internal cdef functions and finally returns as python object float
    def mixed_test2(self):
        cdef double s_impl = self.c_sinh_impl()
        cdef double c_impl = self.c_cosh_impl()
        cdef double t_impl = self.c_tanh_impl()

        return (s_impl + c_impl + t_impl) * 2.0

    def mixed_test3(self):
        cdef double x = self.value

        cdef double s_impl = self.c_sinh_impl2(x)
        cdef double c_impl = self.c_cosh_impl2(x)
        cdef double t_impl = self.c_tanh_impl2(x)

        return (s_impl + c_impl + t_impl) * 2.0

    '''
    cython based functions (no call overhead)
    can only be used from cython
    use when u need to write your own cython functions and don't want python overhead, but want to be private
    from normal python space
    '''

    cdef double c_sinh_impl(self):
        return sinh_impl(self.value) * 2.0
    
    cdef double c_cosh_impl(self):
        return cosh_impl(self.value) * 2.0

    cdef double c_tanh_impl(self):
        return tanh_impl(self.value) * 2.0


    cdef double c_sinh_impl2(self, double x):
        return sinh_impl(self.value) + x * 2.0
        
    cdef double c_cosh_impl2(self, double x):
        return cosh_impl(self.value) + x * 2.0

    cdef double c_tanh_impl2(self, double x):
        return tanh_impl(self.value) + x * 2.0


    '''
    cython based functions (no call overhead, when called from cython)
    but normal python overhead when used from normal python
    can be used from cython and python
    '''

    # about cpdef: https://cython.readthedocs.io/en/latest/src/userguide/language_basics.html#cpdef
    cpdef double cp_sinh_impl(self, double x):
        return sinh_impl(x)
    
    cpdef double cp_cosh_impl(self, double x):
        return cosh_impl(x)

    cpdef double cp_tanh_impl(self, double x):
        return tanh_impl(x)

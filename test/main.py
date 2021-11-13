# Do not run this file in the project folder, otherwise the folder above will be imported

from py_c_plus_plus_examples import c_date
from py_c_plus_plus_examples.c_trig import PyTrig, py_sinh_impl, py_cosh_impl, py_tanh_impl, mixed_test, mixed_test2
from py_c_plus_plus_examples.c_rect import PyRectangle
from py_c_plus_plus_examples.c_dlib import PyDlibLandmark

print(f'{"#" * 10} C++ date example {"#" * 10}')

date = c_date.PyDate(2021, 25, 10)
print(date.getYear(), date.getMonth(), date.getDay())
date.print_all()
date.SetDate(2022, 30, 12)
date.print_all()
print(date.getCurrentDate())

print(f'{"#" * 10} C++ example of trigonometry {"#" * 10}')

print(f'{"#" * 5} Functions form `.h` {"#" * 5}')
print(f'sinh: {py_sinh_impl(2.0)}')
print(f'cosh: {py_cosh_impl(2.0)}')
print(f'tanh: {py_tanh_impl(2.0)}')

print(f'\n{"#" * 5} Mixed test that using functions from `.h` {"#" * 5}')
print(f'mixed_test: {mixed_test(2.0)}')

print(f'\n{"#" * 5} Mixed test same is above but using cdef instead of pure python def {"#" * 5}')
print(f'mixed_test2: {mixed_test2(2.0)}')

py_trig = PyTrig(2.0)

print(f'\n{"#" * 5} PyTrig functions {"#" * 5}')
print(f'sinh: {py_trig.sinh_impl()}')
print(f'cosh: {py_trig.sinh_impl()}')
print(f'tanh: {py_trig.sinh_impl()}')

print(f'\n{"#" * 5} PyTrig mixed tests {"#" * 5}')
print(f'mixed_test: {py_trig.mixed_test2()}')
print(f'mixed_test2: {py_trig.mixed_test2()}')

print(f'\n{"#" * 5} PyTrig functions that uses cpdef {"#" * 5}')
print(f'sinh: {py_trig.cp_sinh_impl(2.0)}')
print(f'cosh: {py_trig.cp_cosh_impl(2.0)}')
print(f'tanh: {py_trig.cp_tanh_impl(2.0)}')

print(f'\n{"#" * 5} C++ example of Rectangle {"#" * 5}')

py_rect = PyRectangle(1, 2, 3, 4)

print(f'area: {py_rect.get_area()}')
py_rect.move(1, 2)
print(f'size: {py_rect.get_size()}')

PyDlibLandmark().run("<path>/shape_predictor_68_face_landmarks.dat".encode(), "<path>/face.<extension>".encode())

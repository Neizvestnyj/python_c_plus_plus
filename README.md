# Python C++

# Installation:
```bash
git clone https://github.com/Neizvestnyj/python_c_plus_plus
cd python_c_plus_plus
python3 setup.py install
```
or

```bash
pip install https://github.com/Neizvestnyj/python_c_plus_plus/archive/master.zip
```

# Android
[How use buildozer](https://buildozer.readthedocs.io/en/latest/installation.html) 
and [python for android](https://python-for-android.readthedocs.io/en/latest/quickstart/)

Move `recipes/<platform>/py_c_plus_plus_examples` to 
`<AppFolder>/.buildozer/android/platform/python-for-android/pythonforandroid/recipes`

**buildozer.spec**

`requirements = kivy==2.0.0, py_c_plus_plus_examples`

```bash 
buildozer android debug
```

# Usage
```python
from py_c_plus_plus_examples import c_date, c_trig

date = c_date.PyDate(1997, 31, 12)
date.print_all()
print(date.getCurrentDate())

print(f'sinh: {c_trig.py_sinh_impl(2.0)}')
print(f'cosh: {c_trig.py_cosh_impl(2.0)}')
print(f'tanh: {c_trig.py_tanh_impl(2.0)}')
```

# Why this project was created?
The project was created so that the [dlib](https://github.com/davisking/dlib) library could be used in 
[p4a](https://github.com/kivy/python-for-android), using a module that uses `c++` functions from this library.
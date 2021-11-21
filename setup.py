# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html
# https://github.com/Technologicat/setup-template-cython/blob/master/setup.py

from setuptools import setup, Extension

import sys
import os
from pathlib import Path
import platform

try:
    from Cython.Build import cythonize
except (ImportError, ModuleNotFoundError) as import_cython_error:
    sys.exit(
        "Cython not found. Cython is needed to build the extension modules. "
        "Type: pip install cython or pip install -r requirements.txt"
    )

__version__ = '0.1'
__name__ = 'py_c_plus_plus_examples'

current_dir = Path(__file__).absolute().parent
py_c_plus_plus_examples_dir = os.path.join(current_dir, __name__)
print(f"py_c_plus_plus_examples_dir: {py_c_plus_plus_examples_dir}")

DEBUG = False

if DEBUG:
    import shutil
    import os

    # remove build dirs
    rm_dirs = ['build', 'dist', 'py_c_plus_plus_examples.egg-info']
    for dir_ in rm_dirs:
        dir_ = os.path.join(current_dir, dir_)

        try:
            if os.path.exists(dir_):
                shutil.rmtree(dir_)
                print(f'{dir_} removed')
        except Exception as del_err:
            print(del_err)

if platform.system() in ['Windows']:
    extra_compile_args = []
else:
    extra_compile_args = ['-std=c++11', '-ljpeg', '-lpng']

with open(os.path.join(current_dir, 'requirements.txt')) as req_f:
    requirements = []
    lines = req_f.readlines()

    for line in lines:
        requirements.append(line.replace('\n', '').strip())

extensions = [
    Extension(f'{__name__}.c_date', [f'{py_c_plus_plus_examples_dir}/c_date.pyx']),
    Extension(f'{__name__}.c_trig', [f'{py_c_plus_plus_examples_dir}/c_trig.pyx']),
    Extension(f'{__name__}.c_rect', [f'{py_c_plus_plus_examples_dir}/c_rect.pyx']),
    Extension(
        f'{__name__}.c_dlib', [f'{py_c_plus_plus_examples_dir}/c_dlib.pyx'],
        extra_compile_args=extra_compile_args,
        library_dirs=[],  # path to .a or .so file(s)
        libraries=["dlib"],
    ),
]

for e in extensions:
    e.cython_directives = {'language_level': "3"}  # all are Python-3
    e.language = "c++"

setup(name=__name__,
      version=__version__,
      author="Neizvestnyj and psychowasp",
      url=f'https://github.com/Neizvestnyj/{__name__}',
      description='C++ extension for Python',
      platforms=['all'],
      license='GPL-3.0 License',
      keywords=["python c++ example using cython"],
      # it is necessary to add `py_c_plus_plus_examples/__init__.py` to the package folder
      packages=[__name__],
      ext_modules=cythonize(extensions),
      install_requires=requirements,
      # Disable zip_safe, because:
      #   - Cython won't find `.pxd` files inside installed .egg, hard to compile libs depending on this one
      #   - dynamic loader may need to have the library unzipped to a temporary directory anyway (at import time)
      zip_safe=False,
      python_requires=">=3.6",
      )

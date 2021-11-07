# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

__version__ = '0.1'

extensions = [
    Extension('py_c_plus_plus_examples.c_date', ['py_c_plus_plus_examples/c_date.pyx']),
    Extension('py_c_plus_plus_examples.c_trig', ['py_c_plus_plus_examples/c_trig.pyx']),
]

setup(name='py_c_plus_plus_examples',
      version=__version__,
      ext_modules=cythonize(extensions),
)

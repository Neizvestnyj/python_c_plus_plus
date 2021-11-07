# https://cython.readthedocs.io/en/latest/src/userguide/source_files_and_compilation.html

from distutils.core import setup
from distutils.extension import Extension

try:
    from Cython.Build import cythonize
except (ImportError, ModuleNotFoundError) as import_cython_error:
    print('Please, install cython')

__version__ = '0.1'
__name__ = 'py_c_plus_plus_examples'

with open('requirements.txt') as req_f:
    requirements = []
    lines = req_f.readlines()
    for line in lines:
        requirements.append(line.replace('\n', '').strip())

extensions = [
    Extension(f'{__name__}.c_date', [f'{__name__}/c_date.pyx']),
    Extension(f'{__name__}.c_trig', [f'{__name__}/c_trig.pyx']),
]

setup(name=__name__,
      version=__version__,
      url=f'https://github.com/Neizvestnyj/{__name__}',
      description='C++ extension for Python',
      platforms=['all'],
      license='GPL-3.0 License',
      ext_modules=cythonize(extensions),
      install_requires=requirements,
      python_requires=">=3.0",
      )

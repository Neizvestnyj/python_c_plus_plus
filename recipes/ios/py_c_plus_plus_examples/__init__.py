from kivy_ios.recipe import CythonRecipe


class CPackageRecipe(CythonRecipe):
    site_packages_name = 'py_c_plus_plus_examples'
    version = '0.1'
    # url = '' # path to setup.py
    depends = ['setuptools', 'cython']
    call_hostpython_via_targetpython = False


recipe = CPackageRecipe()

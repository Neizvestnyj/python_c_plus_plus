from pythonforandroid.recipe import CythonRecipe, IncludedFilesBehaviour


class CPackageRecipe(IncludedFilesBehaviour, CythonRecipe):
    site_packages_name = 'py_c_plus_plus_examples'
    version = '0.1'
    # url = ''
    src_filename = "py_c_plus_plus_examples"  # path to py_c_plus_plus_examples folder
    depends = ['setuptools', 'cython']
    call_hostpython_via_targetpython = False


recipe = CPackageRecipe()

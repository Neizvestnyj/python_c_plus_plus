from pythonforandroid.recipe import IncludedFilesBehaviour, CppCompiledComponentsPythonRecipe

'''
using `CppCompiledComponentsPythonRecipe` instead of `CythonRecipe` because he did not work correct
don't use `install_in_hostpython = True` because it provokes an `setuptools` error
`import _distutils_hack.override # noqa: f401`
'''


class CPlusPlusRecipe(IncludedFilesBehaviour, CppCompiledComponentsPythonRecipe):
    version = '0.1'
    name = 'py_c_plus_plus_examples'

    src_filename = "<path_to>/py_c_plus_plus_examples"

    depends = ['setuptools', 'cython']

    call_hostpython_via_targetpython = False  # as default

    def get_recipe_env(self, arch):
        env = super().get_recipe_env(arch)
        env['LDFLAGS'] += ' -lc++_shared'
        return env


recipe = CPlusPlusRecipe()

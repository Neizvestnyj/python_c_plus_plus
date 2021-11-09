from kivy.lang import Builder
from kivy.app import App
from kivy.uix.popup import Popup

from py_c_plus_plus_examples import c_date
from py_c_plus_plus_examples.c_trig import PyTrig, py_sinh_impl, py_cosh_impl, py_tanh_impl, mixed_test, mixed_test2
from py_c_plus_plus_examples.c_rect import PyRectangle

KV = '''
<MyPopup>:
    title: 'Test C++'
    size_hint: 0.85, 0.85
    ScrollView:
        always_overscroll: False
        Label:
            id: lbl
            size_hint: None, None
            size: self.texture_size
            text: 'text'

Screen:
    Button:
        text: 'Test C++ library'
        on_release: app.test_lib()
'''


class MyPopup(Popup):
    pass


class TestApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kv = Builder.load_string(KV)
        self.popup = MyPopup()

    def build(self):
        return self.kv

    def test_lib(self):
        self.popup.open()
        text = ''
        text += f'{"#" * 10} C++ date example {"#" * 10}\n'

        date = c_date.PyDate(2021, 25, 10)

        text += str(date.getYear()) + '.' + str(date.getMonth()) + '.' + str(date.getDay()) + '\n'
        text += date.getCurrentDate() + '\n'

        text += f'{"#" * 10} C++ example of trigonometry {"#" * 10}\n'

        text += f'{"#" * 5} Functions form `.h` {"#" * 5}\n'
        text += f'sinh: {py_sinh_impl(2.0)}\n'
        text += f'cosh: {py_cosh_impl(2.0)}\n'
        text += f'tanh: {py_tanh_impl(2.0)}\n'

        text += f'\n{"#" * 5} Mixed test that using functions from `.h` {"#" * 5}\n'
        text += f'mixed_test: {mixed_test(2.0)}\n'

        text += f'\n{"#" * 5} Mixed test same is above but using cdef instead of pure python def {"#" * 5}\n'
        text += f'mixed_test2: {mixed_test2(2.0)}\n'

        py_trig = PyTrig(2.0)

        text += f'\n{"#" * 5} PyTrig functions {"#" * 5}\n'
        text += f'sinh: {py_trig.sinh_impl()}\n'
        text += f'cosh: {py_trig.sinh_impl()}\n'
        text += f'tanh: {py_trig.sinh_impl()}\n'

        text += f'\n{"#" * 5} PyTrig mixed tests {"#" * 5}\n'
        text += f'mixed_test: {py_trig.mixed_test2()}\n'
        text += f'mixed_test2: {py_trig.mixed_test2()}\n'

        text += f'\n{"#" * 5} PyTrig functions that uses cpdef {"#" * 5}\n'
        text += f'sinh: {py_trig.cp_sinh_impl(2.0)}\n'
        text += f'cosh: {py_trig.cp_cosh_impl(2.0)}\n'
        text += f'tanh: {py_trig.cp_tanh_impl(2.0)}\n'

        text += f'\n{"#" * 5} C++ example of Rectangle {"#" * 5}\n'
        py_rect = PyRectangle(1, 2, 3, 4)

        text += f'area: {py_rect.get_area()}\n'
        text += f'size: {py_rect.get_size()}\n'

        self.popup.ids.lbl.text = text


if __name__ == '__main__':
    TestApp().run()

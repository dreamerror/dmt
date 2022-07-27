import pybind11
from distutils.core import setup, Extension

ext_modules = [
    Extension(
        'logic',  # название нашей либы
        ['math\main.cpp'],  # файлики которые компилируем
        include_dirs=[pybind11.get_include()],
        language='c++',
        extra_compile_args=['-std=c++11'],
    ),
]

setup(
    name='logic',
    version='0.1.2',
    author='user',
    author_email='user@user.ru',
    description='pybind11 extension',
    ext_modules=ext_modules,
    requires=['pybind11']
)

from setuptools import Extension
from setuptools import setup


module = Extension("spam", sources=["spam.c"], extra_compile_args=["-Wall"])

setup(
    name="spam",
    version="1.0.0",
    description="An example Python C extension module",
    url="https://github.com/jalan/spam",
    author="Jason Alan Palmer",
    author_email="jalanpalmer@gmail.com",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    ext_modules=[module],
    test_suite="tests",
)

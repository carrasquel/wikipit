"""Setup specifications for gitignore project."""

from os import path

from setuptools import setup


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="wikipit",
    version="1.0.1",
    description="A Command Line Tool to Search Wikipedia in the terminal.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/carrasquel/wikipit",
    author="Nelson Carrasquel",
    license='MIT',
    author_email="carrasquel@outlook.com",
    py_modules=["wikipit"],
    entry_points={
        "console_scripts": [
            "wikipit = wikipit:wiki"
        ]
    },
    install_requires=[
        "wikipedia",
        "Click"
    ]
)
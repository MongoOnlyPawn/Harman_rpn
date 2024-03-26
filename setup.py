from setuptools import setup

setup(
    name="rpn",
    version="0.1",
    py_modules=['main', 'rpn_calc', 'menu'],
    install_requires=open(
        "requirements.txt"
    ).readlines(),
    entry_points={
        "console_scripts": [
            "rpn = main:main",
        ],
    },
)

from setuptools import setup, find_packages


setup(
    name='rc-cli',
    version='0.1',
    author='Shlomo Tadela',
    py_modules=['reactive-cells-cli'],
    install_requires=[
        'Click', 'pymongo'
    ],
    entry_points='''
        [console_scripts]
        reactive-cells-cli=cli:cli
    ''',
)

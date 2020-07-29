from setuptools import setup

setup(
    name = "sample",
    version = '0.1',
    install_requires = ['Click',],
    py_modules = ['sample'],
    entry_points = '''
    [console_scripts]
    postgresql_start = sample:start
    postgresql_status = sample:status
    postgresql_stop = sample:stop    
    '''
)
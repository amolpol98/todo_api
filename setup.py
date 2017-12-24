from distutils.core import setup

setup(
    name='todo_api',
    version='0.1',
    description='A ToDo List API built with Django REST Framework',
    author='Amol Pol',
    author_email='amolpol98@gmail.com',
    url='https://github.com/amolpol98/todo_api.git',
    #packages=find_packages(),
    install_requires=[
        'Django==1.11.4',
        'djangorestframework==3.6.3',
        'pytz==2017.2',
    ]
)

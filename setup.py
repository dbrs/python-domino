from distutils.core import setup

setup(
    name='python-domino-dbrs',
    version='0.0.5',
    author='DBRS',
    author_email='modelsupport@dbrs.com',
    packages=['domino', 'domino.response_objects'],
    scripts=[],
    url='http://www.dbrs.com',
    license='LICENSE.txt',
    description='Python bindings for the Domino API',
    long_description='',
    install_requires=[
        'requests>=2.4.2'
    ]
)

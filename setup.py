import codecs
import os

from setuptools import setup, find_packages


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


VERSION = (0, 9, 0)
version = '.'.join(map(str, VERSION))

setup(
    name='python-quickbooks',
    version=version,
    author='Edward Emanuel Jr.',
    author_email='edward.emanuel@gmail.com',
    description='A Python library for accessing the QuickBooks API.',
    url='https://github.com/ej2/python-quickbooks',
    license='MIT',
    keywords=['quickbooks', 'qbo', 'accounting'],
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    test_runner='nosetests',
    entry_points={
        'console_scripts': ['quickbooks-cli=quickbooks.tools.cli:cli_execute']
    },

    install_requires=[
        'setuptools',
        'intuit-oauth==1.2.4',
        'rauth>=0.7.3',
        'authclient',
        'requests>=2.26.0',
        'simplejson>=3.17.0',
        'six>=1.14.0',
        'python-dateutil',
        'pycparser==2.18'
    ],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    packages=find_packages(),
)

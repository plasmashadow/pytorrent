from setuptools import setup
import os


def Readme():
    return open(os.path.join(os.path.dirname(__file__), 'README.md'), "r").read()

setup(
    name='pytorrent',
    packages=['pytorrent'],
    version='0.0.5',
    description='Pythonic way of Bittorrent',
    long_description=Readme(),
    author='plasmashadow',
    author_email='plasmashadowx@gmail.com',
    url='https://github.com/plasmashadow/pytorrent.git',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Intended Audience :: Developers'
    ],
    install_requires=['six', 'mock'],
    include_package_data=True,
    license='BSD License',
)
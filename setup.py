# https://packaging.python.org/tutorials/packaging-projects/#creating-setup-py

from setuptools import setup, find_packages

# with open('README.rst') as f:
#     readme = f.read()

# with open('LICENSE') as f:
#     license = f.read()

setup(
    name='sample project',
    version='0.1.0',
    description='Boiler in Python',
    long_description='',
    long_description_content_type="text/markdown",
    author='Carlos Aparicio',
    author_email='carlos_non86@msn.com',
    url='',
    license='',
    python_requires='>=3.6',
    packages=find_packages(
        exclude=('tests', 'docs', 'venv', '.vscode', 'sample_package')),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)

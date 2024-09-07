from setuptools import setup, find_packages

setup(
	name='assignment0',
	version='1.0',
	author='Vivek Milind Aher',
	author_email='yvaher@ufl.edu',
	packages=find_packages(exclude=('tests', 'docs')),
	setup_requires=['pytest-runner'],
	tests_require=['pytest']	
)
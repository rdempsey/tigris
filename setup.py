from setuptools import setup
import re


def get_version():
    with open('tigris/version.py') as version_file:
        return re.search(r"""__version__\s+=\s+(['"])(?P<version>.+?)\1""",
                         version_file.read()).group('version')


def readme():
    """Returns README.rst contents as str"""
    with open('README.rst') as f:
        return f.read()


install_requires = [
    'click>=7.0'
]

tests_require = [
    'mock',
    'pytest',
    'pytest-cov'
]

lint_requires = [
    'pep8'
]

extras_require = {
    'test': tests_require,
    'all': install_requires + tests_require,
    'docs': ['sphinx'] + tests_require,
    'lint': lint_requires
}

setup(
    name='tigris',
    version=get_version(),
    description='Automating things with Python',
    long_description=readme(),
    author='Robert Dempsey',
    author_email='robertonrails@gmail.com',
    license='MIT',
    url='https://github.com/rdempsey/tigris',
    keywords=['python', 'automation'],
    packages=['tigris'],
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require=extras_require,
    zip_safe=True,
    include_package_data=True,
    entry_points='''
            [console_scripts]
            tigris=tigris.tigris:cli
        ''',
)

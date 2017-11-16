from setuptools import setup, find_packages

setup(
    name='operator_expression_generator',
    version='1.0',

    # This automatically detects the packages in the specified
    # (or current directory if no directory is given).
    packages=find_packages(exclude=['help']),

    license="",

    # All of the following fields are PyPI metadata fields.
    # When registering a package at PyPI this is used as
    # information on the package page.
    author='Molinge',
    author_email='molingejr@gmail.com',

    description='An Operator and Expression Generator',
    long_description=""" """,
    install_requires=['PyQt5', 'pickle', 'gzip'],
    # setup_requires=['PyQt5'],
    package_data={
        # Include (markdown text) documentation files from any directory
        '': ['*.md']
    },

    classifiers=[
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',

    ]
)

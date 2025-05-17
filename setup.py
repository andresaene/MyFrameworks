from setuptools import setup, find_packages

setup(
    name='chatui',
    version='0.1.0',
    description='A library for chatbots UI',
    author='Andre Manuel Saene',
    author_email='andreidsaene7@gmail.com',
    packages=find_packages(where='src/python'),
    package_dir={'':'src/python'},
    include_package_data=True,
    install_requires=[
        'tk', # If you're using tkinter even if it comes with python
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],

    python_requires='>=3.12'
)
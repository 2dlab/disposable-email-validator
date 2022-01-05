from setuptools import setup
from setuptools import find_packages


with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='disposable_email_validator',
    version='0.0.7',
    author='Gusarov Vladislav',
    author_email='tech@2dlab.ru',
    description='Python library for disposable email validation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/2dlab/disposable-email-validator',
    packages=find_packages(),
    package_data={
        "disposable_email_validator": ['disposable_emails'],
    },
    data_files=[
        'disposable_email_validator/disposable_emails'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[]
)

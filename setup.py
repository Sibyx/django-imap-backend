import os

from setuptools import setup

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

REQUIRED = ['Django>=2.0']


def read_files(files):
    data = []
    for file in files:
        with open(file, encoding='utf-8') as my_file:
            data.append(my_file.read())
    return "\n".join(data)


meta = {}
with open('django_imap_backend/version.py', encoding='utf-8') as f:
    exec(f.read(), meta)

setup(
    name='django-imap-backend',
    version=meta['__version__'],
    packages=['django_imap_backend'],
    install_requires=REQUIRED,
    url='https://github.com/Sibyx/django_imap_backend',
    license='MIT',
    author='Jakub Dubec',
    author_email='jakub.dubec@gmail.com',
    description='IMAP backend for Django mail package',
    long_description=read_files(['README.md', 'CHANGELOG.md']),
    long_description_content_type='text/markdown',
    keywords=['django', 'mail', 'imap', 'backend', 'mailbox'],
    classifiers=[
        # As from https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Framework :: Django :: 2.0',
        'Framework :: Django :: 2.1',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: HTTP Servers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Email :: Post-Office :: IMAP',
        'Topic :: Utilities',
        'Environment :: Web Environment',
    ]
)

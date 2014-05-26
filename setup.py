import os
import sys
from setuptools import setup


if sys.argv[-1] == 'test':
    status = os.system('python tests/tests.py')
    sys.exit(1 if status > 127 else status)


requirements = ['cent>=0.2.0']


def long_description():
    return "Centrifuge integration with Django framework"


setup(
    name='adjacent',
    version='0.0.3',
    description="Centrifuge integration with Django framework",
    long_description=long_description(),
    url='https://github.com/centrifugal/adjacent',
    download_url='https://github.com/centrifugal/adjacent',
    author="Alexandr Emelin",
    author_email='frvzmb@gmail.com',
    license='MIT',
    packages=['adjacent', ],
    install_requires=requirements,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Utilities'
    ]
)

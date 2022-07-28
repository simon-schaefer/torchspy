from setuptools import find_packages
from setuptools import setup


setup(
    name='torchspy',
    version='0.0.1',
    packages=find_packages(),
    install_requires=('torch', 'pytest'),
    author='Simon Schaefer',
    author_email='simon.k.schaefer@gmail.com',
    license='MIT',
    url='https://github.com/simon-schaefer/torchspy',
    description='Linewise memory usage profiling for PyTorch.',
)

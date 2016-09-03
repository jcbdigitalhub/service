from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='service',
    version=version,
    description='Service Management',
    author='www.ossph.com',
    author_email='info@ossph.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe","erpnext"),
)

# coding: utf-8

"""
    Browser Selenium
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "RPA"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = []

setup(
    name=NAME,
    version=VERSION,
    description="Browser Selenium",
    author_email="",
    url="",
    keywords=["Selenium"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    #Overview  Browser Selenium: rpaframework browser only
    """
)

from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in credit_limit/__init__.py
from credit_limit import __version__ as version

setup(
	name="credit_limit",
	version=version,
	description="Credit Limit",
	author="zaviago",
	author_email="nabeel@zaviago.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

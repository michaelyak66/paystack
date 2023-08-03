from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in paystack/__init__.py
from paystack import __version__ as version

setup(
	name="paystack",
	version=version,
	description="paystack api",
	author="Michael Mamman",
	author_email="michaelyak66@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)

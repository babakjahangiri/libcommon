from setuptools import find_packages, setup

with open("config/requirements.txt") as requirement_file:
    requirements = requirement_file.read().split()

setup(
    name="simple_package",
    description="A libcommon package.",
    version="0.0.1",
    author="Name",
    author_email="babak@babak.uk",
    install_requires=requirements,
)

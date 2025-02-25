from setuptools import setup, find_packages


setup(
    name="maths_operations",
    version="0.1.0",  # semantic versioning: Major.Minor.Patch
    author="Maaz Khan",
    author_email="maazkhan7454@gmail.com",
    description="A collection of mathematic operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maaz-codes/python-piscine/tree/master/ex09/maths_op",
    packages=find_packages(),  # Automatically finds all the pckgs in the direc
    install_requires=[],  # List dependencies
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.1",  # Minimum Python version required
)

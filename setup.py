from setuptools import setup, find_packages

setup(
    name="cleanpipe",
    version="0.1.0",
    author="Naveen Kumar Baskaran",
    author_email="naveenkb142@gmail.com",
    description="A simple data cleaning pipeline built on pandas",
    packages=find_packages(),
    install_requires=["pandas"],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)

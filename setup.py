from setuptools import setup, find_packages

setup(
    name="cleanpipe",
    version="0.1.0",
    author="Naveen Kumar Baskaran",
    author_email="naveenkb142@gmail.com",
    description="A simple data cleaning pipeline built on pandas",
    url= "https://github.com/naveenkumarbaskaran/cleanpipe",
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'scipy',
        'scikit-learn',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
    ],
)

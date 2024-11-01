from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="easydsa",
    version="0.1.0",
    author="David Salathé",
    author_email="salathe.david@gmail.com",
    description="A simple and intuitive implementation of common data structures and algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dsalathe/easydsa",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    test_suite="tests",
)
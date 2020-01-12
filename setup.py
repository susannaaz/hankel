"""hankel: Hankel Transformations using method of Ogata 2005."""

from setuptools import setup
import os
import re
import io


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(
        r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M
    )
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: End Users/Desktop",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT License",
    "Natural Language :: English",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.5",
    "Programming Language :: Python :: 3.6",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3 :: Only",
    "Topic :: Scientific/Engineering",
    "Topic :: Utilities",
]

# use first version of req. to support py35
setup(
    name="hankel",
    install_requires=["numpy>=1.9.3", "scipy>=0.16.1", "mpmath>=1.0.0"],
    version=find_version("hankel", "__init__.py"),
    classifiers=CLASSIFIERS,
    python_requires=">=3.5",
    packages=["hankel"],
    description="Hankel Transformations using method of Ogata 2005",
    long_description=read("README.rst"),
    author="Steven Murray",
    author_email="steven.murray@curtin.edu.au",
    license="MIT",
    url="https://github.com/steven-murray/hankel",
)

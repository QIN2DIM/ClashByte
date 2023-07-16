from pathlib import Path

from setuptools import setup, find_packages

import clashbyte

# pip install twine
# python setup.py sdist bdist_wheel && python -m twine upload dist/*
setup(
    name="clashbyte",
    version=clashbyte.__version__,
    keywords=["clashbyte", "clash", "clash-meta", "clashapi"],
    author="QIN2DIM",
    author_email="yaoqinse@gmail.com",
    long_description=Path(__file__).parent.joinpath("README.md").read_text(encoding="utf8"),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/QIN2DIM/ClashByte",
    packages=find_packages(include=["clashbyte", "clashbyte.*", "LICENSE"], exclude=["tests"]),
    install_requires=["loguru>=0.7.0", "httpx>=0.24.1"],
    extras_require={"dev": ["nox", "pytest"], "test": ["pytest", "black"]},
    python_requires=">=3.8",
    classifiers=[
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
)

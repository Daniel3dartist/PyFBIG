from pathlib import Path
from setuptools import find_packages, setup

path = Path(__file__).resolve().parent
README = (path / "README.rst").read_text(encoding="utf-8")
VERSION = (path / "VERSION").read_text(encoding="utf-8").strip()

setup(name="pyFBID",
    version=VERSION,
    description="Faker is a Python package that generates fake data for you.",
    long_description=README,
    entry_points={
        "console_scripts": ["faker=faker.cli:execute_from_command_line"],
        "pytest11": ["faker = faker.contrib.pytest.plugin"],
    },
    classifiers=[
        # See https://pypi.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords="Python - Fake Brazilian ID Generator projected for data test mock generator",
    author="Daniel Sobrinho",
    author_email="contact@danielsobrinho.com.br",
    url="https://github.com/Daniel3dartist/PyFBIG",
    project_urls={
        "Bug Tracker": "https://github.com/Daniel3dartist/PyFBIG/issues",
        "Documentation": "https://github.com/Daniel3dartist/PyFBIG",
        "Source Code": "https://github.com/Daniel3dartist/PyFBIGr",
    },
    license="MIT License",
    packages=find_packages(),
    package_data={
        "pyFBID": ["py.typed"],
    },
    platforms=["any"],
    python_requires=">=3.8",
    install_requires=[
        "python-dateutil>=2.4",
        "typing-extensions>=3.10.0.1;python_version<='3.7'",
    ],
)

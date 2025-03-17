### Hands-On Python Packaging Tutorial: Create and Distribute Your Own Package

## Overview

This tutorial introduces you to the core concepts of creating and distributing a Python package. You will learn:

- **Virtual Environments (`venv`)**: To manage and isolate dependencies.
- **Structured Code Organization**: Using a `src` directory.
- **Testing**: Writing simple tests with `pytest`.
- **Packaging Tools**: Using `setuptools` and `build` to create installable Python packages.
- **Publishing**: Optionally distributing your package via PyPI.

We'll create a practical Python package named `unitconvert` with utility functions for converting:

- Temperature: Celsius ↔ Fahrenheit
- Length: Centimeters ↔ Inches
- Weight: Kilograms ↔ Pounds

Having your code as a Python package offers several benefits: easy sharing, reusability, and simpler maintenance. Additionally, you'll learn how to  add a Command-Line Interface (CLI) to enhance usability.

## Using a virtual environment (venv)

```text
+-----------------------+
|     Global System     |
+-----------------------+
| Python Interpreter (v3.x) |
| pip (global)          |
|                       |
|   No Project-Specific  |
|   Packages Installed   |
|                       |
+-----------------------+
          |
          | (Creation of Virtual Environments)
          |
+-----------------------+         +-----------------------+
|     Virtual Env 1     |         |     Virtual Env 2     |
+-----------------------+         +-----------------------+
| Python Interpreter (v3.8) |         | Python Interpreter (v3.10)|
| pip (v23.x)           |         | pip (v24.x)           |
|                       |         |                       |
| site-packages/        |         | site-packages/        |
|   - requests (v2.25)  |         |   - flask (v2.1)      |
|   - numpy (v1.20)     |         |   - sqlalchemy (v1.4) |
|                       |         |                       |
+-----------------------+         +-----------------------+
          ^                         ^
          |                         |
(Activated when working on Project A)   (Activated when working on Project B)
```

When developing Python programs, you might have multiple projects that depend on different Python versions or require specific packages and dependencies. Managing these requirements separately ensures your projects remain stable and consistent. Using a virtual environment (`venv`) helps manage dependencies separately for each Python project, preventing conflicts and inconsistencies.

## Python packaging

Python packaging traditionally uses `setup.py`, while the modern approach uses `pyproject.toml` and `setup.cfg`. We'll briefly explore both methods in this tutorial.

### Traditional vs. Modern Packaging in Python

- **Traditional method (**`**setup.py**`**)**:
  - Relies on a `setup.py` file using the `setuptools` library.
  - Provides flexibility but can lead to complex configurations.
- **Modern approach (**`**pyproject.toml**`**)**:
  - Utilizes a standardized `pyproject.toml` file.
  - Supports modern build systems like `build` and simplified configurations.

------

## Step-by-Step Tutorial

## Step 1: Set up the Project Directory

Create the project directory structure explicitly:

```sh
mkdir -p unitconvert_project/src/unitconvert
mkdir unitconvert_project/tests
cd unitconvert_project
```

Project structure:

```text
unitconvert_project/
├── src/
│   └── unitconvert/
│       ├── __init__.py
│       ├── temperature.py
│       ├── length.py
│       └── weight.py
├── tests/
│   ├── test_temperature.py
│   ├── test_length.py
│   └── test_weight.py
├── pyproject.toml
├── setup.cfg
├── README.md
└── .gitignore
```

### Create and activate the virtual environment:

On Unix/macOS:

```sh
python -m venv venv
source venv/bin/activate
```

On Windows:

```sh
python -m venv venv
venv\Scripts\activate
```

------

## Step 2: Add Conversion Functions 

Inside `src/unitconvert/`, create these Python modules with basic error handling:

temperature.py

```python
def celsius_to_fahrenheit(c):
    if not isinstance(c, (int, float)):
        raise ValueError("Input must be numeric")
    return c * 9/5 + 32

def fahrenheit_to_celsius(f):
    if not isinstance(f, (int, float)):
        raise ValueError("Input must be numeric")
    return (f - 32) * 5/9
```

length.py

```python
def inches_to_cm(inches):
    if not isinstance(inches, (int, float)):
        raise ValueError("Input must be numeric")
    return inches * 2.54

def cm_to_inches(cm):
    if not isinstance(cm, (int, float)):
        raise ValueError("Input must be numeric")
    return cm / 2.54
```

weight.py:

```python
def kg_to_pounds(kg):
    if not isinstance(kg, (int, float)):
        raise ValueError("Input must be numeric")
    return kg * 2.20462

def pounds_to_kg(pounds):
    if not isinstance(pounds, (int, float)):
        raise ValueError("Input must be numeric")
    return pounds / 2.20462
```

`__init__.py`:

```python
from .temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from .length import inches_to_cm, cm_to_inches
from .weight import kg_to_pounds, pounds_to_kg
```

------

## Step 3: Setup Configuration Files

### Traditional Way (`setup.py`)

✔ This is the older method where all package metadata is defined inside setup.py.
✔ Works for all Python versions.
✔ Not as modular as newer approaches.
Create a `setup.py` file:

```
from setuptools import setup, find_packages

setup(
    name="unitconvert",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Utility functions for unit conversions",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.7",
)
```

### Modern Way: `pyproject.toml`

setup.py 

```python
from setuptools import setup

setup()
```

Setup.cfg

```ini
[metadata]
name = unitconvert
version = 0.1.0
author = Your Name
author_email = your.email@example.com
description = Utility functions for unit conversions

[options]
package_dir =
    = src
packages = find:
python_requires = >=3.7

[options.packages.find]
where = src
```

Pyproject.toml

```toml
[build-system]
requires = ["setuptools", "wheel"]
build-backend = "setuptools.build_meta"
```

------

## Step 4: Writing Tests

`pytest` is a widely-used Python testing framework that simplifies writing and running tests. It offers easy-to-use assertions, clear test reporting, and extensive plugin support.

Create basic test files:

```
# tests/test_length.py
from unitconvert.length import inches_to_cm

def test_inches_to_cm():
    assert inches_to_cm(1) == 2.54
```

Install and run tests:

```sh
pip install pytest
pytest tests/
```

------

## Step 5: Building the Package

### Using `setuptools` (traditional method)

To build your package using `setup.py`, run:

```shell
python setup.py sdist bdist_wheel
```

This command generates distribution files in the `dist/` folder.

### Modern Way (Using `build`)

Install build tools and build distributions:

```shell
pip install build
python -m build
```

The output will be in the `dist/` folder, containing two types of distribution files:

- **Source Distribution (**`*.tar.gz`**)**: Contains the source code and can be installed on any platform, typically requiring compilation or build processes upon installation.
- **Wheel Distribution (**`*.whl`**)**: A pre-built package that is quicker and easier to install as it doesn't require compilation. Wheels are recommended for faster installation and easier dependency management.

------

## Step 6: Installing and Using the Package

Install locally for development:

```sh
pip install -e .
```

You can also use the package via the command-line interface (CLI) after installing:

```shell
unitconvert temp --c 100
# Output: 100C = 212.0F
```

Test it out:

```python
>>> import unitconvert
>>> print(unitconvert.celsius_to_fahrenheit(25))
77.0

>>> print(unitconvert.inches_to_cm(10))
25.4
```

------

## Step 7: Publishing and Sharing

After you build the package, you have several options for sharing it:

- Upload the package to Python Package Index (PyPI). You need to have a PyPI account. 
- Upload the package to TestPyPi(For Testing).

    Publish using Twine (test on PyPI Test server first):

    ```sh
    pip install twine
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
    ```

- Share via GitHub Releases.
    1. On GitHub, navigate to the main page of the repository.
    2. To the right of the list of files, click on "Releases".
    3. Choose or create a release tag.
    4. Input the release title and description.
    5. Choose Set as pre-release if it's a pre-release.
    6. Upload the package file (`.tar.gz` or `.whl`) in the release.
    7. Publish the release.
    
    Users can then download and install the package using `pip install https://link_to_the_release_file`.

------

## Conclusion

Congratulations! You've learned to effectively create, structure, test, package, and optionally publish Python packages. Keep exploring and enhancing your projects!
from setuptools import setup

setup()

# Taditional Approach
# ✔ This is the older method where all package metadata is defined inside setup.py.
# ✔ Works for all Python versions.
# ✔ Not as modular as newer approaches.
# from setuptools import setup, find_packages

# setup(
#     name="unitconvert",
#     version="0.1.0",
#     description="A simple Python package for unit conversions.",
#     author="Your Name",
#     author_email="your@email.com",
#     license="MIT",
#     packages=find_packages(where="src"),
#     package_dir={"": "src"},
#     install_requires=["pytest"],
#     python_requires=">=3.6",
# )

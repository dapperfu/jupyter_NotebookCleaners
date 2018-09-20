import setuptools
from setuptools import setup

import os
LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))


def read_requirements(path="requirements.txt"):
    requirements = []

    with open(os.path.join(LOCAL_DIR, "requirements.txt"), "r") as infile:
        for line in infile:
            line = line.strip()
            if line and not line[0] == "#":  # ignore comments
                requirements.append(line)
    return requirements

requirements = read_requirements()


setup(
    name='notebookcleaner',
    description="Cleanup Jupyter Notebooks",
    author="Jed",
    license="MIT",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements,
    include_package_data=True,
    entry_points={
        'nbc_cleaners': [
            'bubble_imports = notebookcleaner:bubble_notebook_imports',
            'blacken_cells = notebookcleaner:black_notebook_cells',
            'isort_notebook_cells = notebookcleaner:isort_notebook_cells',
            'clean_empty = notebookcleaner:clean_empty_notebook_cells',
        ],
        "console_scripts": [
            "notebookcleaner=notebookcleaner:main",
        ],
    }
)

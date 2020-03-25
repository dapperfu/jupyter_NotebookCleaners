import setuptools
from setuptools import setup

import os

LOCAL_DIR = os.path.dirname(os.path.abspath(__file__))

import versioneer

def read_requirements(path="requirements.txt"):
    requirements = []
    with open(path, "r") as fid:
        for line in fid.readlines():
            if line.startswith("#"):
                continue
            line = line.strip()
            requirements.append(line)
    return requirements

requirements = read_requirements()
test_requirements = read_requirements(path="requirements_test.txt")

setup(
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    name='notebookcleaner',
    description="Cleanup Jupyter Notebooks",
    author="Jed",
    license="MIT",
    packages=setuptools.find_packages(),
    zip_safe=False,
    install_requires=requirements,
    extras_require={"test": test_requirements},
    include_package_data=True,
    entry_points={
        'nbc_plugins': [
            'bubble_imports = notebookcleaner:bubble_notebook_imports',
            'clean_empty = notebookcleaner:clean_empty_notebook_cells',
            'black = notebookcleaner:black_notebook_cells',
            'reorder-python-inputs = notebookcleaner:reorder_python_inputs',
            'pyupgrade = notebookcleaner:pyupgrade',
        ],
        "console_scripts": [
            "notebookcleaner=notebookcleaner:main",
        ],
    }
)

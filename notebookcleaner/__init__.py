# -*- coding: utf-8 -*-
"""Notebook Cleaner."""

import os
import sys

import pkg_resources

from .black_notebook_cells import black_notebook_cells
from .bubble_notebook_imports import bubble_notebook_imports
from .clean_empty_notebook_cells import clean_empty_notebook_cells
from .isort_notebook_cells import isort_notebook_cells


def main(args=sys.argv):
    assert len(args) == 2
    notebook = args[1]
    assert os.path.exists(notebook), "%s does not exist" % notebook
    cleaners = pkg_resources.iter_entry_points("nbc_cleaners")
    for cleaner in cleaners:
        cleaning_function = cleaner.load()
        print("Running: {}".format(cleaning_function.__name__))
        cleaning_function(notebook=notebook)


if __name__ == "__main__":
    main()

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

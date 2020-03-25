import os

import nbformat


class NotebookCleaner:
    def __init__(self, notebook):
        notebook_t = type(notebook)
        if notebook_t in ["str"]:
            print(notebook_t)
        else:
            raise Exception("Unknown Type: %s" % notebook_t)

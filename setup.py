from setuptools import setup

setup(
    name='notebookcleaner',
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

import pkg_resources

def test_01():
    nbc_cleaners = list(pkg_resources.iter_entry_points('nbc_cleaners'))
    assert len(nbc_cleaners)==4, "Update tests with the new default cleaner."

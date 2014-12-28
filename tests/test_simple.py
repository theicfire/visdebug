import pytest
import visdebug

def test_one():
    assert(visdebug.sarr([4, 5, 6], [1]) == '[4, [47m5[49m, 6]')
    assert(visdebug.sarr([4, 5, 6], []) == '[4, 5, 6]')
    assert(visdebug.sarr([], []) == '[]')

import pytest
from utils import dicts


@pytest.fixture
def dt():
    un: globals() = "uncorrect key"
    nega = "a negative number"
    nn = "noname"
    return {-1: nega, 0: nega, 1: dicts.collection[1], '-1': nega, '0': nega, '1': dicts.collection[1], 'abc': un,
            10: nn}


def test_getval(dt):
    for k, v in dt.items():
        assert dicts.get_val(dicts.collection, key=k) == v
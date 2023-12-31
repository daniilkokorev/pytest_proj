from utils import dicts


def test_get_val_default():
    assert dicts.get_val({}, 'vcs') == 'git'


def test_get_val_list():
    assert dicts.get_val({'vcs': 'mars'}, 'vcs') == 'mars'


def test_get_val_word():
    assert dicts.get_val({}, 'vcs', 'bazar') == 'bazar'

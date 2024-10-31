import pytest

from twttr import shorten
def main():
    test_Uppercase()

def test_Uppercase():
    assert shorten("KEVIN") == "KVN"

def test_Lowercase():
    assert shorten("kevin") == "kvn"



if __name__ == "__main__":
    main()
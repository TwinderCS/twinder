# pylint: skip-file
import pytest

def test_always_passes():
    assert True

def test_always_not_fails():
    assert not False

def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]

def test_some_primes():
    assert 37 in {
        num for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }
    
@pytest.mark.parametrize("string", [
    "",
    "a",
    "Bob",
    "Never odd or even",
    "Do geese see God?",
])
def test_is_string(string):
    assert isinstance(string, str)

@pytest.mark.parametrize("non_string", [
    -4.36,
    3,
    ["a", "hbhredhfbche"]
])
def test_is_string_not_string(non_string):
    assert not isinstance(non_string, str)

@pytest.mark.parametrize("test_parametrize", [
    [1, 2],
    [-4, -3],
    [102, 103],
    [0, 1]
])
def test_multiple_parametrize(test_parametrize):
    assert test_parametrize[0] + 1 == test_parametrize[1]
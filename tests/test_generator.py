import pytest
import testing_cookiecutter

def test_generator_cat():
    sound = testing_cookiecutter.generator("cat")
    assert sound == "meow"
def test_generator_dog():
    sound = testing_cookiecutter.generator("dog")
    assert sound == "woof"
def test_generator_fish():
    sound = testing_cookiecutter.generator("fish")
    assert sound == "..."
def test_generator_notfound():
    with pytest.raises(Exception):
        testing_cookiecutter.generator("emu")

# import pytest
from classes import CentralObject, SmallObject


def test_create_central_object():
    central_object = CentralObject(5, 25.5)
    assert central_object.mass == 25.5
    assert central_object.diameter == 5


def test_create_small_object():
    small_object = SmallObject([25, 25], 2.5, [2, 4])
    assert small_object.position == [25, 25]
    assert small_object.mass == 2.5
    assert small_object.velocity == [2, 4]


def test_small_object_setters():
    small_object = SmallObject([25, 25], 2.5, [2, 4])
    assert small_object.position == [25, 25]
    assert small_object.velocity == [2, 4]
    assert small_object.color == 'white'
    small_object.position = [20, 12]
    small_object.velocity = [1, 5]
    small_object.color = 'blue'
    assert small_object.position == [20, 12]
    assert small_object.velocity == [1, 5]
    assert small_object.color == 'blue'


def test_small_object_():
    small_object = SmallObject([2, 5], 2, 2)
    assert small_object.velocity == [2, 5]

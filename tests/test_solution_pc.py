import pytest
from solution_pc import *
import timeit

def test_answer():
    assert answer(8) == ["L", "-", "R"]

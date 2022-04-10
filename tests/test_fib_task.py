import pytest

#import list_task
from src import fib_task

def test_fib():
    assert fib_task.calc_fib(12) == 144
    assert fib_task.calc_fib(8) == 21
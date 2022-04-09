import pytest
#import list_task
from src import list_task

def test_func():
    Original  = ['one', 'two', 'three',]
    Add  = ['one', 'two', 'five', 'six']
    Delete = ['two', 'five']
    #print(func(Original,Add,Delete))
    assert list_task.func(Original,Add,Delete) == ['three', 'six', 'one']


def test_func2():
    Original  = ['five', 'seven', 'two',]
    Add  = ['one', 'one', 'eleven', 'six','twelve','eleven']
    Delete = ['twelve']
    #print(func(Original,Add,Delete))
    assert list_task.func(Original,Add,Delete) == [ 'eleven', 'seven', 'five',  'two','six', 'one']

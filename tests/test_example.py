from hexlet_pytest.example import *

# TESTING CODE FROM LESSON 3


def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''


# TESTING CODE FROM LESSON 4
# Testing main functionality of stack
def test_stack():
    stack.append(1)
    stack.append(2)

    assert stack.pop() == 2
    assert stack.pop() == 1


# Testing if stack is empty
def test_emptiness():
    assert not stack

    stack.append(1)
    assert bool(stack)

    stack.pop()
    assert not stack


# Testing .pop()
import pytest

def test_pop_with_empty_stack():
    # проверить что вызывается конкретное исключение можно с помощью конструкции with pytest.raises()
    # если внутри блока вызовется исключение, то тест будет пройден
    with pytest.raises(IndexError):
        stack.pop()

    print("Test for .pop() passed")






import pytest
import PyTestDemo.Calculator as Cal

@pytest.mark.smokeAddTest
def test_add():
    assert Cal.add(10, 5) == 15

def test_sub():
    assert Cal.sub(20, 10) == 10


from calculator import add

def test_add():
	assert add(2, 3) == 5
	assert add(-1, 1) == 0
	assert add(0, 0) == 0
	assert add(14, -8) == 6
	assert add(192, 279) == 471
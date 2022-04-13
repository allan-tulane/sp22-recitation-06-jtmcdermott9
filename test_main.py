from main import *

import random

# 4 pts
def test_qsort_fixed():
	assert(qsort([5,4,3,2,1], lambda a: a[0])) == [1,2,3,4,5]

# 4 pts
def test_qsort_random():
	assert(qsort([5,4,3,2,1], lambda a: random.choice(a))) == [1,2,3,4,5]

def test_qsort_random2():
  assert(qsort([44,5,2,56,23], lambda a: random.choice(a))) == [2,5,23,44,56]
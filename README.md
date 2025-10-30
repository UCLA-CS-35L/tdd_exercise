# TDD Exercise

In this hands-on exercise you should implement an Int to Roman Numerals converter using TDD. 
```
1 -> I
2 -> II
3 -> II
4 -> IV
5 -> V
6 -> VI
...
9 -> IX
10 -> X
15 -> XV
50 -> L
100 -> C
500 -> D
1000 -> M
```

The source code is in: `src/roman/int_to_roman.py`
The test code is in: `tests/test_int_to_roman.py`

After installing pytest (`pip install pytest`) you can run `pytest` to execute the tests. 
Alternatively you can use pipenv (after install `pip install pipenv`) and run the testsvia (`pipenv run pytest`).

Please follow the TDD Red-Green-Refactor steps. Iteratively add one test, then implement code passing the test, the refactor the code. 

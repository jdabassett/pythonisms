# PYTHONISMS

## DATE:
2/7/2024

## AUTHOR:
Jacob Bassett

## DESCRIPTION:
Jacob developed this CustomList and 'timer' decorator to practice using dunder methods, converting a class into an iterator, converting a class into a generator, and working with decorator functions. This CustomList has many of the same methods as a conventional Python list.

## ANALYSIS:
Jacob wanted to see if he could measure the run time of each CustomList method he wrote with the 'timer' decorator. These are the results he found.

| Method       | Time (micro-seconds) | Time Complexity (Big O) |
|--------------|----------------------|-------------------------|
| __add__      | 2.1                  | O(N)                    |
| __bool__     | 0.7                  | O(1)                    |
| __contains__ | 1.0                  | O(N)                    |
| __delitem__  | 1.2                  | O(N)                    |
| __eq__       | 1.2                  | O(N)                    |
| __getitem__  | 0.0                  | O(1)                    |
| __iter__     | 14.8                 | ?                       |
| __len__      | 1.0                  | O(1)                    |
| __setitem__  | 0.0                  | O(1)                    |
| __str__      | 2.1                  | O(N)                    |
| append       | 1.2                  | O(1)                    |
| clear        | 0.0                  | O(1)                    |
| count        | 1.2                  | O(N)                    |
| extend       | 1.0                  | O(N)                    |
| generator    | 1.0                  | O(N)                    |
| index        | 1.0                  | O(N)                    |
| insert       | 1.2                  | O(N)                    |
| pop          | 1.0                  | O(1)                    |
| remove       | 2.9                  | O(N)                    |
| reverse      | 1.2                  | O(N)                    |
| sort         | 1.0                  | O(N)                    |


## USAGE AND UNIT TESTS:
After cloning this repository to your local machine run the following commands.

```bash
# activate virtual environment
➜ project source .venv/bin/activate

# install project dependencies
(.venv) ➜ project pip install -r requirements.txt

# to inspect the code open up in your favorite IDE
(.venv) ➜ project charm .

# run unit tests
(.venv) ➜  project pytest
================================================================ test session starts =================================================================
platform darwin -- Python 3.11.7, pytest-7.4.3, pluggy-1.3.0
rootdir: /Users/jacobbassett/projects/courses/code-401/pythonisms
plugins: anyio-3.7.1
collected 25 items

tests/test_customlist.py .......................                                                                                               [ 92%]
tests/test_decorator.py ..                                                                                                                     [100%]

================================================================= 25 passed in 0.02s =================================================================
```


## DEPENDENCIES:
iniconfig==2.0.0
packaging==23.2
pluggy==1.4.0
pytest==8.0.0

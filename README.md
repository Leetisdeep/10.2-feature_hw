# project home_work

### Testing
98% of the code is covered by tests. All tests complete as expected

## Description:

Simple project for now with mainly processing module.

## Using:

1.Download the project <br>
2.Import scr/processing to your code <br>
3.Use functions from processing module <br>

## Example:
```python
from src.processing import filter_by_state, sort_by_date

transactions = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 59402872, 'state': 'CANCELLED', 'date': '2018-09-17T21:27:25.241241'}
]
executed_transactions = filter_by_state(transactions)
sorted_transactions = sort_by_date(transactions)
```

This project is licensed under [LICENSE MIT](LICENSE).

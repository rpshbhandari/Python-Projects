# Airplane Management System

Tracks aircraft and their parts as fixed assets, with flight hours, cycles and days, in a pandas table.

- `airplane.py`: the `Asset` class, to create, read, update and delete assets. Running it adds two demo assets and prints the table.
- `Hour.py`: an `HH:MM` flight-hours type that adds and subtracts.
- `plan.md`: notes on the fixed-asset actions and the flight log still to build. `test.py` is an unfinished start on that flight log.

The registration, hours and names in the demo and notes are made up.

```bash
pip install pandas tabulate
python airplane.py
```

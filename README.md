# ExpenseTrack

ExpenseTrack is a command-line expense tracking application for managing personal finances. It supports basic operations such as adding, listing, summarizing, and deleting expenses. The application uses a local JSON file for persistent storage and is implemented using only the standard Python library.

## Features

- Add, delete, and list expenses
- View total expense summary
- View monthly expense summary
- Stores data in a local `expenses.json` file
- No external dependencies

## Project at:
https://roadmap.sh/projects/expense-tracker

## Usage

### Add Expense

```
./expense_tracker.py add --description "Lunch" --amount 20
```

### Delete Expense

```
./expense_tracker.py delete --id 1
```

### List Expenses

```
./expense_tracker.py list
```

### View Summary

```
./expense_tracker.py summary
./expense_tracker.py summary --month 4
```

## Data Format

Each expense is stored with the following fields:

```json
{
  "id": 1,
  "date": "2025-04-22",
  "description": "Lunch",
  "amount": 20.0
}
```

## Repository

https://github.com/1ndrayu/expensetrack

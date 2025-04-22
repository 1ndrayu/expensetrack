#!/usr/bin/env python3

import argparse
import json
import os
from datetime import datetime

FILE_NAME = "expenses.json"

def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)

def get_next_id(expenses):
    return max((e["id"] for e in expenses), default=0) + 1

def add_expense(description, amount):
    expenses = load_expenses()
    new_expense = {
        "id": get_next_id(expenses),
        "date": datetime.now().strftime("%Y-%m-%d"),
        "description": description,
        "amount": float(amount)
    }
    expenses.append(new_expense)
    save_expenses(expenses)
    print(f"Expense added successfully (ID: {new_expense['id']})")

def delete_expense(expense_id):
    expenses = load_expenses()
    filtered = [e for e in expenses if e["id"] != expense_id]
    if len(expenses) == len(filtered):
        print("Expense ID not found.")
    else:
        save_expenses(filtered)
        print("Expense deleted successfully")

def list_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    print(f"{'ID':<4} {'Date':<12} {'Description':<20} {'Amount':>7}")
    for e in expenses:
        print(f"{e['id']:<4} {e['date']:<12} {e['description']:<20} ${e['amount']:>6.2f}")

def summarize(month=None):
    expenses = load_expenses()
    if month:
        expenses = [e for e in expenses if datetime.strptime(e["date"], "%Y-%m-%d").month == month]
        total = sum(e["amount"] for e in expenses)
        print(f"Total expenses for month {month}: ${total:.2f}")
    else:
        total = sum(e["amount"] for e in expenses)
        print(f"Total expenses: ${total:.2f}")

def main():
    parser = argparse.ArgumentParser(description="Expense Tracker CLI")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("--description", required=True)
    add_parser.add_argument("--amount", required=True, type=float)

    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("--id", required=True, type=int)

    subparsers.add_parser("list")

    summary_parser = subparsers.add_parser("summary")
    summary_parser.add_argument("--month", type=int, help="Month (1-12)")

    args = parser.parse_args()

    if args.command == "add":
        add_expense(args.description, args.amount)
    elif args.command == "delete":
        delete_expense(args.id)
    elif args.command == "list":
        list_expenses()
    elif args.command == "summary":
        summarize(args.month)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

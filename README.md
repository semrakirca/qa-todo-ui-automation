# QA UI Automation – Todo App

This project is a small UI test automation framework for a Todo application.

It is built with:

- Python
- Pytest
- Selenium WebDriver
- Page Object Model (POM)
- Explicit waits
- Parametrized tests

## Test Scope

The tests focus on the **Add Todo** feature:

- Adding a todo with valid text
- Adding multiple todos
- Preventing empty todos
- Preventing whitespace-only todos
- Verifying that todos persist after a page refresh

## Project Structure

```text
qa-todo-ui-automation/
│
├── pages/
│   └── todo_page.py        # Page Object for the Todo page
│
├── tests/
│   └── test_todo_add.py    # UI tests for Add Todo feature
│
├── conftest.py             # Pytest fixture for WebDriver
├── requirements.txt        # Dependencies
└── README.md               # Project description
```
# qa-todo-ui-automation

# CodingBat Python Solutions

My solutions to [CodingBat](https://codingbat.com/python) Python exercises.

## Project Structure

```
.
├── src/                  # Solutions
│   └── warmup_1.py
├── test/                 # Tests
│   └── warmup_1_test.py
└── conftest.py
```

## Running Tests

```bash
pip install pytest
pytest -v test/
```

## CI

- **Tests** — run automatically on pull requests via GitHub Actions
- **Gemini AI Code Review** — trigger by commenting `/gemini-review` on a PR

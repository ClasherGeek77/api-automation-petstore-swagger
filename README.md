# api-automation-petstore-swagger 🐾

[![Petstore CI](https://github.com/ClasherGeek77/api-automation-petstore-swagger/actions/workflows/petstore-ci.yml/badge.svg)](https://github.com/ClasherGeek77/api-automation-petstore-swagger/actions/workflows/petstore-ci.yml)

## 🧪 Tech Stack

- Python 3.9
- Pytest
- Requests
- **Allure Reporting** (Replaced Pytest-HTML for enterprise-grade reporting)
- Flaky (for retry on unstable endpoints)
- Built-in logging via `pytest.ini`


## 🚀 Setup Instructions

1. Create virtual environment:
```bash
export PYTHONPATH=your-path-to-folder
python3.9 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run tests:
```bash
pytest
```
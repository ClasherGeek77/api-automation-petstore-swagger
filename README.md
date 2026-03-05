[![CI](https://github.com/ClasherGeek77/api-automation-petstore-swagger/actions/workflows/pytest-ci.yml/badge.svg)](https://github.com/ClasherGeek77/api-automation-petstore-swagger/actions/workflows/pytest-ci.yml)

# Petstore API Automation 🐾 

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/Framework-Pytest-blue?logo=pytest)](https://docs.pytest.org/en/7.4.x/)
[![Pydantic](https://img.shields.io/badge/Validation-Pydantic-blue?logo=pydantic)](https://docs.pydantic.dev/)
[![Allure](https://img.shields.io/badge/Reporting-Allure-success)](https://allurereport.org/)

An elite, highly scalable API automation boilerplate utilizing **Python, Pydantic, Requests, and Allure** designed for industrial-strength contract and functional testing.

## 🚀 Key Architectural Pillars

### 1. High-Performance Infrastructure
- **Dependency Management**: Powered by `Poetry` for deterministic, lock-file based environments.
- **BaseClient Abstraction**: A powerful base class that handles retry logic, timeouts, and structured request/response logging.
- **Domain-Driven Design**: Separated into `core`, `models`, `services`, and `utils`.

### 2. Radical Reliability & Type Safety
- **Contract-First Testing**: Every API response is automatically validated against `Pydantic` models to ensure schema integrity.
- **Service-Level Layer**: API calls are abstracted into domain-specific actions (e.g., `pet_service.add_pet()`).
- **Strict Data Validation**: Automatic type coercion and error reporting on API schema violations.

### 3. Deep Observability & DevEx
- **Curl-Ready Logs**: Every request is logged as a copy-pasteable `curl` command for instant debugging.
- **Rich Allure Reports**: Complete request headers, bodies, and response payloads are attached to every test case.
- **Sandbox CLI**: A dedicated `scripts/sandbox.py` for rapid environment setup and test execution.

## 🏁 Getting Started

### 1. Prerequisites
- Python 3.10+
- [Poetry](https://python-poetry.org/docs/#installation)

### 2. Setup
```bash
poetry install
```

### 3. Execution via Sandbox
```bash
# Run tests in parallel (4 workers)
python3 scripts/sandbox.py test --workers 4
```

## 📊 Reporting
Generate the Allure report to see deep API traces:
```bash
python3 scripts/sandbox.py report
```
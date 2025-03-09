# Test Results API

[![Continuous Integration](https://github.com/ocrosby/test-results-api/actions/workflows/ci.yaml/badge.svg)](https://github.com/ocrosby/test-results-api/actions/workflows/ci.yaml)
[![Release](https://github.com/ocrosby/test-results-api/actions/workflows/release.yaml/badge.svg)](https://github.com/ocrosby/test-results-api/actions/workflows/release.yaml)
[![codecov](https://codecov.io/gh/ocrosby/test-results-api/graph/badge.svg?token=LNKA3RTD4K)](https://codecov.io/gh/ocrosby/test-results-api)

The Test Results API is a FastAPI-based application designed to manage and retrieve test results. It provides endpoints for creating, updating, retrieving, and deleting test results, making it suitable for educational institutions, testing centers, and other organizations that need to handle test data efficiently.

You can reference individual [Markdown documents](./docs/index.md) I've added to the `docs` directory
to learn more about concepts I've run into while working on this project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Follow these steps to install and set up the Test Results API on your local machine.

```shell
# Clone the repository
git clone https://github.com/ocrosby/test-results-api.git

# Navigate to the project directory
cd test-results-api

# Create a virtual environment
python -m venv .venv

# Install dependencies
pip install --upgrade pip
pip install invoke flit twine
pip install -e ".[dev]"

# Run the application
uvicorn app.main:app --reload
```

## Usage

Here are some example commands to interact with the Test Results API.

```shell
# Example command
curl -X GET "http://127.0.0.1:8000/items/" -H  "accept: application/json"
```

## API Endpoints

Below is a list of available API endpoints and their descriptions.

### **Authentication**
- **POST** `/auth/register/` - Registers a new user.
- **POST** `/auth/login/` - Logs in a user and returns a JWT token.

### **Test Suites**
- **GET** `/test-suites/` - Retrieves a list of test suites.
- **POST** `/test-suites/` - Creates a new test suite.
- **GET** `/test-suites/{id}/` - Retrieves a test suite by ID.

### **Test Classes**
- **GET** `/test-classes/` - Retrieves a list of test classes.
- **POST** `/test-classes/` - Creates a new test class.
- **GET** `/test-classes/{id}/` - Retrieves a test class by ID.

### **Test Cases**
- **GET** `/test-cases/` - Retrieves a list of test cases.
- **POST** `/test-cases/` - Creates a new test case.
- **GET** `/test-cases/{id}/` - Retrieves a test case by ID.

### **Test Executions**
- **POST** `/test-executions/` - Associates a test case with a test suite and class.
- **GET** `/test-suites/{suite_id}/test-cases/` - Retrieves all test cases in a given test suite.

### **Kubernetes Probes**
- **GET** `/healthz/live/` - Liveness probe to check if the API is running.
- **GET** `/healthz/ready/` - Readiness probe to check if the API is ready to receive traffic.
- **GET** `/healthz/startup/` - Startup probe to check if the API has fully started.

## Contributing

Contributions are welcome! Please follow these guidelines to contribute to the Test Results API project.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

Your Name - [Omar Crosby](mailto:omar.crosby@gmail.com)
Project Link: [test-results-api](https://github.com/ocrosby/test-results-api)

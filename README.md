# Test Results API

[![Continuous Integration](https://github.com/ocrosby/test-results-api/actions/workflows/ci.yaml/badge.svg)](https://github.com/ocrosby/test-results-api/actions/workflows/ci.yaml)
[![Release](https://github.com/ocrosby/test-results-api/actions/workflows/release.yaml/badge.svg)](https://github.com/ocrosby/test-results-api/actions/workflows/release.yaml)
[![codecov](https://codecov.io/gh/ocrosby/test-results-api/graph/badge.svg?token=LNKA3RTD4K)](https://codecov.io/gh/ocrosby/test-results-api)

The Test Results API is a FastAPI-based application designed to manage and retrieve test results. It provides endpoints for creating, updating, retrieving, and deleting test results, making it suitable for educational institutions, testing centers, and other organizations that need to handle test data efficiently.

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

- GET /items/ - Retrieves a list of items.
- POST /items/ - Creates a new item.
- GET /items/{id} - Retrieves an item by ID.
- PUT /items/{id} - Updates an item by ID.
- DELETE /items/{id} - Deletes an item by ID.

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

![JSO](https://github.com/YaelD/JSO-Frontend/assets/63968945/f9d9e5ea-300d-439a-9c3a-98e9afb94181)

# JSO - Job Seeking Organizer (Backend)
This repository contains the backend app of the JSO platform.
JSO is an open-source platform for job seekers that helps users to organize and manage their job-seeking processes.

## Technological stack
- Python
- FastAPI
- SQLModel (for ORM)
- Pydantic
- PostgreSQL server

## Running the JSO-Backend app
1. Clone the [JSO-Backend](https://github.com/YaelD/JSO-Backend) repository via GitHub or using the git command: ``` git clone https://github.com/YaelD/JSO-Backend.git ```.
2. Navigate via a terminal to the cloned directory.
3. Install the Poetry virtual environment on your system, you can do so by following the installation instructions on the [Poetry](https://python-poetry.org/docs/) website.
4. Run `poetry install` command in order to install the project's dependencies which are defined in the `pyproject.toml` file.
5. Run `poetry run uvicorn jso_backend.main:app` command in order to run the app.

## Code Quality and Linting
The following code quality and linting solutions are used:

- [Pyright](https://microsoft.github.io/pyright/#/) - full-featured, standards-based static type checker for Python.
- [black](https://github.com/psf/black) - code formatter.
- [isort](https://github.com/PyCQA/isort) - sorting import statements.
- [flake8](https://flake8.pycqa.org/en/latest/) - Style guide enforcement.

Note black, isort and flake8 are configured with [pyproject.toml](https://github.com/YaelD/JSO-Backend/blob/main/pyproject.toml).
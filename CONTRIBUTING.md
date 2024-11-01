# Contributing to SimpleDSA

First off, thank you for considering contributing to SimpleDSA! It's people like you that make SimpleDSA such a great tool.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* Use a clear and descriptive title
* Describe the exact steps which reproduce the problem
* Provide specific examples to demonstrate the steps
* Describe the behavior you observed after following the steps
* Explain which behavior you expected to see instead and why
* Include screenshots if relevant

### Suggesting Enhancements

If you have a suggestion for a new feature or enhancement, first check the issue list to see if it's already been proposed. If it hasn't, feel free to create a new issue. Please provide:

* A clear and descriptive title
* A detailed description of the proposed feature
* Examples of how the feature would be used
* An explanation of why this feature would be useful

### Pull Requests

Here's a guide for submitting high-quality pull requests:

1. Fork the repo and create your branch from `main`
2. Install development dependencies:

   ```bash
   poetry install
   ```

3. Set up pre-commit hooks:

   ```bash
   poetry add pre-commit --dev
   poetry run pre-commit install
   ```

4. Make your changes, following our coding conventions:
   * Use [Black](https://github.com/psf/black) for code formatting
   * Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
   * Write [good commit messages](https://chris.beams.io/posts/git-commit/)

5. Add tests for any new functionality

6. Run the test suite:

   ```bash
   poetry run pytest
   ```

7. Update documentation if needed

## Development Setup

1. Fork and clone the repository:

   ```bash
   git clone https://github.com/your-username/simpledsa.git
   cd simpledsa
   ```

2. Install Poetry (if you haven't already):

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Install dependencies:

   ```bash
   poetry install
   ```

4. Install pre-commit hooks:

   ```bash
   poetry run pre-commit install
   ```

## Development Workflow

1. Create a new branch:

   ```bash
   git checkout -b feature-or-fix-name
   ```

2. Make your changes and commit:

   ```bash
   git add .
   git commit -m "Description of changes"
   ```

   The pre-commit hooks will automatically run to check your changes.

3. Run tests:

   ```bash
   poetry run pytest
   ```

4. Build and check documentation:

   ```bash
   cd docs
   poetry run make html
   ```

5. Push your changes:

   ```bash
   git push origin feature-or-fix-name
   ```

6. Create a Pull Request on GitHub

## Code Style Guide

### Python Style Guidelines

* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Use meaningful variable names
* Write docstrings for all public modules, functions, classes, and methods
* Keep functions focused and small
* Use type hints

Example:

```python
from typing import Optional, Any

def process_item(item: Any, priority: Optional[float] = None) -> None:
    """
    Process an item with optional priority.

    Args:
        item: The item to process
        priority: Optional priority value (default: None)

    Raises:
        ValueError: If priority is negative
    """
    if priority is not None and priority < 0:
        raise ValueError("Priority must be non-negative")
    # Implementation
```

### Documentation Guidelines

* Write clear, concise docstrings
* Include examples in docstrings
* Update README.md when adding new features
* Keep the documentation up to date with changes

### Test Guidelines

* Write tests for all new functionality
* Use descriptive test names
* Include both positive and negative test cases
* Test edge cases
* Keep tests focused and small

Example:

```python
def test_priority_queue_push_pop():
    """Test basic push and pop operations."""
    pq = PriorityQueue()
    pq.push("task1", 1)
    pq.push("task2", 2)
    assert pq.pop() == "task1"
    assert pq.pop() == "task2"
```

## Release Process

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create and push a new tag:

   ```bash
   git tag v0.1.x
   git push origin v0.1.x
   ```

4. GitHub Actions will automatically:
   * Run tests
   * Build documentation
   * Publish to PyPI

## Questions?

Feel free to open an issue if you have any questions or need clarification about contributing.

Thank you for your contribution! 🎉

# Contributing to TOON JSON Optimizer

First off, thank you for considering contributing to TOON JSON Optimizer! 🎉

## 🤝 Code of Conduct

This project adheres to a code of conduct. By participating, you are expected to uphold this code. Please be respectful and constructive in all interactions.

##  How Can I Contribute?

### Reporting Bugs 🐛

Before creating bug reports, please check existing issues to avoid duplicates. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce** the issue
- **Expected vs actual behavior**
- **Sample JSON** that causes the issue (if applicable)
- **Environment details** (Python version, OS, etc.)

**Bug Report Template:**
```markdown
### Description
[Clear description of the bug]

### Steps to Reproduce
1. Upload JSON file with structure: ...
2. Call endpoint: ...
3. See error: ...

### Expected Behavior
[What should happen]

### Actual Behavior
[What actually happens]

### Environment
- Python version: 3.11
- OS: Ubuntu 22.04
- Browser: Chrome 120

### Sample Data
```json
[Your sample JSON here]
```
```

### Suggesting Enhancements 💡

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case** - why is this enhancement needed?
- **Proposed solution** - how should it work?
- **Alternatives considered**

### Pull Requests 🔧

1. **Fork the repository** and create your branch from `main`
   ```bash
   git checkout -b feature/amazing-feature
   ```

2. **Make your changes**
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation

3. **Test your changes**
   ```bash
   # Run tests (if available)
   pytest
   
   # Test the API manually
   python app/main.py
   ```

4. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature: brief description"
   ```
   
   **Commit Message Guidelines:**
   - Use present tense ("Add feature" not "Added feature")
   - Use imperative mood ("Move cursor to..." not "Moves cursor to...")
   - Limit first line to 72 characters
   - Reference issues: `Fix #123` or `Closes #456`

5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```

6. **Open a Pull Request**
   - Fill in the PR template
   - Link related issues
   - Wait for review

## 📋 Development Setup

### Prerequisites
- Python 3.9+
- pip
- Virtual environment (recommended)

### Setup Steps

```bash
# Clone your fork
git clone https://github.com/yourusername/json-optimizer.git
cd json-optimizer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install development dependencies (if available)
pip install -r requirements-dev.txt

# Run the server
cd app
python main.py
```

## 🏗️ Project Structure

```
JSON-OPTIMIZER/
├── app/
│   ├── main.py              # FastAPI app - add new endpoints here
│   ├── models.py            # Pydantic models - add new schemas here
│   ├── detectors/           # Detection logic
│   ├── optimizers/          # Optimization algorithms
│   ├── formatters/          # Output formatting
│   └── validators/          # Validation logic
├── tests/                   # Test files (add new tests here)
├── docs/                    # Documentation
└── examples/                # Example JSON files
```

## 🎨 Code Style

### Python Style Guide
- Follow [PEP 8](https://pep8.org/)
- Use type hints where applicable
- Maximum line length: 100 characters
- Use descriptive variable names

**Example:**
```python
def optimize_fields(df: pd.DataFrame, method: str = "entropy") -> List[str]:
    """
    Optimize field order using specified method.
    
    Args:
        df: Input DataFrame
        method: Optimization method ("entropy" or "frequency")
    
    Returns:
        List of optimized field names
    """
    # Implementation
    pass
```

### Documentation
- Add docstrings to all functions and classes
- Use Google-style docstrings
- Update README.md for user-facing changes

## 🧪 Testing

### Writing Tests
- Add tests for new features
- Ensure existing tests pass
- Aim for >80% code coverage

```python
# Example test
def test_toon_detection():
    detector = TOONDetector()
    sample_data = [{"id": 1, "name": "Alice"}]
    is_toonable, metadata = detector.detect(sample_data)
    assert is_toonable == True
    assert metadata["total_records"] == 1
```

### Running Tests
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app

# Run specific test file
pytest tests/test_detector.py
```

## 📝 Areas for Contribution

We especially welcome contributions in these areas:

### High Priority 🔥
- [ ] Add comprehensive test suite
- [ ] Support for nested JSON structures
- [ ] CSV/Excel input support
- [ ] Batch processing endpoint
- [ ] Performance optimization for large files (>10MB)

### Medium Priority 📊
- [ ] Additional optimization algorithms (frequency-based, heuristic)
- [ ] Support for more tokenizers (Claude, Llama)
- [ ] Caching layer for repeated optimizations
- [ ] CLI tool for local usage
- [ ] Docker containerization

### Nice to Have ✨
- [ ] Web UI for file upload
- [ ] Real-time optimization preview
- [ ] Export to multiple formats (CSV, Parquet)
- [ ] Compression comparison charts
- [ ] Integration examples (Python, Node.js, curl)

## 🎯 First-Time Contributors

Look for issues labeled:
- `good first issue` - Easy to get started
- `help wanted` - Community help needed
- `documentation` - Improve docs

## 💬 Questions?

- Open a [GitHub Discussion](https://github.com/yourusername/json-optimizer/discussions)
- Create an issue with the `question` label
- Reach out on [Twitter](https://twitter.com/yourhandle)

## 🙏 Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- Project documentation

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making TOON JSON Optimizer better! 🚀**
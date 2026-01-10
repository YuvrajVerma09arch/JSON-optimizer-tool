#  TOON JSON Optimizer

**Reduce LLM token usage by 40-60% with AI-powered JSON compression**

Transform verbose JSON into compact TOON (Table-Oriented Object Notation) format using advanced entropy optimization. Perfect for reducing costs and context window usage when working with LLMs like GPT-4, Claude, and Gemini.

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.15-orange.svg)](https://tensorflow.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 📊 What is TOON?

TOON converts repetitive JSON arrays into a compact tabular format:

**Before (JSON - 156 tokens):**
```json
[
  {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 28},
  {"id": 2, "name": "Bob", "email": "bob@example.com", "age": 34},
  {"id": 3, "name": "Carol", "email": "carol@example.com", "age": 29}
]
```

**After (TOON - 62 tokens, 60% savings):**
```
data[3]{id,name,email,age}: 1 Alice alice@example.com 28 | 2 Bob bob@example.com 34 | 3 Carol carol@example.com 29
```

---

## ✨ Features

- **🤖 AI-Powered Optimization**: TensorFlow entropy analysis sorts fields for maximum compression
- **📉 40-60% Token Reduction**: Validated with tiktoken (OpenAI's tokenizer)
- **🔍 Smart Detection**: Pandas automatically identifies TOON-compatible structures
- **⚡ FastAPI Backend**: Production-ready REST API with automatic documentation
- **📊 Detailed Analytics**: Field-level entropy metrics and optimization reports
- **🎯 Zero Configuration**: Upload JSON → Get optimized TOON instantly

---

## 🏗️ Architecture

```
Browser → FastAPI /upload → Pandas Detection → TensorFlow Entropy Sort → TOON Formatter → JSON Response
                                    ↓
                          Token Validation (tiktoken)
```

### Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **API Framework** | FastAPI | REST endpoints with auto-docs |
| **Detection** | Pandas | JSON structure analysis |
| **Optimization** | TensorFlow 2.15 | Shannon entropy field sorting |
| **Tokenization** | tiktoken | GPT-compatible token counting |
| **Validation** | Pydantic | Type-safe request/response |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/json-optimizer.git
cd json-optimizer

# Install dependencies
pip install -r requirements.txt

# Run the server
cd app
python main.py
```

Server starts at **http://localhost:8000**

### Interactive API Docs

Visit **http://localhost:8000/docs** for Swagger UI

---

## 📖 Usage

### API Endpoints

#### `POST /upload`
Optimize JSON file to TOON format

**Request:**
- Multipart file upload
- Content-Type: `application/json`

**Response:**
```json
{
  "status": "success",
  "original_json": [...],
  "toon_output": "data[3]{id,name,email}: ...",
  "token_stats": {
    "original_tokens": 156,
    "toon_tokens": 62,
    "savings_tokens": 94,
    "savings_percentage": 60.26
  },
  "metadata": {
    "is_toonable": true,
    "detected_arrays": 1,
    "total_records": 3,
    "field_count": 4
  },
  "field_entropy": [
    {
      "field_name": "id",
      "entropy_score": 0.45,
      "optimized_position": 0
    }
  ]
}
```

#### `POST /validate`
Check if JSON is TOON-compatible (no optimization)

#### `GET /`
Health check and service info

---

## 🧪 Example

Create `test_data.json`:
```json
[
  {"user_id": 101, "username": "alice_wonder", "email": "alice@example.com", "status": "active", "credits": 250},
  {"user_id": 102, "username": "bob_builder", "email": "bob@example.com", "status": "active", "credits": 180},
  {"user_id": 103, "username": "carol_codes", "email": "carol@example.com", "status": "inactive", "credits": 420}
]
```

**cURL:**
```bash
curl -X POST "http://localhost:8000/upload" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@test_data.json"
```

**Python:**
```python
import requests

with open('test_data.json', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/upload',
        files={'file': f}
    )
    
result = response.json()
print(f"Token savings: {result['token_stats']['savings_percentage']}%")
print(f"TOON output: {result['toon_output']}")
```

---

## 🧠 How It Works

### 1. **Detection (Pandas)**
```python
# Checks for uniform dictionary arrays
df = pd.json_normalize(json_data)
uniform = all(set(item.keys()) == first_keys for item in data)
```

### 2. **Entropy Optimization (TensorFlow)**
```python
# Shannon entropy: H = -Σ(p_i * log(p_i))
# Fields with low entropy (high predictability) placed first
entropy = -tf.reduce_sum(probs * tf.math.log(probs))
```

### 3. **TOON Formatting**
```python
# Format: arrayname[count]{fields}: row1 | row2 | row3
toon = f"data[{count}]{{{fields}}}: {rows}"
```

### 4. **Token Validation**
```python
# Count tokens using OpenAI's tiktoken
original_tokens = len(encoding.encode(json_str))
toon_tokens = len(encoding.encode(toon_str))
savings = (1 - toon_tokens/original_tokens) * 100
```

---

## 📂 Project Structure

```
JSON-OPTIMIZER/
├── requirements.txt          # Python dependencies
├── README.md                 # This file
└── app/
    ├── main.py              # FastAPI application
    ├── models.py            # Pydantic schemas
    ├── detectors/
    │   ├── __init__.py
    │   └── toon_detector.py # Pandas detection logic
    ├── optimizers/
    │   ├── __init__.py
    │   └── entropy_optimizer.py # TensorFlow entropy sorting
    ├── formatters/
    │   ├── __init__.py
    │   └── toon_formatter.py # TOON generation
    └── validators/
        ├── __init__.py
        └── token_validator.py # tiktoken validation
```

---

## 🎯 Use Cases

- **LLM Cost Optimization**: Reduce API costs by 40-60% on data-heavy prompts
- **Context Window Management**: Fit more data in limited context windows
- **Data Transfer**: Minimize payload sizes for API responses
- **Prompt Engineering**: Compact format for few-shot learning examples
- **Database Exports**: Compress tabular data for AI processing

---

## 🔧 Configuration

Edit `app/optimizers/entropy_optimizer.py` to change tokenizer:

```python
# Default: GPT-3.5 Turbo
encoding = tiktoken.encoding_for_model("gpt-3.5-turbo")

# For GPT-4:
encoding = tiktoken.encoding_for_model("gpt-4")

# For Claude (use cl100k_base):
encoding = tiktoken.get_encoding("cl100k_base")
```

---


## 🤝 Contributing

Contributions welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

##  Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- [TensorFlow](https://tensorflow.org) - Machine learning platform
- [Pandas](https://pandas.pydata.org/) - Data analysis library
- [tiktoken](https://github.com/openai/tiktoken) - OpenAI's tokenizer
- Inspired by the need to optimize LLM costs in production applications

---

##  Contact

**Yuvraj Verma** - [X](https://x.com/YuvrajVerma2909)

Project Link: [https://github.com/YuvrajVerma09arch/JSON-optimization-tool](hhttps://github.com/YuvrajVerma09arch/JSON-optimization-tool)

---

**Built with ❤️ for the AI community**
# 🔄 SQL Transpiler

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sql-transpiler.streamlit.app/)

A powerful and user-friendly SQL transpiler built with [Streamlit](https://streamlit.io/) and [sqlglot](https://github.com/tobymao/sqlglot). This tool allows you to easily convert SQL queries between different dialects (e.g., MySQL to PostgreSQL, Snowflake to BigQuery, etc.) with real-time formatting and identification.

## 🌐 Live Demo

You can try the app directly in your browser:
👉 **[sql-transpiler.streamlit.app](https://sql-transpiler.streamlit.app/)**


## ✨ Features

- **Multi-Dialect Support**: Transpile between dozens of SQL dialects.
- **Formatting Options**: Pretty-print your SQL for better readability.
- **Identification**: Automatically identify and quote identifiers.
- **Interactive UI**: Real-time transpilation with a clean, modern interface.

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mfangyi/sql-transpiler.git
   cd sql-transpiler
   ```

2. Install the requirements:
   ```bash
   pip install -r requirements.txt
   ```

### Running the App

Run the Streamlit application:
```bash
streamlit run streamlit_app.py
```

## 📄 License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

This project incorporates the following third-party software:

- **sqlglot**: Licensed under the **MIT License**. See the [LICENSE](LICENSE) file for the full license text and attribution.

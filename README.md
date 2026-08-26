# SQL Transpiler

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://sql-transpiler.streamlit.app/)

A powerful and user-friendly SQL transpiler built with [Streamlit](https://streamlit.io/) and [sqlglot](https://github.com/tobymao/sqlglot). This tool allows you to easily convert SQL queries between different dialects (e.g., MySQL to PostgreSQL, Snowflake to BigQuery, etc.) with real-time formatting and identification.

## Live Demo

You can try the app directly in your browser:
👉 **[sql-transpiler.streamlit.app](https://sql-transpiler.streamlit.app/)**


## Features

- **Multi-Dialect Support**: Transpile between dozens of SQL dialects.
- **Formatting Options**: Pretty-print your SQL for better readability.
- **Identification**: Automatically identify and quote identifiers.
- **Interactive UI**: Real-time transpilation with a clean, modern interface.

## How to run it on your own machine

Prerequisite: install `uv` if you don't already have it.

```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

1. Sync the dependencies

   ```
   $ uv sync
   ```

2. Run the app

   ```
   $ uv run streamlit run streamlit_app.py
   ```

## License

This project is licensed under the **Apache License 2.0**. See the [LICENSE](LICENSE) file for details.

### Third-Party Licenses

This project incorporates the following third-party software:

- **sqlglot**: Licensed under the **MIT License**. See the [LICENSE](LICENSE) file for the full license text and attribution.

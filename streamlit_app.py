import streamlit as st
import sqlglot
from sqlglot import transpile

st.set_page_config(page_title="SQL Transpiler", layout="wide")

st.title("🔄 SQL Transpiler")
st.markdown("""
### About
This tool leverages the powerful [sqlglot](https://github.com/tobymao/sqlglot) library to transpile SQL queries between different dialects. It supports a wide range of SQL dialects and provides options for formatting and identifying SQL queries.
""")

st.divider()

dialects = sorted([d.value for d in sqlglot.Dialects if d.value])

# Input Section
st.subheader("📥 Input SQL")
input_sql = st.text_area("Enter your SQL query here:", height=200, placeholder="SELECT * FROM table...")

st.divider()

# Options Section
st.subheader("✨ Transpilation Options")

# Dialect Selection and Options
options_columns = st.columns([2, 2, 1, 1])
with options_columns[0]:
    input_dialect = st.selectbox("Input Dialect", options=dialects, index=dialects.index("mysql") if "mysql" in dialects else 0)
with options_columns[1]:
    output_dialect = st.selectbox("Output Dialect", options=dialects, index=dialects.index("postgres") if "postgres" in dialects else 0)
with options_columns[2]:
    enable_identify = st.checkbox("Identify", value=True)
with options_columns[3]:
    enable_pretty = st.checkbox("Pretty", value=True)

# Transpile Button
transpile_button = st.button("✨ Transpile SQL ✨", use_container_width=True)

# Fixed Formatting Options
pad_spaces = 4
indent_spaces = 4

st.divider()

# Output Section
st.subheader("📤 Output SQL")
output_display = st.empty()

if transpile_button:
    if input_sql.strip():
        try:
            transpiled_sql = transpile(
                input_sql,
                read=input_dialect,
                write=output_dialect,
                pretty=enable_pretty,
                identify=enable_identify,
                pad=pad_spaces,
                indent=indent_spaces,
            )
            output_display.code("\n".join(transpiled_sql), language="sql")
        except Exception as error:
            st.error(f"Transpilation Error: {error}")
    else:
        st.warning("Please enter some SQL code first.")
else:
    output_display.info("Click 'Transpile SQL' to see the result.")

st.divider()

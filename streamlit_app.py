import streamlit as st
import sqlglot
from sqlglot import transpile

st.set_page_config(page_title="SQL Transpiler", layout="wide")

st.title("🔄 SQL Transpiler")

st.divider()

dialects = sorted([d.value for d in sqlglot.Dialects if d.value])

col1, col_btn, col2 = st.columns([1, 0.2, 1])

with col1:
    st.subheader("📥 Input SQL")
    read_dialect = st.selectbox("", options=dialects,
                                index=dialects.index("mysql") if "mysql" in dialects else 0, label_visibility="collapsed")
    sql_input = st.text_area("", height=400, placeholder="SELECT * FROM table...", label_visibility="collapsed")

with col_btn:
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    transpile_clicked = st.button("✨Transpile✨", use_container_width=True, key="transpile_btn")
    st.markdown("**Options:**")
    identify = st.checkbox("Identify", value=True)
    pretty = st.checkbox("Pretty", value=True)
    if pretty:
        pad = st.number_input("Pad", min_value=0, value=4, step=1)
        indent = st.number_input("Indent", min_value=0, value=4, step=1)
    else:
        pad = 4
        indent = 4

with col2:
    st.subheader("📤 Output SQL")
    write_dialect = st.selectbox("", options=dialects,
                                 index=dialects.index("postgres") if "postgres" in dialects else 0, label_visibility="collapsed")

    output_container = st.empty()

if transpile_clicked:
    if sql_input.strip():
        try:
            transpiled = transpile(
                sql_input,
                read=read_dialect,
                write=write_dialect,
                pretty=pretty,
                identify=identify,
                pad=pad,
                indent=indent,
            )
            sql_output = "\n".join(transpiled)
            output_container.code(sql_output, language="sql")
        except Exception as e:
            st.error(f"Transpilation Error: {e}")
    else:
        st.warning("Please enter some SQL code first.")
else:
    output_container.info("Click 'Transpile' to see the result.")

st.divider()

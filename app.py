import streamlit as st

st.set_page_config(page_title="SQL Translator", layout="wide")

st.title("🛠️ SQL Translator")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Source Language")
    source_lang = st.selectbox("Choose Source SQL Dialect", ["MySQL", "PostgreSQL", "SQL Server", "Oracle", "BigQuery"], key="source_lang")
    source_sql = st.text_area("Source SQL", height=400, key="source_sql")

with col2:
    st.markdown("### Target Language")
    target_lang = st.selectbox("Choose Target SQL Dialect", ["MySQL", "PostgreSQL", "SQL Server", "Oracle", "BigQuery"], key="target_lang")
    target_sql = st.text_area("Target SQL", height=400, key="target_sql")

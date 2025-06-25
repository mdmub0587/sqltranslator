import streamlit as st
from agents import agent

st.set_page_config(page_title="SQL Translator", layout="wide")
agent_object = agent()

st.markdown("""
    <h1 style='text-align: center; color: #4A4A4A;'>🛠️ SQL Translator</h1>
""", unsafe_allow_html=True)
st.markdown("###")

# Create two columns for source and target
col1, col2 = st.columns(2)

with col1:
    st.markdown("### Source Language")
    source_sql = st.text_area("Source SQL", height=400, key="source_sql")
    dialect = "MySQL"
    op_type = "DDL"
    if source_sql:
        dialect = agent_object.detect_sql_dialect(source_sql)
        op_type = agent_object.detect_sql_type(source_sql)

    col11, col12 = st.columns(2)
    with col11:
        dialect_list = ["MySQL", "PostgreSQL", "SQL Server", "Oracle", "BigQuery"]
        detected_dialect = dialect_list.index(dialect)
        source_lang = st.selectbox("Choose Source SQL Dialect", 
                                dialect_list, 
                                index=detected_dialect,
                                key="source_lang")
    with col12:
        op_type_list = ["DML", "DDL", "DCL", "TCL"]
        detected_op_type = op_type_list.index(op_type)
        sql_type = st.selectbox("SQL Type", 
                                op_type_list,
                                index = detected_op_type,
                                key="sql_type")

with col2:
    st.markdown("### Target Language")
    target_sql = st.text_area("Target SQL", height=400, key="target_sql")

    target_lang = st.selectbox("Choose Target SQL Dialect", 
                               ["MySQL", "PostgreSQL", "SQL Server", "Oracle", "BigQuery"], 
                               key="target_lang")
    

# Centered Convert Button
col_convert = st.columns([0.45,0.1,0.45])
with col_convert[1]:
    convert = st.button("🔄 Convert")

# Optional placeholder for logic
if convert:
    # Placeholder logic: replace with actual translation
    st.success("Translation successful!")
    st.write("🔧 (Translation logic would appear here.)")

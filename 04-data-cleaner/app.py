import streamlit as st
import pandas as pd

st.set_page_config(page_title="Data Cleaner", page_icon="📊", layout="wide")
st.title("📊 CSV / Excel Data Cleaner + Report")
st.caption("Upload messy data → clean it and get a quick summary report.")

uploaded = st.file_uploader("Upload CSV or Excel", type=["csv", "xlsx"])

if uploaded:
    if uploaded.name.endswith(".csv"):
        df = pd.read_csv(uploaded)
    else:
        df = pd.read_excel(uploaded)

    st.subheader("Original Data Preview")
    st.dataframe(df.head(10))

    st.subheader("Basic Cleaning Options")
    drop_na = st.checkbox("Drop rows with missing values", value=True)
    drop_dupes = st.checkbox("Remove duplicate rows", value=True)

    if st.button("Clean Data", type="primary"):
        cleaned = df.copy()
        if drop_na:
            cleaned = cleaned.dropna()
        if drop_dupes:
            cleaned = cleaned.drop_duplicates()

        st.success(f"Cleaned! Rows: {len(df)} → {len(cleaned)}")
        st.dataframe(cleaned)

        st.subheader("Quick Report")
        st.write("Shape:", cleaned.shape)
        st.write("Columns:", list(cleaned.columns))
        st.write("Missing values left:", cleaned.isnull().sum().sum())

        # Download
        csv = cleaned.to_csv(index=False).encode("utf-8")
        st.download_button("Download Cleaned CSV", csv, "cleaned_data.csv", "text/csv")

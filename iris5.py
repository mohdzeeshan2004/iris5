import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# ✅ MUST be the first Streamlit command
st.set_page_config(page_title="IRIS Dataset EDA", layout="wide")

# Clear cache safely
st.cache_data.clear()
if hasattr(st, "cache_resource"):
    st.cache_resource.clear()

# Title
st.title("🌸 IRIS Dataset – Exploratory Data Analysis")

# Load dataset
@st.cache_data
def load_data():
    return sns.load_dataset("iris")

data = load_data()

# Sidebar
st.sidebar.header("EDA Options")
eda_option = st.sidebar.selectbox(
    "Select Analysis Type",
    [
        "Dataset Overview",
        "Statistical Summary",
        "Distribution Plot",
        "Joint Plot",
        "Pair Plot",
        "Boxen Plot",
        "Strip Plot",
        "Swarm Plot"
    ]
)

# ===================== DATASET OVERVIEW =====================
if eda_option == "Dataset Overview":
    st.subheader("📄 Dataset Preview")
    st.dataframe(data)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", data.shape[0])
    col2.metric("Columns", data.shape[1])
    col3.metric("Missing Values", data.isnull().sum().sum())
    
    st.subheader("Column Info")
    st.write(data.dtypes)

# ===================== STATISTICS =====================
elif eda_option == "Statistical Summary":
    st.subheader("📊 Descriptive Statistics")
    st.dataframe(data.describe())

# ===================== DISTRIBUTION =====================
elif eda_option == "Distribution Plot":
    st.subheader("📈 Distribution Plot")
    
    column = st.selectbox(
        "Select Column",
        ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    )
    
    fig, ax = plt.subplots()
    sns.histplot(data[column], kde=True, ax=ax)
    ax.set_title(f"Distribution of {column}")
    st.pyplot(fig)
    plt.close(fig)

# ===================== JOINT PLOT =====================
elif eda_option == "Joint Plot":
    st.subheader("🔗 Joint Plot")
    
    numeric_cols = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    x_col = st.selectbox("X Axis", numeric_cols, key="joint_x")
    y_col = st.selectbox("Y Axis", numeric_cols, index=1, key="joint_y")
    
    if x_col == y_col:
        st.warning("⚠️ Please select different columns for X and Y axis")
    else:
        kind = st.selectbox("Plot Type", ["scatter", "reg", "hex", "kde"])
        

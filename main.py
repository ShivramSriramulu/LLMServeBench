import streamlit as st
import json
import pandas as pd
import plotly.express as px

# Load data
with open("metrics.json") as f:
    data = json.load(f)

df = pd.DataFrame(data)

# Sidebar Filters
st.sidebar.title("🔧 Controls")
model_filter = st.sidebar.multiselect("Select Models", df["model"].unique(), default=df["model"].unique())
device_filter = st.sidebar.radio("Device Type", ["CPU"], index=0)  # Future GPU option

filtered_df = df[df["model"].isin(model_filter)]

# Tabs
tab1, tab2, tab3 = st.tabs(["📊 Overview", "⚡ Latency & RAM", "🧠 KV Cache Insights"])

with tab1:
    st.title("📊 Model Comparison Dashboard")
    st.write("Compare performance across FP32, INT8, and KV cache-optimized models.")
    st.dataframe(filtered_df)

with tab2:
    st.header("⚡ Latency & RAM Usage")

    st.subheader("Latency (ms)")
    st.bar_chart(filtered_df.set_index("model")[["latency_ms"]])

    st.subheader("RAM Usage (MB)")
    st.bar_chart(filtered_df.set_index("model")[["ram_usage_mb"]])

    st.subheader("Model Sizes")
    fig = px.pie(filtered_df, values="size_mb", names="model", title="Model Size Distribution")
    st.plotly_chart(fig)

with tab3:
    st.header("🧠 KV Cache Effectiveness (GPT-2)")

    kv_data = filtered_df[filtered_df["model"].str.contains("GPT2")]
    if not kv_data.empty:
        fig_kv = px.bar(
            kv_data, x="model", y="latency_ms", color="model",
            title="KV Cache vs No Cache - Latency Comparison"
        )
        st.plotly_chart(fig_kv)
    else:
        st.warning("KV cache data not available. Please run GPT2 benchmarks in Colab.")

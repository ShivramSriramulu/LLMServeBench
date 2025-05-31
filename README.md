# LLMServeBench

![LLMServeBench](Image.png)

**LLMServeBench** is a benchmarking and visualization toolkit for evaluating and comparing the performance of Large Language Models (LLMs) under different optimization and serving strategies — including quantization and KV cache reuse.

---

## 🌐 Live Demo

👉 [LLMServeBench Live App](https://shivramsriramulu-llmservebench-main-8sxjtb.streamlit.app/)

---

## 📂 GitHub Repository

👉 [GitHub – ShivramSriramulu/LLMServeBench](https://github.com/ShivramSriramulu/LLMServeBench.git)

---

## 🚀 Overview

LLMServeBench helps ML engineers and researchers:

- Benchmark transformer models (like DistilBERT, GPT-2) for inference latency and memory usage.
- Apply optimizations like ONNX conversion, INT8 quantization, and KV cache reuse.
- Visualize benchmarking results with an interactive Streamlit dashboard.

---

## 🔧 Key Features

- 🧠 **Benchmark LLM inference latency and memory usage**
- ⚙️ **Compare FP32 vs INT8 quantized models**
- 🧮 **KV cache reuse support for decoder-only models (GPT-2)**
- 📉 **Visualize performance metrics using Streamlit and Plotly**
- 💾 **Export results as `metrics.json` from Colab**
- 🔌 **Run locally on CPU (MacBook) or in Colab (T4/A100 GPUs)**

---

## 📥 Installation

```bash
git clone https://github.com/ShivramSriramulu/LLMServeBench.git
cd LLMServeBench
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
▶️ Run the Streamlit App
After generating metrics.json from Colab:

bash
Copy
Edit
streamlit run main.py
Then open your browser at: http://localhost:8501

🧪 Colab Benchmarking Pipeline
✅ What You Can Do in Google Colab
Load and run transformer models (DistilBERT, GPT2-small)

Convert to ONNX and quantize to INT8

Benchmark latency, RAM, and model size

Run GPT-2 with and without KV cache

Export results to metrics.json

❌ What You Can't Fully Do
Run TensorRT (not supported on Colab)

Use FastAPI servers or persistent hosting

Use ONNX Runtime GPU with full support on CPU-only devices

🛠️ Sample Benchmarking Flow
🔹 Step 1: In Colab
Load DistilBERT/GPT2

Convert to ONNX

Quantize using onnxruntime.quantization

Measure:

Latency (ms)

RAM usage (MB)

Model size (MB)

Benchmark GPT2 with KV cache ON/OFF

Save metrics to metrics.json

🔹 Step 2: Locally in Streamlit
bash
Copy
Edit
pip install streamlit plotly pandas
streamlit run main.py
Load and visualize metrics.json

📁 Project Structure
bash
Copy
Edit
LLMServeBench/
├── main.py              # Streamlit dashboard
├── metrics.json         # Benchmark metrics output from Colab
├── requirements.txt     # Project dependencies
├── LLMServeBench.ipynb  # Optional Colab/Notebook version
├── Image.png            # Project banner image
└── README.md            # You are here
📦 Requirements
Listed in requirements.txt:

nginx
Copy
Edit
streamlit
plotly
pandas
numpy
torch
transformers
onnx
onnxruntime
psutil
scikit-learn
Install them with:

bash
Copy
Edit
pip install -r requirements.txt
🤝 Contributing
We welcome contributions! Feel free to:

Fork the repo

Create a new branch

Submit a pull request

📄 License
This project is licensed under the MIT License.


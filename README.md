# Market Snapshot Service

A production-grade Python utility designed to capture and analyze key financial indicators (S&P 500, VIX, 10Y Yield) to provide an instant "Market Volatility" context.

Unlike basic scrapers, this service is engineered for **reliability** and **headless deployment** (e.g., Docker/Raspberry Pi).

## 🚀 Key Features

* **Fault Tolerance:** Implements robust error handling and graceful degradation. If a data source (e.g., Yahoo Finance) fails, the system logs the error and continues without crashing.
* **Structured Logging:** Replaced standard console output with Python's `logging` module for better observability in containerized environments.
* **Data Safety:** Uses dynamic history fetching (`iloc[-1]`) to prevent "index out of range" errors during market holidays or partial data returns.
* **Modular Architecture:** Utility logic is decoupled (`utils.py`) from business logic for better maintainability and testing.

## 🛠️ Tech Stack

* **Core:** Python 3.10+
* **Data:** `yfinance` (Yahoo Finance API)
* **Data Structures:** Pandas (DataFrames)
* **Quality:** Type Hinting (`typing`), PEP 8 Standards

## 📦 Installation

1. **Clone the repository**
```bash
git clone https://github.com/axcelt/market-snapshot.git
cd market-snapshot

```


2. **Set up Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate

```


3. **Install Dependencies**
```bash
pip install -r requirements.txt

```



## 🏃 Usage

Run the entry point directly. The service will fetch live data and print a formatted table to the standard output (stdout).

```bash
python main.py

```

**Sample Output:**

```text
--- MARKET SNAPSHOT: 2026-01-05 09:30:01 ---

Metric               | Value          
-----------------------------------
S&P 500              | 4,780.25       
VIX                  | 12.40          
Volatility State     | Low / Complacent
US 10Y Yield         | 4.05%          
USD/PHP              | 55.50          

```

## 🔮 Roadmap

* [ ] **Docker Support:** Containerize the application for "write once, run anywhere" deployment.
* [ ] **API Mode:** Expose data via FastAPI for consumption by dashboards (e.g., Homepage).
* [ ] **Database Integration:** Persist historical VIX states to track trends over time.

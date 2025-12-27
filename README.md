# Market Snapshot Script

A basic Python script that captures a financial market snapshot. It fetches the current date and values for key market indicators to provide a quick "Market Context" overview.

## Data Points Tracked
* **S&P 500** (Market Performance)
* **VIX** (Volatility Index)
* **Volatility State** (Calculated based on VIX)
* **US 10Y Yield** (Interest Rates)
* **USD/PHP** (Currency Exchange)

## Prerequisites
* Python 3.x installed on your machine.
* Git (for version control).

## Windows Setup Guide

1.  **Initialize the Project**
    Open your terminal/PowerShell in this folder:
    ```powershell
    git init
    ```

2.  **Create the Environment**
    Create a virtual environment to isolate dependencies:
    ```powershell
    python -m venv venv
    ```

3.  **Activate the Environment**
    *Always run this before working on the project:*
    ```powershell
    .\venv\Scripts\activate
    ```
    *(You should see `(venv)` in your terminal prompt)*

4.  **Install Dependencies**
    Install the required financial libraries:
    ```powershell
    pip install yfinance pandas
    ```

## How to Run
*(Ensure your environment is active first)*
```powershell
python main.py

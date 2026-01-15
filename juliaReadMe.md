# Feature Request: Investment Journal

**Status:** Open
**Assignee:** @Sister
**Branch:** feat/journalling

## 1. Overview
We need a way to record personal investment thoughts ("Journal Entries") and automatically attach the current market context (S&P 500 price, VIX, etc.) to those thoughts. This will allow us to analyze how market sentiment influenced our decision-making in the future.

## 2. Developer Setup
Before writing code, ensure your local development environment is ready.

1.  **Python**: Ensure you have Python 3.10+ installed.
2.  **Virtual Environment**: We use a virtual environment to manage dependencies so they don't conflict with other projects.
    ```bash
    # Create the virtual environment (only need to do this once)
    python -m venv venv
    
    # Activate it (Windows)
    .\venv\Scripts\activate

    # Activate it (Mac/Linux)
    source venv/bin/activate
    ```
3.  **Dependencies**: Install the required libraries found in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```
4.  **Verify**: Run the existing main script to make sure it works.
    ```bash
    python main.py
    ```
    *Success criteria:* You should see a table with "S&P 500", "VIX", etc. printed to your console.

## 3. Requirements
Your task is to create a Python script (recommend naming it `journal.py`) that performs the following:

1.  **User Input**: Prompt the user to type in a **Title** and a **Journal Entry**.
2.  **Market Context**: Fetch the *live* market data using the existing logic.
    * *Hint:* You do not need to rewrite the fetching logic. Look at `main.py` to see how `fetch_market_snapshot` is imported and used.
3.  **Data Merge**: Combine the User Input and the Market Context into a single data structure (like a Dictionary).
4.  **Save to File**: Save this combined record into a JSON file named `journal_entries.json`.
    * *Constraint:* If the file already exists, the new entry should be added to the list (append), not overwrite the old ones.

## 4. Definition of Done
* [ ] Running `python journal.py` prompts the user for input.
* [ ] A `journal_entries.json` file is created (or updated).
* [ ] The JSON file contains the user's text AND the market snapshot (e.g., "S&P 500": 4780.25).
* [ ] Code is clean and readable.

## 5. Big Brother Notes
* It is not the 1800s you can use AI, but please use it in an eduactional manner.
* GOOD LUCK Big Sissy!
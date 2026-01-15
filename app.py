from flask import Flask, jsonify, render_template
from main import fetch_market_snapshot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/snapshot')
def get_snapshot():
    """
    Returns the market snapshot as JSON.
    """
    data = fetch_market_snapshot()
    return jsonify(data)

if __name__ == '__main__':
    # reliable dev server
    app.run(host='0.0.0.0', port=5000, debug=True)

    # --- NEW JOURNAL FEATURE START ---

@app.route('/journal', methods=['GET', 'POST'])
def journal_page():
    """
    Handles displaying the journal form (GET) 
    and processing the submitted entry (POST).
    """
    if request.method == 'POST':
        # 1. Get data from the form
        # Hint: title = request.form.get('title')
        
        # 2. Get market data
        # Hint: market_data = fetch_market_snapshot()
        
        # 3. Create the data structure
        
        # 4. Save to JSON file (Reuse your logic from the practice script!)
        
        # 5. Return a success message or render a template with the data
        return "Journal Saved! (You need to make this prettier)"
    
    # If it's a GET request, just show the form
    return render_template('journal_sample.html') # needs to create/rename this

# --- NEW JOURNAL FEATURE END ---
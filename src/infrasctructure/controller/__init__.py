from .app import app

def start():
    app.run(debug=True, host='0.0.0.0', port=5000, use_reloader=False)

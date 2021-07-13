from quantr.maindash import app
from quantr.views import candles

if __name__ == "__main__":
    app.layout = candles.make_layout
    app.run_server(debug=True)

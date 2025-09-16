from flask import Flask, jsonify, render_template
from flask import Flask, jsonify, render_template
from solar_alert import fetch_solar_flare_data, process_data_and_alert

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/alerts')
def get_alerts():
    solar_data = fetch_solar_flare_data()
    alerts = process_data_and_alert(solar_data, threshold=1.0e-6)  

    return jsonify(alerts)

@app.route('/flux_data')
def get_flux_data():
    solar_data = fetch_solar_flare_data()
    flux_list = [{"time": rec.get("time_tag"), "flux": rec.get("flux", 0)} for rec in solar_data]
    return jsonify(flux_list)

if __name__ == '__main__':
    app.run(debug=True)




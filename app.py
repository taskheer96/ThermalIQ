from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__, template_folder='.')

def get_awareness_status(temp):
    # Updated to use highly expressive emojis based on the temperature!
    if temp > 38:
        return {"status": "Extreme Heat", "symbol": "🤬🔥", "color": "#8B0000"}
    elif 30 <= temp <= 38:
        return {"status": "High Heat", "symbol": "🥵💦", "color": "#FF4500"}
    elif 18 <= temp < 30:
        return {"status": "Moderate", "symbol": "😌🍃", "color": "#2E8B57"}
    elif 10 <= temp < 18:
        return {"status": "Light Cold", "symbol": "🥶❄️", "color": "#87CEEB"}
    else:
        return {"status": "Extreme Cold", "symbol": "⛄🧊", "color": "#000080"}
def get_coordinates(location_name):
    # Check if the user already typed a comma (e.g., "Paris, France"). 
    # If not, automatically force it to search in India.
    if "," not in location_name:
        location_name = f"{location_name}, India"

    url = f"https://geocoding-api.open-meteo.com/v1/search?name={location_name}&count=1&format=json"
    response = requests.get(url).json()
    
    if "results" in response and len(response["results"]) > 0:
        # We can also grab the state/country to display it so the user knows it worked!
        lat = response["results"][0]["latitude"]
        lon = response["results"][0]["longitude"]
        
        # Build a better name (e.g., "Nalanda, Bihar, India")
        city = response["results"][0].get("name", "")
        state = response["results"][0].get("admin1", "")
        country = response["results"][0].get("country", "")
        
        # Filter out empty strings and join them nicely
        full_name = ", ".join(filter(None, [city, state, country]))
        
        return lat, lon, full_name
        
    return None, None, None

def get_weather_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max&timezone=auto"
    response = requests.get(url).json()
    dates = response['daily']['time']
    temps = response['daily']['temperature_2m_max']
    avg_temp = sum(temps) / len(temps)
    return dates, temps, avg_temp

# Serve the main frontend
@app.route('/')
def index():
    return render_template('index.html')

# NEW: Serve the books page
@app.route('/books.html')
def books():
    return render_template('books.html')

@app.route('/api/compare', methods=['POST'])
def compare_locations():
    data = request.json
    urban_input = data.get('urban')
    rural_input = data.get('rural')

    u_lat, u_lon, u_name = get_coordinates(urban_input)
    r_lat, r_lon, r_name = get_coordinates(rural_input)

    if not u_lat or not r_lat:
        return jsonify({"error": "Could not find one or both locations. Please try again."}), 404

    u_dates, u_temps, u_avg = get_weather_data(u_lat, u_lon)
    r_dates, r_temps, r_avg = get_weather_data(r_lat, r_lon)

    u_status = get_awareness_status(u_avg)
    r_status = get_awareness_status(r_avg)

    return jsonify({
        "urban": {"name": u_name, "lat": u_lat, "lon": u_lon, "temps": u_temps, "avg": round(u_avg, 2), "status": u_status},
        "rural": {"name": r_name, "lat": r_lat, "lon": r_lon, "temps": r_temps, "avg": round(r_avg, 2), "status": r_status},
        "dates": u_dates,
        "difference": round(u_avg - r_avg, 2)
    })

if __name__ == '__main__':
    app.run(debug=True)
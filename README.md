# 🌡️ ThermalIQ — Urban Heat Island Analysis Tool

**ThermalIQ** is an interactive web application designed to analyze **Urban Heat Island (UHI)** effects by comparing temperature differences between **urban and rural locations** using **live meteorological data**.

The platform transforms raw atmospheric data into **clear visual insights**, helping users understand temperature disparities and environmental impact.

---

# 🎯 Objective

Compare temperature differences between **urban and rural areas** to identify **Urban Heat Island effects** using real-time weather data and intuitive visualizations.

---

# 🚀 Features

* 📍 Location-based temperature comparison
* 🌡️ 7-Day maximum temperature analysis
* ⏱️ 24-Hour hourly temperature profile
* 🔥 Thermal Delta (Heat Gap) calculation
* 📊 Multi-chart visualization suite
* 🗺️ Interactive Leaflet map
* 😊 Dynamic heat severity interpretation
* 🎨 Premium UI with immersive environment

---

# 🧠 System Workflow

### 1. Geographic Input & Geocoding

Users enter location names which are converted into **precise coordinates** using:

* Open-Meteo Geocoding API
* Interactive dropdown selection

---

### 2. Asynchronous Telemetry Fetch

The system retrieves:

* 7-day daily maximum temperatures
* 24-hour hourly temperature data

Using **live meteorological APIs**.

---

### 3. Diagnostic Processing

The internal JavaScript engine calculates:

* Mean temperature (Urban)
* Mean temperature (Rural)
* Thermal Delta (Heat Gap)

This forms the **core analysis metric**.

---

### 4. Multidimensional Visualization

Data is visualized through:

* 📈 Line Chart
* 🕒 Diurnal Chart
* 📊 Bar Comparison
* 🔥 Heat Penalty Chart
* 🗺️ Interactive Leaflet Map

---

### 5. Behavioral & Thematic Output

Based on heat gap severity:

* Emotional status emojis assigned
* Immersive UI theme applied
* Final visual report generated

---

# 🛠️ Technologies Used

* HTML5
* CSS3
* JavaScript (Vanilla JS)
* Open-Meteo API
* Leaflet.js
* Chart.js (or charts library used)

---

# 📂 Project Structure

```
ThermalIQ/
│
├── index.html
├── books.html
├── README.md
└── LICENSE
```

---

# 🌍 Live Demo

Access the live project:

```
https://taskheer96.github.io/ThermalIQ/
```

---

# 📈 Use Cases

* Climate research
* Environmental studies
* Urban planning
* Academic projects
* Weather analytics
* Sustainability analysis

---

# 👨‍💻 Author

**Md Taskheer Kamal**

---

# 📜 License

This project is licensed under **Creative Commons Zero v1.0 Universal (CC0-1.0)**

You are free to:

* Use
* Modify
* Distribute
* Commercialize

No permission required.

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

---

**ThermalIQ — Turning Atmospheric Data into Actionable Insight**

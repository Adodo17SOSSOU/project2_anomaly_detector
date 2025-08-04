# Project 2: Advanced Anomaly Detector

This project implements a **real-time anomaly detection system** for multiple sensors. It continuously monitors simulated sensor data, detects anomalies using a Z-score method, logs all readings with timestamps, and generates plots of the results.

---

## **Features**

* Simulates data from 3 virtual sensors.
* Detects anomalies using a sliding window with Z-score thresholding.
* Logs all readings (with timestamps and anomaly flags) to a CSV file.
* Generates **automated visualizations** saved as PNG files.
* Modular and extensible for real-time applications.

---

## **Project Structure**

```
project2_anomaly_detector/
│
├── src/
│   ├── data_generator.py       # Generates random sensor readings
│   ├── anomaly_detector.py     # Detects anomalies using Z-score
│   ├── run_detector.py         # Main script to monitor data and log to CSV
│   └── visualize_log.py        # Generates PNG plots from CSV logs
│
├── sensor_log.csv              # Auto-generated log of readings and anomalies
├── sensor_plot.png             # Auto-generated visualization of sensor data
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

---

## **Installation**

1. **Clone the repository**

```bash
git clone <your_repo_url>
cd project2_anomaly_detector
```

2. **Create and activate a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

---

## **Usage**

### **1. Generate Sensor Data (Optional)**

You can manually generate random sensor data:

```bash
python src/data_generator.py
```

### **2. Run Real-Time Anomaly Detection**

Start monitoring sensors and logging results:

```bash
python src/run_detector.py
```

* Logs will be saved to `sensor_log.csv`.
* Press **Ctrl + C** to stop monitoring.

### **3. Visualize Results**

Generate a **PNG plot** from the logged data:

```bash
python src/visualize_log.py
```

This will produce `sensor_plot.png` with:

* Sensor value trends over time.
* Marked anomalies in the readings.

---

## **Example Output**

* **sensor\_log.csv**

```
timestamp,sensor1,sensor2,sensor3,anomaly
2025-08-04 14:12:10,49.13,76.06,74.82,0
2025-08-04 14:12:12,57.89,75.39,69.95,0
2025-08-04 14:12:14,61.91,76.31,73.40,0
```

* **sensor\_plot.png**
  A line chart of sensor readings with red crosses marking anomalies.

---

## **Future Improvements**

* Add **automatic plotting every 10 minutes**.
* Support **real sensor inputs** via MQTT or WebSocket.
* Implement **email/SMS alerts** on anomaly detection.
* Deploy as a **web dashboard** using Dash or Streamlit.

---

## **Requirements**

* Python 3.8+
* pandas
* matplotlib
* numpy

Install all using:

```bash
pip install -r requirements.txt
```

---



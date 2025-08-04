import csv
import time
from datetime import datetime
from data_generator import DataGenerator
from anomaly_detector import AnomalyDetector

LOG_FILE = "sensor_log.csv"

def main():
    generator = DataGenerator(max_value=200, anomaly_chance=0.05)
    detector = AnomalyDetector(window_size=50, z_threshold=3.0)

    # Ensure log file exists with header
    with open(LOG_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "sensor1", "sensor2", "sensor3", "anomaly"])

    print("Starting data monitoring... Press Ctrl+C to stop.")

    try:
        while True:
            data = generator.generate()
            values = [data['sensor1'], data['sensor2'], data['sensor3']]
            is_anomaly = detector.detect(values)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            row = [timestamp] + values + [int(is_anomaly)]

            # Append to CSV
            with open(LOG_FILE, 'a', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(row)

            print(f"{timestamp} | {values} | Anomaly: {is_anomaly}")
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nMonitoring stopped. Data saved to sensor_log.csv")

if __name__ == "__main__":
    main()


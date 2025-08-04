import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE = "sensor_log.csv"
OUTPUT_FILE = "sensor_plot.png"

def visualize_log():
    # Load the CSV
    df = pd.read_csv(LOG_FILE)

    if df.empty:
        print("No data found in the log file.")
        return

    # Convert timestamp to datetime for proper plotting
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    # Create figure
    plt.figure(figsize=(12, 6))

    # Plot each sensor
    plt.plot(df['timestamp'], df['sensor1'], label='Sensor 1')
    plt.plot(df['timestamp'], df['sensor2'], label='Sensor 2')
    plt.plot(df['timestamp'], df['sensor3'], label='Sensor 3')

    # Highlight anomalies
    anomalies = df[df['anomaly'] == 1]
    if not anomalies.empty:
        plt.scatter(anomalies['timestamp'], anomalies['sensor1'], color='red', label='Anomaly (S1)', marker='x')
        plt.scatter(anomalies['timestamp'], anomalies['sensor2'], color='orange', label='Anomaly (S2)', marker='x')
        plt.scatter(anomalies['timestamp'], anomalies['sensor3'], color='purple', label='Anomaly (S3)', marker='x')

    plt.xlabel('Time')
    plt.ylabel('Sensor Values')
    plt.title('Sensor Data and Detected Anomalies')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    # Save the plot as a PNG
    plt.savefig(OUTPUT_FILE, dpi=300)
    plt.close()
    print(f"Plot saved as {OUTPUT_FILE}")

if __name__ == "__main__":
    visualize_log()


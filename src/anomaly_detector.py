from collections import deque
import statistics

class AnomalyDetector:
    def __init__(self, window_size=50, z_threshold=3.0):
        self.window_size = window_size
        self.z_threshold = z_threshold
        self.data_window = deque(maxlen=window_size)

    def detect(self, values):
        """Detect anomaly using Z-score."""
        self.data_window.append(values)

        if len(self.data_window) < self.window_size:
            return False  # Not enough data yet

        # Compute mean and std for each sensor
        transposed = list(zip(*self.data_window))  # [(s1,s1,..),(s2..),(s3..)]
        for i, sensor_values in enumerate(transposed):
            mean = statistics.mean(sensor_values)
            stdev = statistics.pstdev(sensor_values)
            if stdev == 0:
                continue
            z_score = abs((values[i] - mean) / stdev)
            if z_score > self.z_threshold:
                return True
        return False


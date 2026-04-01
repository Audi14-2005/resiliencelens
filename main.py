from data.stream_simulator import stream_data, event_queue
from core.anomaly import train_anomaly_model, detect_anomaly
from utils.helpers import print_report
import threading

def main():
    model = train_anomaly_model()

    # Start streaming in background
    threading.Thread(target=stream_data, daemon=True).start()

    while True:
        if not event_queue.empty():
            event = event_queue.get()

            is_anomaly = detect_anomaly(model, event)

            score = 80 if is_anomaly else 20
            issues = ["Anomaly detected in system"] if is_anomaly else []

            print("\033c", end="")
            print("Live Event:", event)
            print_report(score, issues)

if __name__ == "__main__":
    main()
from ultralytics import YOLO
import cv2
from collections import Counter

model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

print("Counting ON - Press 'q' to quit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, conf=0.35, verbose=False)
    annotated = results[0].plot()

    # --- COUNTING LOGIC ---
    if len(results[0].boxes) > 0:
        classes = [model.names[int(c)] for c in results[0].boxes.cls]
        counts = Counter(classes)

        # Build text like "person: 2 | car: 3 | bottle: 1"
        count_text = " | ".join([f"{k}: {v}" for k, v in counts.items()])
        total_text = f"Total: {len(classes)} objects"

        # Draw black background for text
        cv2.rectangle(annotated, (10, 10), (950, 70), (0,0,0), -1)
        cv2.putText(annotated, count_text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
        cv2.putText(annotated, total_text, (20, 65), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,255,255), 2)
    else:
        cv2.rectangle(annotated, (10, 10), (300, 50), (0,0,0), -1)
        cv2.putText(annotated, "No objects", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

    cv2.imshow("Live Counter - Team ObjectDetect", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
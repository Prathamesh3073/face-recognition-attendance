import cv2
import os
from datetime import datetime

# Load Haar Cascade
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

# Load trained model
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/model.yml")

# Load names from dataset
names = {}
for file in os.listdir("dataset"):
    try:
        name, id, _ = file.split("_")
        names[int(id)] = name
    except:
        pass


# 📝 Attendance function
def mark_attendance(name):
    file = "attendance.csv"

    # Create file if not exists
    if not os.path.exists(file):
        with open(file, "w") as f:
            f.write("Name,Time\n")

    # Read existing entries
    with open(file, "r") as f:
        data = f.readlines()
        name_list = [line.split(",")[0] for line in data]

    # Avoid duplicate entry
    if name not in name_list:
        now = datetime.now().strftime("%H:%M:%S")
        with open(file, "a") as f:
            f.write(f"{name},{now}\n")


# Start webcam
cap = cv2.VideoCapture(0)

marked = set()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        # Lower confidence = better match
        if confidence < 70:
            name = names.get(id, "Unknown")
        else:
            name = "Unknown"

        # Mark attendance once
        if name != "Unknown" and name not in marked:
            mark_attendance(name)
            marked.add(name)

        # Draw rectangle
        color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
        cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)

        # Display name
        cv2.putText(
            frame,
            name,
            (x, y-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            color,
            2
        )

    cv2.imshow("Face Recognition Attendance", frame)

    # Press ESC to exit
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
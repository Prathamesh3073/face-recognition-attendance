import cv2
import os

# Create folder for saving faces
if not os.path.exists("captured_faces"):
    os.makedirs("captured_faces")

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

cap = cv2.VideoCapture(0)

img_count = 0

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera error")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 👥 Face count
    face_count = len(faces)

    for (x, y, w, h) in faces:
        # Draw rectangle
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Label
        cv2.putText(frame, "Face", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

        # 📸 Save face (press 's')
        key = cv2.waitKey(1)

        if key == ord('s'):
            face_img = frame[y:y+h, x:x+w]
            filename = f"captured_faces/face_{img_count}.jpg"
            cv2.imwrite(filename, face_img)
            print(f"Saved: {filename}")
            img_count += 1

    # 👥 Display face count
    cv2.putText(frame, f"Faces: {face_count}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    # Show window
    cv2.imshow("Face Detection Pro", frame)

    # Exit on ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
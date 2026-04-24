import cv2
import os
import numpy as np

path = "dataset"

faces = []
ids = []

for file in os.listdir(path):
    img = cv2.imread(os.path.join(path, file), 0)
    id = int(file.split("_")[1])

    faces.append(img)
    ids.append(id)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(faces, np.array(ids))

if not os.path.exists("trainer"):
    os.makedirs("trainer")

recognizer.save("trainer/model.yml")

print("Model trained!")
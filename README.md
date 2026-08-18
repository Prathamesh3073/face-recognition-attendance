# 🎓 Face Recognition Attendance System

A real-time **face recognition-based attendance system** built with **Python and OpenCV**. The system captures face data, trains an LBPH recognition model, recognizes registered users through a webcam, and automatically records attendance with the current time.

## 📌 Overview

Manual attendance tracking can be time-consuming and prone to errors. This project automates the process by using computer vision to identify registered faces through a webcam and record their attendance automatically.

The project follows a simple workflow:

```text
Capture Face Data
       ↓
Train Recognition Model
       ↓
Real-Time Face Detection
       ↓
Face Recognition
       ↓
Automatic Attendance Logging
       ↓
Web Attendance Dashboard
```

## ✨ Features

* 📷 Capture face datasets using a webcam
* 👤 Register users with a unique ID and name
* 🔍 Real-time face detection using Haar Cascade
* 🧠 Face recognition using LBPH
* ✅ Automatic attendance marking
* 🕒 Records attendance with timestamp
* 🚫 Prevents duplicate attendance entries
* 📊 Web-based attendance dashboard
* 🖥️ Simple and lightweight Python implementation

## 🛠️ Tech Stack

| Technology | Purpose                                          |
| ---------- | ------------------------------------------------ |
| Python     | Core programming language                        |
| OpenCV     | Face detection, image processing and recognition |
| LBPH       | Face recognition algorithm                       |
| NumPy      | Numerical and array operations                   |
| Flask      | Web dashboard backend                            |
| HTML       | Dashboard structure                              |
| Bootstrap  | Dashboard styling                                |
| CSV        | Attendance data storage                          |

## 📂 Project Structure

```text
face-recognition-attendance/
│
├── app.py              # Flask web dashboard
├── capture.py          # Captures face dataset
├── train.py            # Trains the LBPH recognition model
├── recognize.py        # Real-time recognition and attendance
├── index.html          # Attendance dashboard
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

> The `dataset/`, `trainer/`, and `attendance.csv` files are generated locally while using the application and are not included in the repository.

## ⚙️ How It Works

### 1. Capture Face Dataset

Run:

```bash
python capture.py
```

Enter the user's ID and name. The application accesses the webcam, detects the face using OpenCV's Haar Cascade classifier, and saves grayscale face images to the `dataset` folder.

The capture process collects up to 50 face images for each registered user.

### 2. Train the Recognition Model

After capturing the dataset, run:

```bash
python train.py
```

The training script reads the captured images, extracts the user IDs from their filenames, trains an **LBPH Face Recognizer**, and saves the trained model as:

```text
trainer/model.yml
```

### 3. Run Face Recognition

Start the recognition system:

```bash
python recognize.py
```

The application:

* Opens the webcam
* Detects faces
* Predicts the identity using the trained LBPH model
* Displays the recognized name
* Marks attendance for recognized users
* Stores the attendance time

### 4. View Attendance Dashboard

The project also contains a lightweight Flask dashboard.

Run:

```bash
python app.py
```

Then open:

```text
http://127.0.0.1:5000/
```

The dashboard displays attendance records from the generated `attendance.csv` file.

## 📋 Attendance Format

Attendance is stored in a CSV file with the following structure:

```text
Name,Time
Prathamesh,10:30:25
User2,10:35:12
```

The system checks existing records to help prevent duplicate attendance entries for the same person.

## 🚀 Installation

### Prerequisites

* Python 3.x
* Webcam
* Windows/Linux/macOS
* Git

### 1. Clone the repository

```bash
git clone https://github.com/Prathamesh3073/face-recognition-attendance.git
```

### 2. Navigate to the project

```bash
cd face-recognition-attendance
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Capture face data

```bash
python capture.py
```

### 5. Train the model

```bash
python train.py
```

### 6. Start recognition

```bash
python recognize.py
```

## ⚠️ Important Notes

* A working webcam is required.
* Face images should be captured in reasonable lighting conditions.
* The trained model is generated locally and is not included in the repository.
* The dataset is generated locally and should not be committed to GitHub.
* Recognition accuracy can vary depending on lighting, camera quality, face angle, and dataset quality.

## 🔒 Privacy

This project processes face images locally for educational and demonstration purposes.

If deploying the system for real-world use, appropriate consent, privacy protections, secure storage, and applicable data-protection requirements should be considered.

## 🔮 Future Improvements

Possible future enhancements include:

* 🔐 User authentication
* 🗄️ Database integration
* 📅 Date-wise attendance reports
* 📊 Attendance analytics
* 📥 Export attendance reports
* 👨‍💼 Admin dashboard
* 🌐 Improved responsive web interface
* 📱 Mobile-friendly dashboard
* 🎯 Improved recognition accuracy
* 🛡️ Liveness detection to reduce spoofing
* ☁️ Cloud deployment

## 👨‍💻 Author

**Prathamesh Kulkarni**

Computer Engineering | Python | Software Development | AI/ML

GitHub:
https://github.com/Prathamesh3073

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

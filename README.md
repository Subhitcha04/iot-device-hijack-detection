# IoT Anomaly Detection System

This repository contains a full-stack IoT anomaly detection system that simulates IoT traffic, preprocesses data, builds machine learning models for anomaly detection, and visualizes results using a React frontend. The backend uses Python for data processing, model building, and MQTT communication, while MongoDB stores the data.

## Table of Contents
- [Requirements](#requirements)
- [Project Setup](#project-setup)
  - [1. Preprocessing](#1-preprocessing)
  - [2. Model Building](#2-model-building)
  - [3. MQTT Communication](#3-mqtt-communication)
  - [4. Frontend](#4-frontend)
- [File Structure](#file-structure)

## Requirements

### 1. Frontend: React
To run the React frontend for data visualization:
- **Node.js**: `>= 18.0.0`
- **react**: `^18.2.0`
- **react-dom**: `^18.2.0`
- **react-scripts**: `^5.0.1`
- **axios**: `^1.5.0` (for making API requests)
- **recharts**: `^2.4.1` (for charts)

### 2. Backend: Python for Preprocessing, Model Building, and MQTT Communication
To run the backend for data preprocessing, model building, and MQTT-based IoT device simulation:
- **Python**: `>= 3.9`
- **Flask**: `^2.3.3`
- **flask-cors**: `^3.1.1`
- **numpy**: `^1.26.0`
- **pandas**: `^2.1.1`
- **scikit-learn**: `^1.3.1`
- **tensorflow**: `^2.15.0`
- **joblib**: `^1.4.0`
- **paho-mqtt**: `^1.6.1`
- **matplotlib**: `^3.7.3`
- **seaborn**: `^0.13.0`

### 3. Database: MongoDB
For storing the IoT data and anomaly detection results:
- **MongoDB**: `>= 5.0`
- **pymongo**: `^4.6.0`
- **flask-pymongo**: `^2.3.0`
- **dnspython**: `^2.4.2` (for MongoDB Atlas DNS connections)

### 4. IoT Device Simulation: Python
To simulate an IoT device sending MQTT data:
- **paho-mqtt**: `^1.6.1`

### 5. MQTT Broker
To set up an MQTT broker for communication between the IoT device and the backend:
- **Mosquitto**: `2.0.15`

---

## Project Setup

### 1. Preprocessing

First, preprocess the IoT traffic data to prepare it for model building. Run the `data_preprocessing.ipynb` notebook to clean and preprocess the data.

To run the notebook:
```bash
# From the backend directory
jupyter notebook data_preprocessing.ipynb
```

This will generate the preprocessed dataset required for training the models.

### 2. Model Building

After preprocessing the data, build four machine learning models for anomaly detection: Decision Tree, SVM, Naive Bayes, and CNN. Each model is built in its respective Jupyter notebook.

1. **Decision Tree Model:**
    - Run the notebook to train the Decision Tree model:
    ```bash
    jupyter notebook decision_tree_model.ipynb
    ```
    - The trained model will be saved as a `decision_tree_model.joblib` file for later use.

2. **SVM Model:**
    - Train the SVM model by running:
    ```bash
    jupyter notebook svm_model.ipynb
    ```

3. **Naive Bayes Model:**
    - Train the Naive Bayes model by running:
    ```bash
    jupyter notebook naive_bayes_model.ipynb
    ```

4. **CNN Model:**
    - Train the CNN model by running:
    ```bash
    jupyter notebook cnn_model.ipynb
    ```

### 3. MQTT Communication

To simulate IoT data transmission via MQTT and run the backend anomaly detection service:

1. **Run IoT Device Simulation:**
    - Navigate to the `iot_device` directory:
    ```bash
    cd iot_device
    ```
    - Run the MQTT publisher to simulate the IoT device sending data:
    ```bash
    python mqtt_publisher.py
    ```

2. **Start the Backend Server:**
    - Open a new terminal and navigate to the `backend` directory:
    ```bash
    cd backend
    ```
    - Run the Flask application:
    ```bash
    python app.py
    ```

3. **Start the SVM MQTT Subscriber:**
    - In the same terminal, run the SVM subscriber to classify incoming IoT data:
    ```bash
    python svm_mqtt_subscriber.py
    ```

### 4. Frontend

The React frontend provides an interface for users to visualize the IoT data and anomaly detection results.

To set up and run the frontend:

1. Navigate to the `frontend/iot-anomaly-detection` directory:
    ```bash
    cd frontend/iot-anomaly-detection
    ```

2. Install the required dependencies:
    ```bash
    npm install
    ```

3. Start the development server:
    ```bash
    npm start
    ```

The frontend will be available at `http://localhost:3000`, and it can display the real-time IoT data and anomaly detection results.

---

## File Structure

```bash
.
├── backend/
│   ├── app.py                     # Flask backend entry point
│   ├── data_preprocessing.ipynb    # Preprocessing notebook
│   ├── decision_tree_model.ipynb   # Decision Tree model training
│   ├── svm_model.ipynb             # SVM model training
│   ├── naive_bayes_model.ipynb     # Naive Bayes model training
│   ├── cnn_model.ipynb             # CNN model training
│   ├── svm_mqtt_subscriber.py      # SVM MQTT subscriber
│   └── decision_tree_model.joblib  # Trained Decision Tree model
├── frontend/
│   └── iot-anomaly-detection/
│       ├── src/
│       │   ├── components/
│       │   ├── App.js
│       │   └── api.js
│       └── public/
├── iot_device/
│   └── mqtt_publisher.py           # IoT device MQTT publisher script
└── README.md                       # This README file
```

---

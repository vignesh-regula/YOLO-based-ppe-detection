# YOLO-based PPE Detection System

## Overview
This project is a Personal Protective Equipment (PPE) detection system powered by YOLO (You Only Look Once) via the Ultralytics library. It features a React-based frontend for interacting with the system and a Flask-based backend server handling image and video processing using computer vision to enhance safety monitoring and compliance in industrial environments.

## Features
- **Image Processing**: Upload and process images to detect PPE compliance.
- **Video Processing**: Analyze video files or streams for continuous PPE detection.
- **RESTful API**: Flask backend providing endpoints for user authentication, image, and video analysis.
- **Modern UI**: Frontend built with React and React Router for a seamless user experience.

## Technology Stack

### Backend
- **Framework**: Flask, Flask-CORS
- **Computer Vision**: OpenCV (`opencv-python`)
- **Machine Learning**: Ultralytics YOLO
- **Other Utilities**: NumPy, Pillow

### Frontend
- **Framework**: React.js
- **Routing**: React Router DOM

## Project Structure
```text
/
├── backend-server/          # Flask backend application
│   ├── app/                 # Main application module
│   │   ├── routes/          # API endpoint handlers (auth, image, video)
│   │   ├── services/        # Core processing logic (yolo_service)
│   ├── requirements.txt     # Python dependencies
│   └── run.py               # Application entry point
│
└── frontend-react/          # React frontend application
    ├── src/                 # React source files
    ├── public/              # Public static assets
    └── package.json         # Node.js dependencies
```

## Getting Started

### Prerequisites
- Python 3.x
- Node.js & npm

### Running the Backend

1. Navigate to the backend directory:
   ```bash
   cd backend-server
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the Flask server:
   ```bash
   python run.py
   ```
   *The backend will typically start on `http://localhost:5000`.*

### Running the Frontend

1. Navigate to the frontend directory:
   ```bash
   cd frontend-react
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   *The frontend will run on `http://localhost:3000` and proxy API requests to the backend.*

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

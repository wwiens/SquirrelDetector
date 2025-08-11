# SquirrelDetector 🐿️

An end-to-end computer vision application for real-time squirrel detection using YOLO and edge computing on NVIDIA Jetson Nano.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![YOLO](https://img.shields.io/badge/YOLOv8-Ultralytics-red.svg)](https://github.com/ultralytics/ultralytics)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-orange.svg)](https://opencv.org/)

## 🎯 Project Overview

SquirrelDetector is a complete machine learning pipeline that demonstrates practical edge AI deployment for wildlife monitoring. This project showcases the entire ML workflow from data collection to production deployment, all accessible through an intuitive web interface - **no coding required for end users**.

Featured in: [Roboflow Blog - Squirrel Detection with Computer Vision](https://blog.roboflow.com/squirrel-detection-computer-vision/)

### Key Achievements
- **Full-Stack ML Pipeline**: Integrated data collection, annotation, training, and inference in a single application
- **Edge Deployment**: Optimized for real-time inference on resource-constrained devices (Jetson Nano)
- **Interactive Web Interface**: Built with Flask and Socket.IO for real-time updates during training and detection
- **Hardware Integration**: GPIO control for triggering physical responses (relay activation) upon detection

## 🚀 Features

### 1. **Data Collection Module**
- Web-based camera interface for capturing training images
- Automatic image preprocessing and standardization (640x360)
- UUID-based file naming for dataset management

### 2. **Annotation Tool**
- Browser-based bounding box annotation using Fabric.js
- COCO format data storage with automatic YOLO conversion
- Support for manual and automated annotation workflows

### 3. **Model Training**
- YOLOv8 integration with Ultralytics framework
- Configurable train/validation/test splits
- Real-time training progress updates via WebSocket
- Automatic model evaluation with confusion matrix generation

### 4. **Real-Time Detection**
- Live video stream processing with OpenCV
- Motion-triggered inference for computational efficiency
- Configurable confidence thresholds
- GPIO relay control for automated responses

## 🛠️ Technical Stack

- **Backend**: Python, Flask, Flask-SocketIO
- **ML Framework**: Ultralytics YOLOv8, OpenCV
- **Frontend**: HTML5, Bootstrap, Fabric.js, jQuery
- **Data Format**: COCO → YOLO conversion pipeline
- **Deployment**: NVIDIA Jetson Nano, Edge computing

## 📊 Architecture Highlights

```
User Interface (Web)
       ↓
Flask Application
       ↓
┌─────────────┬──────────────┬──────────────┬────────────┐
│   Collect   │   Annotate   │    Train     │   Detect   │
│  (OpenCV)   │  (Fabric.js) │ (YOLOv8)     │ (Inference)│
└─────────────┴──────────────┴──────────────┴────────────┘
       ↓              ↓              ↓              ↓
   Dataset      COCO JSON      Model Weights    GPIO/Relay
```

## 🚦 Getting Started

### Prerequisites
- Python 3.8+
- NVIDIA Jetson Nano (or compatible edge device)
- USB Camera

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/SquirrelDetector.git
cd SquirrelDetector

# Install dependencies
pip install -r requirements.txt

# Run the application
python serve.py
```

Access the application at `http://localhost:5000`

## 💡 Use Cases

- **Wildlife Monitoring**: Automated detection and tracking of backyard wildlife
- **Property Protection**: Smart deterrent system for gardens and bird feeders  
- **Research Applications**: Data collection for animal behavior studies
- **Educational Tool**: Demonstrating end-to-end ML pipeline development

## 🎓 Skills Demonstrated

- **Machine Learning**: Training and deploying YOLO object detection models
- **Full-Stack Development**: Flask backend with interactive web frontend
- **Edge Computing**: Optimizing ML models for resource-constrained devices
- **Hardware Integration**: GPIO programming for IoT applications
- **Data Engineering**: Building data pipelines with format conversion (COCO to YOLO)
- **Real-Time Systems**: WebSocket implementation for live updates

## 📈 Performance

- **Inference Speed**: ~15-20 FPS on Jetson Nano
- **Detection Accuracy**: Configurable confidence threshold (default: 0.5)
- **Training Time**: ~30 minutes for 100 epochs on small dataset

## 🔮 Future Enhancements

- [ ] Multi-class detection support
- [ ] Cloud training integration
- [ ] Mobile app companion
- [ ] Advanced analytics dashboard
- [ ] Docker containerization

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contact

Warren Wiens - [wwiens@gmail.com](mailto:wwiens@gmail.com)

Project Link: [https://github.com/yourusername/SquirrelDetector](https://github.com/wwiens/SquirrelDetector)

---

*Built with passion for combining AI with practical, real-world applications*

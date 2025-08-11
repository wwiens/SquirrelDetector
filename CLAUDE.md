# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

SquirrelDetector is a Flask-based web application for training and deploying YOLO object detection models targeting squirrels on Jetson Nano devices. It provides a complete ML pipeline through a web interface with four main components:

1. **Collect**: Capture images using webcam
2. **Annotate**: Draw bounding boxes in browser
3. **Train**: Train YOLO models with configurable epochs and data splits
4. **Detect**: Run real-time inference on camera feed with GPIO relay triggering

## Development Commands

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run the Application
```bash
python serve.py
```
The application will be available at http://localhost:5000

### Type Checking
The project uses Pyright for type checking. A pyrightconfig.json is configured to suppress missing import warnings.

## Architecture and Key Components

### Core Files
- **serve.py**: Main Flask application with REST endpoints and SocketIO for real-time communication
  - Handles video capture, model training callbacks, and inference
  - Missing import: `YOLO_Video` module referenced but not present in codebase (line 23)
  
- **yoloutils.py**: Utility functions for YOLO data preparation
  - Converts COCO format annotations to YOLO format
  - Creates train/valid/test directory structure
  - Handles coordinate transformations

### Data Flow
1. **Image Collection**: Webcam → OpenCV → static/dataset/
2. **Annotations**: Stored in coco.json (COCO format)
3. **Training**: COCO → YOLO format conversion → Ultralytics training
4. **Model Output**: best.pt (trained weights)

### Web Interface
- Templates in `/templates/`: index, collect, annotate, train, detect
- Static assets in `/static/`: Bootstrap CSS, Fabric.js for annotation UI
- Real-time updates via Flask-SocketIO

### Training Pipeline
- Uses Ultralytics YOLO with callbacks for progress tracking
- Dynamically creates YOLO directory structure (train/valid/test)
- Copies results (confusion matrix, results.png) to static/images/
- Updates best.pt with trained weights

### Key Technical Details
- Single class detection ("Guy" in data.yaml, but UI shows "Squirrel")
- Fixed image resize to 640x360 for consistency
- Windows-specific camera capture (cv2.CAP_DSHOW)
- Hardcoded Windows paths in data.yaml need updating for cross-platform use

## Known Issues
- Missing YOLO_Video module import in serve.py
- Platform-specific camera initialization (Windows only)
- Hardcoded paths in data.yaml (c:/projects/squirrelbuster/)
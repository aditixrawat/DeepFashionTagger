
# DeepFashionTagger  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey) ![TensorFlow](https://img.shields.io/badge/TensorFlow-Keras-orange) ![License](https://img.shields.io/badge/License-MIT-green)  

A web-based fashion attribute and category tagging tool that leverages deep learning to automatically classify and annotate attributes for fashion images. Built with **Python**, **TensorFlow/Keras**, and **Flask**, it features an easy-to-use web interface for uploading images and visualizing predictions.

---

## Features
- Automatic prediction of multiple fashion attributes and categories for uploaded images  
- Clean Flask web interface for easy image upload and result display  
- Uses a pre-trained custom model on the **Fashion Product Images** dataset  
- Modular codebase for backend, model management, and interface  

---

## Directory Structure
```

DEEPFASHIONTAGGER/
│
├── app/
│   ├── **init**.py         # App initialization and config
│   ├── predict.py          # Model inference script
│   ├── routes.py           # Flask route definitions
│   ├── templates/
│   │   └── index.html      # Main HTML interface
│   ├── static/             # Static files (CSS/JS)
│   └── **pycache**/        # Python cache files
│
├── model_data/
│   ├── deepfashion.keras   # Trained model weights
│   └── labels.txt          # Labels for prediction indices
│
├── static/uploads/         # Uploaded images storage
├── uploads/                # (if used) Alternative upload handling
├── utils/                  # Utility functions (if created)
├── venv/                   # Virtual environment
├── requirements.txt        # Python dependencies
├── README.md
└── run.py                  # App entry point

````

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/deepfashion-tagger.git
cd deepfashion-tagger
````

### 2. Setup Environment

Create and activate a Python virtual environment:

```bash
python -m venv venv
# For Unix/macOS
source venv/bin/activate
# For Windows
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Model & Labels

Ensure `deepfashion.keras` and `labels.txt` are inside the `model_data/` directory.
Update the path in `predict.py` if these files are moved.

### 4. Run the App

```bash
python run.py
```

Open your browser and go to:

```
http://localhost:5000
```

---

## Usage

1. Upload a fashion image through the web interface
2. The app will display predicted **category** and **attribute tags**

---


## Requirements

* Python 3.8+
* TensorFlow / Keras (see `requirements.txt`)
* Flask

---

## License

This project is licensed under the **MIT License**.



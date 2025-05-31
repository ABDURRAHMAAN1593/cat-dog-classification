# Cat-Dog Classification

## 🛠️ Getting Started

Follow these steps to get your development environment up and running:

- 📥 **Clone the repository:**
  ```bash
  git clone https://github.com/ABDURRAHMAAN1593/cat-dog-classification.git
  cd cat-dog-classification
  ```
- 🐍 **(Optional) Set up a virtual environment:**
  ```bash
  python -m venv venv
  # For Linux/Mac
  source venv/bin/activate
  # For Windows
  venv\Scripts\activate
  ```
- 📦 **Install dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- 🚀 **Run the Flask web app:**
  1. Navigate to the app directory:
     ```bash
     cd app
     ```
  2. Start the app:
     ```bash
     python app.py
     ```
- 📓 **(Optional) Run the training/testing notebooks:**
  1. Navigate to the notebooks directory:
     ```bash
     cd notebooks
     ```
  2. Open `.ipynb` files in Jupyter Notebook or VS Code.

A web-based application for classifying images as cats or dogs using deep learning. This project features a Flask web app that loads pre-trained Keras models for real-time image classification, and includes Jupyter notebooks for data preprocessing and model training. Designed for easy extension and reproducibility, this project demonstrates end-to-end workflow from data preparation to deployment.

## Tech Stack
- Python
- Flask
- Keras
- TensorFlow

## Directory Structure
```
cat-dog-classification/
├── app/                # Flask web app
│   ├── app.py          # Main Flask application
│   ├── static/         # Static files (CSS, JS, images)
│   ├── templates/      # HTML templates
│   ├── model.h5        # Pre-trained Keras model
│   └── model3.h5       # Additional pre-trained model
├── notebooks/          # Jupyter notebooks for training/evaluation
│   ├── Ai.ipynb        # Model training notebook
│   ├── Ai2.ipynb       # Additional experiments
│   └── model3.h5       # Extra pre-trained model
```

## Running the Flask App
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Run the app:**
   ```bash
   cd app
   python app.py
   ```
3. Open your browser and go to `http://127.0.0.1:5000/`.

## Running the Jupyter Notebooks
1. **Install dependencies (if not already done):**
   ```bash
   pip install -r requirements.txt
   ```
2. Launch Jupyter:
   ```bash
   jupyter notebook
   ```
3. Open and run the notebooks in the `notebooks/` directory for data preprocessing, training, or evaluation.

## Preparing a Custom Dataset
To train or evaluate with your own data, structure your dataset as follows:
```
train/
  cats/
    cat001.jpg
    ...
  dogs/
    dog001.jpg
    ...
test/
  test1.jpg
  test2.jpg
  ...
```
**Note:** The dataset used for this project is not included due to size and licensing restrictions.

## Project Notes
- This project was developed as a university group project.
- For questions or contributions, please open an issue or pull request. 
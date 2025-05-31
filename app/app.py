from flask import Flask, request, jsonify, render_template, send_from_directory
from keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
import numpy as np

# Load the Keras models
model1 = load_model('model.h5')
model2 = load_model('model3.h5')

# Create Flask app
app = Flask(__name__)

# Configure upload folder for images
app.config['UPLOAD_FOLDER'] = 'uploads'

# Add route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/')
def index():
    return render_template('index.html')

# Define endpoint for combined prediction
@app.route('/predict/combined', methods=['POST'])
def predict_combined():
    file = request.files['image']
    
    # Load image data from the FileStorage object using BytesIO
    img = image.load_img(BytesIO(file.read()), target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    
    # Make predictions using both models
    predictions_model1 = model1.predict(img_array)
    predictions_model2 = model2.predict(img_array)
    
    # Combine predictions
    combined_predictions = (predictions_model1 + predictions_model2) / 2  # Averaging
    
    # Thresholding: If average probability is greater than 0.5, predict class 1 (Dog), else predict class 0 (Cat)
    thresholded_predictions = (combined_predictions > 0.5).astype(int)
    
    # Convert prediction to class label
    prediction_label = 'Dog' if thresholded_predictions[0][0] == 1 else 'Cat'
    
    return jsonify({'prediction': prediction_label})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)

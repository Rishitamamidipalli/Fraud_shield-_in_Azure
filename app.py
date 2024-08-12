from flask import Flask, render_template, request
from keras.models import load_model
import numpy as np

app = Flask(__name__)

# Load the pre-saved model
model =load_model('half_model.keras')

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = ""
    if request.method == 'POST':
        # Retrieve input data from the form
        v1 = float(request.form.get('v1'))
        v2 = float(request.form.get('v2'))
        v3 = float(request.form.get('v3'))
        amount = float(request.form.get('amount'))
        
        
        # Prepare the input data as a NumPy array
        input_data = np.array([[v1, v2, v3, amount]])
        print(input_data)
        
        # Make a prediction
        prediction = model.predict(input_data)
        prediction = "Fraud" if prediction[0][0] > 0.5 else "Not Fraud"
        
    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)

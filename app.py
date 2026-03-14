from flask import Flask, render_template, request, jsonify
import pickle
import os
import sys

# Initialize Flask app
app = Flask(__name__)

# Load the trained pipeline
print("="*70)
print("SMS SPAM CLASSIFIER - FLASK APPLICATION")
print("="*70)

try:
    print("\nLoading trained model pipeline...")
    with open('spam_classifier_pipeline.pkl', 'rb') as f:
        pipeline = pickle.load(f)
    print("✓ Pipeline loaded successfully")
    
    # Load metadata if available
    if os.path.exists('model_metadata.pkl'):
        with open('model_metadata.pkl', 'rb') as f:
            metadata = pickle.load(f)
        print(f"✓ Model: {metadata['model_name']}")
        print(f"✓ Accuracy: {metadata['accuracy'] * 100:.2f}%")
        print(f"✓ Precision: {metadata['precision'] * 100:.2f}%")
        print(f"✓ Recall: {metadata['recall'] * 100:.2f}%")
    else:
        metadata = None
        print("⚠ Metadata file not found")
        
except FileNotFoundError:
    print("\n❌ ERROR: Model pipeline not found!")
    print("Please run 'python train_model.py' first to train and save the model.")
    print("="*70)
    sys.exit(1)

@app.route('/')
def home():
    """Render the home page"""
    return render_template('index.html', metadata=metadata)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict if a message is spam or not.
    Returns prediction with confidence percentage.
    """
    if request.method == 'POST':
        try:
            # Get message from form
            message = request.form.get('message', '').strip()
            
            # Validate input
            if not message:
                return render_template('index.html',
                                     error="Please enter a message",
                                     message=message,
                                     metadata=metadata)
            
            # Make prediction using the pipeline
            # The pipeline handles preprocessing and vectorization automatically
            prediction = pipeline.predict([message])[0]
            
            # Get prediction probability
            if hasattr(pipeline.named_steps['classifier'], 'predict_proba'):
                # For models that support predict_proba (Naive Bayes, Logistic Regression)
                proba = pipeline.predict_proba([message])[0]
                
                if prediction == 1:  # Spam
                    confidence = proba[1] * 100  # Probability of spam
                else:  # Ham
                    confidence = proba[0] * 100  # Probability of ham
            else:
                # For SVM, use decision function
                decision = pipeline.decision_function([message])[0]
                # Convert decision function to confidence-like score
                confidence = min(abs(decision) * 10, 99)
            
            # Convert prediction to readable result
            result = "Spam" if prediction == 1 else "Not Spam"
            
            # Format confidence
            confidence_str = f"{confidence:.1f}%"
            
            return render_template('index.html',
                                 prediction=result,
                                 confidence=confidence_str,
                                 message=message,
                                 metadata=metadata)
        
        except Exception as e:
            return render_template('index.html',
                                 error=f"An error occurred: {str(e)}",
                                 message=message,
                                 metadata=metadata)

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """
    API endpoint for predictions.
    Accepts JSON: {"message": "text"}
    Returns JSON: {"prediction": "Spam/Not Spam", "confidence": "95.5%"}
    """
    try:
        data = request.get_json()
        message = data.get('message', '').strip()
        
        if not message:
            return jsonify({'error': 'No message provided'}), 400
        
        # Make prediction
        prediction = pipeline.predict([message])[0]
        
        # Get confidence
        if hasattr(pipeline.named_steps['classifier'], 'predict_proba'):
            proba = pipeline.predict_proba([message])[0]
            confidence = (proba[1] if prediction == 1 else proba[0]) * 100
        else:
            decision = pipeline.decision_function([message])[0]
            confidence = min(abs(decision) * 10, 99)
        
        result = "Spam" if prediction == 1 else "Not Spam"
        
        return jsonify({
            'prediction': result,
            'confidence': f"{confidence:.1f}%",
            'message': message
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/test')
def test():
    """Test endpoint to verify model is working correctly"""
    test_cases = [
        ("Hi, are we meeting tomorrow?", "Not Spam"),
        ("Can you pick up milk?", "Not Spam"),
        ("Thanks for the birthday wishes!", "Not Spam"),
        ("WIN FREE PRIZE! Click now!", "Spam"),
        ("URGENT! Your account will be closed!", "Spam"),
        ("Congratulations! You won $1000!", "Spam"),
    ]
    
    results = []
    for msg, expected in test_cases:
        prediction = pipeline.predict([msg])[0]
        actual = "Spam" if prediction == 1 else "Not Spam"
        
        # Get confidence
        if hasattr(pipeline.named_steps['classifier'], 'predict_proba'):
            proba = pipeline.predict_proba([msg])[0]
            confidence = (proba[1] if prediction == 1 else proba[0]) * 100
        else:
            decision = pipeline.decision_function([msg])[0]
            confidence = min(abs(decision) * 10, 99)
        
        results.append({
            'message': msg,
            'expected': expected,
            'actual': actual,
            'confidence': f"{confidence:.1f}%",
            'correct': '✓' if expected == actual else '✗'
        })
    
    return jsonify({'test_results': results})

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': pipeline is not None,
        'model_name': metadata['model_name'] if metadata else 'Unknown'
    })

if __name__ == '__main__':
    print("\n" + "="*70)
    print("Server starting at http://127.0.0.1:5000/")
    print("Press CTRL+C to quit")
    print("="*70 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)

import pandas as pd
import numpy as np
import pickle
import string
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("SMS SPAM CLASSIFIER - TRAINING WITH REAL DATASET")
print("="*80)

# Step 1: Load the real SMS Spam Collection dataset
print("\n[1/7] Loading dataset from spam_dataset.csv...")
df = pd.read_csv("spam_dataset.csv")

print(f"[OK] Dataset loaded: {len(df)} messages")
print(f"  - Spam: {len(df[df['label']=='spam'])} ({len(df[df['label']=='spam'])/len(df)*100:.1f}%)")
print(f"  - Ham: {len(df[df['label']=='ham'])} ({len(df[df['label']=='ham'])/len(df)*100:.1f}%)")

# Step 2: Text preprocessing function
print("\n[2/7] Setting up text preprocessing...")

def preprocess_text(text):
    """
    Preprocess text with improved cleaning:
    - Convert to lowercase
    - Remove punctuation (but keep numbers for spam detection)
    - Remove extra spaces
    """
    # Convert to lowercase
    text = str(text).lower()
    
    # Remove punctuation (keep numbers as they're important for spam detection)
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text

# Apply preprocessing
df['processed_message'] = df['message'].apply(preprocess_text)

# Remove empty messages
df = df[df['processed_message'].str.strip() != ''].reset_index(drop=True)
print(f"[OK] Preprocessing complete: {len(df)} messages retained")

# Step 3: Encode labels
print("\n[3/7] Encoding labels...")
df['label_encoded'] = df['label'].map({'spam': 1, 'ham': 0})
print("[OK] Labels encoded (spam=1, ham=0)")

# Step 4: Split dataset (80/20)
print("\n[4/7] Splitting dataset into train/test (80/20)...")
X = df['processed_message']
y = df['label_encoded']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=42, stratify=y
)

print(f"[OK] Training set: {len(X_train)} messages (Spam: {sum(y_train)}, Ham: {len(y_train)-sum(y_train)})")
print(f"[OK] Test set: {len(X_test)} messages (Spam: {sum(y_test)}, Ham: {len(y_test)-sum(y_test)})")

# Step 5: Create ML Pipeline
print("\n[5/7] Creating ML Pipeline...")
print("  - TfidfVectorizer: max_features=6000, ngram_range=(1,2)")
print("  - LogisticRegression: max_iter=2000")

pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(
        max_features=6000,
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.9,
        sublinear_tf=True
    )),
    ('classifier', LogisticRegression(
        max_iter=2000,
        C=1.0,
        random_state=42,
        solver='lbfgs'
    ))
])

print("[OK] Pipeline created")

# Step 6: Train the model
print("\n[6/7] Training the model...")
pipeline.fit(X_train, y_train)
print("[OK] Model training complete")

# Step 7: Evaluate the model
print("\n[7/7] Evaluating model performance...")
print("-" * 80)

# Predictions
y_pred = pipeline.predict(X_test)

# Calculate metrics
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)

# Print evaluation metrics
print("\nEVALUATION METRICS:")
print("-" * 80)
print(f"Accuracy:  {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall:    {recall * 100:.2f}%")
print(f"F1-Score:  {f1 * 100:.2f}%")

print("\nCONFUSION MATRIX:")
print("-" * 80)
print(f"True Negatives (Ham as Ham):   {cm[0][0]}")
print(f"False Positives (Ham as Spam):  {cm[0][1]}")
print(f"False Negatives (Spam as Ham):  {cm[1][0]}")
print(f"True Positives (Spam as Spam):  {cm[1][1]}")

print("\nCLASSIFICATION REPORT:")
print("-" * 80)
print(classification_report(y_test, y_pred, target_names=['Ham', 'Spam']))

# Test with specific spam examples
print("\nTESTING WITH REAL-WORLD SPAM EXAMPLES:")
print("-" * 80)

test_messages = [
    "Airtel Warning: SPAM | Deposit now and win 1 cr",
    "Whatsapp +447310399942 to claim your prize",
    "Your account will be blocked! Verify at sbi-verify.com",
    "Bet on cricket and win 10 lakh! Register at bet365.in",
    "CONGRATULATIONS! You won 25 lakh in KBC lottery! Call now",
    "Personal loan approved! Get 5 lakh instantly at quickloan.in",
    "Work from home - earn 50000 monthly! WhatsApp +919876543210",
    "iPhone 14 Pro at 50% discount! Buy now at iphone-sale.in",
    "Hi, how are you doing today?",
    "Can we meet tomorrow at 5pm?",
    "Thanks for your help yesterday!",
    "I'll be late for the meeting, sorry",
]

for msg in test_messages:
    prediction = pipeline.predict([msg])[0]
    proba = pipeline.predict_proba([msg])[0]
    confidence = max(proba) * 100
    result = "SPAM" if prediction == 1 else "HAM"
    
    print(f"\nMessage: {msg[:60]}{'...' if len(msg) > 60 else ''}")
    print(f"Prediction: {result} ({confidence:.1f}% confidence)")

# Save the trained pipeline
print("\n" + "="*80)
print("SAVING MODEL")
print("="*80)

with open('spam_classifier_pipeline.pkl', 'wb') as f:
    pickle.dump(pipeline, f)

# Save metadata
metadata = {
    'model_name': 'Logistic Regression Pipeline',
    'accuracy': accuracy,
    'precision': precision,
    'recall': recall,
    'f1_score': f1,
    'training_samples': len(X_train),
    'test_samples': len(X_test),
    'confusion_matrix': cm.tolist(),
    'dataset_size': len(df),
    'spam_count': len(df[df['label']=='spam']),
    'ham_count': len(df[df['label']=='ham'])
}

with open('model_metadata.pkl', 'wb') as f:
    pickle.dump(metadata, f)

print(f"[OK] Pipeline saved: spam_classifier_pipeline.pkl")
print(f"[OK] Metadata saved: model_metadata.pkl")

print("\n" + "="*80)
print("TRAINING COMPLETE!")
print("="*80)
print(f"\n[OK] Model Accuracy: {accuracy * 100:.2f}%")
print(f"[OK] Dataset Size: {len(df)} messages")
print(f"[OK] Spam Detection: {recall * 100:.1f}% recall")
print(f"[OK] False Positive Rate: {cm[0][1]/(cm[0][0]+cm[0][1]) * 100:.1f}%")
print("\n[OK] You can now run the Flask app: python app.py")
print("="*80)

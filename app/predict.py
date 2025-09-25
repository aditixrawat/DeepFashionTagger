# app/predict.py
import os
import numpy as np
import keras

MODEL_PATH = "model_data/deepfashion.keras"
LABELS_PATH = "model_data/labels.txt"

def _load_labels():
    if os.path.exists(LABELS_PATH):
        with open(LABELS_PATH, "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    # fallback if no file present
    return ["T-Shirt", "Jeans", "Dress", "Sneakers", "Jacket"]

CLASS_LABELS = _load_labels()

model = keras.models.load_model(MODEL_PATH, compile=False, safe_mode=False)

def _prepare_image(img_path: str):
    img = keras.utils.load_img(img_path, target_size=(224, 224))
    x = keras.utils.img_to_array(img)
    x = np.expand_dims(x, axis=0) / 255.0
    return x

# --- Step 5: Predict Function ---

def predict_image(file_path: str):
    x = _prepare_image(file_path)
    probs = model.predict(x)[0]  # shape: (num_classes,)
    topk = min(5, probs.shape[0])
    top_idx = np.argsort(probs)[-topk:][::-1].tolist()

    def name(i):
        return CLASS_LABELS[i] if i < len(CLASS_LABELS) else str(i)

    tags = [{"name": name(i), "prob": float(probs[i])} for i in top_idx]
    return {
        "label": tags[0]["name"],
        "tags": [t["name"] for t in tags],
        "top": tags,  # optional: names + probs for display, can remove if unwanted
    }
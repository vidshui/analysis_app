from PIL import Image
import cv2
import numpy as np

def analyze_skin_tone(image_path):
    image = Image.open(image_path)
    
    pixels = list(image.getdata())
    r, g, b = zip(*pixels)
    
    avg_r = sum(r) / len(r)
    avg_g = sum(g) / len(g)
    avg_b = sum(b) / len(b)
    
    avg_hex = '#%02x%02x%02x' % (int(avg_r), int(avg_g), int(avg_b))

    if avg_hex < '#6b4f2d':
        return 'Dark'
    elif avg_hex < '#b8956d':
        return 'Medium'
    elif avg_hex < '#dfb385':
        return 'Light'
    
    



def analyze_body_type(image_path):
    
    image = cv2.imread(image_path)
    resized_image = cv2.resize(image, (256, 256))
    gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    
    # Example machine learning model inference (replace with your actual model)
    # This is just a placeholder; replace with your actual model inference code
    # Assuming you have a model.predict function to predict body type
    predicted_body_type = model.predict(gray_image)  # Replace with your actual model prediction logic
    
    return predicted_body_type

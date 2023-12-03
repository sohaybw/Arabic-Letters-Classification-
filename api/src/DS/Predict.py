
import torch
from .Preprocess_img import preprocess_image
from .model import MyModel
import os

# Get the current directory of the script
current_directory = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the model file relative to the script's location
file_path = os.path.join(current_directory, '..', 'static', 'final_model.pth')




def load_model () :
        # Load the model and class encodings
    checkpoint = torch.load(file_path, map_location=torch.device('cpu'))

    loaded_model = MyModel()  # Instantiate your model
    loaded_model.load_state_dict(checkpoint['model_state_dict'])

    loaded_class_names = checkpoint['class_name_mapping']

    return loaded_model , loaded_class_names

   

def make_prediction(base64_image_string):
    try:
        # Preprocess the image using the preprocess_image function
        img_tensor = preprocess_image(base64_image_string)
        loaded_model , class_name_mapping = load_model ()

        if img_tensor is not None:
            # Make prediction using the preprocessed image tensor
            with torch.no_grad():
                loaded_model.eval()  # Set model to evaluation mode
                outputs = loaded_model(img_tensor)
                probabilities = torch.softmax(outputs, dim=1)
                _, predicted = torch.max(outputs, 1)
                predicted_class = predicted.item()
                probability = probabilities[0, predicted_class].item()
                
                # Retrieve class name based on predicted class index
                predicted_class_name = class_name_mapping.get(predicted_class, "Unknown")
                
                return {
                    'predicted_class': predicted_class_name,
                    'probability': probability
                }

    except Exception as e:
        print(f"Error during prediction: {e}")
        return {'error': str(e)}
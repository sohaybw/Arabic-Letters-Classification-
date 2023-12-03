import base64
import  io
from PIL import Image
from torchvision import transforms

def preprocess_image(base64_string):
    try:
        if ',' in base64_string:
            base64_string = base64_string.split(',')[1]  # Remove header if present

        # Decode base64 string to bytes
        img_data = base64.b64decode(base64_string)
        
        # Convert bytes to PIL Image
        img = Image.open(io.BytesIO(img_data)).convert('RGB')

        # Define image transformations
        preprocess = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ])

        # Apply transformations to the image
        img = preprocess(img)
        img = img.unsqueeze(0)  # Add batch dimension
        return img

    except Exception as e:
        print(f"Error during image preprocessing: {e}")
        return None  # Return None or handle the error accordingly

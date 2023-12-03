import base64
# os.chdir(r"C:\Users\Sohayb\Desktop\valify task\project\client")

# image_path ="1011.png"

def load_img(image_path) :

    with open(image_path, 'rb') as img_file:
        base64_image = base64.b64encode(img_file.read()).decode('utf-8')

    return base64_image
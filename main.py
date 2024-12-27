from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
   
   
    if not isinstance(key, int) or key < 0 or key > 255:
        raise ValueError("Key must be a number between 0-255")
        
  
    img = Image.open(input_path)
    img_array = np.array(img)
    

    processed = img_array ^ key
    
    # Save result
    result = Image.fromarray(processed.astype('uint8'))
    result.save(output_path)


if __name__ == "__main__":
    try:
        # Encrypt
        encrypt_image('input.png', 'encrypted.png', key=223)
        print("Image encrypted!")
        
        # Decrypt (using same key)
        encrypt_image('encrypted.png', 'decrypted.png', key=23)
        print("Image decrypted!")
        
    except Exception as e:
        print(f"Error: {e}")

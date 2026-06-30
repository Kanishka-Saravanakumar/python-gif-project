import imageio.v3 as iio
from PIL import Image
import numpy as np

filenames = ['drake-img1.png', 'drake-img2.png']
images = []

for filename in filenames:
    # 1. Open the image
    img = Image.open(filename)
    
    # 2. Force it to standard RGB color mode (removes any alpha transparency differences)
    img_rgb = img.convert('RGB')
    
    # 3. Resize to a matching 500x500 pixels square
    img_resized = img_rgb.resize((500, 500))
    
    # 4. Convert it to a clean NumPy array so imageio receives pure data
    images.append(np.array(img_resized))

# 5. Save the final GIF outside the loop 
iio.imwrite('drake.gif', images, duration=500, loop=0)

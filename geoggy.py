from PIL import Image
import numpy as np
import os 


geoggy = "/Users/ryanc/downloads/geoggy/geoggy/converted"

files = os.listdir(geoggy) 
sorted_files = sorted(files)

for file in sorted_files:
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"): 
        try:
            filepath = os.path.join(geoggy, filename)
            print(filepath)
            image = Image.open(filepath)
            gray = image.convert("L")
            gray_array = np.array(gray) / 255.0
            albedo = np.mean(gray_array)
            print(round(albedo, 3))
        except Exception as e:
            print (e)

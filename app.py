from PIL import Image
import sys

# Quality, the lower the quality the more pixelated and the smaller the size
quality = 95

if len(sys.argv) != 2:
    print("Use: python3 app.py <path/to/image.jpg>")

else:
    directory = sys.argv[1]
    ext = directory.split(".")[-1]
    possibles_extensions = ["jpg", "jpeg", "png", "gif", "tiff"]
    if ext.lower() in possibles_extensions:

        foo = Image.open(directory)
        print("Size:", foo.size)

        
        
        foo.save("otimize."+ext,optimize=True,quality=quality)
    else:
        print("This file isn't an image.")
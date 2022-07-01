from PIL import Image
import os

folder = "" # /Users/geovanny/Downloads
destinationFolder = "" # /Users/geovanny/Pictures

if __name__ == "__main__":
  for filename in os.listdir(folder):
    name, extension = os.path.splitext(folder + filename)

    if extension in [".jpg", ".jpeg", ".png", ".gif"]:
      picture = Image.open(folder + filename)
      picture.save(destinationFolder + "compressed_" + filename, optimize=True, quality=80)
      os.remove(folder + filename)
      print(name + ": " + filename)
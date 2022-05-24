
import sys
import random

if __name__ == "__main__":
    file_path = "./all/boxes.txt"
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    try:
        file = open(file_path, "r")
        boxes = file.read().splitlines()
        file.close()
        random_number = random.randrange(len(boxes))
        print(f"Box: {boxes[random_number]}")
    except:
        print(f"Usage: {sys.argv[0]} <box_file>")
        print(f"Default file is ./all/boxes.txt")
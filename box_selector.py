import argparse
import random

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Select randomly from a list of HTB Boxes.')
    parser.add_argument('-f', type=str, default='./all/boxes.txt', help='Path of boxes list file.')
    parser.add_argument('--ignore-solved', action='store_true', help='Ignore solved.txt list to choose a random box.')
    args = parser.parse_args()
    try:
        boxes_file = open(args.f, 'r')
        boxes = boxes_file.read().splitlines()
        boxes_file.close()
        selected_box = ''
        if args.ignore_solved:
            random_number = random.randrange(len(boxes))
            selected_box = boxes[random_number]
        else:
            solved_boxes_file = open('./solved.txt', 'r')
            solved_boxes = solved_boxes_file.read().splitlines()
            solved_boxes_file.close()
            solved = True
            while(solved and len(boxes) != 0):
                random_number = random.randrange(len(boxes))
                random_box = boxes[random_number]
                if random_box not in solved_boxes:
                    solved = False
                    selected_box = random_box
                boxes.pop(random_number)
        if selected_box == '':
            print(f'All boxes were solved!')    
        else:
            print(f'Box: {selected_box}')
    except:
        parser.print_help()
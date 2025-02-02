import os
import shutil
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Recursively copy and sort files by extension.')
    parser.add_argument('source', help='Path to the source directory')
    parser.add_argument('destination', nargs='?', default='dist', help='Path to the destination directory')
    return parser.parse_args()

def copy_and_sort_files(source, destination):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        for root, dirs, files in os.walk(source):
            for file in files:
                file_path = os.path.join(root, file)
                ext = file.split('.')[-1] if '.' in file else 'no_extension'
                dest_dir = os.path.join(destination, ext)
                if not os.path.exists(dest_dir):
                    os.makedirs(dest_dir)
                shutil.copy2(file_path, dest_dir)
    except Exception as e:
        print(f'Error: {e}')

def main():
    args = parse_arguments()
    copy_and_sort_files(args.source, args.destination)

if __name__ == '__main__':
    main()

# To test the script, run it with the following command: python3 hw_2/task_1.py hw_1
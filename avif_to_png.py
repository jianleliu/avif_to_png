from os import listdir, mkdir, path
from PIL import Image, UnidentifiedImageError  # Import UnidentifiedImageError
import pillow_avif
from config import dir_, folder, new_dir

def convert(old_path, new_path, lis: list):
    try:
        count = 1
        for pic in lis:
            if pic.split('.')[-1] == 'avif':
                try:
                    img = Image.open(f"{old_path}/{pic}")
                    img.save(f"{new_path}/{count}.png", "png")
                    count += 1
                except UnidentifiedImageError:
                    print(f"Skipping invalid image: {pic}")
    except Exception as e:
        print(f"An error occurred while converting images: {str(e)}")

if __name__ == '__main__':
    try:
        old_path = path.join(dir_, folder)
        lis = listdir(old_path)
        print(lis)

        new_path = path.join(dir_, new_dir)
        if not path.exists(new_path):
            mkdir(new_path)

        count = 1
        for item in lis:
            if path.isdir(f'{old_path}/{item}'):
                sub_old_path = path.join(old_path, item)
                sub_new_path = path.join(new_path, str(count))
                if not path.exists(sub_new_path):
                    mkdir(sub_new_path)
                convert(sub_old_path, sub_new_path, listdir(f'{sub_old_path}/{item}'))
                count += 1
            else:
                convert(old_path, new_path, lis)
                break
    except Exception as e:
        print(f"An error occurred: {str(e)}")

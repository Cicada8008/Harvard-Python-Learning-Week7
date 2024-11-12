from sys import exit, argv
from PIL import Image, ImageOps


def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    elif len(argv) > 3:
        exit("Too many arguments")
    else:
        if file_extension_check(1) != file_extension_check(2):
            exit("different extensions")

    try:
        shirt = Image.open("shirt.png")
        before = Image.open(argv[1])
    except FileNotFoundError:
        exit("Could not find the image file")
    else:
        size = shirt.size # it is a tuple (600, 600)
        before = ImageOps.fit(before, size) # resize and crop the input
        before.paste(shirt, box = (0, 0), mask = shirt)
        before.save(argv[2], format=None) # saving the image


def file_extension_check(i):
    match endpart := argv[i][(argv[i].index('.')):].lower():
        case ".png" | ".jpg" | ".jpeg":
            return endpart
        case _:
            exit("Invalid output")


if __name__ == "__main__":
    main()

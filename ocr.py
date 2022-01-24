import pytesseract as ocr
import sys, os
from pdf2image import convert_from_path
from PIL import Image

def main():

    # Check argv
    if len(sys.argv) != 2 and len(sys.argv) != 3:
       sys.exit("Usage: filename [language].")

    # Tesseract config parameters
    if len(sys.argv) == 3:
        if sys.argv[2] in ocr.get_languages():
            custom_config = f"-l {sys.argv[2]} --oem 3 --psm 4"
        else:
            sys.exit("Unavailable language.")
    else:
        custom_config = r"-l por --oem 3 --psm 4"

    # Convert PDF file to image if necessary and recognize characters
    if ".pdf" in sys.argv[1].split("/")[-1]:

        try:
            pages = convert_from_path(sys.argv[1], 500, poppler_path=r"poppler-0.68.0\bin")
        except:
            sys.exit("Unable to locate file.")

        if len(pages) > 10:
            sys.exit("Page limit exceeded.")

        count = 1
        text = ""
        for page in pages:
            temp_file ="temp_ocr_page_" + str(count) + ".jpg"
            page.save(temp_file, "jpeg")
            text += ocr.image_to_string(Image.open(temp_file), config=custom_config)
            os.remove(temp_file)
            count += 1

    # Recognize characters from images
    else:
        img = sys.argv[1]
        try:
            text = ocr.image_to_string(img, config=custom_config)
        except:
            sys.exit("Unable to locate file.")

    # Write found characters in output file
    with open("out.txt", "w", encoding="utf-8") as f:
        f.write(text)
    return

if __name__ == "__main__":
    main()

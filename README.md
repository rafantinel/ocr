# OCR - Command Line

## Description

Optical character recognition from image files.

Technologies used:

- Poppler
- pytesseract
- PIL
- pdf2image

## How the program works?

By providing the filename and, optionally, a language as command line arguments, the program can recognize characters in images or PDF files.

## Implementation Details

- pip install pytesseract
- pip install PIL
- pip install pdf2image
- sudo apt-get install tesseract-ocr (Linux)
- download Tesseract in (Windows): https://github.com/UB-Mannheim/tesseract/wiki
- install and add Tesseract to PATH (Windows)
- run tesseract --list-langs to check available languages
- install a language if needed by downloading a ".traineddata" file and placing it inside the "Tesseract-OCR/tessdata" folder (Windows): https://github.com/tesseract-ocr/tessdata
- make shure poppler is in the program's main folder

## Github Repository

https://github.com/rafantinel/OCR-Command-Line

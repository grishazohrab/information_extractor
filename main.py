from pix2struct import extract_information


if __name__ == '__main__':
    pdf_path = "docs/1.pdf"
    print(extract_information(pdf_path))
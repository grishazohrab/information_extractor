from transformers import Pix2StructForConditionalGeneration as psg
from transformers import Pix2StructProcessor as psp

from pdf2image import convert_from_path

from config import DEVICE, MODEL_NAME, QUESTIONS

model = psg.from_pretrained(MODEL_NAME).to(DEVICE)
processor = psp.from_pretrained(MODEL_NAME)


def generate(img, questions):
    inputs = processor(images=[img for _ in range(len(questions))],
                       text=questions, return_tensors="pt").to(DEVICE)
    predictions = model.generate(**inputs, max_new_tokens=256)
    return zip(questions, processor.batch_decode(predictions, skip_special_tokens=True))


def convert_pdf_to_image(filename):
    return convert_from_path(filename)


def extract_information(file_name: str):
    image = convert_pdf_to_image(file_name)[0]
    print("pdf to image conversion complete.")
    questions = [item[1] for item in QUESTIONS]
    completions = generate(image, questions)
    result = {}
    for ii, completion in enumerate(completions):
        result[QUESTIONS[ii][0]] = completion

    return result


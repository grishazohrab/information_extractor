import torch


MODEL_NAME = "google/pix2struct-docvqa-large"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"


QUESTIONS = [("sender", "who is the sender?"),
             ("receiver", "who is the receiver?"),
             ("product code", "What is the product code?"),
             ("item name", "What is the item name?"),
             ("quantity", "what is the quantity?"),
             ("unit price", "what is the unit price?"),
             ("hs code", "what is the harmonized system code?"),
             ("total price", "what is the total price?")]

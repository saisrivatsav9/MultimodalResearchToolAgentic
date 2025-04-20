from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import torch

class VisionLanguageAgent:
    def __init__(self):
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
        self.model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")

    def answer_question(self, image_path, question):
        image = Image.open(image_path).convert('RGB')
        inputs = self.processor(image, question, return_tensors="pt")
        outputs = self.model(**inputs)
        answer = self.processor.tokenizer.decode(outputs.logits.argmax(-1))
        return answer
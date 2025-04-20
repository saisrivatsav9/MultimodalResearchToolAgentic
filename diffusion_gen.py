from diffusers import StableDiffusionPipeline
import torch

class DiffusionGenerator:
    def __init__(self):
        self.pipe = StableDiffusionPipeline.from_pretrained(
            "runwayml/stable-diffusion-v1-5",
            torch_dtype=torch.float16
        ).to("cpu")

    def generate_image(self, prompt, output_path="generated.png"):
        image = self.pipe(prompt).images[0]
        image.save(output_path)
        return output_path
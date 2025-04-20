from core.controller import Controller
import os
from dotenv import load_dotenv
load_dotenv()

# Load from .env or input manually
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def run():
    controller = Controller(api_key=OPENAI_API_KEY)

    while True:
        mode = input("\n[Mode: text / image / generate / exit]: ").strip()
        if mode == "exit":
            break
        elif mode == "text":
            q = input("Question: ")
            url = input("Optional URL: ").strip()
            url = url if url else None
            print("Answer:", controller.process_text_query(q, url))
        elif mode == "image":
            path = input("Image path: ")
            q = input("Question about image: ")
            print("Answer:", controller.process_image_query(path, q))
        elif mode == "generate":
            prompt = input("Describe image to generate: ")
            output_path = controller.generate_image(prompt)
            print(f"Image generated at {output_path}")

if __name__ == "__main__":
    run()
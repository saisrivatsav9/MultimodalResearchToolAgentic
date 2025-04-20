from models.llm_rag import LLMWithRAG
from models.vlm_blip import VisionLanguageAgent
from models.diffusion_gen import DiffusionGenerator
from core.memory import MemoryStore

class Controller:
    def __init__(self, api_key):
        self.memory = MemoryStore()
        self.llm = LLMWithRAG(api_key)
        self.vision_agent = VisionLanguageAgent()
        self.diffuser = DiffusionGenerator()

    def process_text_query(self, query, url=None):
        if url:
            vectorstore = self.llm.build_vectorstore_from_url(url)
            response = self.llm.query(query, vectorstore)
        else:
            response = self.llm.llm.predict(query)
        self.memory.add(query, response)
        return response

    def process_image_query(self, image_path, question):
        response = self.vision_agent.answer_question(image_path, question)
        self.memory.add(question, response)
        return response

    def generate_image(self, prompt):
        path = self.diffuser.generate_image(prompt)
        self.memory.add(f"ImageGen: {prompt}", path)
        return path
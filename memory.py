class MemoryStore:
    def __init__(self):
        self.past_interactions = []

    def add(self, user_input, system_response):
        self.past_interactions.append({"input": user_input, "response": system_response})

    def get_context(self):
        return "\n".join([f"User: {i['input']}\nAssistant: {i['response']}" for i in self.past_interactions])
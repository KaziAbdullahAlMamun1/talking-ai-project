from ollama import Client

class Ai(Client):
    
    def __init__(self,model="mistral"):
        super().__init__()
        self.model= model
        self.prompt=""
        self.response=""
    def feedback(self,prompt):
        self.response = self.generate(model=self.model,prompt=prompt)
        return self.response["response"]


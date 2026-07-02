from backend.llm import LLMClient

print("Secure-RAG Backend Initialized")

llm = LLMClient()

print(llm.generate("Hello"))
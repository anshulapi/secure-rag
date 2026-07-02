from backend.context_builder import build_context
from backend.prompts import SYSTEM_PROMPT


class RAGEngine:

    def __init__(self, retriever, llm):

        self.retriever = retriever
        self.llm = llm

    def answer(self, question):

        chunks = self.retriever.retrieve(
            question
        )

        context = build_context(chunks)

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=question
        )

        return self.llm.generate(prompt)
def build_context(chunks):

    context = ""

    for i, chunk in enumerate(chunks, start=1):

        context += f"\nDocument {i}:\n"

        context += chunk

        context += "\n"

    return context
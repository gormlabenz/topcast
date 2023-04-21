from fastapi.testclient import TestClient

from server import app

def test_generate_podcast_text():
    client = TestClient(app)
    response = client.post("/generate_podcast/", json={"tts_provider":"gcp",
        "text": """
LangChain is a software development framework designed to simplify the creation of applications using large language models (LLMs) such as from OpenAI, Anthropic, or Hugging Face. The framework offers a suite of tools, components, and interfaces to manage interactions with language models, chain together multiple components, and integrate resources such as APIs, databases, and a wide variety of document types. LangChain provides components for use cases such as virtual assistants, question answering about collections of documents, chatbots, querying tabular data, using APIs, and document extraction and summarization.[1]"""})
    
    print(response.json())

if __name__ == "__main__":
  test_generate_podcast_text()

from fastapi.testclient import TestClient

from server import app

def test_wikipedia():
    client = TestClient(app)
    response = client.post("/wikipedia/", json={
      "term": "Dachshund",
      })
    
    print(response.json())

if __name__ == "__main__":
  test_wikipedia()

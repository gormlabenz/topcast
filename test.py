from server import app
from fastapi.testclient import TestClient


def test_generate_podcast_text():
    client = TestClient(app)
    response = client.post("/generate_podcast/", json={"text": """
Gorm is the reported son of semi-legendary Danish king Harthacnut. Chronicler Adam of Bremen says that Harthacnut came from Northmannia to Denmark and seized power in the early 10th century.[6] He deposed the young king Sigtrygg Gnupasson, reigning over Western Denmark.[3] When Harthacnut died, Gorm ascended the throne.

Heimskringla reports Gorm taking at least part of the kingdom by force from Gnupa, and Adam himself suggests that the kingdom had been divided prior to Gorm's time. Gorm is first mentioned as the host of Archbishop Unni of Hamburg and Bremen in 936.[6] According to the Jelling Stones, Gorm's son, Harald Bluetooth, "won all of Denmark", so it is speculated that Gorm only ruled Jutland from his seat in Jelling.[6]"""})
    
    print(response.json())

if __name__ == "__main__":
  test_generate_podcast_text()

from server import app
from fastapi.testclient import TestClient



def test_generate_podcast_text():
    client = TestClient(app)
    response = client.post("/generate_podcast/", json={"text": """The Achaemenid royal inscriptions are the surviving inscriptions in cuneiform script from the Achaemenid Empire, dating from the 6th to 4th century BCE (reigns of Cyrus II to Artaxerxes III). These inscriptions are primary sources for the history of the empire, along with archaeological evidence and the administrative archives of Persepolis. However, scholars are reliant on Greek sources (such as Herodotus) to reconstruct much of Achaemenid history.[1]

The Achaemenid royal inscriptions differ from earlier Assyrian and Babylonian inscriptions in their multilingualism, rhetorical style and their structure.[2] The inscriptions are mostly trilingual – in Old Persian, Elamite and Babylonian, which use two separate scripts (Babylonian and Elamite use variants of the same cuneiform). When they appear together, the privileged position is usually occupied by the Old Persian inscription: at the top when arranged vertically, and in the middle when arranged horizontally.[2]

The initial decipherment of cuneiform was based on the Achaemenid royal inscriptions from Persepolis, later supplemented with the Behistun Inscription. Scholars deciphered the Old Persian cuneiform script first, followed by the Babylonian and Elamite language versions using the trilingual inscriptions.[3]"""})
    
    print(response.json())

if __name__ == "__main__":
  test_generate_podcast_text()

import sys
sys.path.append(r"C:\Users\sadhanas\OneDrive - Synopsys, Inc\Documents\Project\sample")

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_all():
    response = client.get("/book/")
    assert response.status_code == 200
    
def test_create_book():
    response = client.post("/book/add", 
                           json = {
                                    "id": "20000",
                                    "Title": "string",
                                    "Authors": "string",
                                    "Description": "string",
                                    "Category": "string",
                                    "Publisher": "string",
                                    "Price": 0,
                                    "Publish_Month": "string",
                                    "Publish_Date": 0
                                    })
    assert response.status_code == 200
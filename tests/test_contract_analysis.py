import unittest
from fastapi.testclient import TestClient
from app.api import app

class TestContractAnalysis(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_contract_audit(self):
        req = {
            "contract_title": "Enterprise Cloud Agreement",
            "contract_text": "Vendor agrees to indemnify and hold harmless the customer from all liability."
        }
        res = self.client.post("/analyze-contract", json=req)
        self.assertEqual(res.status_code, 200)
        data = res.json()
        self.assertIn("DISCLAIMER", data["disclaimer"])
        self.assertGreater(len(data["key_clauses"]), 0)

if __name__ == "__main__":
    unittest.main()

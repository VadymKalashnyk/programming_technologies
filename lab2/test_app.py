import unittest
import json
import xmlrunner
from app import app, cinema

class TestCinemaAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        cinema.sessions.clear()
        cinema._next_id = 1
        self.session_id = cinema.add_session("Interstellar", "21:00", 20, 200.0)

    # Позитивний тест: перевірка створення сеансу через POST HTTP
    def test_create_session_api_success(self):
        payload = {"movie": "Matrix", "time": "19:00", "total_seats": 30, "price": 120.0}
        response = self.app.post('/sessions', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn("session_id", response.get_json())

    # Позитивний тест: бронювання квитків через API
    def test_book_tickets_api_success(self):
        payload = {"count": 2}
        response = self.app.post(f'/sessions/{self.session_id}/book', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["total_price"], 400.0)

    # Негативний тест: спроба бронювання більшої кількості квитків, ніж є (код 400)
    def test_book_tickets_api_overbooking(self):
        payload = {"count": 100}
        response = self.app.post(f'/sessions/{self.session_id}/book', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertIn("error", response.get_json())

    # Негативний тест: запит неіснуючого сеансу (код 404)
    def test_get_nonexistent_session_api(self):
        response = self.app.get('/sessions/999')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    # Збереження результатів у папку test-reports
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
#gfgf
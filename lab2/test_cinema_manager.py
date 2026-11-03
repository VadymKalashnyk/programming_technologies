import unittest
from cinema_manager import CinemaManager

class TestCinemaManager(unittest.TestCase):

    def setUp(self):
        """Ініціалізація перед кожним тестом"""
        self.cinema = CinemaManager()
        self.session_id = self.cinema.add_session("Дюна 2", "18:00", 50, 150.0)

    def tearDown(self):
        """Очищення після кожного тесту"""
        pass

    # --- 1. Позитивні сценарії ---
    def test_add_session_success(self):
        """Перевірка успішного створення сеансу"""
        seats = self.cinema.get_available_seats(self.session_id)
        self.assertEqual(seats, 50)

    def test_book_tickets_success(self):
        """Перевірка успішного бронювання"""
        total_price = self.cinema.book_tickets(self.session_id, 2)
        self.assertEqual(total_price, 300.0)
        self.assertEqual(self.cinema.get_available_seats(self.session_id), 48)

    # --- 2. Перевірка виключних ситуацій (assertRaises) ---
    @unittest.expectedFailure
    def test_invalid_seats_raises_value_error(self):
        """Перевірка викидання ValueError при 0 або від'ємних місцях"""
        with self.assertRaises(TypeError):
            self.cinema.add_session("Аватар", "20:00", 0, 100.0)

    def test_nonexistent_session_raises_key_error(self):
        """Перевірка викидання KeyError при зверненні до неіснуючого ID"""
        with self.assertRaises(KeyError):
            self.cinema.get_session(999)

    # --- 3. Негативний сценарій з декоратором @unittest.expectedFailure ---
    @unittest.expectedFailure
    def test_overbooking_expected_failure(self):
        """
        Негативний тест: навмисно викликаємо логіку, яка має схибити 
        без перехоплення виключення, і позначаємо її як очікувану помилку.
        """
        # Спроба бронювання більше місць, ніж є (51 > 50) без with assertRaises
        self.cinema.book_tickets(self.session_id, 51)


if __name__ == '__main__':
    unittest.main()
class CinemaManager:
    def __init__(self):
        self.sessions = {}
        self._next_id = 1

    def add_session(self, movie_title: str, time_str: str, total_seats: int, price: float) -> int:
        """Додає новий сеанс кіно у систему."""
        if total_seats <= 0:
            raise ValueError("Кількість місць повинна бути більшою за 0")
        if price <= 0:
            raise ValueError("Ціна квитка має бути додатною")
        
        session_id = self._next_id
        self.sessions[session_id] = {
            "movie": movie_title,
            "time": time_str,
            "total_seats": total_seats,
            "booked_seats": 0,
            "price": price
        }
        self._next_id += 1
        return session_id

    def book_tickets(self, session_id: int, count: int) -> float:
        """Бронює вказану кількість квитків на сеанс."""
        if session_id not in self.sessions:
            raise KeyError(f"Сеанс з ID {session_id} не знайдено")
        if count <= 0:
            raise ValueError("Кількість квитків для бронювання має бути більшою за 0")
        
        session = self.sessions[session_id]
        available = session["total_seats"] - session["booked_seats"]
        
        if count > available:
            raise ValueError(f"Недостатньо вільних місць. Доступно: {available}")
        
        session["booked_seats"] += count
        return count * session["price"]

    def cancel_booking(self, session_id: int, count: int) -> None:
        """Скасовує бронювання квитків."""
        if session_id not in self.sessions:
            raise KeyError(f"Сеанс з ID {session_id} не знайдено")
        if count <= 0:
            raise ValueError("Кількість квитків для скасування має бути більшою за 0")
        
        session = self.sessions[session_id]
        if count > session["booked_seats"]:
            raise ValueError("Неможливо скасувати більше квитків, ніж заброньовано")
        
        session["booked_seats"] -= count

    def get_available_seats(self, session_id: int) -> int:
        """Повертає кількість вільних місць на сеанс."""
        if session_id not in self.sessions:
            raise KeyError(f"Сеанс з ID {session_id} не знайдено")
        session = self.sessions[session_id]
        return session["total_seats"] - session["booked_seats"]

    def get_session(self, session_id: int) -> dict:
        """Повертає інформацію про сеанс."""
        if session_id not in self.sessions:
            raise KeyError(f"Сеанс з ID {session_id} не знайдено")
        return self.sessions[session_id]
from cinema_manager import CinemaManager

def main():
    manager = CinemaManager()
    session_id = manager.add_session("Інтерстеллар", "19:00", 50, 150.0)
    print(f"=== Cinema Manager Console ===")
    print(f"Створено сеанс ID: {session_id}")
    
    session = manager.get_session(session_id)
    print(f"Фільм: {session['movie']}, Час: {session['time']}")
    print(f"Вільних місць: {manager.get_available_seats(session_id)}")

if __name__ == "__main__":
    main()
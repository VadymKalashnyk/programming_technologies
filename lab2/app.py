from flask import Flask, request, jsonify
from cinema_manager import CinemaManager

app = Flask(__name__)

cinema = CinemaManager()

@app.route('/sessions', methods=['POST'])
def create_session():
    data = request.get_json()
    try:
        session_id = cinema.add_session(
            data['movie'], data['time'], data['total_seats'], data['price']
        )
        return jsonify({"message": "Сеанс створено", "session_id": session_id}), 201
    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/sessions/<int:session_id>/book', methods=['POST'])
def book_tickets(session_id):
    data = request.get_json()
    count = data.get('count', 0)
    try:
        total_price = cinema.book_tickets(session_id, count)
        return jsonify({
            "message": "Квитки успішно заброньовано",
            "total_price": total_price,
            "remaining_seats": cinema.get_available_seats(session_id)
        }), 200
    except (ValueError, KeyError) as e:
        return jsonify({"error": str(e)}), 400

@app.route('/sessions/<int:session_id>', methods=['GET'])
def get_session(session_id):
    try:
        session_info = cinema.get_session(session_id)
        return jsonify(session_info), 200
    except KeyError as e:
        return jsonify({"error": str(e)}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
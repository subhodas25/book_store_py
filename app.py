from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "1984", "author": "George Orwell"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee"}
]

# Get all books


@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Get a single book by ID


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Add a new book


@app.route('/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    if "title" in new_book and "author" in new_book:
        new_book["id"] = len(books) + 1
        books.append(new_book)
        return jsonify(new_book), 201
    return jsonify({"error": "Invalid data"}), 400

# Update an existing book


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book["id"] == book_id), None)
    if book:
        updated_data = request.get_json()
        book.update(updated_data)
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

# Delete a book


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200


if __name__ == '__main__':
    app.run(debug=True)

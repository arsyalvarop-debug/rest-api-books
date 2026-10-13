from flask import Blueprint, jsonify, request
from database.db import get_db_connection

books_bp = Blueprint("books", __name__)


@books_bp.route("/books", methods=["GET"])
def get_books():
    connection = get_db_connection()

    books = connection.execute(
        "SELECT * FROM books"
    ).fetchall()

    connection.close()

    return jsonify([dict(book) for book in books])

from flask import request

@books_bp.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()

    if not data:
        return jsonify({"message": "JSON body is required"}), 400

    title = data.get("title")
    author = data.get("author")

    if not title or not author:
        return jsonify({
            "message": "Title and author are required"
        }), 400

    connection = get_db_connection()

    cursor = connection.execute(
        """
        INSERT INTO books (title, author, publisher, year, isbn)
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            title,
            author,
            data.get("publisher"),
            data.get("year"),
            data.get("isbn")
        )
    )

    connection.commit()
    book_id = cursor.lastrowid
    connection.close()

    return jsonify({
        "message": "Book created successfully",
        "id": book_id
    }), 201

@books_bp.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    connection = get_db_connection()

    book = connection.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    connection.close()

    if book is None:
        return jsonify({"message": "Book not found"}), 404

    return jsonify(dict(book))


@books_bp.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()

    if not data:
        return jsonify({"message": "JSON body is required"}), 400

    title = data.get("title")
    author = data.get("author")

    if not title or not author:
        return jsonify({
            "message": "Title and author are required"
        }), 400

    connection = get_db_connection()

    book = connection.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    if book is None:
        connection.close()
        return jsonify({"message": "Book not found"}), 404

    connection.execute(
        """
        UPDATE books
        SET title = ?, author = ?, publisher = ?, year = ?, isbn = ?
        WHERE id = ?
        """,
        (
            title,
            author,
            data.get("publisher"),
            data.get("year"),
            data.get("isbn"),
            book_id
        )
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Book updated successfully",
        "id": book_id
    }), 200


@books_bp.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    connection = get_db_connection()

    book = connection.execute(
        "SELECT * FROM books WHERE id = ?",
        (book_id,)
    ).fetchone()

    if book is None:
        connection.close()
        return jsonify({"message": "Book not found"}), 404

    connection.execute(
        "DELETE FROM books WHERE id = ?",
        (book_id,)
    )

    connection.commit()
    connection.close()

    return jsonify({
        "message": "Book deleted successfully",
        "id": book_id
    }), 200

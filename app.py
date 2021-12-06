from flask import Flask, render_template, jsonify
import json, os

app = Flask(__name__)

@app.route('/')
def home():
	return 'Hello World'

@app.route('/about')
def about():
	return 'This Is The About Page'
	
books=json.load(open("data/books.json"))

@app.route('/books', methods=["GET"])
def list_books():
	return jsonify(books)
	
@app.route('/book/<int:id>', methods=["GET"])
def get_book(id):
	book = None
	for i in books:
		if i.get('isbn') == str(id):
			book = i
	return jsonify(book)
	

@app.route("/book/<string:title>", methods=["GET"])
def get_title_book(title):
    book = None
    for i in books:
        if i.get("title") == title:
            book = i
            break
    return render_template("book_by_title.html", book=book)
    
    
'''
@app.route('/book')
def blog():
	books = [{'title': 'Le Horla', 'author': 'Guy de Maupassant'},
	{'title': 'Le malade imaginaire', 'author': 'Molière'}]
	return render_template('book.html', books=books)
		
@app.route('/blog/<blog_id>')
def blog_post(blog_id):
	return 'This Is The Blog Page : ' + blog_id
	'''

if __name__ == '__main__':
	app.run()

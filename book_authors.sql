CREATE DATABASE bookstore;

CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    author_name VARCHAR(100) NOT NULL
);

CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) NOT NULL,
    publication_year INTEGER NOT NULL,
    author_id INTEGER REFERENCES authors(author_id)
);

-- Insert authors
INSERT INTO authors (author_name) VALUES
    ('J.K. Rowling'),
    ('George R.R. Martin'),
    ('Harper Lee');

-- Insert books
INSERT INTO books (title, isbn, publication_year, author_id) VALUES
    ('Harry Potter and the Sorcerer''s Stone', '978-0590353427', 1997, 1),
    ('A Game of Thrones', '978-0553593716', 1996, 2),
    ('To Kill a Mockingbird', '978-0061120084', 1960, 3);


-- Select all books with their authors
SELECT
    books.title,
    books.isbn,
    books.publication_year,
    authors.author_name
FROM
    books
JOIN
    authors ON books.author_id = authors.author_id;


-- Update the publication year of a book
UPDATE books
SET publication_year = 1998
WHERE title = 'Harry Potter and the Sorcerer''s Stone';


-- Delete a book
DELETE FROM books
WHERE title = 'A Game of Thrones';

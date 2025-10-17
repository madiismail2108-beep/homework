CREATE SCHEMA IF NOT EXISTS my_function;

SET search_path TO my_function;

CREATE TABLE books(
id SERIAL PRIMARY KEY,
title VARCHAR(100) NOT NULL,
author VARCHAR(100) NOT NULL,
year_of_manuf int,
created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO books(title, author, year_of_manuf) 
VALUES
('Alkimyogar', 'Paulo Coelho', 1988),
('1984', 'George Orwell', 1949),
('Animal Farm', 'George Orwell', 1949),
('Otkan kunlar', 'Abdulla Qodiriy', 1926),
('Sapiens', 'Yuval Noah Harari', 2011),
('Rich Dad Poor Dad', 'Robert Kiyosaki', 1997),
('Hamlet', 'William Shakespeare', 1603),
('The Little Prince', 'Antoine de Saint-Exupéry', 1943),
('War and Peace', 'Leo Tolstoy', 1869),
('Sherlock Holmes', 'Arthur Conan Doyle', 1892),
('Qorako‘z Majnun', 'Cho‘lpon', 1934),
('Nineteen Eighty-Four Essays', 'George Orwell', 1949);

CREATE OR REPLACE FUNCTION book_y(p_year INT)
RETURNS VARCHAR
LANGUAGE plpgsql
AS $$
DECLARE
    b_title VARCHAR(100);
BEGIN
   SELECT title
   INTO b_title
   FROM books
   WHERE year_of_manuf = p_year;

   RETURN b_title;
END;
$$;


DROP FUNCTION book_y;

SELECT * FROM book_y(1949);


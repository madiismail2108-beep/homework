CREATE TABLE university(
  id SERIAL PRIMARY KEY,
  name VARCHAR (100) NOT NULL,
  CITY VARCHAR (100)
);

CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  fullname VARCHAR (100) NOT NULL,
  age INT,
  student_id 
  university_id INT REFERENCES university(id) ON DELETE CASCADE
);

INSERT INTO university (name, city)
VALUES 
 ('TTPU', 'TASHKENT'),
 ('FKKT', 'FERGANA'),
 ('IDU', 'ANGREN'),
 ('BFU', 'BUKHARA')

INSERT INTO students (fullname, age, university_id)
VALUES
    ('Ali Karimov', 20, 1),
    ('Madina Ismailova', 19, 1),
    ('Jasur Usmonov', 21, 1),
    ('Shahnoza Rasulova', 20, 1),
    ('Dilshod Bek', 22, 1),

    ('Aziza Otabekova', 19, 2),
    ('Kamol Tursunov', 21, 2),
    ('Umida Rahmonova', 20, 2),
    ('Bekzod Aliyev', 23, 2),
    ('Saida Karimova', 19, 2),
	
    ('Amir Ergashev', 20, 3),
    ('Lola Olimova', 21, 3),
    ('Javlon Abdukarimov', 22, 3),
    ('Nigora Shomurodova', 19, 3),
    ('Rustam Jalilov', 20, 3),

    ('Shohruh Rakhimov', 21, 4),
    ('Malika Umarova', 22, 4),
    ('Shaxzod Kholikov', 20, 4),
    ('Gulbahor Mamatova', 19, 4),
    ('Zafar Sobirov', 23, 4)
    
	
SELECT * FROM students ORDER BY fullname ASC;

SELECT * FROM students ORDER BY age DESC;

DELETE FROM students WHERE age = 22;

DELETE FROM university WHERE name = 'FKKT';

SELECT * FROM university;

--3dars
CREATE SCHEMA my_app;

CREATE TABLE my_app.comment (
    id SERIAL PRIMARY KEY,
    message TEXT NOT NULL,
    owner VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    rating INT DEFAULT 0,
    file_url TEXT
);

ALTER TABLE my_app.comment
ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

ALTER TABLE my_app.comment
RENAME COLUMN owner TO author;

ALTER TABLE my_app.comment
ALTER COLUMN rating TYPE SMALLINT;

ALTER TABLE my_app.comment
ALTER COLUMN rating SET DEFAULT 1;

ALTER TABLE my_app.comment
ALTER COLUMN rating DROP DEFAULT;

ALTER TABLE my_app.comment
DROP COLUMN file_url;

ALTER TABLE my_app.comment
RENAME TO comments;


INSERT INTO my_app.comments (message, author, rating, is_active)
VALUES 
('Bu mening birinchi kommentariyam', 'Madina', 5, TRUE),
('Post juda foydali ekan', 'Ali', 4, TRUE),
('Rahmat!', 'Dilshod', 3, FALSE);

select * from  my_app.comments
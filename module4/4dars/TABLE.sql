--4dars
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
	first_name VARCHAR(50) NOT NULL,
    second_name VARCHAR(50) NOT NULL,
	phone VARCHAR(30)
);

CREATE TABLE groups (
    group_id SERIAL PRIMARY KEY,
    group_name VARCHAR(50) NOT NULL
);

CREATE TABLE teachers(
  employee_id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  second_name VARCHAR(50) NOT NULL
);



CREATE TABLE teacher_groups (
    id SERIAL PRIMARY KEY,
    teacher_id INT REFERENCES teachers(employee_id),
    group_id INT REFERENCES groups(group_id)
);

CREATE TABLE students (
 students_id SERIAL PRIMARY KEY,
 customer_id INT UNIQUE REFERENCES customers(id),
 group_id INT REFERENCES groups(group_id)
);

INSERT INTO customers (first_name, second_name, phone)
VALUES 
('Nodira', 'Karimova', '+998901112233'),
('Bekzod', 'Sodiqov', '+998909998877'),
('Malika', 'Umarova', '+998907771122');

INSERT INTO groups (group_name)
VALUES 
('NO11'),
('IS11'),
('NO12'),
('IS12'),
('NO13'),
('IS13'),
('FS14'),
('FN14'),
('FG14');

INSERT INTO teachers (first_name, second_name)
VALUES 
('Ali', 'Valiyev'),     
('Dilnoza', 'Rustamova'),
('Jasur', 'Qodirov');

INSERT INTO teacher_groups (teacher_id, group_id)
VALUES
(1, 1), (1, 3), (1, 5), 
(2, 2), (2, 4), (2, 6),
(3, 7), (3, 8); 

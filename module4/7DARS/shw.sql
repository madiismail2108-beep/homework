create schema if not exists erp;

set search_path to erp;
set timezone to 'Asia/Tashkent';

create table profiles(
    id serial primary key,
    username varchar(50) not null unique,
    password varchar(255) not null,
    role varchar(15) not null
        check (role in ('teacher','student','support'))
        default 'student',
    created_at timestamptz default current_timestamp
);

create table teachers(
    id serial primary key,
    full_name varchar(255) not null,
    phone varchar(15) not null unique,
    specialization text,
    profile_id int references profiles(id)
);

create table courses(
    id serial primary key,
    name varchar(255) not null unique,
    description text,
    duration int default 3,
    price decimal(14,2) not null
);

create table groups(
    id serial primary key,
    name varchar(255) not null unique,
    room_number varchar(255) unique,
    started_at date,
    ended_at date,
    teacher_id int,
    course_id int,
    constraint teacher_id_fk
        foreign key (teacher_id) references teachers(id) on delete set null,
    constraint course_id_fk
        foreign key (course_id) references courses(id) on delete set null
);

create table students(
    id serial primary key,
    full_name varchar(255) not null,
    phone varchar(15) not null unique,
    address text,
    age int check (age > 13),
    group_id int references groups(id),
    profile_id int references profiles(id)
);

create table subjects(
    id serial primary key,
    name varchar(255) not null,
    file_url varchar(255),
    started_at date,
    ended_at date,
    subjects_dat date,
    groups_id int references groups(id)
);


create table exams(
    id serial primary key,
    file_url varchar(255),
    description text,
    started_at date,
    ended_at date,
    group_id int references groups(id)
);

create table result_st(
    id serial primary key,
    rate int check (rate between 0 and 100),
    status varchar(20) check (status in ('passed','failed')),
    ended_at date,
    student_id int references students(id)
);

create table attendances(
    id serial primary key,
    attendance_date date,
    status varchar(20) check (status in ('present','absent','late')) default 'absent',
    student_id int references students(id),
    subject_id int references subjects(id)
);

create table payments(
    id serial primary key,
    student_id int references students(id),
    payment_date date,
    method varchar(10) check (method in ('cash','card','online')),
    amount int,
    status varchar(10) check (status in ('paid','unpaid')) default 'unpaid'
);

insert into profiles (username, password, role)
values 
('teacherAV', '12334', 'teacher'),
('teacherMS', '12334', 'teacher'),
('teacherFG', '56123', 'teacher'),
('supportAS', '78123', 'support'),
('supportAD', '79123', 'support'),
('Malika.I', '09768', 'student'),
('Akmal.K', '132456', 'student'),
('Madina.I', 'pass123', 'student');


insert into teachers (full_name, phone, specialization, profile_id)
values
('Ali Valiyev', '+998901112233', 'Mathematics', 1),
('Mahmud Saydullaev', '+998901112244', 'Physics', 2),
('Faruh Gofurov', '+998901112255', 'Informatics', 3);

insert into courses (name, description, duration, price)
values
('Mathematics Basic', 'Introductory math course', 6, 500000.00),
('Physics Advanced', 'Deep physics course', 6, 750000.00);

insert into groups (name, room_number, started_at, ended_at, teacher_id, course_id)
values
('Group A', '101', '2025-02-01', '2025-08-01', 1, 1),
('Group B', '102', '2025-03-01', '2025-09-01', 2, 2);

insert into students (full_name, phone, address, age, group_id, profile_id)
values 
('Malika Ismoilova', '+998901112266', 'Tashkent, Yunusabad', 18, 1, 6),
('Akmal Karimov', '+998901112277', 'Tashkent, Chilonzor', 20, 1, 7),
('Madina Ismoilova', '+998901112288', 'Tashkent, Sergeli', 19, 2, 8);

insert into exams (file_url, description, started_at, ended_at, group_id)
values
('exam_math.pdf', 'Mathematics Exam', '2025-06-01', '2025-06-01', 1),
('exam_physics.pdf', 'Physics Exam', '2025-06-02', '2025-06-02', 2);

insert into result_st (rate, status, ended_at, student_id)
values
(85, 'passed', '2025-06-01', 1),
(65, 'failed', '2025-06-01', 2),
(90, 'passed', '2025-06-02', 3);

select s.full_name as student_name,
       e.description as exam_name,
       r.rate,
       r.status
from result_st r
inner join students s 
    on r.student_id = s.id
inner join exams e 
    on e.group_id = s.group_id;


select s.full_name as student_name,
       r.rate,
       r.status
from students s
left join result_st r 
    on s.id = r.student_id;

select e.description as exam_name,
       r.rate,
       r.status
from result_st r
right join exams e 
    on e.group_id = r.student_id;

select e.description as exam_name,
       avg(r.rate) as avg_rate
from exams e
inner join students s 
    on e.group_id = s.group_id
inner join result_st r 
    on s.id = r.student_id
group by e.description;

select s.full_name as student_name,
       count(*) filter (where r.status = 'passed') as passed_exams,
       count(*) filter (where r.status = 'failed') as failed_exams
from students s
left join result_st r 
    on s.id = r.student_id
group by s.full_name
order by passed_exams desc;

select s.full_name as student_name,
       count(*) filter (where r.status = 'passed') as passed_exams,
       count(*) filter (where r.status = 'failed') as failed_exams
from students s
left join result_st r 
    on s.id = r.student_id
group by s.full_name
order by passed_exams desc;



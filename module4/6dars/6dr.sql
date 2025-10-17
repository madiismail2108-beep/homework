-----------------------5DARS
create schema if not exists erp;


set
search_path to erp;

set
timezone to 'Asia/Tashkent';

create table profile
(
    id       serial primary key,
    username varchar(50)  not null unique,
    password varchar(255) not null,
    role     varchar(15)  not null
        check (role in ('teacher', 'student', 'support'))
        default 'student'

);


alter table profile
    add column created_at timestamptz default current_timestamp;


create table teacher
(
    id             serial primary key,
    full_name      varchar(255) not null,
    phone          varchar(15)  not null unique,
    specialization text,
    profile_id     int references profile (id)
);


create table course
(
    id          serial primary key,
    name        varchar(255)   not null unique,
    description text,
    duration    int default 3,
    price       decimal(14, 2) not null
);


create table "group"
(
    id          serial primary key,
    name        varchar(255) not null unique,
    room_number varchar(255) unique,
    started_at  date,
    ended_at    date,
    teacher_id  int,
    course_id   int,
    constraint teacher_id_fk
        foreign key (teacher_id)
            references teacher (id)
            on delete set null,
    constraint course_id_fk
        foreign key (course_id)
            references course (id)
            on delete set null


);


create table student
(
    id         serial primary key,
    full_name  varchar(255) not null,
    phone      varchar(15)  not null unique,
    address    text,
    age        int check ( age > 13 ),
    group_id   int references "group" (id),
    profile_id int references profile (id)

);

create table subject
(
    id          serial primary key,
    name        varchar(255) not null,
    file_url    varchar(255),
    started_at  date,
    ended_at    date,
    subject_dat date,
    group_id    int,
    foreign key (group_id) references "group" (id)
);


create table exam
(
    id          serial primary key,
    file_url    varchar(255),
    description text,
    started_at  date,
    ended_at    date,
    group_id    int,
    foreign key (group_id) references "group" (id)
);


create table result
(
    id         serial primary key,
    rate       int check ( rate between 0 and 100),
    status     varchar(20) check ( status in ('passed', 'failed')),
    ended_at   date,
    student_id int references student (id)

);

create table attendance
(
    id              serial primary key,
    attendance_date date,
    status          varchar(20) check ( status in ('present', 'absent', 'late')),
    student_id      int references student (id),
    subject_id      int references subject (id)
);

alter table attendance
    alter column status set default 'absent';

create table payment
(
    id           serial primary key,
    student_id   int references student (id),
    payment_date date,
    method       varchar(10) check ( method in ('cash', 'card', 'online')),
    amount       int,
    status       varchar(10) check ( status in ('paid', 'unpaid')) default 'unpaid'
);

insert into profile (username, password, role)
values ('teacherAV', '12334', 'teacher'),
       ('teacherMS', '12334', 'teacher'),
       ('teacherFG', '56123', 'teacher'),
       ('supportAS', '78123', 'support'),
       ('supportAD', '79123', 'support'),
       ('Malika I.D', '09768', 'student'),
       ('Akmal K.Yu', '132456', 'student'),
       ('Madina I.D', 'pass123', 'student');

insert into teacher (full_name, phone, specialization, profile_id)
values ('Ali Valiyev', '+998901112233', 'Mathematics', 1),
       ('Mahmud Saydullaev', '+998901112244', 'Fiziks', 2),
       ('Faruh Gofurv', '+998901112255', 'Mathemat', 3);


CREATE EXTENSION IF NOT EXISTS pgcrypto;

SELECT *
FROM pg_extension
WHERE extname = 'pgcrypto';

create table if not exists users(
    id serial primary key,
    username varchar(255) unique,
    email varchar(255) not null unique ,
    password varchar(255) not null,
    created_at timestamp default now(),
    bio text,
    is_private boolean default 'False'
    );

create table post(
    id serial primary key,
    title varchar(255),
    location varchar(155),
    caption varchar(155),
    file_url varchar(255),
    posted_at timestamp default now(),
    user_id int  references users(id)
);

create table commenties(
    id serial primary key ,
    message text ,
    user_id int references  users(id) on delete cascade ,
    post_id int references post(id) on delete cascade,
    messaged_at timestamptz default current_timestamp
);


create table users_post_like(
    user_id int references  users(id) on delete cascade ,
    post_id int references post(id) on delete cascade,
    created_at timestamptz default current_timestamp,
    primary key (user_id,post_id)
);

create table follower(
    follower_id int references users(id) on delete cascade ,
    followed_id int references users(id) on delete cascade ,
    created_at timestamptz default current_timestamp,
    primary key (follower_id,followed_id),
    check ( follower_id <> followed_id )
);

create table saved_post(
                           user_id int references  users(id) on delete cascade ,
                           post_id int references post(id) on delete cascade,
                           created_at timestamptz default current_timestamp,
                           unique(user_id,post_id)
);



create table saved_like(
                           user_id int references  users(id) on delete cascade ,
                           post_id int references post(id) on delete cascade,
                           created_at timestamptz default current_timestamp,
                           unique (user_id,post_id)
);


create table tag(
    id serial primary key ,
    name varchar(255) unique
);

create table post_tag(
    id serial primary key ,
    tag_id int ,
    post_id int,
    foreign key (tag_id) references tag(id),
    foreign key (post_id) references post(id)
);

create or replace function login(p_username varchar,p_password varchar)
returns text language plpgsql
as
$$

    declare
        stored_username varchar;
        stored_pass varchar;
    begin
        select username into stored_username from users where username = p_username;
        select password into stored_pass from users where username = p_username;

        if stored_username is null then
--             raise notice 'This % not found' , p_username;
            return format('This %s not found',p_username);
        end if;

        if (stored_pass is null) or (stored_pass <> crypt(p_password,stored_pass)) then
--             raise notice 'Password did not match';
            return format('Password did not match');
        end if;

        return 'Login successfully';

    end;
$$ ;

INSERT INTO users (username, email, password, bio, is_private)
VALUES 
 ('Ali Aliev', 'al.aliev@gmail.com', 'pqwe2341', 'Bio of user 1', FALSE),
 ('Malika Safarova', 'malin.s@gmail.com', 'pass234', 'Bio of user 2', TRUE),
 ('Monu Vohidova', 'vohid.monu3@gmail.com', 'pass3645', 'Bio of user 3', FALSE),
 ('Murod Murodov', 'murod4@gmail.com', 'pass5678', 'Bio of user 4', TRUE),
 ('Mahmud Mahmudov', 'emahmud123@gmail.com', 'pass5977', 'Bio of user 5', FALSE),
 ('Akmal Akmalov', 'ak.ak134@gmail.com', 'pass6999', 'Bio of user 6', TRUE),
 ('Mashxura Tohtaeva', 'Mahxurtoht7@gmail.com', 'pass70044', 'Bio of user 7', FALSE),
 ('Nazal Niyazova', 'niyazova2134@gmail.com', 'pass87654', 'Bio of user 8', TRUE),
 ('Hanna', 'hannnn@gmail.com', 'pass9', 'Bio of user 9339', FALSE),
 ('JImmi Toyu', 'Jimm56@gmail.com', 'pass10945', 'Bio of user 10', TRUE);

INSERT INTO post (title, location, caption, file_url, user_id) VALUES 
('Post 10', 'Location 1', 'Caption 1', 'http://example.com/file1.jpg', 1),
 ('Post 23', 'Location 2', 'Caption 2', 'http://example.com/file2.jpg', 2),
 ('Post 34', 'Location 3', 'Caption 3', 'http://example.com/file3.jpg', 3),
 ('Post 45', 'Location 4', 'Caption 4', 'http://example.com/file4.jpg', 4),
('Post 54', 'Location 5', 'Caption 5', 'http://example.com/file5.jpg', 5),
 ('Post 63', 'Location 6', 'Caption 6', 'http://example.com/file6.jpg', 6),
 ('Post 72', 'Location 7', 'Caption 7', 'http://example.com/file7.jpg', 7),
 ('Post 81', 'Location 8', 'Caption 8', 'http://example.com/file8.jpg', 8),
('Post 96', 'Location 9', 'Caption 9', 'http://example.com/file9.jpg', 9),
 ('Post 104', 'Location 10', 'Caption 10', 'http://example.com/file10.jpg', 10);

INSERT INTO commenties (message, user_id, post_id)
VALUES 
('This is so good ', 6, 5),
('where to find it', 8, 7);

INSERT INTO follower (follower_id, followed_id)
VALUES
 (1, 2),
 (2, 3),
 (3, 4),
 (4, 5),
 (5, 6),
 (6, 7),
 (7, 8);

INSERT INTO saved_post (user_id, post_id) 
VALUES
 (1, 5),
 (2, 2),
 (3, 4),
 (4, 6),
 (5, 2);

INSERT INTO users_post_like (user_id, post_id)
VALUES 
 (1, 1),
 (2, 2),
 (3, 3),
 (5, 4),
 (3, 5);

INSERT INTO tag (name) 
VALUES
 ('cats'),
 ('cars'),
 ('hauses'),
 ('get ready with me'),
 ('exams');

INSERT INTO post_tag (tag_id, post_id) 
VALUES 
 (1, 6),
 (2, 2),
 (3, 3),
 (4, 4),
 (5, 5);
 
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

INSERT INTO users (username, email, password, bio, is_private) VALUES 
('madina_ismailova', 'madina@example.com', 'pass1', 'Traveler & foodie ', FALSE),
('azizbek_karimov', 'azizbek@example.com', 'pass2', 'Love photography ', TRUE),
('dilnoza_tursunova', 'dilnoza@example.com', 'pass3', 'Bookworm & coffee addict ', FALSE),
('jamshid_nazarov', 'jamshid@example.com', 'pass4', 'Cyclist and tech enthusiast ', TRUE),
('malika_sobirova', 'malika@example.com', 'pass5', 'Dream big, work hard ', FALSE),
('islom_toshpulatov', 'islom@example.com', 'pass6', 'Nature is my therapy ', TRUE),
('aziza_rahmonova', 'aziza@example.com', 'pass7', 'Designer • Minimalist ', FALSE),
('behruz_akramov', 'behruz@example.com', 'pass8', 'Music is life ', TRUE),
('nilufar_saidova', 'nilufar@example.com', 'pass9', 'Writer & poet ', FALSE),
('umid_karimov', 'umid@example.com', 'pass10', 'Tech blogger ', TRUE);


INSERT INTO post (title, location, caption, file_url, user_id) VALUES
('Sunset over Samarkand', 'Samarkand', 'Golden hour vibes ', 'http://example.com/sunset.jpg', 1),
('Coffee Moments', 'Tashkent', 'Morning routine ', 'http://example.com/coffee.jpg', 2),
('Hiking the Chimgan Mountains', 'Chimgan', 'Breathtaking views ', 'http://example.com/chimgan.jpg', 3),
('New Design Drop', 'Online', 'Check out my latest work ', 'http://example.com/design.jpg', 4),
('Music Festival', 'Bukhara', 'Feeling alive ', 'http://example.com/music.jpg', 5),
('Forest Walk', 'Namangan', 'Fresh air & peace ', 'http://example.com/forest.jpg', 6),
('Minimal Art', 'Home Studio', 'Simplicity speaks volumes ', 'http://example.com/art.jpg', 7),
('New Track Release', 'Spotify', 'Out now ', 'http://example.com/track.jpg', 8),
('Poetry Night', 'Cafe Verona', 'Words from the soul ', 'http://example.com/poetry.jpg', 9),
('Coding Marathon', 'Tashkent', 'Let’s build something great ', 'http://example.com/code.jpg', 10);-- COMMENTS

INSERT INTO commenties (message, user_id, post_id) VALUES
('Wow, amazing photo!', 2, 1),
('That coffee looks perfect ', 3, 2),
('Mountains look stunning!', 4, 3),
('Great design bro ', 5, 4),
('Music festival was awesome ', 6, 5),
('So peaceful ', 7, 6),
('Love your art style!', 8, 7),
('Listening to it right now ', 9, 8),
('Beautiful words ', 10, 9),
('Keep coding ', 1, 10);


INSERT INTO follower (follower_id, followed_id) VALUES
(1, 8),
(2, 10),
(3, 5),
(4, 6),
(5, 7),
(6, 8),
(7, 1),
(8, 9),
(9, 10),
(10, 1);

INSERT INTO saved_post (user_id, post_id)
VALUES
(1, 2),
(2, 5),
(3, 6),
(4, 2),
(5, 8);

INSERT INTO users_post_like (user_id, post_id) 
VALUES
(1, 10),
(2, 6),
(3, 2),
(4, 5),
(5, 3),
(6, 4),
(7, 8),
(8, 9),
(9, 7),
(10, 1);

INSERT INTO tag (name) VALUES
('travel'),
('coffee'),
('nature'),
('design'),
('music'),
('coding'),
('art'),
('poetry'),
('festival'),
('motivation');

INSERT INTO post_tag (tag_id, post_id) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(3, 6),
(7, 7),
(5, 8),
(8, 9),
(6, 10);

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

CREATE OR REPLACE FUNCTION g_u_p()
RETURNS TABLE(
user_id INT,
username VARCHAR,
post_id INT,
title VARCHAR,
caption VARCHAR,
posted_at TIMESTAMP
)
LANGUAGE SQL
AS $$
SELECT
u.id AS user_id,
u.username,
p.id AS post_id,
p.title,
p.caption,
p.posted_at
FROM users u 
JOIN post p on u.id=p.user_id;
$$;


CREATE OR REPLACE FUNCTION g_p_c()
RETURNS TABLE(
    post_id INT,
    post_title VARCHAR,
    comment_id INT,
    message TEXT,
	commenter VARCHAR,
    messaged_at TIMESTAMPTZ
)
LANGUAGE SQL
AS $$
    SELECT 
        p.id AS post_id,
        p.title AS post_title,
        c.id AS comment_id,
        c.message,
        u.username AS commenter,
        c.messaged_at
    FROM post p
    JOIN commenties c ON p.id = c.post_id
    JOIN users u ON c.user_id = u.id;
$$;


create or replace function g_p_l()
returns table(
    post_id int,
    title varchar,
    liked_by varchar,
    liked_at timestamptz
)
language sql
as $$
    select 
        p.id as post_id,
        p.title,
        u.username as liked_by,
        l.created_at as liked_at
    from post p
    left join users_post_like l on p.id = l.post_id
    left join users u on u.id = l.user_id;
$$;


create or replace function g_u_f()
returns table(
    user_id int,
    username varchar,
    follower_id int,
    follower_name varchar,
    followed_at timestamptz
)
language sql
as $$
    select 
        f.followed_id as user_id,
        u.username,
        f.follower_id,
        u2.username as follower_name,
        f.created_at as followed_at
    from follower f
    join users u on f.followed_id = u.id
    join users u2 on f.follower_id = u2.id;
$$;


create or replace function g_p_t()
returns table(
    post_id int,
    title varchar,
    tag_name varchar
)
language sql
as $$
    select 
        p.id as post_id,
        p.title,
        t.name as tag_name
    from post p
    join post_tag pt on p.id = pt.post_id
    join tag t on t.id = pt.tag_id;
$$;


create or replace function g_s_p()
returns table(
    user_id int,
    username varchar,
    post_id int,
    post_title varchar,
    saved_at timestamptz
)
language sql
as $$
    select 
        u.id as user_id,
        u.username,
        p.id as post_id,
        p.title as post_title,
        s.created_at as saved_at
    from saved_post s
    join users u on u.id = s.user_id
    join post p on p.id = s.post_id;
$$;


create or replace function g_s_l()
returns table(
    user_id int,
    username varchar,
    liked_post varchar,
    saved_like_at timestamptz
)
language sql
as $$
    select 
        u.id as user_id,
        u.username,
        p.title as liked_post,
        sl.created_at as saved_like_at
    from saved_like sl
    join users u on u.id = sl.user_id
    join post p on p.id = sl.post_id;
$$;


select * from g_u_p();
select * from g_p_c();
select * from g_p_l();
select * from g_u_f();
select * from g_p_t();
select * from g_s_p();
select * from g_s_l();

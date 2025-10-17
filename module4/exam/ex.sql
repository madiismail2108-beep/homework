CREATE SCHEMA IF NOT EXISTS md;

set search_path to md;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT,
    parent_id INT REFERENCES categories(id) ON DELETE SET NULL
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    category_id INT REFERENCES categories(id) ON DELETE CASCADE,
    name VARCHAR(200) NOT NULL,
    description TEXT,
    price NUMERIC(10,2) NOT NULL,
    stock INT DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product_images (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    image_url TEXT NOT NULL,
    is_main BOOLEAN DEFAULT FALSE
);

CREATE TABLE commenties (
    id SERIAL PRIMARY KEY,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    comment_text TEXT NOT NULL,
    rating INT CHECK (rating BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users(id) ON DELETE CASCADE,
    total_amount NUMERIC(10,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INT REFERENCES orders(id) ON DELETE CASCADE,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    price NUMERIC(10,2) NOT NULL
);

CREATE TABLE carts (
    id SERIAL PRIMARY KEY,
    user_id INT UNIQUE REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE cart_items (
    id SERIAL PRIMARY KEY,
    cart_id INT REFERENCES carts(id) ON DELETE CASCADE,
    product_id INT REFERENCES products(id) ON DELETE CASCADE,
    quantity INT DEFAULT 1
);


INSERT INTO users (username, email, password) VALUES
('madina', 'madina@example.com', 'pass123'),
('aziz', 'aziz@example.com', 'secret456'),
('dilshod', 'dilshod@example.com', 'qwerty789'),
('nilufar', 'nilufar@example.com', 'pass999'),
('bekzod', 'bekzod@example.com', 'mypassword');


INSERT INTO categories (name, description) VALUES
('Electronics', 'Phones, laptops, and accessories'),
('Clothing', 'Men and women fashion'),
('Home Appliances', 'Household electronics'),
('Books', 'All kinds of books'),
('Sports', 'Fitness and sports equipment');

INSERT INTO products (category_id, name, description, price, stock) VALUES
(1, 'iPhone 14', 'Apple smartphone with A15 chip', 899.99, 15),
(1, 'Samsung Galaxy S23', 'Flagship Android smartphone', 799.50, 20),
(2, 'Men T-Shirt', 'Cotton shirt, various sizes', 19.99, 100),
(3, 'LG Washing Machine', 'Automatic washing machine 7kg', 499.00, 8),
(4, 'The Alchemist', 'Novel by Paulo Coelho', 12.50, 30),
(5, 'Yoga Mat', 'Non-slip mat for yoga and fitness', 25.00, 50);

INSERT INTO product_images (product_id, image_url, is_main) VALUES
(1, 'https://example.com/img/iphone14-main.jpg', TRUE),
(1, 'https://example.com/img/iphone14-side.jpg', FALSE),
(2, 'https://example.com/img/samsung-s23-main.jpg', TRUE),
(3, 'https://example.com/img/tshirt-blue.jpg', TRUE),
(4, 'https://example.com/img/washing-machine.jpg', TRUE),
(5, 'https://example.com/img/alchemist-book.jpg', TRUE);

INSERT INTO commenties (product_id, user_id, comment_text, rating) VALUES
(1, 2, 'Juda zo‘r telefon, lekin biroz qimmat.', 5),
(2, 1, 'Kamera sifati yaxshi, batareya uzoq vaqtga yetadi.', 4),
(3, 4, 'Material sifati yaxshi emas.', 2),
(4, 3, 'Ishlayapti, lekin tovushi baland.', 3),
(5, 5, 'Kitob hayotimni o‘zgartirdi!', 5);

INSERT INTO orders (user_id, total_amount, status) VALUES
(1, 924.99, 'delivered'),
(2, 39.98, 'pending'),
(3, 511.50, 'processing'),
(4, 25.00, 'canceled'),
(5, 812.49, 'delivered');

INSERT INTO order_items (order_id, product_id, quantity, price) VALUES
(1, 1, 1, 899.99),
(1, 5, 1, 25.00),
(2, 3, 2, 19.99),
(3, 4, 1, 499.00),
(3, 2, 1, 12.50),
(5, 2, 1, 799.50),
(5, 6, 1, 12.99);

INSERT INTO carts (user_id) VALUES
(1),
(2),
(3),
(4),
(5);

INSERT INTO cart_items (cart_id, product_id, quantity) VALUES
(1, 2, 1),
(1, 5, 2),
(2, 3, 3),
(3, 1, 1),
(4, 6, 1),
(5, 4, 1),
(5, 3, 2);

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
            return format('This %s not found',p_username);
        end if;

        if (stored_pass is null) or (stored_pass <> crypt(p_password,stored_pass)) then
            return format('Password did not match');
        end if;

        return 'Login successfully';

    end;
$$ ;

create or replace function register_u(
    p_username varchar,
    p_email varchar,
    p_password varchar
)
returns text 
as
$$
declare
    v_hashed_password TEXT;
    v_exists BOOLEAN;
begin
    select exists (
        select 1 from users
        where username = p_username or email = p_email
    ) into v_exists;

    if v_exists then
        return 'Error: username or email already exists';
    end if;
	
    v_hashed_password := crypt(p_password, gen_salt('bf'));

    insert into users (username, email, password)
    values (p_username, p_email, v_hashed_password);

    return 'User registered successfully';
end;
$$ 
language plpgsql;

create or replace function p_add(
    p_category_id int,
    p_name varchar,
    p_description text,
    p_price numeric,
    p_stock int
)
returns
text as
$$
declare
    v_new_id int;
begin
    insert into products (category_id, name, description, price, stock)
     values (p_category_id, p_name, p_description, p_price, p_stock)
    returning
	id into v_new_id;

    return 'Product added successfully. ID ';
exception
    when foreign_key_violation
	then
        return 'Error: invalid category_id';
    when others then
        return 'Error adding product';
end;
$$ 
language plpgsql;

create or replace function up_pr(
    p_id int,
    p_name varchar,
    p_description text,
    p_price numeric,
    p_stock int
)
returns text
as $$
begin
    if not exists (select 1 from products where id = p_id) then
        return 'Error: product not found';
    end if;

    update products
    set name = p_name,
        description = p_description,
        price = p_price,
        stock = p_stock
    where id = p_id;

    return 'Product updated successfully';
exception
    when others then
        return 'Error updating product';
end;
$$ 
language plpgsql;

create or replace function search_products(p_keyword text)
returns table(
    id int,
    name varchar,
    description text,
    price numeric,
    stock int
)
language sql
as $$
select id, name, description, price, stock
from products
where name ilike '%' || p_keyword || '%'
   OR description ILIKE '%' || p_keyword || '%'
order by name;
$$;

create or replace function get_user_orders(p_user_id int)
returns table (
    order_id int,
    total_amount numeric,
    status varchar,
    created_at timestamp
)
language sql
as
$$
select id as order_id, total_amount, status, created_at
from orders
where user_id = p_user_id
order by created_at desc;
$$;

select 
    c.id as category_id,
    c.name as category_name,
    max(p.price) as max_price
from categories c
join products p on c.id = p.category_id
group by c.id, c.name
order by max_price DESC;

select 
    c.id as category_id,
    c.name as category_name,
    count(p.id) as product_count
from categories c
left join products p on c.id = p.category_id
group by c.id, c.name
order by product_count desc;


create or replace function add_to_c(
    c_user_id int,
    c_product_id varchar,
    quantity int
)
returns
text as
$$
declare
    v_new_id int;
begin
    insert into carts (user_id, product_id, quantity)
     values (c_user_id, c_product_id, c_quantity)
    returning
	id into v_new_id;

    return 'Cart added successfully. ID ';
exception
    when foreign_key_violation
	then
        return 'Error: invalid cart_id';
    when others then
        return 'Error adding product';
end;
$$ 
language plpgsql;

create or replace function remove_from_cart(p_user_id INT, p_product_id INT)
returns text
as $$
begin
   if not exists (
       select 1 from cart where user_id = p_user_id and product_id = p_product_id
    ) then
        return 'Error: product not found in cart';
    end if;

    delete from cart
    where user_id = p_user_id and product_id = p_product_id;

    return 'Product removed from cart successfully';
exception
   when others then
       return 'Error: failed to remove product from cart';
end;
$$ 
language plpgsql;

create or replace function get_cart(p_user_id INT)
returns table (
    product_id INT,
    product_name VARCHAR,
    price NUMERIC,
    quantity INT,
    total NUMERIC
)
as $$
begin
   return query
     select   p.id,
        p.name,
        p.price,
        c.quantity,
        (p.price * c.quantity) as total
  from cart c
    join products p on c.product_id = p.id
    where c.user_id = p_user_id;
end;
$$ 

language plpgsql;

create or replace function clear_cart(p_user_id INT)
returns TEXT
as $$
begin
delete from cart where user_id = p_user_id;

    return 'Cart cleared successfully';
exception
   when others then
        return 'Error: failed to clear cart';
end;
$$ 
language plpgsql;

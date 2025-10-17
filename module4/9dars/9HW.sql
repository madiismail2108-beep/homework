 CREATE SCHEMA IF NOT EXISTS shop;
 
SET search_path TO shop;

CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    created_at timestamptz default current_timestamp
);

CREATE TABLE product (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    price DECIMAL(10,2) NOT NULL,
    category_id INT REFERENCES category(id) ON DELETE CASCADE,
    created_at timestamptz default current_timestamp
);

DROP TABLE product

INSERT INTO category (name) 
VALUES
('Drinks'),
('Snacks'),
('Fruits'),
('Electronics');

INSERT INTO product (name, price, category_id) 
VALUES
('Cola', 12000.00, 1),
('Pepsi', 11000.00, 1),
('Chips', 8500.00, 2),
('Apple', 15000.00, 3),
('Banana', 18000.00, 3),
('Headphones', 250000.00, 4),
('Phone Charger', 90000.00, 4);

create or replace function product_list()
returns table(
    id int,
    name varchar,
    price decimal(10,2),
    category_id int,
    created_at timestamptz
) as $$
begin
    return query
    select product.id,
           product.name,
           product.price,
           product.category_id,
           product.created_at
    from product;
end;
$$ language plpgsql;


drop function  get_product(INT);

SELECT product_list();

create or replace function get_product(product_id int)
returns table (
    id int,
    name varchar,
    price decimal(10,2),
    category_id int,
    created_at timestamptz
) as $$
begin
    return query
    select p.id, p.name, p.price, p.category_id, p.created_at
    from product p
    where p.id = product_id;
end;
$$ language plpgsql;

select get_product(5);

ALTER TABLE product ADD COLUMN description text;


create or replace function add_product(
    p_name varchar,
    p_description text,
    p_price decimal(10,2),
    p_category_id int
)
returns integer
as $$
declare
    new_id int;
begin
    insert into product(name, description, price, category_id)
    values (p_name, p_description, p_price, p_category_id)
    returning id into new_id;

    return new_id;
end;
$$ language plpgsql;

select add_product('test','test',2424,2);

create or replace function create_category(cat_name varchar)
returns void
as 
$$
begin
    insert into category(name) 
	values (cat_name);
	
end;
$$ language plpgsql;

create or replace function get_categories()
returns table(id int, name varchar, created_at timestamptz)
as
$$
begin
    return query select * from category;
end;
$$ language plpgsql;

create or replace function update_category(cat_id int, new_name varchar)
returns void 
as
$$
begin
    update category set name = new_name where id = cat_id;
	
end;
$$
language plpgsql;

create or replace function delete_category(cat_id int)
returns void
as
$$
begin
    delete from category where id = cat_id;

end;
$$
language plpgsql;

create or replace function update_product(prod_id int, new_name varchar, new_price numeric, new_cat_id int)
returns void 
as
$$
begin
    update product 
    set name = new_name,
        price = new_price,
        category_id = new_cat_id
    where id = prod_id;

end;
$$ 
language plpgsql;

create or replace function delete_product(prod_id int)
returns void
as 
$$
begin
    delete from product where id = prod_id;

end;
$$ 
language plpgsql;

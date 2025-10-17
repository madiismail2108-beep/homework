do
    $$
    declare
    counter integer:= 1;
    begin
    loop if counter % 2 =0 then
    raise notice '%', counter;
    end if;
    counter = counter + 1;

    if counter = 100 then
    exit;
    end if;
    end loop;
    end;
    $$

CREATE OR REPLACE FUNCTION add_numbers(x INT, y INT)
    RETURNS INTEGER
	AS
	$$
	BEGIN RETURN x+y;
	end;
	$$ LANGUAGE plpgsql;

SELECT add_numbers(30, 88)

CREATE OR REPLACE FUNCTION sub_numbers(x INT, y INT)
    RETURNS INTEGER
	AS
	$$
	BEGIN RETURN x-y;
	end;
	$$ LANGUAGE plpgsql;	

SELECT sub_numbers(30, 88);

CREATE OR REPLACE FUNCTION mul_numbers(x INT, y INT)
    RETURNS INTEGER
	AS
	$$
	BEGIN RETURN x*y;
	end;
	$$ LANGUAGE plpgsql;

SELECT mul_numbers(30, 88)

CREATE OR REPLACE FUNCTION div_numbers(x INT, y INT)
    RETURNS INTEGER
	AS
	$$
	BEGIN RETURN x/y;
	end;
	$$ LANGUAGE plpgsql;
drop function div_numbers

SELECT div_numbers(30, 15);

df  
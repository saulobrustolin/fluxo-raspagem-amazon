python -m venv venv
venv\Scripts\activate
pip install -r requirement
playwright install
python main.py

struct database:

create database amazon;
create table products (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name text, price decimal(8,2), price_shipping decimal(8,2), link text not null);
create table brand (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), name varchar(60), isRegister boolean);
alter table products add column brand UUID references brand(id);
create table temp (id UUID PRIMARY KEY DEFAULT gen_random_uuid(), link text not null, brand UUID references brand(id));

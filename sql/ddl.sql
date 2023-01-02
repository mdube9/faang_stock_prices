create table if not exists "public.stock_data_tmp"
(
"Date" timestamp,
"Open" float,
"High" float,
"Low" float,
"Close" float,
"Adj Close" float,
"Volume" float,
"company" varchar
);

drop table if exists "public.stock_data";
create table "public.stock_data"
(
"Date" timestamp,
"Open" float,
"High" float,
"Low" float,
"Close" float,
"Adj Close" float,
"Volume" float,
"company" varchar,
PRIMARY KEY("Date", "company")
);
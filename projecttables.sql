
use dbmsproject;
create table vehicle(vehicle_id varchar(10) primary key, model_name varchar(20), release_date date, price double, engineC integer, fuel varchar(15), mileage integer, quantity integer); 

insert into vehicle values('V01', 'Lightning McQueen', '2018-05-16', 5.81, 128, 'Petrol', 40, 10);
insert into vehicle values('V02', 'Cruz Ramirez', '2018-09-09', 8.77, 220, 'Petrol', 25, 15);
insert into vehicle values('V03', 'DeLorean', '2017-02-02', 4.73, 128, 'Diesel', 18, 20);
insert into vehicle values('V04', 'Ecto1', '2017-06-20', 10.5, 250, 'Petrol', 23, 5);
insert into vehicle values('V05', 'Ford Anglia', '2017-12-10', 7.35, 115, 'Diesel', 27, 10);

 create table employee(emp_id integer not null auto_increment primary key, emp_name varchar(30));
 insert into employee values (1001, 'Voldemort');
 insert into employee(emp_name) values('Bellatrix');
 insert into employee(emp_name) values('Peter');
 
 create table customer(cust_id integer not null auto_increment primary key, cust_name varchar(25), vehicle_id varchar(10) references vehicle(vehicle_id), dob date, phone char(10), email varchar(60), aadhar char(12), address varchar(100));

insert into customer values(01, 'Harry Potter', 'V01', '1980-07-31', '9742229977', 'harry@hedwig.com', '231456789456', '4, Privet Drive, Lil Whinging');
insert into customer(cust_name, vehicle_id, dob, phone, email, aadhar, address) values('Ron Weasley', 'V02', '1980-03-01', '8623501261', 'ron@errol.com', '894569123587', '8, Burrow, Ottery St. Catchpole');
insert into customer(cust_name, vehicle_id, dob, phone, email, aadhar, address) values('Hermione Granger', 'V04', '1979-09-19', '9876543217', 'hermione@crooksh.com', '878455569812', '15, Hampstead, Heathgate');

create table service(service_num integer not null auto_increment primary key, vehicle_id varchar(10) references vehicle(vehicle_id), cust_id integer references customer(cust_id), date_given date, exp_del_date date, odo_read integer, next_ser_date date, emp_id integer references employee(emp_id));

insert into service values(100, 'V04', 3, '2018-11-02', '2018-11-05', 10000, '2019-02-02', 1001);
insert into service(vehicle_id, cust_id, date_given, exp_del_date, odo_read, next_ser_date, emp_id) values('V02', 2, '2018-10-31', '2018-11-03', 150000, '2019-01-31', 1002);

create table spare_parts(part_id varchar(5) primary key, part_name varchar(20),cost double, durability integer, quantity_avail integer);
insert into spare_parts values('P01', 'Engine Oil Filter', 1000.0, 6, 50);
insert into spare_parts values('P02','Air Filter', 500.0, 6, 50);
insert into spare_parts values('P03','Brake Fluid', 800, 6, 100);
insert into spare_parts values('P04','Engine Coolant', 950, 6, 50);
insert into spare_parts values('P05','Spark Plug', 550, 6, 150); 
use dbmsproject;
create table booking(booking_id integer not null auto_increment primary key, booked_date date, del_date date, vehicle_id varchar(10) references vehicle(vehicle_id), price double, cust_id integer references customer(cust_id));
 create table login_credentials(emp_id integer references employee(emp_id), passwordd varchar(20) not null, primary key(emp_id,passwordd));
 create table sales_info(vehicle_id varchar(10) references vehicle(vehicle_id),no_of_models_sold integer, total_sales double, primary key(vehicle_id));
 
 
 

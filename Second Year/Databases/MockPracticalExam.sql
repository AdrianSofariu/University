create table Chefs(
	chefId INT PRIMARY KEY,
	name VARCHAR(100),
	gender VARCHAR(1),
	birthdate DATE,
)

create table CakeTypes(
	typeId int primary key,
	name VARCHAR(100),
	description VARCHAR(200)
)

create table Cake(
	cakeId int primary key,
	name VARCHAR(100),
	shape VARCHAR(50),
	weight decimal(6,2),
	price decimal(6,2),
	typeId int foreign key references CakeTypes(typeId)
)

create table Specializations(
	chefId INT,
	cakeId INT,
	primary key (chefId, cakeId)
)

create table OrderEntries(
	orderId int,
	cakeCount int,
	cakeId int,
	primary key (orderId, cakeId)	
)


-- insert data
insert into Chefs values (1, 'John Doe', 'M', '1990-01-01'),
						 (2, 'Jane Doe', 'F', '1991-01-01'),
						 (3, 'Jack Doe', 'M', '1992-01-01'),
						 (4, 'Jill Doe', 'F', '1993-01-01')

insert into CakeTypes values (1, 'Chocolate', 'A cake made of chocolate'),
							 (2, 'Vanilla', 'A cake made of vanilla'),
							 (3, 'Strawberry', 'A cake made of strawberry'),
							 (4, 'Cheese', 'A cake made of cheese')

insert into Cake values (1, 'Chocolate Cake', 'Round', 1.5, 20.00, 1),
						(2, 'Vanilla Cake', 'Square', 2.0, 25.00, 2),
						(3, 'Strawberry Cake', 'Round', 1.0, 15.00, 3),
						(4, 'Cheese Cake', 'Square', 1.0, 30.00, 4)

insert into Specializations values (1, 1),
								  (2, 2),
								  (3, 3),
								  (4, 4),
								  (1, 3),
							      (2, 4)
insert into Specializations values (1,2), (1,4)

insert into OrderEntries values (1, 2, 1),
								(2, 3, 2),
								(3, 1, 3),
								(4, 1, 4)


-- create a procedure to add cakes to an order
go
create or alter procedure usp_addToOrder @orderId INT, @cakeName VARCHAR(100) , @p int as
begin

if @p < 1
return

--first check if cake exists
declare @cakeId int = (SELECT c.cakeId FROM Cake c WHERE @cakeName = c.name)

if @cakeId is null
return

--check if entry exists
declare @count int = (SELECT o.cakeCount FROM OrderEntries o WHERE o.orderId = @orderId and o.cakeId = @cakeId)

--if not, we create it
if @count is null
begin
	insert into OrderEntries values (@orderId, @p, @cakeId)
end
else
	update OrderEntries set cakeCount = @p where orderId = @orderId and cakeId = @cakeId 
end
go

select * from Cake
select * from OrderEntries

exec usp_addToOrder 1, 'Cheese Cake', 3;
exec usp_addToOrder 3, 'Strawberry Cake', 10;
exec usp_addToOrder 3, 'Strawberry Cake', -3;


-- create a function that shows all the chefs specialized in all cakes
go
create or alter function specialistChefs () 
returns @ChefNames table(
	name VARCHAR(100)
)
as
begin
declare @count int = (SELECT COUNT(*) FROM Cake)
insert into @ChefNames 
select c.name
from Chefs c
where @count = (SELECT COUNT(*) FROM Specializations s WHERE s.chefId = c.chefId)

return
end
go

select * from specialistChefs()






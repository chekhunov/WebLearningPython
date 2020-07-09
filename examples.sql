select * from polls_employer;
select * from polls_employer order by id limit 1;
select * from polls_employer order by age;
select * from polls_employer order by salary desc limit 1;
select * from polls_employer where first_name='ihor';
select * from polls_employer where first_name='ihor' order by joined_date;
select * from polls_employer where salary<100;
select * from polls_employer where salary>100 order by salary;


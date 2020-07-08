select * from polls_employer;
select * from polls_employer order by id limit 1;
select * from polls_employer order by age;
select * from polls_employer order by salary;
select * from polls_employer where first_name='ihor';
select * from polls_employer where first_name='ihor' and salary<100;
select * from polls_employer where first_name='ihor' and salary>100 order by salary desc;

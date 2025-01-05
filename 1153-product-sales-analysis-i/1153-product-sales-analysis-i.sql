# Write your MySQL query statement below
select a.product_name as product_name,
        b.year as year,
        b.price as price 
from sales as b inner join product as a ON a.product_id=b.product_id 
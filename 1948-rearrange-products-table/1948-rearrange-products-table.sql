# Write your MySQL query statement below
select product_id, "store1" as store,store1 as price from products where store1 IS NOT NULL
UNion all
select product_id, "store2" as store,store2 as price from products where store2 IS NOT NULL
Union all 
select product_id, "store3" as store,store3 as price from products where store3 IS NOT NULL
order by product_id asc
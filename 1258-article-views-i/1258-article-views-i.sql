# Write your MySQL query statement below
select Distinct(viewer_id) as id from views  where author_id=viewer_id group by article_id order by viewer_id Asc
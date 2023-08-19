# Write your MySQL query statement below
select request_at as Day, round(count(case when status <> 'completed' then id end)/count(id),2) as "Cancellation Rate"
from 
(
select id, A.client_id, B.banned as client_ban, A.driver_id, C.banned as driver_ban, status, request_at
from Trips A
left join
Users B
on A.client_id = B.users_id and B.role = 'client'
left join
Users C
on A.driver_id = C.users_id and C.role = 'driver') A where client_ban = 'No' and driver_ban ='No' and
(request_at between '2013-10-01' and '2013-10-03') group by Day order by Day;
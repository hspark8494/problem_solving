-- Q59412 입양 시각 구하기(1)
-- https://school.programmers.co.kr/learn/courses/30/lessons/59412?language=mysql
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR(DATETIME)) AS COUNT 
FROM ANIMAL_OUTS 
GROUP BY HOUR 
HAVING HOUR BETWEEN 9 AND 20
ORDER BY HOUR
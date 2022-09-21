-- Q59041 동명 동물 수 찾기
-- https://school.programmers.co.kr/learn/courses/30/lessons/59041
 SELECT NAME, COUNT(NAME) 
 FROM ANIMAL_INS 
 WHERE NAME IS NOT NULL 
 GROUP BY NAME 
 HAVING COUNT(NAME)>=2
 ORDER BY NAME
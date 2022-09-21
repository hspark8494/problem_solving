-- Q59040 고양이와 개는 몇 마리 있을까
-- https://school.programmers.co.kr/learn/courses/30/lessons/59040
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS Count FROM ANIMAL_INS WHERE ANIMAL_TYPE IN('Cat', 'Dog') GROUP BY ANIMAL_TYPE ORDER BY ANIMAL_TYPE
-- Q59409 중성화 여부 파악하기

-- https://school.programmers.co.kr/learn/courses/30/lessons/59409
SELECT ANIMAL_ID, NAME, IF(SEX_UPON_INTAKE LIKE 'Spayed%' OR SEX_UPON_INTAKE LIKE 'Neutered%', 'O', 'X') FROM ANIMAL_INS
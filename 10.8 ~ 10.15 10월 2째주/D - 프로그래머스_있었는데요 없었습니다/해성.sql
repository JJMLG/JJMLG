-- ORACLE 전통적 표기법
SELECT A.animal_id,
       B.name
FROM   animal_ins A,
       animal_outs B
WHERE  A.animal_id = B.animal_id(+)
       AND A.datetime > B.datetime
ORDER  BY A.datetime; 



-- ANSI SQL 표기법
SELECT A.ANIMAL_ID, B.NAME 
FROM ANIMAL_INS A
LEFT JOIN ANIMAL_OUTS B ON A.ANIMAL_ID = B.ANIMAL_ID
WHERE A.DATETIME > B.DATETIME 
ORDER BY A.DATETIME;

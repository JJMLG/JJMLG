SELECT A.animal_id,
       B.name
FROM   animal_ins A,
       animal_outs B
WHERE  A.animal_id = B.animal_id(+)
       AND A.datetime > B.datetime
ORDER  BY A.datetime; 
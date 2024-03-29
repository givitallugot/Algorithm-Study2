-- 없어진 기록 찾기
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS AS O LEFT JOIN ANIMAL_INS AS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE I.DATETIME IS NULL
ORDER BY O.ANIMAL_ID


-- 있었는데요 없었습니다
SELECT O.ANIMAL_ID, O.NAME
FROM ANIMAL_OUTS AS O LEFT JOIN ANIMAL_INS AS I ON O.ANIMAL_ID = I.ANIMAL_ID
WHERE O.DATETIME < I.DATETIME
ORDER BY I.DATETIME


-- 오랜 기간 보호한 동물(1)
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS AS I LEFT JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE O.DATETIME IS NULL
ORDER BY I.DATETIME
LIMIT 3

-- 보호소에서 중성화한 동물
SELECT I.ANIMAL_ID, I.ANIMAL_TYPE, I.NAME
FROM ANIMAL_INS AS I LEFT JOIN ANIMAL_OUTS AS O ON I.ANIMAL_ID = O.ANIMAL_ID
WHERE LEFT(I.SEX_UPON_INTAKE,6) = 'Intact' and LEFT(O.SEX_UPON_OUTCOME,6) != 'Intact'
ORDER BY I.ANIMAL_ID
-- 최솟값 구하기
SELECT MIN(DATETIME) AS 시간
FROM ANIMAL_INS

SELECT DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1

-- MS
SELECT TOP 1 DATETIME AS 시간
FROM ANIMAL_INS
ORDER BY DATETIME

-- 
SELECT COUNT(ANIMAL_ID) AS count
FROM ANIMAL_INS


-- 중복값 제거와 NULL이 아닌 경우의 수
SELECT COUNT(A.NAME) as count
FROM (SELECT DISTINCT NAME FROM ANIMAL_INS WHERE NAME IS NOT NULL) AS A


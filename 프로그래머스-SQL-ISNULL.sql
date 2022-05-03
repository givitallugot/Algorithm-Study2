-- 이름이 없는 동물의 아이디
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NULL

-- 이름이 있는 동물의 아이디
SELECT ANIMAL_ID
FROM ANIMAL_INS
WHERE NAME IS NOT NULL

-- NULL 처리하기
SELECT ANIMAL_TYPE, ISNULL(NAME,'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS

SELECT ANIMAL_TYPE, 
    CASE WHEN NAME IS NULL
        THEN 'No name'
        ELSE NAME
    END NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS


SELECT ANIMAL_TYPE, 
    CASE WHEN NAME IS NULL THEN 'No name' ELSE NAME
    END NAME,
    SEX_UPON_INTAKE
FROM ANIMAL_INS


SELECT ename, deptno 
    CASE WHEN detpno=10 THEN '경리팀' 
         WHEN detpno=20 THEN '연구팀' 
         WHEN detpno=30 then '총무팀' 
         WHEN detpno=40 then '연구팀' 
    END deptname
FROM sungjuk;

출처: https://ninearies.tistory.com/23 [초급의 끄적거림]


SELECT ANIMAL_TYPE, NVL(NAME, 'No name') AS NAME, SEX_UPON_INTAKE
FROM ANIMAL_INS
-- NVL은 오라클에서 NULL 값인 경우 특정값으로 출력하고 싶을 때 사용
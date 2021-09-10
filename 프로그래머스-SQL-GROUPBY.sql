-- 개와 고양이 수
SELECT ANIMAL_TYPE, COUNT(ANIMAL_TYPE) AS count
FROM ANIMAL_INS
WHERE ANIMAL_TYPE = 'Cat' or ANIMAL_TYPE = 'Dog'
GROUP BY ANIMAL_TYPE
ORDER BY ANIMAL_TYPE

-- 이름 중 두 번 이상 쓰인 이름과 해당 이름이 쓰인 횟수
SELECT NAME, COUNT(NAME) AS count
FROM ANIMAL_INS
GROUP BY NAME
HAVING count > 1
ORDER BY NAME

-- 
SELECT HOUR(DATETIME) AS hour, COUNT(ANIMAL_ID) AS count
FROM ANIMAL_OUTS
GROUP BY hour
HAVING hour BETWEEN 9 and 19
ORDER BY hour

-- 09:00부터 19:59까지, 각 시간대별로 입양이 몇 건이나 발생했는지
SELECT HOUR(DATETIME) AS hour, COUNT(ANIMAL_ID) AS count
FROM ANIMAL_OUTS
GROUP BY hour
HAVING hour BETWEEN 9 and 19
ORDER BY hour

-- 
with recursive time as
(select 0 as hour union all select hour+1 from time where hour<23)
select hour, count(animal_id) count
from time
left outer join animal_outs on (hour = date_format(datetime, '%H') )
group by hour;


-- WITH common_table_expression(Transact-SQL), CTE(공통 테이블 식)라고도 하는 임시로 이름이 지정된 결과 집합을 지정
-- 참고 코드
WITH RECURSIVE TIMETABLE(HOUR) AS (
    SELECT 0
    UNION
    SELECT TIMETABLE.HOUR + 1 FROM TIMETABLE WHERE TIMETABLE.HOUR < 23
)
SELECT HOUR, COUNT(A.ANIMAL_ID)
FROM TIMETABLE AS T LEFT JOIN ANIMAL_OUTS AS A ON T.HOUR = HOUR(A.DATETIME)
GROUP BY HOUR
ORDER BY HOUR


-- My 코드
WITH RECURSIVE TIME_RANGE(n) 
AS (
    SELECT 0
    UNION ALL
    SELECT n + 1
    FROM    
        TIME_RANGE
    WHERE n < 24
)
SELECT T.n AS hour, COUNT(A.ANIMAL_ID) AS count
FROM TIME_RANGE AS T LEFT JOIN ANIMAL_OUTS AS A ON T.n = HOUR(A.DATETIME)
GROUP BY hour
ORDER BY hour;
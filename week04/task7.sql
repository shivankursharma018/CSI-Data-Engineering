-- https://www.hackerrank.com/challenges/the-report/problem
SELECT IF(g.grade<8, NULL, s.name), g.grade, s.marks 
FROM students s JOIN grades g 
ON s.marks 
BETWEEN g.min_mark AND g.max_mark 
ORDER BY g.grade DESC, s.name;

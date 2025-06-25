-- https://www.hackerrank.com/challenges/african-cities/problem
SELECT city.name FROM city 
JOIN country ON city.countrycode = country.code 
WHERE LOWER(country.continent) LIKE 'africa';
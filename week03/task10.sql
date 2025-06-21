SELECT country.continent, FLOOR(AVG(city.population)) 
FROM city join country 
ON city.countrycode=country.code 
GROUP BY country.continent;
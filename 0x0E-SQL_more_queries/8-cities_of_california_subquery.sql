-- Retrieve the cities from the 'cities' table that belong to the state of California
-- by selecting the state_id from the 'states' table where the state name is 'California'
-- Results are sorted in ascending order by cities.id
SELECT id, name FROM cities WHERE state_id = (
  SELECT id
  FROM states
  WHERE name='California'
) ORDER BY id ASC;

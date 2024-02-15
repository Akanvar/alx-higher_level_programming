-- script that displays the max temperature of each state
-- order output by State name
SELECT `state`, MAX(`value`) AS `max_temp`
FROM `temperatures` GROUP BY `state`
ORDER BY `state` ASC;

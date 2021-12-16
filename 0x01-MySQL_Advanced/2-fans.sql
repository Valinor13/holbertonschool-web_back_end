-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
SELECT origin, SUM(fans) AS nb_fans FROM metal_bands GROUP BY origin ORDER BY nb_fans DESC;

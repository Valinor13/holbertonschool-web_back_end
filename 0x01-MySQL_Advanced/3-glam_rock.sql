-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
SELECT band_name, IFNULL(split, 2020) - formed AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style)
ORDER BY lifespan DESC;

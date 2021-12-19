-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
DELIMITER //
CREATE FUNCTION SafeDiv (
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END
//
DELIMITER ;

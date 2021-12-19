-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser (
    IN user_id INT
)
BEGIN
    DECLARE zum FLOAT;
    DECLARE divisor INT;
    DECLARE mean FLOAT;
    SELECT SUM(score) INTO zum FROM corrections WHERE corrections.user_id = user_id;
    SELECT COUNT(project_id) INTO divisor FROM corrections WHERE corrections.user_id = user_id;
    SET mean = zum / divisor;
    UPDATE users SET average_score = mean WHERE id = user_id;
END
//
DELIMITER ;
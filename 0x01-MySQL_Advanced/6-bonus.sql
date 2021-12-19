-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
DELIMITER //

CREATE PROCEDURE AddBonus
(
    IN user_id INT, IN project_name VARCHAR(255), IN score INT
)
BEGIN
    INSERT INGORE INTO projects (name)
    VALUES (project_name);
    SET @project_id := (
        SELECT id
        FROM projects
        WHERE name = project_name;
    )
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, project_id, score);
END;
//
DELIMITER ;

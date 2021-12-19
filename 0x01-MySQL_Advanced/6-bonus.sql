-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
DELIMITER //

CREATE PROCEDURE AddBonus
(
    IN id INT, IN project_name VARCHAR(255), IN score INT
)
BEGIN
    SET @project_id := (
        SELECT id
        FROM projects
        WHERE name = project_name;
    IF project_id IS NULL THEN
        INSERT INTO projects (name)
        VALUES (project_name)
    END IF;
    SET @project_id := (
        SELECT id
        FROM projects
        WHERE name = project_name;
    )
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (id, project_id, score)
END;
//
DELIMITER ;

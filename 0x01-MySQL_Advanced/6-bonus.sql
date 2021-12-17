-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
DELIMITER //

CREATE PROCEDURE AddBonus
(
    IN id INT, IN project_name VARCHAR(255), IN score INT
)
BEGIN
    INSERT IGNORE INTO projects (name)
    VALUES (project_name);
    SELECT id AS project_id
    FROM projects
    WHERE name = project_name;
    INSERT IGNORE INTO corrections (user_id, project_id)
    VALUES (id, project_id);
    UPDATE corrections
    SET score = score
    WHERE project_id = project_id;
END;
//
DELIMITER ;

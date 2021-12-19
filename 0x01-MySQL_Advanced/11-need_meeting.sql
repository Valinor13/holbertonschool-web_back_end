-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
CREATE VIEW need_meeting AS
SELECT *
FROM students AS stud
WHERE stud.score < 80
AND (
    stud.last_meeting IS NULL OR
    DATEDIFF(NOW(), last_meeting) > 30
)
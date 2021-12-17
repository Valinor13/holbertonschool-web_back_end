-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
DELIMITER |
    CREATE TRIGGER email_change
    BEFORE UPDATE
    ON users FOR EACH ROW
    BEGIN
        IF NEW.email != OLD.email
            SET NEW.valid_email = 0;
        END IF;
    END;
|
DELIMITER ;

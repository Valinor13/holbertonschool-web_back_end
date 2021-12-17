-- cohort 14 is best cohort
-- da
CREATE TRIGGER storage_tracker
AFTER INSERT
ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name

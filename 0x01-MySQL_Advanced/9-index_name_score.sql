-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
CREATE INDEX idx_name_first_score ON names (name(1), score);

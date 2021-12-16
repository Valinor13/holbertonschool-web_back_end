-- 6 first students in the Batch ID=14a
-- because Batch 14a is the best!
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255) DEFAULT NULL,
    country ENUM('US', 'CO', 'TN') NOT NULL,
    PRIMARY KEY(id)
    );

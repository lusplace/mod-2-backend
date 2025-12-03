CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    mail VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    user_disabled BOOLEAN NOT NULL DEFAULT 1
    );


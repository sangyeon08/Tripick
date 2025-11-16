-- Tripick Users Database
-- Last Updated: 2025-11-17 01:27:25

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- Clear existing data
DELETE FROM users;

-- User Data
INSERT INTO users (username, password, created_at) VALUES ('admin', '0ffe1abd1a08215353c233d6e009613e95eec4253832a761af28ff37ac5a150c', '2025-11-17 01:27:25');

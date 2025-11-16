-- Tripick Users Database
-- Last Updated: 2025-11-17

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL,
    created_at TEXT NOT NULL
);

-- Clear existing data
DELETE FROM users;

-- User Data
INSERT INTO users (username, password, created_at) VALUES ('자고 싶어요', '1111', '2025-11-17');

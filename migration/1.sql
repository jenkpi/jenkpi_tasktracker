CREATE TABLE tasks (
    task_id INTEGER PRIMARY KEY,
    task VARCHAR(50) NOT NULL,
    description VARCHAR(100) NULL,
    user_id INTEGER NOT NULL,
    status VARCHAR(20) NOT NULL,
    deadline TIMESTAMPTZ NULL);
DROP TABLE IF EXISTS suggestions;

CREATE TABLE suggestions (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    lat REAL NOT NULL,
    long REAL NOT NULL,
    state TEXT,
    country TEXT NOT NULL
);

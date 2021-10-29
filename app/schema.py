instructions = [
    'DROP TABLE IF EXISTS contacts;',
    """
        CREATE TABLE contacts (
            id INT PRIMARY KEY AUTO_INCREMENT,
            company TEXT NOT NULL,
            role TEXT NOT NULL,
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            mail TEXT NOT NULL,
            phone TEXT NOT NULL
        )
    """,
]
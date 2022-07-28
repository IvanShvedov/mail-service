"""

"""

from yoyo import step

__depends__ = {}

steps = [
    step('''
        CREATE TABLE mailing
        (id SERIAL,
        start_time TIMESTAMP,
        message TEXT,
        filter TEXT,
        end_time TIMESTAMP,
        PRIMARY KEY(id))''',
        "DROP TABLE mailing"
    ),
    step('''
        CREATE TABLE clients
        (id SERIAL,
        phone TEXT,
        code TEXT,
        tag TEXT,
        timezone TEXT,
        PRIMARY KEY(id))
    ''',
    "DROP TABLE clients"),
    step('''
        CREATE TABLE messanges
        (id SERIAL,
        created_at TIMESTAMPTZ,
        status TEXT,
        mailing_id INT,
        client_id INT,
        PRIMARY KEY(id),
        FOREIGN KEY(client_id) REFERENCES clients(id) ON DELETE CASCADE,
        FOREIGN KEY(mailing_id) REFERENCES mailing(id) ON DELETE CASCADE)''',
        "DROP TABLE messanges"
    ),
]

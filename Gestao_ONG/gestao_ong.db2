CREATE TABLE voluntarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    contato TEXT NOT NULL,
    disponibilidade TEXT NOT NULL
);

CREATE TABLE doacoes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT NOT NULL,
    valor REAL NOT NULL,
    doador TEXT NOT NULL,
    finalidade TEXT NOT NULL
);

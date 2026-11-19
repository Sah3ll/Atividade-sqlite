import sqlite3

biblioteca = sqlite3.connect('biblioteca.db')
cursor = biblioteca.cursor()

print('Banco conectado!')

cursor.execute("""
CREATE TABLE IF NOT EXISTS livros (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT,
    ano INTEGER,
    disponivel INTEGER CHECK (disponivel IN (0,1))
    ) 
""")

cursor.execute("DELETE FROM livros")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='livros'")
cursor.execute("INSERT INTO livros(titulo, autor, ano, disponivel) VALUES ('A cabeça do santo','Socorro Acioli', 2014, 1)")
cursor.execute("INSERT INTO livros(titulo, autor, ano, disponivel) VALUES ('Olhos dágua','Conceição Evaristo', 2014, 1)")
cursor.execute("INSERT INTO livros(titulo, autor, ano, disponivel) VALUES ('Vidas secas','Graciliano Ramos', 1938, 1)")
cursor.execute("INSERT INTO livros(titulo, autor, ano, disponivel) VALUES ('Quarto de despejo','Carolina Maria de Jesus', 1960, 1)")
cursor.execute("INSERT INTO livros(titulo, autor, ano, disponivel) VALUES ('O peso do passaro morto','Aline Bei', 2017, 1)")
biblioteca.commit()
print("Livros adicionados com sucesso!")

print("Todos:", cursor.execute("SELECT * FROM livros").fetchall())

cursor.execute("UPDATE livros SET disponivel = 0 WHERE id = 1")
biblioteca.commit()

print("Disponiveis:", cursor.execute("SELECT * FROM livros WHERE disponivel = 1").fetchall())
biblioteca.commit()

cursor.execute("DELETE FROM livros WHERE id = 2")
biblioteca.commit()

print("Pós 2000:", cursor.execute("SELECT * FROM livros WHERE ano > 2000").fetchall())
biblioteca.commit()

biblioteca.close()

import sqlite3

lanchonete = sqlite3.connect('lanchonete.db')
cursor = lanchonete.cursor()

print('Banco conectado!')

cursor.execute("""
CREATE TABLE IF NOT EXISTS cardapio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT NOT NULL,
    categoria TEXT,
    preco REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedido (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    item TEXT,
    quantidade INTEGER
)
""")

cursor.execute("DELETE FROM cardapio")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='cardapio'")
cursor.execute("INSERT INTO cardapio (item, categoria, preco) VALUES ('Eggburguer', 'Artesanal',26.99)")
cursor.execute("INSERT INTO cardapio (item, categoria, preco) VALUES ('Misto', 'Simples', 8.99)")
cursor.execute("INSERT INTO cardapio (item, categoria, preco) VALUES ('Hamburguer duplo cheddar', 'Artesanal', 32.99)")
cursor.execute("INSERT INTO cardapio (item, categoria, preco) VALUES ('Hamburguer insano', 'Artesanal', 30.99)")
cursor.execute("INSERT INTO cardapio (item, categoria, preco) VALUES ('Bauru', 'Simples', 12.99)")
cursor.execute("INSERT INTO cardapio (item, categoria, preco) VALUES ('Gauchão', 'Mega', 38.99)")
lanchonete.commit()
print("Itens do cardapio adicionados!")

cursor.execute("DELETE FROM pedido")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='pedido'")
cursor.execute("INSERT INTO pedido (cliente, item, quantidade) VALUES ()")
cursor.execute
cursor.execute
cursor.execute



print("Todos:", cursor.execute("SELECT * FROM cardapio").fetchall())


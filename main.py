import sqlite3

# Connect to the SQLite database (it will be created if it does not exist)
conn = sqlite3.connect('my_graph.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a table for edges in the graph
cursor.execute('''DROP TABLE IF EXISTS E''')
cursor.execute('''CREATE TABLE IF NOT EXISTS E (
                  i INT,
                  j INT)''')

# Insert some edges into the table (replace this with your actual data)
edges = [(1, 2), (1, 4), (1, 5), (1, 7), (1, 11),
         (2, 1), (2, 3), (2, 6), (2, 7), (2, 11),
         (3, 2), (3, 6), (3, 7), (3, 8), (3, 9),
         (4, 1), (4, 7),
         (5, 1), (5, 11),
         (6, 2), (6, 3), (6, 8), (6, 10), (6, 11),
         (7, 1), (7, 2), (7, 3), (7, 4),
         (8, 3), (8, 6), (8, 9), (8, 10),
         (9, 3), (9, 8),
         (10, 6), (10, 8),
         (11, 1), (11, 2), (11, 5), (11, 6)]
cursor.executemany('INSERT INTO E VALUES (?, ?)', edges)

# Commit the transaction
conn.commit()

# Query for triangle enumeration
cursor.execute('''
SELECT E1.i AS v1, E1.j AS v2, E2.j AS v3
FROM
E E1 JOIN E E2 ON E1.j=E2.i
JOIN E E3 ON E2.j=E3.i
WHERE E1.i<E1.j AND E2.i<E2.j AND E3.j=E1.i;
''')

# Fetch and print all the results
triangles = cursor.fetchall()
for triangle in triangles:
  print(triangle)

# Close the connection
conn.close()

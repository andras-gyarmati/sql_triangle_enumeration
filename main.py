import sqlite3

# Connect to the SQLite database (it will be created if it does not exist)
conn = sqlite3.connect('my_graph.db')

# Create a cursor object using the cursor() method
cursor = conn.cursor()

# Create a table for edges in the graph
cursor.execute('''CREATE TABLE IF NOT EXISTS edges (
                  node1 INT,
                  node2 INT)''')

# Insert some edges into the table (replace this with your actual data)
cursor.execute('INSERT INTO edges VALUES (1, 2)')
cursor.execute('INSERT INTO edges VALUES (2, 3)')
cursor.execute('INSERT INTO edges VALUES (3, 1)')

# Commit the transaction
conn.commit()

# Query for triangle enumeration (this is a simple example; replace with your optimized query)
cursor.execute('''
SELECT a.node1, a.node2, b.node2 
FROM edges a 
JOIN edges b ON a.node2 = b.node1 
JOIN edges c ON b.node2 = c.node1 
WHERE a.node1 = c.node2
''')

# Fetch and print all the results
triangles = cursor.fetchall()
for triangle in triangles:
    print(triangle)

# Close the connection
conn.close()

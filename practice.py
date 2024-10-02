# Practice Session
# Exercise 1
# Import sqlite3
# Import display from visualizer.py
# Connect to the Chinook database and get a cursor
# Use an aggregate function inside a SELECT query to count the number of albums on the tracks table
# Pass the output to display, run this file in the terminal, and check your results

import sqlite3
from visualizer import display

conn = sqlite3.connect('chinook.db')
cur = conn.cursor()

cur.execute("SELECT COUNT(DISTINCT AlbumId) FROM tracks;")
display(cur)

# Exercise 2
# Use an aggregate function inside a SELECT query to find the average song length
# Convert milliseconds to minutes using the / operator like this:
# Milliseconds/60000
# Pass the output to display, run this file in the terminal, and check your results

cur.execute("SELECT AVG(Milliseconds / 60000.0) AS 'Average Length (Minutes)' FROM tracks;")
display(cur)

# Exercise 3
# Use an aggregate function inside a SELECT query to find the most expensive song in tracks
# Pass the output to display, run this file in the terminal, and check your results

cur.execute("SELECT MAX(UnitPrice) AS 'Most Expensive Song' FROM tracks;")
display(cur)

# Exercise 4
# Use the GROUP BY clause to count the number of albums per genre on the tracks table
# Execute the query, call display, run the file, and check output

cur.execute("SELECT GenreId, COUNT(AlbumId) AS 'Albums per Genre' FROM tracks GROUP BY GenreId;")
display(cur)

# Exercise 5
# Create a SELECT query to count the number of albums per artist 
# in the albums table
# Execute the query and pass results to the display function

cur.execute("SELECT ArtistId, COUNT(AlbumId) AS 'Albums per Artist' FROM albums GROUP BY ArtistId;")
display(cur)

# Exercise 6
# Recreate the above query to show the artist's name as well
# You will need to select from both the albums and artists tables, and use a WHERE clause
# Execute the query and pass results to the display function

cur.execute("""
SELECT artists.Name, COUNT(albums.AlbumId) AS 'Albums per Artist' 
FROM albums, artists 
WHERE albums.ArtistId = artists.ArtistId 
GROUP BY artists.Name;
""")
display(cur)

# Exercise 7 - advanced students
# Run the above query using a JOIN instead of the WHERE clause

cur.execute("""
SELECT artists.Name, COUNT(albums.AlbumId) AS 'Albums per Artist' 
FROM albums 
JOIN artists ON albums.ArtistId = artists.ArtistId 
GROUP BY artists.Name;
""")
display(cur)

# Exercise 8
# Check to make certain all of your queries worked
# Add a method to close the connection to the database

conn.commit()
conn.close()

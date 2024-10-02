# We will be working with a very large database called Chinook
# It is a public database created specifically for students to practice SQL queries
# It is was built for a pretend streaming service application like Spotify or ITunes

# Tables on chinook.db:
# albums          employees       invoices        playlists     
# artists         genres          media_types     tracks        
# customers       invoice_items   playlist_track

# Exercise 1 
#
# Import sqlite3
# Import the display function from visualizer.py
# Create/Connect to the chinook.db database
# Get a cursor so you can write queries to the database
# Create a SELECT query to get 50 rows from the tracks table
# Execute the query, pass the results to the display function, 
# Run this file in terminal, and check the output



# Exercise 2
# Write a SELECT query to the tracks table 
# Use COUNT() on the TrackId column
# Execute the query and pass the results to display() 
# Run the file in terminal, and check your output
# Part 2: Edit the query using the AS keyword to change the column name to "Total Songs"
# Run the file in terminal, and check your output



# Exercise 3
# Create a SELECT query to show the values in the Composer column 
# without repeating them, 
# use AS to change the column heading to "Composers"
# Execute the query, call display, run the file, and check output
# Part 2: Edit the SELECT query to count the number of composers
# Run the file again, and check output




# Exercise 4: Count the number of albums per genre on the tracks table
# Write a SELECT query to get the GenreId, and COUNT(TrackId) columns 
# from tracks, GROUP BY GenreId
# Execute the query, call display, run the file, and check output
# Part 2: Edit the SELECT query to add Name AS "Example song"
# Run the file again, and check output




# Exercise 5
# Create a SELECT query to retrieve: 
# GenreId column on tracks table,
# Name column on genres table AS "Genre Name",  
# Name column on tracks table AS "Example song"
# COUNT TrackId on tracks table AS "Number of songs in genre"
# GROUP BY tracks.GenreId, execute and pass results to display()



# Exercise 6
# Copy, paste, and edit the last SELECT query to add a WHERE condition setting genres.GenreId equal to tracks.GenreId
# Run the file again and check output



# Bonus
# Copy, paste and edit the last query
# Convert it into a more modern form using a JOIN clause
# View the slides for JOIN clause construction
# Run the file again and check output
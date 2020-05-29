import csv

filename = "1\3\2.csv"
header = ("Rank", "Rating", "Title")
data = [
(1, 9.2, "The Shawshank Redemption(1994)"),
(2, 9.2, "The Godfather(1972)"),
(3, 9, "The Godfather: Part II(1974)"),
(4, 8.9, "Pulp Fiction(1994)")
]

def writer(header, data, filename):
      with open (filename, "w", newline = "") as csvfile:
        movies = csv.writer(csvfile)
        movies.writerow(header)
        for x in data:
          movies.writerow(x)
writer(header, data, filename)
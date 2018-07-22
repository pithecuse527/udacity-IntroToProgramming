
import media
import fresh_tomatoes

Twilight = media.Movie("Twilight",
                        "A story of vampire and a young girl",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/b/b6/Twilight_%282008_film%29_poster.jpg/220px-Twilight_%282008_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=uxjNDE2fMjI")


LaLaLand = media.Movie("La La Land",
                     "A story of jazz and love",
                     "https://upload.wikimedia.org/wikipedia/en/a/ab/La_La_Land_%28film%29.png",
                     "https://www.youtube.com/watch?v=0pdqf4P9MB8")


school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=3PsUJFEBC74")

Edge_of_tomorrow = media.Movie("Edge of tomorrow",
                          "A story of officer who fights with the alien",
                          "https://upload.wikimedia.org/wikipedia/en/f/f9/Edge_of_Tomorrow_Poster.jpg",
                          "https://www.youtube.com/watch?v=vw61gCe2oqI")

Avengers = media.Movie("Avengers",
				"A story of MARVEL heroes",
				"https://upload.wikimedia.org/wikipedia/en/thumb/f/f9/TheAvengers2012Poster.jpg/220px-TheAvengers2012Poster.jpg",
				"https://www.youtube.com/watch?v=eOrNdBpGMv8")

Captain_America = media.Movie("Captain America",
                           "A story of captain america",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/9/91/CaptainAmerica109.jpg/250px-CaptainAmerica109.jpg",
                           "https://www.youtube.com/watch?v=JerVrbLldXw")

movies = [Twilight, LaLaLand, school_of_rock, Edge_of_tomorrow, Avengers, Captain_America]

fresh_tomatoes.open_movies_page(movies)

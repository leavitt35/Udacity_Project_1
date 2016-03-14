import fresh_tomatoes  # Function to create and style webpage from objects

import media  # Function with Class Movie

# Creates Movie Objects which follow the following form:
# (title,
# storyline,
# poster_image_url,
# trailer_youtube_url,
# director,
# release_year)

the_hobbit_3 = media.Movie("The Hobbit: The Battle of the Five Armies",
                           "Bilbo and Company are forced to engage in a war"
                           " against an array of combatants and keep the"
                           " Lonely Mountain from falling into the hands of a"
                           " rising darkness",
                           "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",   # NOQA
                           "https://www.youtube.com/watch?v=YQt1OzQRV68",
                           "Peter Jackson",
                           "2014")

war_room = media.Movie("War Room",
                       "A seemingly perfect family looks to fix their"
                       " problems with the help of Miss Clara, an older,"
                       " wiser woman",
                       "https://upload.wikimedia.org/wikipedia/en/a/a7/WarRoomMoviePoster.jpg",   # NOQA
                       "https://www.youtube.com/watch?v=mIl-XY9t_Lw",
                       "Alex Kindrick",
                       "2015")

kung_fu_3 = media.Movie("Kung Fu Panda 3",
                        "Continuing his legendary adventures of awesomeness,"
                        " Po must face two hugely epic, but different"
                        " threats: one supernatural and the other a little"
                        " closer to his home",
                        "https://upload.wikimedia.org/wikipedia/en/e/e6/Kung_Fu_Panda_3_poster.jpg",   # NOQA
                        "https://www.youtube.com/watch?v=10r9ozshGVE",
                        "Jennifer Yuh",
                        "2016")

dark_knight = media.Movie("The Dark Knight",
                          "When the menace known as the Joker wreaks havoc"
                          " and chaos on the people of Gotham, the caped"
                          " crusader must come to terms with one of the"
                          " greatest psychological tests of his ability"
                          " to fight injustice",
                          "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",   # NOQA
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q",
                          "Christopher Nolan",
                          "2008")

x_men = media.Movie("X-Men: Days of Future Past",
                    "The X-Men send Wolverine to the past in a desperate"
                    " effort to change history and prevent an event that"
                    " results in doom for both humans and mutants",
                    "https://upload.wikimedia.org/wikipedia/en/0/0c/X-Men_Days_of_Future_Past_poster.jpg",   # NOQA
                    "https://www.youtube.com/watch?v=pK2zYHWDZKo",
                    "Bryan Singer",
                    "2014")

the_avengers = media.Movie("The Avengers",
                           "Earth's mightiest heroes must come together and"
                           " learn to fight as a team if they are to stop"
                           " the mischievous Loki and his alien army from "
                           " enslaving humanity",
                           "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",   # NOQA
                           "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                           "Josh Whedon",
                           "2012")


movies = [the_avengers, the_hobbit_3, dark_knight, war_room, x_men, kung_fu_3]
# Groups Movie objects into a list
fresh_tomatoes.open_movies_page(movies)
# Uses movie list as input to generate an HTML file and open it in the browser

import fresh_tomatoes
import media

fault_in_our_stars = media.Movie(
    "Fault in our stars",
    "Hazel Grace Lancaster meets and falls in love with Augustus Waters",
    "C:\Python27\exercise\movie_trailer\The_Fault_in_Our_Stars.jpg",
    "https://www.youtube.com/watch?v=9ItBvH5J6ss"
    )

kung_fu_panda = media.Movie(
    "The Kung fu Panda",
    "Panda and his friends are great warriors",
    "C:\Python27\exercise\movie_trailer\kung_fu_panda.jpg",
    "https://www.youtube.com/watch?v=10r9ozshGVE"
    )

storks = media.Movie(
    "STORKS",
    "Storks is an entertaining family film",
    "C:\Python27\exercise\movie_trailer\storks.jpg",
    "https://www.youtube.com/watch?v=ZVzL94jZNdU"
    )

school_of_rock = media.Movie(
    "School of Rock",
    "Overly enthusiastic guitarist gets thrown out"
    "of his bar band and finds himself",
    "C:\Python27\exercise\movie_trailer\School_of_Rock.jpg",
    "https://www.youtube.com/watch?v=3PsUJFEBC74"
    )

captain_america_civil_war = media.Movie(
    "Captain America CIVIL WAR",
    "Civil War between Avengers, earths mightiest heroes",
    "C:\Python27\exercise\movie_trailer\captain_america_civil_war.jpg",
    "https://www.youtube.com/watch?v=uVdV-lxRPFo"
    )

midnight_in_paris = media.Movie(
    "Midnight in Paris",
    "A romantic love track movie",
    "C:\Python27\exercise\movie_trailer\midnight_in_paris.jpg",
    "https://www.youtube.com/watch?v=BYRWfS2s2v4"
    )

doctor_strange = media.Movie(
    "Doctor Strange",
    "Doctor Strange is an upcoming American superhero film"
    "featuring the Marvel Comics character",
    "C:\Python27\exercise\movie_trailer\doctor_strange.jpg",
    "https://www.youtube.com/watch?v=HSzx-zryEgM"
    )

wonder_woman = media.Movie(
    "Wonder woman",
    "An Amazonian princess leaves her island home to explore the world",
    "C:\Python27\exercise\movie_trailer\wonder_woman.jpg",
    "https://www.youtube.com/watch?v=T6DJcgm3wNY"
    )

madagascar = media.Movie(
    "Madagascar",
    "A story of 4 animal best friends.",
    "C:\Python27\exercise\movie_trailer\madagascar.jpg",
    "https://www.youtube.com/watch?v=_FvCgabQVjA"
    )

movies = [fault_in_our_stars, storks, midnight_in_paris, doctor_strange,
          wonder_woman, madagascar, kung_fu_panda, school_of_rock, 
          captain_america_civil_war
          ]
print(media.Movie.__bases__)
fresh_tomatoes.create_movie_tiles_content(movies)
fresh_tomatoes.open_movies_page(movies)

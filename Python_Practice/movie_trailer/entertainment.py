import fresh_tomatoes
import media

fault_in_our_stars = media.Movie("Fault in our stars",
                                 "Hazel Grace Lancaster meets and falls in love with Augustus Waters",
                                 "C:\Python27\exercise\movie_trailer\The_Fault_in_Our_Stars.jpg",
                                 "https://www.youtube.com/watch?v=9ItBvH5J6ss")

kung_fu_panda = media.Movie("The Kung fu Panda",
                     "Panda and his friends are great warriors",
                     "C:\Python27\exercise\movie_trailer\kung_fu_panda.jpg",
                       "https://www.youtube.com/watch?v=10r9ozshGVE")

storks = media.Movie("STORKS",
                     "Storks is an entertaining family film",
                     "C:\Python27\exercise\movie_trailer\storks.jpg",
                     "https://www.youtube.com/watch?v=ZVzL94jZNdU")

school_of_rock = media.Movie("School of Rock",
                     "Overly enthusiastic guitarist gets thrown out of his bar band and finds himself",
                     "C:\Python27\exercise\movie_trailer\School_of_Rock.jpg",
                     "https://www.youtube.com/watch?v=3PsUJFEBC74")

captain_america_civil_war = media.Movie("CIVIL WAR",
                     "War between Avengers",
                     "C:\Python27\exercise\movie_trailer\captain_america_civil_war.jpg",
                     "https://www.youtube.com/watch?v=uVdV-lxRPFo")

midnight_in_paris = media.Movie("Midnight in Paris",
                     "A romantic love track movie",
                     "C:\Python27\exercise\movie_trailer\midnight_in_paris.jpg",
                     "https://www.youtube.com/watch?v=BYRWfS2s2v4")

#print(revenant.description)
#revenant.show_trailer()
#storks.show_trailer()
#print(fault_in_our_stars.description)

# Create an array movie, that is input paramaeter to the method open_movies_page()
movies = [fault_in_our_stars, captain_america_civil_war, kung_fu_panda, storks, school_of_rock, midnight_in_paris]
#fresh_tomatoes.open_movies_page(movies)
#print(media.Movie.VALID_RATINGS)
print(media.Movie.__bases__)

import media
import fresh_tomatoes


#an instance of class Movie
toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

print(toy_story.storyline)
#toy_story.show_trailer()

#an instance of class Movie
avatar = media.Movie("Avatar",
                     "A marine on an alient planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=XtEcU3tkZBc")
print(avatar.storyline)
#avatar.show_trailer()


#an instance of class Movie
school_of_rock = media.Movie("School of Rock", "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")
print(school_of_rock.storyline)
#school_of_rock.show_trailer()


#an instance of class Movie
ratatouille = media.Movie("Ratatouille", "A rat is a chef in paris",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")
print(ratatouille.storyline)
#ratatouille.show_trailer()


#an instance of class Movie
midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                                "https://www.youtube.com/watch?v=FAfR8omt-CY")
print(midnight_in_paris.storyline)
#midnight_in_paris.show_trailer()


#an instance of class Movie
hunger_games = media.Movie("Hunger Games","A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
                           "https://www.youtube.com/watch?v=4S9a5V9ODuY")
print(hunger_games.storyline)
#hunger_games.show_trailer()


# an array of list of names of movies
movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]


#calling open_movies_page from fresh_tomatoes
fresh_tomatoes.open_movies_page(movies)

print(media.Movie.__doc__)



import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "images/Toy_Story.jpg",
                        "By From impawards., https://en.wikipedia.org/w/index.php?curid=26009601",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "images/Avatar-Teaser-Poster.jpg",
                     "By Source, Fair use, https://en.wikipedia.org/w/index.php?curid=23732044",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8")

batman = media.Movie("The Lego Batman Movie",
                     "A cooler-than-ever Bruce Wayne must deal with the usual suspects as they plan to rule Gotham City, while discovering that he has accidentally adopted a teenage orphan who wishes to become his sidekick.",
                     "images/The_Lego_Batman_Movie_PromotionalPoster.jpg",
                     "By Source, Fair use, https://en.wikipedia.org/w/index.php?curid=49903959",
                     "https://www.youtube.com/watch?v=rGQUKzSDhrg")

movies = [toy_story, avatar, batman]

fresh_tomatoes.open_movies_page(movies)


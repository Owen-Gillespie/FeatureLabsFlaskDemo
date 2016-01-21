# FeatureLabsFlaskDemo
Creating a test application with Flask and React

Run from cmd from within the repo with Flask/Scripts/python run.py or the equivalent for other OS's to use the copy of python from virtualenv.

The database will add all the words it encounters in new comments.  New words have never been seen before.  Unique words are if they have only been used before in the database by this user.  Top words are calculated based on an algorithm that compares the frequency the user uses each word with the general reddit population based on other users that have been scraped and added to the database.  For example u/poem_for_your_sprog has a very high rating on the word rhyme.

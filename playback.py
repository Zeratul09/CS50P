# This code was made while learning Python by classroom course and by practicing coding in VSC.
# The name of the classroom course is: Harvard's CS50’s Introduction to Programming with Python.

# The purpose of this code is to replicate a 0.75 playback speed text to speech with putting
# "..." between every word format similar how it would look like when you play a Youtube video with 0.75 speed.

#User enters the text that we want to "slowdown"
text = input("What...is...it...that...you...want...to...say? ")

#Text formatting by replacing each space with "..." and removing all whitespace before and after the string.
text = text.replace(" ", "...").strip()

#Sloweddown text gets printed
print(text)
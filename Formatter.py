# -*- coding: utf-8 -*-
#a formatter

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % (True, False, True, False)
print formatter % ("eeny", "meeny", "miney", "mo")
print formatter % ("Forget", "about", "it", "!")
print formatter % ("Tempus", "fugit", "Tempus", "fugit.")

print ""
print "---Escape Cats---"
print ""

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\on a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

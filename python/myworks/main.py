#!/usr/bin/python

# Open a file
fo = open("foo.txt", "rw+")
print "Name of the file: ", fo.name

# Assuming file has following 5 lines
# This is 1st line
# This is 2nd line
# This is 3rd line
# This is 4th line
# This is 5th line

line = fo.readlines()
print "Read Line: %s" % (line)

line = fo.readlines(2)
print "Read Line: %s" % (line)

# Close opend file
fo.close()

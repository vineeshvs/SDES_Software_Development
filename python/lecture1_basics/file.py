#!/usr/bin/python

import sys

try:
  # open file stream
  file = open(test, "w")
except IOError:
  print "There was an error writing to", text
  sys.exit()
print "Enter '", file_finish,
print "' When finished"

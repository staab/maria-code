import sys
import os

if len(sys.argv) < 2:
    print "Please include a template to knit."
    sys.exit(1)

if sys.argv[1] == 'list':
    print "Available templates:\n"
    print "\n".join(os.listdir('./templates'))
    sys.exit(0)

try:
    with open("./templates/%s" % sys.argv[1], 'r') as f:
        template = f.read()
except IOError:
    print "That template doesn't exist."
    sys.exit(1)

lines = template.split('\n')

for x in range(5):
    for line in lines:
        print line * 5


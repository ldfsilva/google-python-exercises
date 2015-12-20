#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""


def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    name_list = []
    # regex to capture the year in the text file
    regex1 = 'name="year".*value="([0-9]+)">'
    # regex to capture rank, male and female names
    regex2 = '<td>([0-9]+)</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>'
    # iterate over the given files
    for file in filename:
        baby_names = []
        with open(file, 'r') as fp:
            text = fp.read()

            year = re.search(regex1, text)
            year = year.group(1)
            # In case year is found proceed otherwise the pattern may incorrect
            # it's better to abort
            if year:
                baby_names.append(year)
            else:
                assert "Unable to find year on file - different pattern"
            # Hunt for the names and append to the list
            for line in text.splitlines():
                name = re.search(regex2, line)
                if name:
                    rank = name.group(1)
                    male_name = name.group(2)
                    female_name = name.group(3)

                    baby_names.append('{} {}'.format(male_name, rank))
                    baby_names.append('{} {}'.format(female_name, rank))

        fp.close()

        baby_names.sort()

        name_list.append(baby_names)

    return name_list


def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print('usage: [--summaryfile] file [file ...]')
        sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]
        # Print each one of the list returned by extract_names function
        for name_list in extract_names(args):
            print(name_list)


if __name__ == '__main__':
    main()

#! /usr/bin/env python3

"A script for calculating the area of a rectangle."

import sys


def area_of_rectangle(height, width = None):
    """
    Returns the area of a rectangle.

    Parameters
    ----------
    height : int or float 
        The height of the rectangle.
    width : int or float
        The width of the rectangle. If `None` width is assumed to be equal to 
        the height.

    Returns
    -------
    int or float
        The area of the rectangle

    Examples
    --------
    >>> area_of_rectangle(7)
    49
    >>> area_of_rectangle (7, 2)
    14
    """

    #I added "is None" to the following line, which allows for the calculation of a square or rectangle by first checking if width is given and then moving to the line "width = height" if it is not. "Width" alone would not be enough to accomplish this task.
    if width is None:
        width = height
    area = height * width
    return area

if __name__ == '__main__':
    if (len(sys.argv) < 2) or (len(sys.argv) > 3):
        message = (
            #these lines were not correctly indented
            "{script_name}: Expecting one or two command-line arguments:\n"
            "\tthe height of a square or the height and width of a "
            "rectangle".format(script_name = sys.argv[0]))
        sys.exit(message)
    #to address the error from the first test, I turned the height and width variables into integers as they were previously defined as strings.
    height = int(sys.argv[1])
    width = height
    #the > in the following line needed to be replaced with == to specify that the third command line argument, if it exists, should be used as width
    if len(sys.argv) == 3:
        width = int(sys.argv[2])

    area = area_of_rectangle(height, width)

    message = "The area of a {h} X {w} rectangle is {a}".format(
        #these variables were not correctly indented
        h = height,
        w = width,
        a = area)
    print(message)

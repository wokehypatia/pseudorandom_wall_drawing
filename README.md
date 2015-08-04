# pseudorandom_wall_drawing
#Randomly generates the schematic for an iterative wall drawing, with options to change color, overlay a grid (for ease of copying on a wall), and save the image. Uses a picture class created by the Oberlin College CS Dept.


User:
Thanks for checking out my wall drawing generator! To run, use the command line "python walldrawing.py"

Once the program has started, it will give you an option to learn some general info on wall drawings. To see this info, enter 'Y'. If you do, you will be given a brief string on wall drawings and the artistic theory this program utilizes, and then your drawing will be generated. If you opt to skip the intro by entering 'N', the program will immediately generate your drawing. 

Once the drawing has been generated, you will be given the options to overlay a grid, save your drawing, or close the program. Enter 'grid' in your terminal to grid, 'save' to save, and 'close' to close. 

Once you overlay a grid, you will be again given the options to save and close. Whenever you choose to save, the program will prompt you for a name for the file and then save it to your current directory.


Program Design:
This program works by initializing a Drawing class with functions which create a new picture2 object, get the position of the pen, randomly generate a line, find the placement of the pen after each segment is drawn, repeat the line, and overlay a grid on the canvas.

The function that generates the line (drawnLine) is a recursive function that works by randomly generating an angle between 0 and 180 (so that the line always moves downwards) and drawing forward a short segment at that angle. These angles are saved to a list for easy access by the repeatLine function. The base case for this recursive drawLine function occurs when the pen's position returns with its y-coordinate greater than or equal to the length of the image window (1000).

The line is repeated by calling a function repeatLine, which has two versions that it can choose to call between. If the line ends on the left side of its start point, the lines are repeated from the right side of the page to the left using repeatLineNegative. In the opposite case, repeatLinePositive is called. Both of these functions repeat the original line by pulling the angles they need to draw segments in from the list created in drawnLine. the repeatLine function is run in a while-loop which ends when the x-value of the pen position is on the opposite edge of the image window.

Outside of the Drawing class, a function generateDrawing creates a new Drawing object, calls drawnLine and repeatLine to create a complete drawing, and displays it. This function runs within the main function, which first welcomes the user, than generates a drawing, and then offers the user the option to add a grid to the image, save it, or close the program using nested if-statements. Exception handling also occurs within the main function.


Techniques:
Loops: This program uses while-loops for exception handline and to repeat the line the correct number of times, and for-loops to overlay a grid and access each element in the angleList.

Functions: The only lines of code not in functions in this program are my intro comments, the main call, and my imports.

Strings or Lists: Strings are used for the user interface and the angleList allows lines to be duplicated.

Exception Handling: This program runs both general exceptions and a RunTime Error exception for the unavoidable issues that come with recursing function a different number of times every time the program is run.

Recursion: The drawnLine function works recursively.

Classes and Inheritance: This program makes heavy use of a Drawing class which inherits from the picture2 Picture class.


Lessons Learned:
Creating my own class worked really well, because it allowed me to move through my program that made sense to me. In addition, I think that my strategy of randomly generating an angle and using very small line segments worked very well in terms of "randomly drawing" a line. I learned a lot about differences in syntax from moving back to python from python3, and I also learned more about how a computer moves through a program through the multiple steps in my program. I originally tried to integrate multiprocessing into this program, which proved very difficult because multiprocessing doesn't play very nicely with our picture class. If I could change only one thing, I would've liked to create the modules that my program uses myself because learning the peculiarities of separate programmers codes was sometimes frustrating. In the future, I will also be planning the way that my user will move through the program before I start it, because figuring that out halfway through made it much more confusing than it had to be. 

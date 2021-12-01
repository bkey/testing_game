# Willow's Game

<img src="https://www.sfu.ca/content/sfu/wwest/WWEST_blog/depictions-of-women-in-stem--willow-rosenberg/jcr:content/main_content/textimage_0/image.img.2000.high.jpg/1532118417937.jpg">

Buffy, Willow, Xander and Cordelia are celebrating successfully saving the world again by playing a fun computer trivia game. The only problem is Willow keeps winning. She is too good at witchcraft and science! Being as she's also an expert computer hacker, she wants to modify the source code for the game to add new categories and make it harder. Unfortunately, the code is terrible and untested. 

Having read "Working Effectively with Legacy Code" in her spare time, she decides she wants to follow the book's advice and start by writing characterization test(s) of the game module. How should she go about this? 

The Heuristic for Writing Characterization Tests:
1. Write tests for the area where you will make your changes. Write as many cases as you feel you need to understand the behavior of the code.
2. After doing this, take a look at the specific things you are going to change, and attempt to write tests for those.
3. If you are attempting to extract or move some functionality, write tests that verify the existence and connection of those behaviors on a case-by-case basis. Verify that you are exercising the code that you are going to move and that it is connected properly. Exercise conversions.

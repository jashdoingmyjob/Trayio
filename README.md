# Trayio
Take home assignment Part 1: Robotic Hoover. 

## How to run
First, open terminal and ```git clone https://github.com/jashdoingmyjob/Trayio/``` in your desired directory to clone this repository. Be sure to be in the `Part1` subdirectory before running these commands. The robotic hoover program was developed using Python, so you can run the following CLI in terminal:                          						
	```
	python trayio_roomba.py
	```										
This will run the program and use the `input.txt` file that exists in the same directory as an input. 

## Unit Testing
I've also included a file called `trayio_roomba_test.py` which serves as my personal unit test for the program. As clean coding convention, I created the unit tests prior to developing the program (Test Driven Development). To run the unit test:                                                                                  ```
       python trayio_roomba_test.py
       ```

## Output
The output will be printed out to terminal in the same format as the instructions indicated. The first line represents the final position (x, y) of the Roomba upon completion. The second line represents how many dirt piles it cleaned up. 


## Runtime Complexity
**The overall time complexity of this program is O(n+m).** 
### Details ###
There are three functions in this program `extract_parameters_from_file()`, `clean_up()`, and `move_roomba()`. 
   - extract_parameters_from_file(): The first part of this function is just reading in the lines from the `input.txt` file which is O(1) time. The `for` loop ierates through each of the dirt pile locations which is O(n). Some may argue that because there is a `strip()` within the `for` loop, the actual overall runtime should be O(n^2) but this is not the case. `strip()` actually only takes O(1) time because it is working on a fixed-size string each time. Therefore, that runtime does not affect if we scale the inputs up. **Thus, the runtime for this function is O(n)**
   
   - clean_up(): The function starts by creating a set of the dirt_loc values which takes O(n) time (the reason I create a set is to allow for O(1) look up times later in the function) where n represents the length of `dirt_loc`. Then there is a `for` loop which loops through each char of the instructions string which takes O(m) time where m represents the length of `instructions`. Within this `for` loop we have an `if-statement` that checks if the current position exists in the set of dirt pile locations *which takes O(1) time* since I created a set earlier in the function (had it been a list, we would have had O(n)). Our **overall runtime is O(n) + O(m) = O(n+m) which is still linear runtime**. 
   
   - move_roomba(): This helper function is responsible for updating the position of the roomba based on the current value of `instructions` being processed. **The runtime of this function is O(1)**. 

**Overall, we have time complexity of O(n+m) which is linear runtime.**

## Edge Cases ##
In case the dimensions include negative values, we raise a `ValueError` which terminates the program. In case the robot drive instructions include a value otherthan 'N', 'S', 'E,' or 'W', the program will skip that instruction **and continue to the next instruction**. In case any of the inputed dirt locations had negative x and/or y values, no special behavior was necessary to add as the Roomba doesn't care about the sign of the values— it just checks if the current location exists in the set of all dirt piles. 

## My Process and Thoughts ##
The first thing I did after reading the instructions was sketch out a grid on a piece of paper and represent the roomba's movements using my pencil. After understanding the algorithm required, I started working developing a basic test case and then running it to ensure it fails. I did this because I want a base line to know I'm running the program correctly since I knew the program had to fail. Then I developed a couple more test cases and went on to code the clean_up() function since that is where all the magic happens. I used my test cases to pass the values from input.txt directly to the function so I can isolate the function. I used this test driven, modular approach for developing the entire program. After I got it working, I worked on refactoring and optimizations. One of the optimizations I did was I used a set instead of an array to achieve O(1) lookup times instead of O(n) when I had to check if the current roomba position had a dirt pile. I really enjoyed this assignment and hope I have another opportunity to showcase my work to Tray.io. 

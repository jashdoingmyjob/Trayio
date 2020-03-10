# Trayio
Take home assignment Part 1: Robotic Hoover

## How to run
The robotic hoover program was developed using Python, so you can run the following CLI in terminal:                          						
	```
	python trayio_roomba.py
	```										
This will run the program and use the `input.txt` file that exists in the same directory as an input. 

## Unit Testing
I've also included a file called `trayio_roomba_test.py` which serves as my personal unit test for the program. As clean coding convention, I created the unit tests prior to developing the program (Test Driven Development). To run the unit test:                                                                                  ```
       python trayio_roomba_test.py
       ```

## Output
The output will be printed out to terminal in the same format as the instructions indicated.


## Runtime Complexity
**The overall time complexity of this program is O(n+m).** 
### Details ###
There are two functions in this program `extract_parameters_from_file()` and `clean_up()`. 
   - extract_parameters_from_file(): The first part of this function is just reading in the lines from the `input.txt` file which is O(1) time. The `for` loop ierates through each of the dirt pile locations which is O(n). Some may argue that because there is a `strip()` within the `for` loop, the actual overall runtime should be O(n^2) but this is not the case. `strip()` actually only takes O(1) time because it is working on a fixed-size string each time. Therefore, that runtime does not affect if we scale the inputs up. *Thus, the runtime for this function is O(n)*
   
   - clean_up(): The function starts by creating a set of the dirt_loc values which takes O(n) time (the reason I create a set is to allow for O(1) look up times later in the function). Then there is a `for` loop which loops through each char of the instructions string which takes O(M) time as well. Within this `for` loop we have an `if-statement` at the very end that checks if the current position exists in the set of dirt pile locations *which takes O(1) time* since I created a set earlier in the function (had it been a list, we would have had O(n)). Our *overall runtime is O(n) + O(M) = O(n+M) which is still linear runtime*. 

**Overall, we have time complexity of O(n+m) which is linear runtime.


				   	SMARTGRID PUZZLE SOLVER USER MANUAL
	Table of Contents:
      •	Introduction
      •	Getting Started
          o	System Requirements
          o	Installation
      •	Usage Instructions
          o	Choosing Difficulty Level
          o	Generating Sudoku Puzzles
          o	Solving Sudoku Puzzles
      •	Advanced Features
          o	Optimized Backtracking
          o	Performance Metrics
      •	Trouble shooting
      •	Contact and Support
      
1. Introduction:
 
   Welcome to the Puzzle Solver project! This software allows you to generate and solve Sudoku puzzles of varying difficulty levels. Whether you're a Sudoku enthusiast or a beginner, this solver provides a convenient way to play and challenge yourself.
   
	
2. Getting Started:
   
   System Requirements:
   
				  	Python 3.x installed on your system.
   
				  	Basic understanding of the command line.
   
      Installation:
   
				  	Clone or download the project repository from https://github.com/sai460/AI_Final_Project.git
			   
				  	Navigate to the project directory in the terminal.
      Install required dependencies using the following command:
	  •	pip install numpy matplotlib*
	  or
	  •	pip3 install numpy matplotlib

4. Usage Instructions:
		After successful installation, Let’s run the python file using the following command
			python puzzle_solver_final.py			or
			python3 puzzle_solver_final.py
     			 ![image](https://github.com/sai460/AI_Final_Project/assets/52188773/41c3f949-61b5-4bd2-8cc4-756c75ff95f2)

	User will be prompted to enter the grid size i.e., either 4 or 9 as per standard of sudoku game. (Sudoku Board should contain a Square number nxn grid).
	After entering the grid size (limited to 4 or 9), user will be asked to choose the level of difficulty like below:
		 	![image](https://github.com/sai460/AI_Final_Project/assets/52188773/2a04d0fc-84e3-457f-9231-dac40309e94c)

	After choosing the difficulty level, the program generates a Sudoku puzzle for you.
	The puzzle is displayed on the console.
	The program will display the solved puzzle along with performance metrics, including time taken and backtracking information.
  			![image](https://github.com/sai460/AI_Final_Project/assets/52188773/d3ece236-60a7-4335-a2e9-e88c3f1f215b)


	![image](https://github.com/sai460/AI_Final_Project/assets/52188773/c80733d5-8ca9-414d-b842-5c3e0d290349)
	
	
 
 	**Performance Metrics:**
	  			![image](https://github.com/sai460/AI_Final_Project/assets/52188773/693d1e53-6e04-4160-9b21-06afb9f4e516)

5. Advanced Features:
		Optimized Backtracking
		The solver utilizes an optimized backtracking algorithm to efficiently solve Sudoku puzzles.
		This optimization reduces the number of recursive calls and backtracks, improving overall performance.
		
		Performance Metrics
		The solver provides performance metrics such as time taken, number of recursive calls and number of backtracks.

		
6. Troubleshooting:
		If you encounter issues, ensure that you have Python installed and the required dependencies are installed using pip.
		Check for any error messages in the terminal for guidance.
	
7. Contact and Support:
		If you have any queries, feel free to contact us via email saimohan.yedla@gmail.com


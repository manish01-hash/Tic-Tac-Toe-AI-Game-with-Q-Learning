Tic Tac Toe AI Game

Welcome to the Tic Tac Toe AI Game, a modern twist on the classic game, powered by Python and Pygame. This project allows players to challenge an AI using a Minimax algorithm for strategic gameplay, or to enjoy a friendly match with another player.
Table of Contents

    About the Project
    Features
    Screenshots
    How to Play
    Technologies Used
    Installation and Setup
    How the AI Works
    Contributing
    License

About the Project

This is a Tic Tac Toe game where you can play against an AI using Q-learning for decision-making. Built with Python and the Pygame library, the AI learns to make better moves as it plays more games. Players can choose between playing against the AI or another player in PvP mode.
Features

    AI Mode: Play against the AI with adjustable difficulty (Easy, Normal, Hard).
    PvP Mode: Play with another player locally.
    Q-Learning AI: The AI uses reinforcement learning to improve its decision-making over time.
    Dynamic Difficulty: You can change the AI difficulty during the game.

Screenshots


 ![image alt](https://github.com/manish01-hash/Tic-Tac-Toe-AI-Game-with-Q-Learning/blob/6daea188091d55affbdc63047347469f70006551/Tic%20tac%20toe%20home%20pic)


How to Play

    Start the Game: Press Enter to begin the game.
    Change Game Mode: Press G to switch between AI and PvP modes.
    Make a Move: Click on the grid to place your mark.
    Restart the Game: Press R to restart the game at any time.
    Set AI Difficulty: During the start of the game, set the AI's difficulty by pressing 0, 1, or 2.

Technologies Used

    Python 3.x: Programming language used to build the game.
    Pygame: Library used to create the graphical user interface (GUI) and game loop.
    Numpy: Used for efficient array manipulation to represent the game board.
    Q-learning: Machine learning algorithm used for the AI's decision-making process.

Installation and Setup

    git clone https://github.com/manish01-hash/Tic-Tac-Toe-AI-Game-with-Q-Learning.git


    
    Tic-Tac-Toe-AI-Game-with-Q-Learning


Install the required dependencies:

    pip install pygame numpy

Run the game:

    python game.py

How the AI Works

The AI is powered by Q-learning, a reinforcement learning algorithm. It learns the best moves over time by updating a Q-table based on rewards it receives from the game outcome. The AI balances exploration (trying random moves) and exploitation (choosing the best-known move based on Q-values).

    AI Actions: The AI chooses to either explore new moves (random choice) or exploit the best-known moves based on the Q-values.

    Q-values: The Q-table stores values that represent the potential future rewards of taking specific actions in different board states. The AI updates these values using the Q-learning formula:
    Q(s,a)=Q(s,a)+α×(R(s,a)+γ×max⁡aQ(s′,a)−Q(s,a))
    Q(s,a)=Q(s,a)+α×(R(s,a)+γ×amax​Q(s′,a)−Q(s,a))

    Where:
        αα is the learning rate
        γγ is the discount factor
        R(s,a)R(s,a) is the immediate reward
        max⁡aQ(s′,a)maxa​Q(s′,a) is the best future reward

Contributing

If you would like to contribute to this project, feel free to fork the repository, create a new branch, and submit a pull request. Make sure to include tests for any new features or bug fixes.
License

This project is licensed under the MIT License - see the LICENSE file for details.

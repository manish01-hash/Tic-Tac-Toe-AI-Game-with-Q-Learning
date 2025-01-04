Description:

This project is an implementation of the classic Tic Tac Toe game, featuring an AI opponent powered by Q-Learning. The game is built using Python and the Pygame library, providing an interactive and engaging user interface. The AI player learns to make optimal decisions using Q-Learning, a type of reinforcement learning that enables it to improve over time.

Key Features:

    Classic Tic Tac Toe Gameplay: Players can choose between playing against an AI or another human player (PvP mode).

    AI Powered by Q-Learning: The AI uses Q-Learning to learn from its gameplay and improve its performance. It explores the board and makes decisions based on previously learned experiences.

    Three Levels of Difficulty: The AI can be set to three difficulty levels, ranging from easy to hard, based on how deep the algorithm explores the game tree.

    Smooth Graphics and User Interface: Pygame handles the graphical display, making the game visually appealing with smooth transitions, highlighting winning moves, and a user-friendly interface.

    Real-Time Q-Table Updates: During each game, the AI's Q-Table is updated in real-time based on the outcome, refining its decision-making ability for future games.

    Customizable Game Modes: Users can toggle between AI vs Player and Player vs Player modes. The game can also be restarted at any point.

    Game Result Display: At the end of each game, the result (win/lose/draw) is displayed with a short pause before the game restarts.

Technologies Used:

    Python: The programming language used for the development of the game logic and AI functionality.
    Pygame: The library used to create the game's graphical interface and handle user input.
    NumPy: For handling arrays and matrix operations, such as the board's state and Q-Table management.
    Q-Learning: A machine learning technique used to enable the AI to learn from its actions and outcomes in the game environment.

Learning Outcomes:

    Understanding and implementing Q-Learning in a real-world application.
    Gaining experience with game development using Python and Pygame.
    Building an interactive AI system that learns and improves over time.

Installation and Setup:

    Clone the repository: git clone https://github.com/manish01-hash/TicTacToe-AI-Game.git
    Install the necessary dependencies:

pip install pygame numpy

Run the game:

    python main.py

Future Improvements:

    Integration of a neural network-based AI for more sophisticated gameplay.
    Enhanced graphical design with animations and sound effects.
    Multiplayer support via network connection for remote player interaction.
    Implementation of additional AI strategies like minimax for comparison with Q-Learning.

Contributions:

Feel free to fork the repository, open issues, or submit pull requests to contribute to improving the game or adding new features!

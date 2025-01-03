import sys  #quit the application
import pygame
import random
import copy
import numpy as np
from constants import *


#pygame SETUP
pygame.init()  #initialize the pygame
screen = pygame.display.set_mode( (WIDTH, HEIGHT))
pygame.display.set_caption('TIC TAC TOE AI GAME ')
screen.fill(bg_color) 


# Function to render text on the screen
def draw_text(text, size, color, pos):
    font = pygame.font.Font(None, size)  # Use default font, or replace with a specific font file path
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=pos)
    screen.blit(text_surface, text_rect) 

def is_enter(event):
        # Check if Enter key is pressed
    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
        return True
    return False  

class Board:

    def __init__(self):

        self.squares = np.zeros((ROW, COLS))  # Create an array filled with zeros

        self.marked_sqr = 0  # Initialize the counter for marked squares


    def final_state(self, show=False):

        # Vertical wins

        for col in range(COLS):

            if self.squares[0][col] == self.squares[1][col] == self.squares[2][col] != 0:

                if show:

                    color = CIRC_COLOR if self.squares[0][col] == 2 else CROSS_COLOR

                    iPos = (col * SQSIZE + SQSIZE // 2, 20)

                    fPos = (col * SQSIZE + SQSIZE // 2, HEIGHT - 20)

                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)

                return self.squares[0][col]


        # Horizontal wins

        for row in range(ROW):

            if self.squares[row][0] == self.squares[row][1] == self.squares[row][2] != 0:

                if show:

                    color = CIRC_COLOR if self.squares[row][0] == 2 else CROSS_COLOR

                    iPos = (20, row * SQSIZE + SQSIZE // 2)

                    fPos = (WIDTH - 20, row * SQSIZE + SQSIZE // 2)

                    pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)

                return self.squares[row][0]


        # Desc Diagonal wins

        if self.squares[0][0] == self.squares[1][1] == self.squares[2][2] != 0:

            if show:

                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR

                iPos = (20, 20)

                fPos = (WIDTH - 20, HEIGHT - 20)

                pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)  # Draw the diagonal line

            return self.squares[1][1]


        # Asc Diagonal wins

        if self.squares[0][2] == self.squares[1][1] == self.squares[2][0] != 0:

            if show:

                color = CIRC_COLOR if self.squares[1][1] == 2 else CROSS_COLOR

                iPos = (20, HEIGHT - 20)

                fPos = (WIDTH - 20, 20)

                pygame.draw.line(screen, color, iPos, fPos, LINE_WIDTH)  # Draw the diagonal line

            return self.squares[1][1]


        # No win yet

        return 0


    def mark_sqr(self, row, col, player):

        self.squares[row][col] = player

        self.marked_sqr += 1


    def empty_sqr(self, row, col):

        return self.squares[row][col] == 0


    def get_empty_sqrs(self):

        empty_sqrs = []

        for row in range(ROW):

            for col in range(COLS):

                if self.empty_sqr(row, col):

                    empty_sqrs.append((row, col))

        return empty_sqrs


    def isfull(self):

        return self.marked_sqr == ROW * COLS


    def isempty(self):

        return self.marked_sqr == 0
        

# class AI:
#     def __init__(self, level=2, player=2):
#         self.level = level
#         self.player = player

#     def minimax(self, board, depth, alpha, beta, maximizing):
#         case = board.final_state()

#         if case == 1:  # Player 1 wins
#             return 10 - depth, None
#         if case == 2:  # AI wins
#             return -10 + depth, None
#         if board.isfull():  # Draw
#             return 0, None

#         empty_sqrs = board.get_empty_sqrs()
#         best_move = None

#         if maximizing:
#             max_eval = -float('inf')
#             for (row, col) in empty_sqrs:
#                 temp_board = copy.deepcopy(board)
#                 temp_board.mark_sqr(row, col, self.player)  # AI's move
#                 eval = self.minimax(temp_board, depth - 1, alpha, beta, False)[0]
#                 if eval > max_eval:
#                     max_eval = eval
#                     best_move = (row, col)
#                 alpha = max(alpha, eval)
#                 if beta <= alpha:
#                     break  # Beta cut-off
#             return max_eval, best_move
#         else:
#             min_eval = float('inf')
#             for (row, col) in empty_sqrs:
#                 temp_board = copy.deepcopy(board)
#                 temp_board.mark_sqr(row, col, 1)  # Player 1's move
#                 eval = self.minimax(temp_board, depth - 1, alpha, beta, True)[0]
#                 if eval < min_eval:
#                     min_eval = eval
#                     best_move = (row, col)
#                 beta = min(beta, eval)
#                 if beta <= alpha:
#                     break  # Alpha cut-off
#             return min_eval, best_move

#     def eval(self, main_board):
#         if self.level == 0:
#             move = self.rnd(main_board)
#         elif self.level == 1:
#             _, move = self.minimax(main_board, 1, -float('inf'), float('inf'), True)  # Depth 1 for Normal
#         elif self.level == 2:
#             _, move = self.minimax(main_board, 3, -float('inf'), float('inf'), True)  # Depth 3 for Hard

#         if move is None:
#             print("No valid moves available!")
#             return None

#         print(f'AI has chosen to mark the square in pos {move}')
#         return move  # row, col

class QLearningAI:
    def __init__(self, player=2, learning_rate=0.1, discount_factor=0.9, exploration_rate=1.0, exploration_decay=0.99):
        self.player = player
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.exploration_rate = exploration_rate
        self.exploration_decay = exploration_decay

    def get_state_key(self, board):
        return str(board.squares.reshape(9))  # Convert board to a string key

    def choose_action(self, board):
        state_key = self.get_state_key(board)

        if state_key not in self.q_table:
            self.q_table[state_key] = np.zeros(9)  # Initialize Q-values for this state

        # Log current state and exploration rate
        print(f"State:\n{board.squares}\nQ-Table for this state: {self.q_table[state_key]}")
        print(f"Exploration rate: {self.exploration_rate}")

        if random.uniform(0, 1) < self.exploration_rate:
            # Explore: choose a random valid move
            action = random.choice(np.where(board.squares.flatten() == 0)[0])
            print(f"Exploring: Chose random action {action}")
        else:
            # Exploit: choose the best move based on Q-values
            action = np.argmax(self.q_table[state_key])
            print(f"Exploiting: Chose best action {action}")

        return action

    def update_q_value(self, board, action, reward, next_board):
        state_key = self.get_state_key(board)
        next_state_key = self.get_state_key(next_board)

        if next_state_key not in self.q_table:
            self.q_table[next_state_key] = np.zeros(9)  # Initialize Q-values for the next state

        # Q-learning formula
        best_next_q = np.max(self.q_table[next_state_key])
        old_q_value = self.q_table[state_key][action]
        self.q_table[state_key][action] += self.learning_rate * (reward + self.discount_factor * best_next_q - old_q_value)

        # Log the Q-value update
        print(f"Updating Q-value for state {state_key} and action {action}")
        print(f"Old Q-value: {old_q_value}, Reward: {reward}, Best next Q-value: {best_next_q}")
        print(f"New Q-value: {self.q_table[state_key][action]}")

    def decay_exploration(self):
        self.exploration_rate *= self.exploration_decay
        # Log the exploration rate decay
        print(f"Decayed exploration rate: {self.exploration_rate}")

        
class Game:

    def __init__(self):

        self.board = Board()

        self.ai = QLearningAI()  # Use QLearningAI

        self.player = 1  # 1-cross, 2-circle

        self.gamemode = 'ai'  # pvp or ai

        self.running = True

        self.show_lines()


    def show_lines(self):

        # Fill the background color

        screen.fill(bg_color)

        # Draw vertical lines

        pygame.draw.line(screen, line_color, (SQSIZE, 0), (SQSIZE, HEIGHT), LINE_WIDTH)

        pygame.draw.line(screen, line_color, (WIDTH - SQSIZE, 0), (WIDTH - SQSIZE, HEIGHT), LINE_WIDTH)


        # Draw horizontal lines

        pygame.draw.line(screen, line_color, (0, SQSIZE), (WIDTH, SQSIZE), LINE_WIDTH)

        pygame.draw.line(screen, line_color, (0, HEIGHT - SQSIZE), (WIDTH, HEIGHT - SQSIZE), LINE_WIDTH)


    def draw_fig(self, row, col):

        if self.player == 1:

            # Draw cross

            # Descending line

            start_desc = (col * SQSIZE + OFFSET, row * SQSIZE + OFFSET)

            end_desc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + SQSIZE - OFFSET)

            pygame.draw.line(screen, CROSS_COLOR, start_desc, end_desc, CROSS_WIDTH)

            # Ascending line

            start_asc = (col * SQSIZE + OFFSET, row * SQSIZE + SQSIZE - OFFSET)

            end_asc = (col * SQSIZE + SQSIZE - OFFSET, row * SQSIZE + OFFSET)

            pygame.draw.line(screen, CROSS_COLOR, start_asc, end_asc, CROSS_WIDTH)

        elif self.player == 2:

            # Draw circle

            center = (col * SQSIZE + SQSIZE // 2, row * SQSIZE + SQSIZE // 2)

            pygame.draw.circle(screen, CIRC_COLOR, center, RADIUS, CIRC_WIDTH)


    def make_move(self, row, col):

        self.board.mark_sqr(row, col, self.player)

        self.draw_fig(row, col)

        if not self.isover():

            self.next_turn()  # Only change turn if game isn't over


    def next_turn(self):

        if self.isover():  # Avoid switching turn if game is over

            return

        self.player = self.player % 2 + 1  # Switch between player 1 and player 2


    def change_gamemode(self):

        self.gamemode = 'ai' if self.gamemode == 'pvp' else 'pvp'


    def isover(self):

        result = self.board.final_state(show=True)

        if result == 0 and self.board.isfull():

            return 'Draw'

        elif result == 1:

            return 'Player 1 Wins'

        elif result == 2:

            return 'Player 2 Wins' if self.gamemode == 'pvp' else 'AI Wins'

        return None


    def reset(self):

        self.__init__()  # Reinitialize the game

def main():
    game_started = False
    game_instance = None
    difficulty_set = False

    while True:
        if not game_started:
            screen.fill(bg_color)
            # Welcome screen
            draw_text("Welcome to Tic Tac Toe", 50, CROSS_COLOR, (WIDTH // 2, HEIGHT // 3))
            draw_text("Press Enter to Start", 40, line_color, (WIDTH // 2, HEIGHT // 2))
            draw_text("Press G to Change Mode (AI/PvP)", 30, CROSS_COLOR, (WIDTH // 2, HEIGHT // 2 + 50))
            draw_text("Press R to Restart Board", 30, CROSS_COLOR, (WIDTH // 2, HEIGHT // 2 + 100))
            draw_text("Set AI Difficulty: 0 (Easy), 1 (Normal), 2 (Hard)", 30, CROSS_COLOR, (WIDTH // 2, HEIGHT // 2 + 150))
            pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not game_started:
                    game_started = True
                    difficulty_set = False
                    game_instance = Game()
                    game_instance.show_lines()

                if game_started and game_instance:
                    # Change game mode
                    if event.key == pygame.K_g:
                        game_instance.change_gamemode()
                        print(f"Game mode changed to: {game_instance.gamemode.upper()}")

                    # Restart the game
                    if event.key == pygame.K_r:
                        game_instance.reset()
                        print("Game has been restarted!")

                    # Set AI difficulty
                    if not difficulty_set:
                        if event.key == pygame.K_0:
                            game_instance.ai.level = 0
                            difficulty_set = True
                            print("AI level set to Easy.")
                        elif event.key == pygame.K_1:
                            game_instance.ai.level = 1
                            difficulty_set = True
                            print("AI level set to Normal.")
                        elif event.key == pygame.K_2:
                            game_instance.ai.level = 2
                            difficulty_set = True
                            print("AI level set to Hard.")

            # Handle player moves
            if game_started and event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                row = pos[1] // SQSIZE
                col = pos[0] // SQSIZE
                if game_instance.board.empty_sqr(row, col) and game_instance.running:
                    game_instance.make_move(row, col)
                    if game_instance.isover():
                        game_instance.running = False

            # AI's turn
            if game_instance and game_instance.gamemode == 'ai' and game_instance.player == game_instance.ai.player and game_instance.running:
                action = game_instance.ai.choose_action(game_instance.board)  # Choose action based on Q-learning
                row, col = divmod(action, 3)  # Convert action to row and column
                if game_instance.board.empty_sqr(row, col):
                    game_instance.make_move(row, col)


                    # Determine the reward based on the game outcome

                    reward = 0  # Default reward

                    if game_instance.isover():

                        result = game_instance.isover()

                        if result == 'AI Wins':

                            reward = 1  # Reward for winning

                        elif result == 'Draw':

                            reward = 0  # Neutral reward for a draw

                        else:

                            reward = -1  # Penalty for losing


                    # Update Q-values based on the move

                    next_board = game_instance.board  # Get the next board state

                    game_instance.ai.update_q_value(game_instance.board, action, reward, next_board)  # Update Q-value

                    game_instance.ai.decay_exploration()  # Decay exploration rate


                    if game_instance.isover():

                        game_instance.running = False


        # Check if the game is over and display the result

        if game_instance and game_instance.isover():

            result = game_instance.isover()

            screen.fill(bg_color)

            draw_text(result, 50, CROSS_COLOR, (WIDTH // 2, HEIGHT // 2))

            pygame.display.update()

            pygame.time.wait(2000)  # Wait for 2 seconds before restarting or exiting

            game_instance.reset()

            game_started = False

            difficulty_set = False


        pygame.display.update()


if __name__ == "__main__":

    main()
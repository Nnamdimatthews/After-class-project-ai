import random

# Optional: Track player move history for smarter AI
player_history = []

# Define possible moves
moves = ["rock", "paper", "scissors"]

def get_player_move():
    move = input("Enter your move (rock, paper, scissors): ").lower()
    while move not in moves:
        print("Invalid input. Please try again.")
        move = input("Enter your move (rock, paper, scissors): ").lower()
    player_history.append(move)
    return move

def get_ai_move():
    # Basic strategy: random choice
    return random.choice(moves)

def determine_winner(player, ai):
    if player == ai:
        return "It's a tie!"
    elif (player == "rock" and ai == "scissors") or \
         (player == "scissors" and ai == "paper") or \
         (player == "paper" and ai == "rock"):
        return "You win!"
    else:
        return "AI wins!"

def play_game():
    player_score = 0
    ai_score = 0

    while True:
        print("\n--- New Round ---")
        player_move = get_player_move()
        ai_move = get_ai_move()
        print(f"AI chose: {ai_move}")

        result = determine_winner(player_move, ai_move)
        print(result)

        if "You win" in result:
            player_score += 1
        elif "AI wins" in result:
            ai_score += 1

        print(f"Score -> You: {player_score} | AI: {ai_score}")

        play_again = input("Play another round? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

play_game()

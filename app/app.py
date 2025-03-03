from flask import Flask, render_template, request, jsonify
import random

player_wins = 0
computer_wins = 0

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
    

@app.route('/play', methods=['POST'])
def play():

    # Get player's choice from the request
    player_choice = request.json.get('choice')
    
    # Computer makes a random choice
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    
    # Determine winner
    result = determine_winner(player_choice, computer_choice)
    if result == "You win!":
        global player_wins
        player_wins += 1
    elif result == "Computer wins!":
        global computer_wins
        computer_wins += 1

    return jsonify({
        'player_choice': player_choice,
        'computer_choice': computer_choice,
        'result': result,
        'player_score': player_wins,
        'computer_score': computer_wins
    })

def determine_winner(player, computer):
    if player not in ['rock', 'paper', 'scissors']:
        return "Invalid choice. Please choose rock, paper, or scissors."
    if player == computer:
        return "It's a tie!"
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"
@app.route('/reset', methods=['POST'])
def reset():
    global player_wins, computer_wins
    player_wins = 0
    computer_wins = 0
    return jsonify({'message': 'Game reset successful!',
                    'player_score': player_wins,
                    'computer_score': computer_wins})
@app.route('/score', methods=['GET'])
def get_score():
    return jsonify({
        'player_score': player_wins,
        'computer_score': computer_wins
    })

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()
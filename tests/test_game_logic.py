import pytest
from app.app import app, determine_winner

def test_determine_winner():
    assert determine_winner('rock', 'scissors') == "You win!"
    assert determine_winner('paper', 'rock') == "You win!"
    assert determine_winner('scissors', 'paper') == "You win!"
    assert determine_winner('rock', 'paper') == "Computer wins!"
    assert determine_winner('paper', 'scissors') == "Computer wins!"
    assert determine_winner('scissors', 'rock') == "Computer wins!"
    assert determine_winner('rock', 'rock') == "It's a tie!"
    assert determine_winner('paper', 'paper') == "It's a tie!"
    assert determine_winner('scissors', 'scissors') == "It's a tie!"
    assert determine_winner('lizard', 'spock') == "Invalid choice. Please choose rock, paper, or scissors."

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    with app.test_client() as client:
        yield client
def test_play_endpoint(client):
    response = client.post('/play', json={'choice': 'rock'})
    assert response.status_code == 200
    data = response.get_json()
    assert 'player_choice' in data
    assert 'computer_choice' in data
    assert 'result' in data
    assert 'player_score' in data
    assert 'computer_score' in data
def test_reset_endpoint(client):
    response = client.post('/reset')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Game reset successful!'
    assert data['player_score'] == 0
    assert data['computer_score'] == 0
def test_score_endpoint(client):
    response = client.get('/score')
    assert response.status_code == 200
    data = response.get_json()
    assert 'player_score' in data
    assert 'computer_score' in data

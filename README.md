# Python Mini Projects 🐍

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)

In this repository, it contains 4 small Python projects that demonstrate fundamental programming concepts such as control flow, data structures, randomness, user input handling, and basic algorithms.

## Projects Included
- `Poker.py` (Texas Hold’em vs dealer with hand evaluation)
- `TicTacToe.py` (you vs computer)
- `MiniYahtzee.py` (dice game + scoring)
- `WeatherAPI.py` (forecast using Open-Meteo API)

## Projects

## Poker (Poker.py)
A command-line **Texas Hold’em** style game (player vs dealer).

Commands:
- `deal` -> shuffles + deals 2 cards to you and 2 to the dealer (hidden)
- `draw` -> draws 5 shared community cards
- `show` -> reveals the dealer’s 2 cards
- `result` -> evaluates both hands and prints the winner
- `quit` -> exits the game

### Features
- Builds and shuffles a full 52-card deck
- Evaluates hands using **best 5 out of 7 cards**
- Supports standard poker rankings (high card -> straight flush)

## TicTacToe (TicTacToe.py)
A terminal and simple Tic-Tac-Toe game: you vs. the computer.

How Does This Work?
- The board is numbered 0–8
- Computer plays X
- You play @
- You enter a number (0–8) for your move
- Program checks wins + ties automatically

## MiniYahtzee (MiniYahtzee.py)
To put it in a few words, a simplified Yahtzee-style dice game.

How Does This Work?
- You roll 5 dice up to 3 times
- After each roll, you choose which dice to re-roll
- The game scores your final dice using categories:
  - Yahtzee (50)
  - Large Straight (40)
  - Small Straight (30)
  - Full House (25)
  - Four / Three of a Kind (sum of dice)
  - Chance (sum of dice)

## Weather App (WeatherAPI.py)
A command-line weather checker using the Open-Meteo API (no API key needed).

### Features
- City -> latitude/longitude using Open-Meteo geocoding
- Handles duplicate city names by allowing an optional country code (ex: CA, US, cities such as Waterloo being filtered based on country code)
- Prints a short forecast (today + tomorrow)












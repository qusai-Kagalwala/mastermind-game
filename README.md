# 🎯 Mastermind Game

Classic Mastermind code-breaking game implemented in Python. Crack the secret color code using logic and deduction!

## 🎮 About the Game

Mastermind is a classic code-breaking game where you try to guess a secret sequence of colors. The computer generates a random 4-color code, and you have 10 attempts to crack it using the feedback provided after each guess.

## ✨ Features

- 🌈 **6 Color Options**: Red (R), Green (G), Blue (B), Yellow (Y), White (W), Orange (O)
- 🎯 **4-Color Code**: Secret sequence of 4 colors to crack
- 🔢 **10 Attempts**: Challenge yourself to solve it within the limit
- 📊 **Detailed Feedback**: Get precise information about correct positions and colors
- ✅ **Input Validation**: Prevents invalid guesses and guides user input
- 🎮 **Clean Interface**: Simple terminal-based gameplay

## 🚀 Quick Start

### Prerequisites
- Python 3.x (no additional libraries required!)

### Installation & Run
1. 📥 Clone this repository:
   ```bash
   git clone https://github.com/qusai-Kagalwala/mastermind-game.git
   cd mastermind-game
   ```

2. ▶️ Run the game:
   ```bash
   python mastermind.py
   ```

## 🕹️ How to Play

### Game Setup
- The computer generates a secret 4-color code
- Colors can repeat in the sequence
- You have 10 attempts to guess the correct code

### Making Guesses
1. 🎯 Enter 4 colors separated by spaces (e.g., `R G B Y`)
2. 📝 Use these color codes:
   - **R** = Red
   - **G** = Green  
   - **B** = Blue
   - **Y** = Yellow
   - **W** = White
   - **O** = Orange

### Understanding Feedback
After each guess, you'll receive three types of feedback:

- 🎯 **Correct Positions**: Colors that are correct and in the right position
- 🔄 **Correct Colors in Wrong Positions**: Right colors but in wrong spots
- ❌ **Incorrect Colors**: Colors not in the secret code at all

### Example Gameplay
```
Secret Code: R G B Y (hidden from player)

Attempt 1: R R R R
Feedback: Correct Positions: 1 | Correct Colors in Wrong Positions: 0 | Incorrect Colors: 3

Attempt 2: R G W O  
Feedback: Correct Positions: 2 | Correct Colors in Wrong Positions: 0 | Incorrect Colors: 2

Attempt 3: R G B Y
Feedback: Correct Positions: 4 | Correct Colors in Wrong Positions: 0 | Incorrect Colors: 0
🎉 You won!
```

## 🧠 Strategy Tips

### Beginner Tips
- 🎯 **Start Simple**: Try using all different colors first to identify which colors are in the code
- 📝 **Track Your Guesses**: Keep mental notes of the feedback from previous attempts
- 🔍 **Use Process of Elimination**: Rule out colors that aren't in the code

### Advanced Strategies
- 🎮 **Two-Phase Approach**: First identify all colors, then determine positions
- 🧩 **Strategic Positioning**: Once you know the colors, systematically test positions
- 📊 **Analyze Patterns**: Use feedback to narrow down possibilities efficiently
- ⚡ **Optimize Guesses**: Each guess should provide maximum information

### Example Strategy
1. **Discovery Phase**: `R G B Y` - Identify which colors are in the code
2. **Refinement Phase**: `R R G G` - Test for duplicates and positions
3. **Solution Phase**: Use feedback to place colors in correct positions

## 🛠️ Technical Details

### Game Configuration
```python
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O']  # Available colors
TRIES = 10                                # Maximum attempts
CODE_LENGTH = 4                           # Length of secret code
```

### Core Functions
- **`generate_code()`**: Creates random secret code
- **`guess_code()`**: Handles user input and validation
- **`check_code()`**: Compares guess with secret code and provides feedback
- **`game()`**: Main game loop and flow control

### Algorithm Details
The feedback system uses a two-pass algorithm:
1. **First Pass**: Count exact position matches
2. **Second Pass**: Count color matches in wrong positions
3. **Remainder**: Calculate completely incorrect colors

## 🎯 Game Variations

### Easy Mode Modifications
```python
TRIES = 15        # More attempts
CODE_LENGTH = 3   # Shorter code
```

### Hard Mode Modifications  
```python
TRIES = 8         # Fewer attempts
COLORS = ['R', 'G', 'B', 'Y', 'W', 'O', 'P', 'V']  # More colors
CODE_LENGTH = 5   # Longer code
```

### Custom Rules
- **No Repeats**: Modify `generate_code()` to use each color only once
- **Hints**: Add a hint system that reveals one position after 5 wrong guesses
- **Timed Mode**: Add time pressure with countdown timer

## 🏆 Scoring System Ideas

Want to add scoring? Consider these metrics:
- **Attempts Used**: Fewer attempts = higher score
- **Time Taken**: Faster solving = bonus points
- **Difficulty Multiplier**: Harder settings = more points
- **Streak Counter**: Consecutive wins = multiplier bonus

## 🤝 Contributing

Feel free to fork and improve the game! Some enhancement ideas:

### Feature Requests
- 🎨 **GUI Version**: Tkinter or Pygame interface with colored circles
- 📱 **Web Version**: Browser-based implementation
- 🏆 **Leaderboard**: High scores and statistics tracking
- 🎵 **Sound Effects**: Audio feedback for guesses and wins
- 🤖 **AI Solver**: Computer player that solves codes
- 👥 **Multiplayer**: Two-player mode where players take turns

### Code Improvements
- 📊 **Statistics**: Track win rate, average attempts, best time
- 💾 **Save/Load**: Resume interrupted games
- 🎮 **Game Modes**: Different difficulty levels and rule variations
- 🎨 **Better UI**: Colored terminal output, ASCII art

## 📚 Learning Resources

### Mastermind Strategy
- [Optimal Strategy Guide](https://en.wikipedia.org/wiki/Mastermind_(board_game)#Optimal_strategy)
- [Mathematical Analysis](https://www.cs.uni.edu/~wallingf/teaching/cs3530/resources/knuth-mastermind.pdf)

### Python Game Development
- Learn about random number generation
- Practice with list manipulation and loops
- Understand user input validation
- Explore algorithm optimization

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Qusai Kagalwala**
- GitHub: [@qusai-Kagalwala](https://github.com/qusai-Kagalwala)

---

🎯 **Ready to crack the code? Start playing now!** 🧠

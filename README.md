<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Higher or Lower Game</title>
    <script src="https://cdn.jsdelivr.net/npm/showdown@1.9.1/dist/showdown.min.js"></script>
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            let markdownContent = `
# Higher or Lower Game

This is a simple command-line game where the player has to guess which of two given options has more followers on social media. The game is based on comparing the follower counts of two celebrities or popular accounts. The player's goal is to make a streak of correct guesses. The game continues until the player makes a wrong guess.

## Getting Started

These instructions will help you set up the game on your local machine.

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository or download the source code:

   \`\`\`
   git clone https://github.com/your_username/higher-or-lower-game.git
   \`\`\`
   
2. Change to the game's directory:

   \`\`\`
   cd higher-or-lower-game
   \`\`\`

3. Install the required packages:

   \`\`\`
   pip install -r requirements.txt
   \`\`\`

## Usage

To play the game, run the \`main.py\` script:

\`\`\`
python main.py
\`\`\`

## Game Structure

The game consists of the following components:

- \`main.py\`: The main script that runs the game.
- \`art.py\`: Contains the ASCII art for the game, such as the logo and the "vs" symbol.
- \`game_data.py\`: Contains the data used for the game, including the names, descriptions, countries, and follower counts of various celebrities and popular accounts.

## How to Play

1. The game will present two options, labeled "A" and "B", along with their descriptions and countries of origin.
2. The player has to guess which option has more followers by typing "A" or "B" and pressing Enter.
3. If the player's guess is correct, their score will increase by 1 and they will move on to the next comparison. The winning choice will be compared against a new random choice.
4. If the player's guess is incorrect, the game will end and display their final score.

## Contributing

If you want to contribute to this project, please feel free to submit a pull request. We appreciate any help, whether it's fixing bugs, adding new features, or updating documentation.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
            `;
            let converter = new showdown.Converter();
            let htmlContent = converter.makeHtml(markdownContent);
            document.getElementById("markdown-content").innerHTML = htmlContent;
        });
    </script>
</head>
<body>
    <div id="markdown-content"></div>
</body>
</html>

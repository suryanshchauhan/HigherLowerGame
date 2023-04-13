<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>

<body>
    <h1>Higher or Lower Game</h1>
    <p>This is a simple command-line game in Python where the player has to guess which of two given options has more followers on
        social media. The game is based on comparing the follower counts of two celebrities or popular accounts. The
        player's goal is to make a streak of correct guesses. The game continues until the player makes a wrong guess.</p>

    <h2>Getting Started</h2>
    
    <p>These instructions will help you set up the game on your local machine.</p>

    <h3>Prerequisites</h3>
    <ul>
        <li>Python 3.x</li>
    </ul>

    <h3>Installation</h3>
    <ol>
        <li>Clone the repository or download the source code:</li>
        <pre><code>git clone https://github.com/your_username/higher-or-lower-game.git</code></pre>
        <li>Change to the game's directory:</li>
        <pre><code>cd higher-or-lower-game</code></pre>
        <li>Install the required packages:</li>
        <pre><code>pip install -r requirements.txt</code></pre>
    </ol>

    <h2>Usage</h2>
    <p>To play the game, run the <code>main.py</code> script:</p>
    <pre><code>python main.py</code></pre>

    <h2>Game Structure</h2>
    <p>The game consists of the following components:</p>
    <ul>
        <li><code>main.py</code>: The main script that runs the game.</li>
        <li><code>art.py</code>: Contains the ASCII art for the game, such as the logo and the "vs" symbol.</li>
        <li><code>game_data.py</code>: Contains the data used for the game, including the names, descriptions, countries,
            and follower counts of various celebrities and popular accounts.</li>
    </ul>

    <h2>How to Play</h2>
    <ol>
        <li>The game will present two options, labeled "A" and "B", along with their descriptions and countries of
            origin.</li>
        <li>The player has to guess which option has more followers by typing "A" or "B" and pressing Enter.</li>
        <li>If the player's guess is correct, their score will increase by 1 and they will move on to the next
            comparison. The winning choice will be compared against a new random choice.</li>
        <li>If the player's guess is incorrect, the game will end and display their final score.</li>
    </ol>

    <h2>Contributing</h2>
    <p>If you want to contribute to this project, please feel free to submit a pull request. We appreciate any help,
        whether it's fixing bugs, adding new features, or updating documentation.</p>

    <h2>License</h2>
    <p>This project is licensed under the MIT License - see the <a href="LICENSE.md">LICENSE.md</a> file for details.</p>
</body>

</html>

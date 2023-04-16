# Dual N back game

### I got interested in making [N back game](https://github.com/kjs29/dual_nback) and I wanted to challenge myself so I decided to make dual N back game. My highest level is brown belt in the game so far, I dare you to achieve black belt!

# Dual N back game

The game is designed to enhance players' memory skills, and it shows series of numbers and positions one at a time. 

Players are supposed to memorize N-th number and position ago and compare those to current number and position. The higher the N, more challenging it becomes. 

# Download the game 

## Method 1 - Clone the repo from Github (MacOS or Windows)

Copy & Paste the following code below in your terminal.

The game will be downloaded in the folder named `~/Desktop/pygame_dual_nback`, wait a few seconds, and it will start playing automatically.

<em>MacOS or Linux</em>

```
cd ~/Desktop && mkdir pygame_dual_nback && cd pygame_dual_nback && python3 -m venv env && source env/bin/activate && git clone https://github.com/kjs29/dual_nback.git && cd dual_nback && pip install -r requirements.txt && python main.py && deactivate
```

<em>Windows</em>

Replace `<username>` with your own username.

```
cd C:\Users\<username>\Desktop && mkdir pygame_dual_nback && cd pygame_dual_nback
python -m venv env && .\env\Scripts\activate
git clone https://github.com/kjs29/dual_nback.git
cd dual_nback && pip install -r requirements.txt && python main.py && deactivate
```

👨🏻‍💻 Currently figuring out how to convert python file to executable files for all OS.

~~## Method 2 (Windows only for now) - Download from itch.io~~

~~1. Go to https://kjs29.itch.io/dual_nback and click download button~~

~~2. Unzip the file you downloaded~~

~~3. Run `main.exe` file~~

## How to run the game again once the game is downloaded

<em>MacOS or Linux</em>

Go to terminal and type

```
cd ~/Desktop/pygame_dual_nback && source env/bin/activate && cd dual_nback && python main.py && deactivate
```

<em>Windows</em>

Replace `<username>` with your own username.

```
cd C:\Users\<username>\Desktop\pygame_dual_nback && .\env\Scripts\activate && cd dual_nback && python main.py && deactivate
```

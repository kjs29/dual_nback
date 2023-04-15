# Dual N back game

<p float="left">
  <img width="250" alt="Screenshot 2022-12-16 at 5 19 31 AM" src="https://user-images.githubusercontent.com/96529477/208098017-426e2adf-437c-43aa-b909-900e7e3c045f.png">
  <img width="250" alt="Screenshot 2022-12-16 at 5 29 24 AM" src="https://user-images.githubusercontent.com/96529477/208099008-c8e8f1b3-dd92-49aa-b9f7-02634a9a1101.png">
  <img width="250" alt="Screenshot 2022-12-16 at 5 30 45 AM" src="https://user-images.githubusercontent.com/96529477/208099049-7897efba-1e3a-4da8-9160-f00a9660e307.png">
  <img width="250" alt="Screenshot 2022-12-16 at 5 30 53 AM" src="https://user-images.githubusercontent.com/96529477/208099085-2ca1433e-001a-493e-92aa-faed166b2d6e.png">
  <img width="250" alt="Screenshot 2022-12-16 at 5 31 21 AM" src="https://user-images.githubusercontent.com/96529477/208099114-f98f15c2-d52f-4530-badc-f88030c1eef9.png">
  <img width="250" alt="image" src="https://user-images.githubusercontent.com/96529477/208099337-436c8701-1d6d-4e48-a410-948d7ac37f42.png">
</p>

### I got interested in making [N back game](https://github.com/kjs29/dual_nback) and I wanted to challenge myself so I decided to make dual N back game. My highest level is brown belt in the game so far, I dare you to achieve black belt!

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

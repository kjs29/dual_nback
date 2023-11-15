# Dual N back game

# Motivation

Inspired by one TV show that individuals solve brain puzzles to intellectually challenge themselves, where 'N-back' game was introduced as a training to increase one's IQ, I decided to replicate the 'N-back' training. After creating N-back game, I wanted to make something more challenging than 'N-back', which is 'Dual-N-back'. (However, I realized there exist trainings that are very similar to N-back, Dual-N-back trainings.)

# Objectives

To apply basic knowledge in programming for a tangible(?) product that live outside of terminal.

To create games that intellectually challenge & train brains.

<em>I dare you to achieve black belt! My highest level is brown belt in the game so far.</em>

# How does the game work?

The game is designed to enhance players' memory skills, and it shows series of numbers and positions one at a time. 

Players are supposed to memorize N-th number and position ago and compare those to current number and position. The higher the N, more challenging it becomes.

For example, let's consider the following 2-back question. 

```
2-Back

Question:
|1|2|3|
|4|5|6| <- Position grid
|7|8|9|
-------------------------
Event:

1.
| | |X|
| | | |
| | | |

2.
| | | |
| |X| |
| | | |

3.
| | |X|
| | | |     Answer: O
| | | |
-------------------------
Explanation:

In the 1st event, X was marked in position 3.

In the 2nd event, X was marked in position 5.

In the 3rd event, X was marked in position 3.

In the 3rd event, the position 2 events ago was 3. We have to compare the position 2 events ago, because it is demonstrating a 2-back game now.

Because the current position in the 3rd event and the previous position in the 1st event are identical, we have to submit 'O' as an answer.
```

So far, this explained only the position aspect, but different numbers appear in the game.

Let's consider another example of 2-back game.

```
2-Back 

Event:

1.
| | |2|
| | | |
| | | |

2.
| | | |
| |6| |
| | | |

3.
| | |8|
| | | |     Position answer: O
| | | |     Number answer: X
---------------------------
Explanation:

In the 1st event, the position was 3, the number was 2.
In the 2nd event, the position was 5, the number was 6.
In the 3rd event, the position was 3, the number was 8.

Because the position in the 1st event and the position in the 3rd event are the same, Position answer is 'O'.
Because the number in the 1st event(2) and the number in the 3rd event (8) are not the same, Number answer is 'X'.
```

# Download the game

## Method 1 - Clone the repo from Github, run `main.py`

```
git clone https://github.com/kjs29/dual_nback.git
```

## Method 2 - Copy & Paste the following command in your terminal

You can copy & paste the following code below in your terminal, the game will start automatically.

<em>MacOS or Linux</em>

```
cd ~/Desktop && mkdir pygame_dual_nback && cd pygame_dual_nback && python3 -m venv env && source env/bin/activate && git clone https://github.com/kjs29/dual_nback.git && cd dual_nback && pip install -r requirements.txt && python main.py && deactivate
```

The command is the following:

1. Create a folder `pygame_dual_nback` at `<your_home_directory>/Desktop/`. 

2. Set up a virtual environment and download the current repository and the requirements(`pygame`) inside it. Because any python packages downloaded will locate within this virtual environment.

3. It will start playing automatically, once the game is finished, deactivate the virtual environment.

<em>Windows</em>

Replace `<username>` with your own username.

```
cd C:\Users\<username>\Desktop && mkdir pygame_dual_nback && cd pygame_dual_nback && python -m venv env && .\env\Scripts\activate && git clone && https://github.com/kjs29/dual_nback.git && cd dual_nback && pip install -r requirements.txt && python main.py && deactivate
```

I am sorry, I don't have windows computer at this time, so I couldn't verify if it works 100% on Windows. Please contact me at jsk.jinsung@gmail.com for any inquiry.

---

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

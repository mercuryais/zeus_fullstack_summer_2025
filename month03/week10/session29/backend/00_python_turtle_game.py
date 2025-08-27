import psycopg2 
import turtle
import random
import time
DB_CONFIG = {
"dbname": "python_game",
"user": "postgres",
"password": "",
"host": "localhost",
"port": "5433"
}
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
GAME_DURATION = 20
score = 0 
time_left = GAME_DURATION 

def save_score_to_db(player_name, final_score):
    conn = None
    try:
        print("Connecting to the PostgreSQL database to save score...")
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        sql = """INSERT INTO high_scores (player_name, score)
        VALUES(%s, %s)"""
        cur.execute(sql, (player_name, final_score))
        conn.commit()
        print(f"✅ Score for {player_name} ({final_score}) saved successfully!")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error while saving score: {error}")
    finally:
        if conn is not None:
            conn.close()
def get_high_score_from_db():
    conn = None
    high_score = 0
    try:
        print("Fetching high score from the database...")
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()
        SELECT_MAX = """SELECT score from high_scores order by score desc LIMIT 1       """
        cur.execute(SELECT_MAX)
        result = cur.fetchall()
        if result and result[0] is not None:
            high_score = result[0]
        print(f"🏆 All-time high score is: {high_score}")
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error while fetching high score: {error}")
    finally:
        if conn is not None:
            conn.close()
            print("Database connection closed.")
    return high_score
def move_up():
    y = player.ycor()
    if y < SCREEN_HEIGHT / 2 - 20:
        player.sety(y + 20)
def move_down():
    y = player.ycor()
    if y > -SCREEN_HEIGHT / 2 + 20:
        player.sety(y - 20)
def move_left():
    x = player.xcor()
    if x > -SCREEN_WIDTH / 2 + 20:
        player.setx(x - 20)
def move_right():
    x = player.xcor()
    if x < SCREEN_WIDTH / 2 - 20:
        player.setx(x + 20)
def is_collision(t1, t2):
    is_collision = False
    distance = t1.distance(t2)
    if distance < 21:
        is_collision = True
    return is_collision

def update_score():
    score_pen.clear()
    score_pen.write(
        f"Score: {score} | Time: {time_left}",
        align="center",
        font=("Courier", 24, "normal")
    )
def countdown():
    global time_left
    time_left -= 1
    update_score()
    if time_left > 0:
        screen.ontimer(countdown, 1000)
    else:
        end_game()  

def end_game():
    player.hideturtle()
    food.hideturtle()
    score_pen.goto(0, 40)
    score_pen.write(
    f"Game Over! Final Score: {score}",
    align="center",
    font=("Courier", 24, "normal")
    )
    save_score_to_db(player_name, score)
    high_score = get_high_score_from_db()
    score_pen.goto(0, -20)
    score_pen.write(
    f"All-Time High Score: {high_score}",
    align="center",
    font=("Courier", 20, "normal")
    )

screen = turtle.Screen()
screen.title("Turtle Catcher Game with PostgreSQL")
screen.bgcolor("skyblue")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

player_name = screen.textinput("Player Name", "Enter your name:")
if not player_name:
    player_name = "Anonymous"

# --- CREATE GAME OBJECTS ---
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.shapesize(stretch_wid=1.5, stretch_len=1.5)
player.penup()
player.speed(0)
food = turtle.Turtle()
food.shape("circle")
food.color("red")

x = random.randint(-280, 280)
y = random.randint(-280, 280)
food.penup()
food.goto(x, y)
food.pd()
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, 260)
update_score()
# --- KEYBOARD BINDINGS ---
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
# --- START THE GAME TIMER ---
countdown()
while time_left > 0:
    screen.update()
    bool = is_collision(food, player)
    if bool:
        food.pu()
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)
        food.pd()
        score += 10
    update_score()
turtle.done()
from food import Food

width = 1400
height = 1000

foods = [Food(width, height) for _ in range(200)]
bad_foods = [Food(width, height) for _ in range(5)]

points = 0

mark_start_x = 0
mark_start_y = 0

value = 1
def setup():
    size(width, height)
    background(255)
    
def draw():
    global mark_start_x, mark_start_y, points
    background(255)
    
    for food in foods:
        fill(0, 255, 23)
        food.display()

    for bad_food in bad_foods:
        fill(254, 34, 100)
        bad_food.display()
    fill(0)
    if mousePressed:
        rectMode(CORNER)
        noFill()
        rect(mark_start_x, mark_start_y, mouseX -
             mark_start_x, mouseY - mark_start_y)
    font = loadFont('Purisa-Bold-48.vlw')
    textFont(font, 32)
    text("punkty: {}".format(points), width - width / 6, height / 6)

def mouseReleased():
    global mark_start_x, mark_start_y, points
    for food in foods:
        if (mark_start_x < food.x_position < mouseX) and (mark_start_y < food.y_position < mouseY):
            foods.remove(food)
            points += 1
            print('mam Cie')
    for bad_food in bad_foods:
        if (mark_start_x < bad_food.x_position < mouseX) and (mark_start_y < bad_food.y_position < mouseY):
            bad_foods.extend([Food(width, height) for _ in range(5)])
            points -= 10
def mousePressed():
    global mark_start_x, mark_start_y
    mark_start_x = mouseX
    mark_start_y = mouseY
    print("Mouse clicked %d : %d" % (mouseX, pmouseY))
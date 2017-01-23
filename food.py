
class Food():
    def __init__(self, canvas_width, canvas_height):
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.volume = random(10, 20)
        self.x_speed = random(-1,1)
        self.y_speed = random(-1,1)
        self.x_position = random(0, canvas_width)
        self.y_position = random(0, canvas_height)
        
        
    def display(self):
        rectMode(CENTER)
        rect(self.x_position, self.y_position,self.volume, self.volume)
        self.move()
        
    def move(self):
        self.x_position += self.x_speed  
        self.y_position += self.y_speed
        self.x_position %= self.canvas_width
        self.y_position %= self.canvas_height
        
    
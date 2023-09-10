from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing
import random


def main():
    scene_width = 800
    scene_height = 500
    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_cloud(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    for x in range(10, 50000, 30):
        y = random.randint(0, scene_height / 1)
        draw_grass(canvas, x, y)

    finish_drawing(canvas)

def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 4,
        scene_width, scene_height, width=0, fill="gray45")
def draw_cloud(canvas, scene_width, scene_height):
    for i in range(75):
        x = random.randint(0, scene_width)
        y = random.randint(0, scene_height / 0.5)
        diameter = random.randint(130, 130)
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="slateGray")        
def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 4, width=0, fill="sienna4")
def draw_grass(canvas, scene_width, scene_height):
        draw_line(canvas, scene_width  / 5, scene_height / 200,
            scene_width / 5, scene_height / 3, width=5, fill="darkGreen")

main()
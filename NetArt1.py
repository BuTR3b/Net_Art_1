import random
import pygame
pygame.init()

black = [0, 0, 0]
Size = (700, 700)
done = False

print("\n\n================================")
print("Draw a pic - 0 \nDraw one figure - 1")
UserChoice = int(input(">> "))
print("Enter FPS \n1 - low \t30 - fast")
Speed = int(input(">> "))
print("================================")

def DrawLine():
    Figure = random.choice(["line", "circle", "rect"])
    Red = random.randint(0, 255)
    Green = random.randint(0, 255)
    Blue = random.randint(0, 255)
    color = [Red, Green, Blue]
    Radius = random.randint(1, 100)
    x1 = random.randint(0, 500)
    x2 = random.randint(0, 500)
    y1 = random.randint(0, 500)
    y2 = random.randint(0, 500)
    lineSize = random.randint(1, 50)
    circleSize = random.randint(0, 1)
    thickness = random.randint(0, 1)
    if Figure == "line":
        pygame.draw.line(screen, color, [x1, y1], [x2, y2], lineSize)
    elif Figure == "rect":
        pygame.draw.rect(screen, color, (x1 ,y1 , x2, y2), thickness)
    else:
        pygame.draw.circle(screen, color, [x1, y1], Radius, circleSize)

clock = pygame.time.Clock()
screen = pygame.display.set_mode(Size)
pygame.display.set_caption("COLORS")
pygame.mouse.set_visible(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    if UserChoice == 1:
        screen.fill(black)

    DrawLine()

    pygame.display.flip()
    clock.tick(Speed)

pygame.quit()

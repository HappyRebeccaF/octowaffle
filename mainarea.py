import sys
import pygame
import time
import random
# 1. Initialize Pygame
pygame.init()

# 2. Set up the display (Width, Height)
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Optional: Add a window title
pygame.display.set_caption("A Spooking Day")

# 3. Set up a clock to regulate frame rate
clock = pygame.time.Clock()
character = pygame.image.load("imagesfolder/charactergood.png").convert_alpha()
character = pygame.transform.scale(character, (100, 100))
characterbad = pygame.image.load("imagesfolder/characterbad.jpeg").convert_alpha()
characterbad = pygame.transform.scale(characterbad, (100, 100))
map = pygame.image.load("imagesfolder/map.jpeg").convert_alpha()
map = pygame.transform.scale(map, (5000, 5000))
start = pygame.image.load("imagesfolder/startscreen.jpeg").convert_alpha()
start = pygame.transform.scale(start, (600, 600))
tort = [start];
start = pygame.image.load("imagesfolder/t1.jpeg").convert_alpha()
start = pygame.transform.scale(start, (600, 600))

end = pygame.image.load("imagesfolder/endscreen.jpeg").convert_alpha()
end = pygame.transform.scale(end, (600, 600))
tort.append(start);
graph = []
# character = pygame.transform.scale(character, (100, 100))

# 4. Main Game Loop
distall = 100
speed = 5;
running = True
clocker = 0
lastmove = 0
listpoint = [];
# Load the coordinate representation of the map.
file =  open("pointsgrid.txt", "r");

for line in file:
    content = line.strip()
    content = content.split(',')
    listpoint.append([int(content[0]),int(content[1])])
file.close();
#content = content.split(',')
##file.close()
##print("hi")
###for i in range(0,len(content),2):
##    listpoint.append({int(content[i]),int(content[i+1])})

appfile = open("pointsgrid.txt", "a") ;
pygame.init()
pygame.joystick.init()
#dance_pad = pygame.joystick.Joystick(1)
#awdance_pad.init()

hasquit = False;
ton = 0;
camera = pygame.Rect(0, 0, 600, 600)
pointchosen = random.randint(0,len(listpoint)-1);
camera.x = listpoint[pointchosen][0]
camera.y = listpoint[pointchosen][1]
camera2 = pygame.Rect(0, 0, 600, 600)
pointchosen = random.randint(0,len(listpoint)-1);
camera2.x = listpoint[pointchosen][0]
camera2.y = listpoint[pointchosen][1]
while running:
    # Look through all user actions / events
    for event in pygame.event.get():
        # If user clicks the "X" window button, close the game
        if event.type == pygame.QUIT:
            running = False
            hasquit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ton += 1;
            elif event.key == pygame.K_SPACE:
                print(x,y)
                appfile.write(f"\n{x},{y}")
                listpoint.append(x,y)
        if event.type == pygame.JOYBUTTONUP:
            print(event.button)
            if (event.button == 2):
                ton += 1
        if (ton == 2):
            running = False

    # Fill the screen background with a color (RGB format)
    screen.fill((40, 44, 52)) # Dark gray background
    if (ton < 2):
        screen.blit(tort[ton], (0, 0))
        if (ton < 2):
            screen.blit(tort[ton], (600, 0))

    # 5. Refresh the screen display
    pygame.display.flip()

    # Limit the game to 60 frames per second (FPS)
    clock.tick(60)
    clocker += 1
running = True;
while running:
    if (hasquit):
        running = false
    # Look through all user actions / events
    for event in pygame.event.get():
        # If user clicks the "X" window button, close the game
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print(upone[0], upone[1])
                camera.x = upone[0]
                camera.y = upone[1]
            elif event.key == pygame.K_DOWN:
                camera.x = downone[0]
                camera.y = downone[1]
            elif event.key == pygame.K_LEFT:
                camera.x = leftone[0]
                camera.y = leftone[1]
            elif event.key == pygame.K_RIGHT:
                camera.x = rightone[0]
                camera.y = rightone[1]
            if event.key == pygame.K_w:
                #print(upone[0], upone[1])
                camera2.x = upone2[0]
                camera2.y = upone2[1]
            elif event.key == pygame.K_s:
                camera2.x = downone2[0]
                camera2.y = downone2[1]
            elif event.key == pygame.K_a:
                camera2.x = leftone2[0]
                camera2.y = leftone2[1]
            elif event.key == pygame.K_d:
                camera2.x = rightone2[0]
                camera2.y = rightone2[1]
            elif event.key == pygame.K_SPACE:
                appfile.write(f"\n{camera.x},{camera.y}")
        if event.type == pygame.JOYBUTTONUP:
            print(event.button)
            if (event.instance_id == 1):
                if (event.button == 2):
                    camera.x = upone[0]
                    camera.y = upone[1]
                elif (event.button  == 3):
                    camera.x = downone[0]
                    camera.y = downone[1]
                elif (event.button  == 1):
                    camera.x = rightone[0]
                    camera.y = rightone[1]
                elif (event.button  == 0):
                    camera.x = leftone[0]
                    camera.y = leftone[1]
            else:
                if (event.button == 2):
                    camera2.x = upone[0]
                    camera2.y = upone[1]
                elif (event.button  == 3):
                    camera2.x = downone[0]
                    camera2.y = downone[1]
                elif (event.button  == 1):
                    camera2.x = rightone[0]
                    camera2.y = rightone[1]
                elif (event.button  == 0):
                    camera2.x = leftone[0]
                    camera2.y = leftone[1]
    # Fill the screen background with a color (RGB format)
    screen.fill((40, 44, 52)) # Dark gray background
    upone = [camera.x,camera.y]
    for one in listpoint:
        if (one[1] < camera.y and one[1] > camera.y-distall and one[0] > camera.x-distall  and one[0] < camera.x+distall ):
            if (upone[1] > one[1]):
                upone = one;
    ##print(downone)

    downone = [camera.x, camera.y]
    ##print(camera.x, camera.y,upone[1])
    for one in listpoint:
        if (one[1] > camera.y and one[1] < camera.y + distall and one[0] > camera.x - distall and one[0] < camera.x + distall):
            ##print(one[0],one[1])
            if (downone[1] > one[1]):
                downone = one;
    ##print(upone)

    leftone = [camera.x, camera.y]
    for one in listpoint:
        if (one[0] <camera.x and one[0] > camera.x - distall and one[1] > camera.y - distall and one[1] < camera.y + distall):
            if (leftone[0] > one[0]):
                leftone = one;
    #print(leftone)

    rightone = [camera.x, camera.y]
    for one in listpoint:
        if (one[0] > camera.x and one[0] < camera.x + distall and one[1] > camera.y - distall and one[1] < camera.y + distall):
            if (rightone[0] < one[0]):
                rightone = one;

    upone2 = [camera2.x, camera2.y]
    for one in listpoint:
        if (one[1] < camera2.y and one[1] > camera2.y - distall and one[0] > camera2.x - distall and one[
            0] < camera2.x + distall):
            if (upone2[1] > one[1]):
                upone2 = one;
    ##print(downone)

    downone2 = [camera2.x, camera2.y]
    for one in listpoint:
        if (one[1] > camera2.y and one[1] < camera2.y + distall and one[0] > camera2.x - distall and one[
            0] < camera2.x + distall):
            if (downone2[1] < one[1]):
                downone2 = one;
    ##print(upone)

    leftone2 = [camera2.x, camera2.y]
    for one in listpoint:
        if (one[0] < camera2.x and one[0] > camera2.x - distall and one[1] > camera2.y - distall and one[
            1] < camera.y + distall):
            if (leftone2[0] > one[0]):
                leftone2 = one;
    # print(leftone)

    rightone2 = [camera2.x, camera2.y]
    for one in listpoint:
        if (one[0] > camera2.x and one[0] < camera2.x + distall and one[1] > camera2.y - distall and one[
            1] < camera2.y + distall):
            if (rightone2[0] < one[0]):
                rightone2 = one;
    ##print(rightone)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_j]:
        camera.x -= speed
    if keys[pygame.K_l]:
        camera.x += speed
    if keys[pygame.K_i]:
        camera.y -= speed  # Pygame (0,0) is top-left, so up decrements Y
    if keys[pygame.K_k]:
        camera.y += speed
    if keys[pygame.K_f]:
        camera2.x -= speed
    if keys[pygame.K_h]:
        camera2.x += speed
    if keys[pygame.K_t]:
        camera2.y -= speed  # Pygame (0,0) is top-left, so up decrements Y
    if keys[pygame.K_g]:
        camera2.y += speed

    camera.x = max(0, min(camera.x, map.get_width() - camera.width))
    camera.y = max(0, min(camera.y, map.get_height() - camera.height))
    camera2.x = max(0, min(camera2.x, map.get_width() - camera.width))
    camera2.y = max(0, min(camera2.y, map.get_height() - camera.height))
    # --- Draw your game elements here ---
    visible_map = map.subsurface(camera)
    screen.blit(visible_map, (600, 0))
    visible_map = map.subsurface(camera2)
    screen.blit(visible_map, (0, 0))
    screen.blit(characterbad, (800, 200))
    screen.blit(character, (200, 200))

    if (abs(camera2.x-camera.x) <= 400 and abs(camera2.y-camera.y) <= 400):
        screen.blit(characterbad, ((camera2.x-camera.x)+200, (camera2.y-camera.y)+200))
    if (abs(camera2.x-camera.x) <= 400 and abs(camera2.y-camera.y) <= 400):
        screen.blit(character, ((camera2.x-camera.x)+800, (camera2.y-camera.y)+200))
    if (abs(camera2.x-camera.x) <= 40 and abs(camera2.y-camera.y) <= 40):
        running = False
    #screen.blit(map, (x+600, y))
    #screen.blit(character, (800, 200))
    font = pygame.font.SysFont("Arial", 36)
    text_surface = font.render(f"{camera.x}, {camera.y}", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(100, 300))
    screen.blit(text_surface, text_rect)

    # 5. Refresh the screen display
    pygame.display.flip()

    # Limit the game to 60 frames per second (FPS)
    clock.tick(60)
    clocker += 1
running = True
while running:
    # Look through all user actions / events
    for event in pygame.event.get():
        # If user clicks the "X" window button, close the game
        if event.type == pygame.QUIT:
            running = False
            hasquit = True


    # Fill the screen background with a color (RGB format)
    screen.fill((40, 44, 52)) # Dark gray background

    screen.blit(end, (0, 0))
    font = pygame.font.SysFont("Arial", 60)
    text_surface = font.render(f"{clocker}", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(300, 400))
    screen.blit(text_surface, text_rect)

    screen.blit(end, (600, 0))
    font = pygame.font.SysFont("Arial", 60)
    text_surface = font.render(f"{1000000-clocker}", True, (0, 0, 0))
    text_rect = text_surface.get_rect(center=(900, 400))
    screen.blit(text_surface, text_rect)

    # 5. Refresh the screen display
    pygame.display.flip()

    # Limit the game to 60 frames per second (FPS)
    clock.tick(60)

running = True;
# Clean up and close down properly
print("Game over")
print(f"Score {clocker}")
pygame.quit()
sys.exit()
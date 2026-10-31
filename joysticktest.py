import pygame

# Initialize Pygame and the joystick module
pygame.init()
pygame.joystick.init()
dance_pad = pygame.joystick.Joystick(0)
dance_pad.init()
# Check how many joysticks/controllers are connected
joystick_count = pygame.joystick.get_count()
print(f"Number of joysticks detected: {joystick_count}")

if joystick_count == 0:
    print("No L-TEK dance pad found. Make sure it is plugged into a USB port.")
else:
    # Initialize the first detected joystick
    dance_pad = pygame.joystick.Joystick(1)
    dance_pad.init()
    print(f"Connected Dance Pad: {dance_pad.get_name()}")
    print(f"Number of buttons: {dance_pad.get_numbuttons()}")
    print(f"Number of axes: {dance_pad.get_numaxes()}")
    print(f"Number of hats (D-pads): {dance_pad.get_numhats()}")

# Main loop to listen for pad steps/inputs
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Detect when a panel/button on the dance pad is stepped on
        if event.type == pygame.JOYBUTTONDOWN:
            print(f"Button DOWN: {event.button} on joystick {event.instance_id}")

        # Detect when the foot is lifted off the panel
        if event.type == pygame.JOYBUTTONUP:
            print(f"Button UP: {event.button} on joystick {event.instance_id}")

        # Some L-TEK configurations or adapters may map arrows to hats/D-pad
        if event.type == pygame.JOYHATMOTION:
            print(f"Hat motion: {event.value} on joystick {event.instance_id}")

    clock.tick(60)

pygame.quit()
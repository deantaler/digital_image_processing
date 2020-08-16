import sys
import cv2

# The script gets parameters: image path, radius, interpolation function
# 1 - nearest_neighbour 2
# 2 - bi_linear
# 3 - cubic

# globals
path = sys.argv[1]
img = cv2.imread(path, 0)
cv2.namedWindow('image')
drawing = False
prev_x = 0
prev_y = 0
target_x = 0
target_y = 0


def nearest_neighbour(x, y, delta_x, delta_y):

    new_color = img[x, y]

    # Right-down-hypo
    if (delta_x > 0) and (delta_y < 0):
        new_color += int(img[x+1, y-1])

    # Right-up-hypo
    elif (delta_x > 0) and (delta_y > 0):
        new_color += int(img[x+1, y+1])

    # Left-up-hypo
    elif (delta_x < 0) and (delta_y > 0):
        new_color += int(img[x-1, y+1])

    # Left-down-hypo
    elif (delta_x < 0) and (delta_y < 0):
        new_color += int(img[x-1, y-1])

    # Left
    elif (delta_x < 0) and (delta_y == 0):
        new_color += int(img[x-1, y])

    # Right
    elif (delta_x > 0) and (delta_y == 0):
        new_color += int(img[x+1, y])

        # Up
    elif (delta_x == 0) and (delta_y > 0):
        new_color += int(img[x, y+1])

        # Down
    elif (delta_x == 0) and (delta_y < 0):
        new_color += int(img[x, y-1])

    img[x, y] = new_color/2


def bi_linear(x, y, delta_x, delta_y):
    count = 4

    # Right-down-hypo
    if(delta_x < 0) and (delta_y < 0):
        new_color = (int(img[x, y]) + int(img[x, y-1]) + int(img[x-1, y]) + int(img[x-1, y-1]))

    # Left-up-hypo
    elif(delta_x > 0) and (delta_y > 0):
        new_color = (int(img[x, y]) + int(img[x, y+1]) + int(img[x+1, y]) + int(img[x+1, y+1]))

    # Left-down-hypo
    elif(delta_x > 0) and (delta_y < 0):
        new_color = (int(img[x, y]) + int(img[x, y-1]) + int(img[x+1, y]) + int(img[x+1, y-1]))

    # Right-up-hypo
    elif(delta_x < 0) and (delta_y > 0):
        new_color = (int(img[x, y]) + int(img[x, y+1]) + int(img[x-1, y]) + int(img[x-1, y+1]))

    # Left
    elif(delta_x > 0) and (delta_y == 0):
        new_color = (int(img[x, y]) + int(img[x+1, y]))
        count = 2

    # Right
    elif (delta_x < 0) and (delta_y == 0):
        new_color = (int(img[x, y]) + int(img[x-1, y]))
        count = 2

    # Up
    elif(delta_x == 0) and (delta_y > 0):
        new_color = (int(img[x, y]) + int(img[x, y+1]))
        count = 2

    # Down
    elif (delta_x == 0) and (delta_y < 0):
        new_color = (int(img[x, y]) + int(img[x, y-1]))
        count = 2

    new_color = new_color/int(count)
    img[x, y] = new_color


def cubic(x, y, delta_x, delta_y):

    new_color = img[x, y]

    # Right-down-hypo
    if (delta_x > 0) and (delta_y < 0):
        new_color += int(img[x, y-1]) + int(img[x, y-2]) + \
                     int(img[x+1, y]) + int(img[x+1, y-1]) + int(img[x+1, y-2]) + \
                     int(img[x+2, y]) + int(img[x+2, y-1]) + int(img[x+2, y-2])

    # Right-up-hypo
    elif (delta_x > 0) and (delta_y > 0):
        new_color += int(img[x, y+1]) + int(img[x, y+2]) + \
                     int(img[x+1, y]) + int(img[x+1, y+1]) + int(img[x+1, y+2]) + \
                     int(img[x+2, y]) + int(img[x+2, y+1]) + int(img[x+2, y+2])

    # Left-up-hypo
    elif (delta_x < 0) and (delta_y > 0):
        new_color += int(img[x, y+1]) + int(img[x, y+2]) + \
                     int(img[x-1, y]) + int(img[x-1, y+1]) + int(img[x-1, y+2]) + \
                     int(img[x-2, y]) + int(img[x-2, y+1]) + int(img[x-2, y+2])

    # Left-down-hypo
    elif (delta_x < 0) and (delta_y < 0):
        new_color += int(img[x, y-1]) + int(img[x, y-2]) + \
                     int(img[x-1, y]) + int(img[x-1, y-1]) + int(img[x-1, y-2]) + \
                     int(img[x-2, y]) + int(img[x-2, y-1]) + int(img[x-2, y-2])

    # Left
    elif (delta_x < 0) and (delta_y == 0):
        new_color += int(img[x, y-1]) + int(img[x, y+1]) + \
                     int(img[x-1, y]) + int(img[x-1, y-1]) + int(img[x-1, y+1]) + \
                     int(img[x-2, y]) + int(img[x-2, y-1]) + int(img[x-2, y+1])

    # Right
    elif (delta_x > 0) and (delta_y == 0):
        new_color += int(img[x, y-1]) + int(img[x, y+1]) + \
                     int(img[x+1, y]) + int(img[x+1, y-1]) + int(img[x+1, y+1]) + \
                     int(img[x+2, y]) + int(img[x+2, y-1]) + int(img[x+2, y+1])

        # Up
    elif (delta_x == 0) and (delta_y > 0):
        new_color += int(img[x, y+1]) + int(img[x, y+2]) + \
                     int(img[x+1, y]) + int(img[x+1, y+1]) + int(img[x+1, y+2]) + \
                     int(img[x-1, y]) + int(img[x-1, y+1]) + int(img[x-1, y+2])

        # Down
    elif (delta_x == 0) and (delta_y < 0):
        new_color += int(img[x, y-1]) + int(img[x, y-2]) + \
                     int(img[x+1, y]) + int(img[x+1, y-1]) + int(img[x+1, y-2]) + \
                     int(img[x-1, y]) + int(img[x-1, y-1]) + int(img[x-1, y-2])

    img[x, y] = new_color/9


def draw_circle(event, x, y, flags, param, radius=None):
    global drawing, prev_x, prev_y, target_x, target_y
    if event == cv2.EVENT_LBUTTONDOWN:
       drawing = True

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:

            target_x = x
            target_y = y
            radius = int(sys.argv[2])
            cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=20, maxRadius=20)

            # move over each pixel in the circle
            for pixel_x in range(target_x - radius, target_x + radius):
                for pixel_y in range(target_y - radius, target_y + radius):
                    dx = (pixel_x - target_x) * (pixel_x - target_x)
                    dy = (pixel_y - target_y) * (pixel_y - target_y)
                    distance_squared = dx + dy
                    radius_squared = radius * radius
                    if distance_squared <= radius_squared:
                        if int(sys.argv[3]) == 1:
                            nearest_neighbour(pixel_y, pixel_x, int(prev_y - y), int(prev_x - x))
                        if int(sys.argv[3]) == 2:
                            bi_linear(pixel_y, pixel_x, int(prev_y-y), int(prev_x-x))
                        if int(sys.argv[3]) == 3:
                            cubic(pixel_y, pixel_x, int(prev_y - y), int(prev_x - x))
            # save the prev position for calculate the delta between
            # the next (x,y) and found the direction of the mouseMove
            prev_x = x
            prev_y = y
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


def main():
    cv2.setMouseCallback('image', draw_circle)

    while(1):
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()


if __name__== "__main__":
    main()

### last update 09:32 29.11
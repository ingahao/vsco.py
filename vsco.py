"""
File: vsco.py
The user answers a series of questions about qualities they want their picture
to have. The program will return the original photo and the edited photo with
a popular VSCO filter with a brief description based on the user's responses.
"""

from simpleimage import SimpleImage


def main():
    count = 0
    print("Welcome to the VSCO filter algorithm!")
    start = str(input("Do you have a photo you'd like to edit? (y/n): "))
    while start == 'y':
        print("Make sure your image is the same folder as this file.")
        filename = str(input("Type in the full image name: "))
        image = SimpleImage(filename)
        quiz(image, count)
        start = str(input("Want to try a different image/filter? (y/n): "))
    thanks()


def quiz(image, count):
    print("This algorithm will place a VSCO filter on your photo based on your responses.")
    print("Instructions: select your answer by typing in a, b, c, or d.")
    question_one(image, count)


def question_one(image, count):
    print("")
    print("------ 1 ------")
    print("Question 1: What's the main focus of this picture?")
    print("a. person or animal")
    print("b. object")
    print("c. landscape")
    response_1 = input("Type a, b, or c and hit enter: ")
    if response_1 == 'a':
        count += 1  # person or animal
    if response_1 == 'b':
        count += 2  # object
    if response_1 == 'c':
        count += 3  # landscape
    vibe(image, count)


def vibe(image, count):
    print("")
    print("------ 2 ------")
    print("Question 2: What's the vibe you're looking for?")
    print("a. vibrant")
    print("b. a natural 'no-filter' look")
    print("c. black and white")
    print("d. vintage")
    response_2 = input("Type a, b, c, or d and hit enter: ")
    if response_2 == 'a':  # vibrant
        tone(image, count)
    if response_2 == 'b':  # natural no-filter
        brightness(image, count)
    if response_2 == 'c':  # black and white
        print("")
        if count == 1:
            print("The VSCO filter you should use is B1!")
            B1(image)
        if count != 1:
            print("The VSCO filter you should use is B5!")
            B5(image)
    if response_2 == 'd':  # vintage
        vintage_tone(image, count)


def tone(image, count):
    print("")
    print("------ 3 ------")
    print("Question 3: What tones do you want your picture to have?")
    print("a. warm")
    print("b. cool")
    print("c. general vibrancy")
    response_3 = input("Type a, b, or c and hit enter: ")
    if response_3 == 'a':
        print("")
        print("The VSCO filter you should use is OAK3!")
        OAK3(image)
    if response_3 == 'b':
        print("")
        print("The VSCO filter you should use is F5!")
        F5(image)
    if response_3 == 'c':
        if count == 1:
            setting(image)
        if count != 1:
            print("")
            print("The VSCO filter you should use is C1!")
            C1(image)


def setting(image):  # additional question for "person / animal" selections only
    print("")
    print("------ 4 ------")
    print("Question 4: What kind of theme do you want?")
    print("a. light & bright")
    print("b. dark & edgy")
    response_4 = input("Type a or b and hit enter: ")
    print("")
    if response_4 == 'a':
        print("The VSCO filter you should use is F2!")
        F2(image)
    if response_4 == 'b':
        print("The VSCO filter you should use is M5!")
        M5(image)


def brightness(image, count):
    print("")
    print("------ 3 ------")
    print("Question 3: What level of light do you want to your picture to have?")
    print("a. brighter!")
    print("b. darker!")
    response_brightness = input("Type a or b and hit enter: ")
    print("")
    if response_brightness == 'a':
        print("The VSCO filter you should use is A6!")
        A6(image)
    if response_brightness == 'b':
        if count == 2:
            print("The VSCO filter you should use is NC!")
            NC(image)
        if count != 2:
            print("The VSCO filter you should use is HB2!")
            HB2(image)


def vintage_tone(image, count):
    print("")
    print("------ 3 ------")
    print("Question 3: What tones do you want your picture to have?")
    print("a. warm")
    print("b. cool")
    response_vintage_tone = input("Type a or b and hit enter: ")
    print("")
    if response_vintage_tone == 'a':
        if count == 1:
            print("The VSCO filter you should use is DOG1!")
            DOG1(image)
        if count != 1:
            print("The VSCO filter you should use is OAK1!")
            OAK1(image)
    if response_vintage_tone == 'b':
        if count == 3:
            print("The VSCO filter you should use is A5!")
            A5(image)
        if count != 3:
            print("The VSCO filter you should use is T1!")
            T1(image)


# BELOW ARE THE 14 FILTERS:

def OAK3(image):
    print("OAK3 gives your photos a peachy & purple look that picks up pinkish tones and softens whites.")
    process()
    image.show()
    for pixel in image:
        pixel.red *= 1.08
        pixel.green *= 0.95
        pixel.blue *= 1.03
    image.show()


def F5(image):
    print("F5 adds a blue tint to your photo, accentuating undertones of cooler shades.")
    process()
    image.show()
    for pixel in image:
        pixel.red *= 0.91
        pixel.green *= 1.05
        pixel.blue *= 1.2
    image.show()


def F2(image):
    print("This light filter brightens whites, and is a light theme for any feed for humans & animal subjects alike.")
    process()
    image.show()
    for pixel in image:
        pixel.red = pixel.red * 1.05
        pixel.green = pixel.green * 1.12
        pixel.blue = pixel.blue * 1.17
    image.show()


def M5(image):
    print("This bold filter adds a flair of modern grunge to any person, exuding an edgy and bold vibe.")
    process()
    image.show()
    for pixel in image:
        pixel.red -= 30
        pixel.green -= 20
        pixel.blue -= 20
    image.show()


def A6(image):
    print("A6 gives a subtle, clean brightness while adding warmth to the richer tones in humans and objects.")
    process()
    image.show()
    for pixel in image:
        pixel.red = pixel.red * 1.1
        pixel.green = pixel.green * 1.2 - 10
        pixel.blue = pixel.blue * 1.1
    image.show()


def HB2(image):
    print("This filter will draw attention to those dark elements in your photo, producing a dramatic effect.")
    process()
    image.show()
    for pixel in image:
        pixel.red -= 22
        pixel.green -= 22
        pixel.blue -= 22
    image.show()


def B1(image):
    print("This simple b&w filter adds class to people or objects, and it's a lighter counterpart to the B5 filter.")
    process()
    image.show()
    for pixel in image:
        avg_color = (pixel.red + pixel.green + pixel.blue) // 3
        pixel.red = avg_color
        pixel.green = avg_color
        pixel.blue = avg_color
    image.show()


def B5(image):
    print("B5 brings out more shadows than its B1 counterpart, which is ideal for food/drink or landscape photos.")
    process()
    image.show()
    for pixel in image:
        avg_color = (pixel.red + pixel.green + pixel.blue) // 3
        pixel.red = avg_color - 17
        pixel.green = avg_color - 17
        pixel.blue = avg_color - 17
    image.show()


def DOG1(image):
    print("This appropriately-named filter mutes brights and achieves an elegant, serene look on pets & humans alike.")
    process()
    image.show()
    for pixel in image:
        pixel.red *= 0.8
        pixel.green *= 0.7
        pixel.blue *= 0.6
    image.show()


def T1(image):
    print("With cool undertones and muted brights, T1 provides a dusty, vintage look on pets and humans alike.")
    process()
    image.show()
    for pixel in image:
        pixel.red *= 0.85
        pixel.green *= 0.85
        pixel.blue = pixel.blue // 1.3
    image.show()


def C1(image):
    print("This versatile filter saturates warm and cool tone colors, giving a summery feel to any scenery or object.")
    process()
    image.show()
    for pixel in image:
        pixel.red *= 1.1
        pixel.green *= 1.1
        pixel.blue = pixel.blue * 1.2 - 20
    image.show()


def NC(image):
    print("This filter will pick up warm tones nicely for any object and dim bright spots, creating a sultry vibe.")
    process()
    image.show()
    for pixel in image:
        pixel.red = pixel.red * 0.8 ** 1.3
        pixel.green *= 0.8
        pixel.blue *= 0.8
    image.show()


def OAK1(image):
    print("OAK1 gives an indie retro look, ideal for any object or scenery with a light backgrounds.")
    process()
    image.show()
    for pixel in image:
        pixel.red *= 1.2
        pixel.green *= 1.2
        pixel.blue *= 1.05
    image.show()


def A5(image):
    print("A5 is a unique filter that works best on cool-toned landscapes that offers a surreal twist on reality.")
    process()
    image.show()
    for pixel in image:
        pixel.red *= 0.75
        pixel.green *= 0.8
        pixel.blue *= 0.9
    image.show()


def process():
    print("processing filter...")


"""
def pick_another(image):
    print("a. OAK3")
    print("b. F5")
    print("c. F2")
    print("d. M5")
    print("e. A6")
    print("f. HB2")
    print("g. B1")
    print("h. DOG1")
    print("i. T1")
    print("j. C1")
    print("k. NC")
    print("l. B5")
    print("m. OAK1")
    print("n. A5")

    ans = str(input("Which filter do you want to try next? Type any letter 'a' through 'n': "))
    if ans == 'a':
        OAK3(image)
    if ans == 'b':
        F5(image)
    if ans == 'c':
        F2(image)
    if ans == 'd':
        M5(image)
    if ans == 'e':
        A6(image)
    if ans == 'f':
        HB2(image)
    if ans == 'g':
        B1(image)
    if ans == 'h':
        DOG1(image)
    if ans == 'i':
        T1(image)
    if ans == 'j':
        C1(image)
    if ans == 'k':
        NC(image)
    if ans == 'l':
        B5(image)
    if ans == 'm':
        OAK1(image)
    if ans == 'n':
        A5(image)
"""


def thanks():
    print("Thanks for using the VSCO filter algorithm!")


if __name__ == '__main__':
    main()

import re

# -------------------------------------------------------------------Templates dictionary---------------------------------------------------------------------
templates = {
    1: "One day, a [adjective] [noun] decided to [verb] at the [place]. Everyone was [adjective] when they saw it [verb] with a [noun]. People couldn't stop [verb]-ing. It was the [adjective] day ever!",
    2: "Did you know that the [noun] was first discovered in [year]? It is used to [verb] in [place] and is considered [adjective] for [noun]. Scientists say that [noun] can even [verb], making it truly [adjective] for [field of study].",
    3: "On a [adjective] night, [name] walked into the [place], holding a [noun]. Suddenly, they heard a [adjective] noise coming from the [noun]. They tried to [verb], but the [adjective] [noun] wouldn’t let them. It was the beginning of their [adjective] nightmare!",
    4: "The [adjective] agent, [name], was on a mission to [verb] the stolen [noun] from the [place]. With only a [noun] in their hand, they had to [verb] through [adjective] obstacles. In the end, they [verb] the day and became the [adjective] hero of [place].",
    5: "In the magical land of [place], there lived a [adjective] [noun] who possessed a [adjective] [noun]. The [noun] could [verb], and it was the key to saving the [adjective] kingdom from the evil [noun]. Only by [verb]-ing the [adjective] spell could they restore peace."
}

# --------------------------------------------------------------- Function Definitions -------------------------------------------------------------------
def welcome_screen():
    print("🎉 Welcome to the Mad Libs Game!")
    input("Press Enter to continue...")

def introduction():
    print("\n📚 What is Mad Libs?")
    print("Mad Libs is a fun game where YOU fill in the blanks to create a custom story!")
    print("You'll provide words like nouns, verbs, and adjectives, and watch the story come to life!")
    input("Press Enter to continue...")

def choose_template():
    print("\n📝 Choose a Template")
    templates_list = [
        "Fun/Comedy", 
        "Knowledge/Educational", 
        "Horror", 
        "Action", 
        "Fantasy"
    ]

    for index, genre in enumerate(templates_list):
        print(f"{index + 1}. {genre}")
    
    while True:
        try:
            choice = int(input("Select a template by number (1-5): "))
            if choice in templates:
                return templates[choice]
            else:
                print("Please enter a valid number (1-5).")
        except ValueError:
            print("Invalid input. Please enter a number.")

def fill_in_the_blanks(template):
    print("\n🖊️ Fill in the Blanks")
    placeholders = re.findall(r"\[(\w+)]", template)
    inputs = {}

    for placeholder in placeholders:
        inputs[placeholder] = input(f"Enter a {placeholder}: ")

    filled_story = template
    for key, value in inputs.items():
        filled_story = re.sub(f"\\[{key}\\]", value, filled_story, count=1)

    return filled_story

def display_story(filled_story):
    print("\n🎉 Your Story")
    print(filled_story)
    input("\nPress Enter to play again or exit.")

# --------------------------------------------------------------- Main Program -------------------------------------------------------------------
def main():
    while True:
        welcome_screen()
        introduction()
        selected_template = choose_template()
        filled_story = fill_in_the_blanks(selected_template)
        display_story(filled_story)

if __name__ == "__main__":
    main()

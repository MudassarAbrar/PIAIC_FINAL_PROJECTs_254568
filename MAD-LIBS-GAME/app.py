import streamlit as st
import re

#==============================================================Templates dictionary===============================================
templates = {
    1: "One day, a [adjective] [noun] decided to [verb] at the [place]. Everyone was [adjective] when they saw it [verb] with a [noun]. People couldn't stop [verb]-ing. It was the [adjective] day ever!",
    2: "Did you know that the [noun] was first discovered in [year]? It is used to [verb] in [place] and is considered [adjective] for [noun]. Scientists say that [noun] can even [verb], making it truly [adjective] for [field of study].",
    3: "On a [adjective] night, [name] walked into the [place], holding a [noun]. Suddenly, they heard a [adjective] noise coming from the [noun]. They tried to [verb], but the [adjective] [noun] wouldn’t let them. It was the beginning of their [adjective] nightmare!",
    4: "The [adjective] agent, [name], was on a mission to [verb] the stolen [noun] from the [place]. With only a [noun] in their hand, they had to [verb] through [adjective] obstacles. In the end, they [verb] the day and became the [adjective] hero of [place].",
    5: "In the magical land of [place], there lived a [adjective] [noun] who possessed a [adjective] [noun]. The [noun] could [verb], and it was the key to saving the [adjective] kingdom from the evil [noun]. Only by [verb]-ing the [adjective] spell could they restore peace."
}

#============================================================ Initialize session state=======================================================
if "page" not in st.session_state:
    st.session_state.page = 1
if "inputs" not in st.session_state:
    st.session_state.inputs = {}
if "filled_story" not in st.session_state:
    st.session_state.filled_story = ""
if "selected_template" not in st.session_state:
    st.session_state.selected_template = ""

#=========================================================Navigation function====================================================================
def go_to_page(page):
    st.session_state.page = page

# ========================================================Page 1: Welcome Screen=================================================================
if st.session_state.page == 1:
    st.title("🎉 Welcome to the Mad Libs Game!")
    st.write("Get ready to create your own hilarious and unique story! 😊")
    st.button("Next", on_click=lambda: go_to_page(2))

# ==========================================================Page 2: Introduction=================================================================
if st.session_state.page == 2:
    st.title("📚 What is Mad Libs?")
    st.write("Mad Libs is a fun game where YOU fill in the blanks to create a custom story!")
    st.write("You'll provide words like nouns, verbs, and adjectives, and watch the story come to life!")
    st.button("Next", on_click=lambda: go_to_page(3))

# ========================================================Page 3: Template Selection=================================================================
if st.session_state.page == 3:
    st.title("📝 Choose a Template")
    genres = [
        "Fun/Comedy", 
        "Knowledge/Educational", 
        "Horror", 
        "Action", 
        "Fantasy"
    ]

    for index, genre in enumerate(genres):
        st.write(f"{index + 1}. {genre}")

    genre = st.selectbox("Select a template by number:", range(1, 6))
    st.session_state.selected_template = templates[genre]
    st.button("Start Story", on_click=lambda: go_to_page(4))

# =================================================================Page 4: Fill in the Blanks============================================================
if st.session_state.page == 4:
    st.title("🖊️ Fill in the Blanks")
    selected_template = st.session_state.selected_template

    # Extract placeholders
    placeholders = re.findall(r"\[(\w+)]", selected_template)

    # =================================================================Create inputs=================================================================
    for x, placeholder in enumerate(placeholders):
        if f"{x}{placeholder}" not in st.session_state.inputs:
            st.session_state.inputs[placeholder] = ""
        st.session_state.inputs[placeholder] = st.text_input(
            f"Enter a {placeholder}:",
            st.session_state.inputs[placeholder],
            key=f"{placeholder}{x}" # Use unique keys for each input
        )
    st.button("Generate Story",on_click=lambda:go_to_page(5))
    # Generate Story Button
if st.session_state.page == 5:
        filled_story = st.session_state.selected_template
        for key, value in st.session_state.inputs.items():
            filled_story = re.sub(f"\\[{key}\\]", value, filled_story)

        # Save the filled story and go to the next page
        st.session_state.filled_story = filled_story
        st.button("CLICK TO SEE YOUR STORY 😎  " , on_click= lambda:go_to_page(6))


#================================================================= Page 5: Display the Story=================================================================
if st.session_state.page == 6:
    filled_story = st.session_state.selected_template
    for key, value in st.session_state.inputs.items():
        filled_story = re.sub(f"\\[{key}\\]", value, filled_story)

    st.session_state.filled_story = filled_story

    st.title("🎉 Your Story")
    st.write(st.session_state.filled_story)
    st.button("Play Again", on_click=lambda: go_to_page(1))

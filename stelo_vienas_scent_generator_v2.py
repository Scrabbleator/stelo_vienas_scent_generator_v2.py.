import streamlit as st

# Define character classes and their unique traits
character_classes = {
    "Alliance Swordsman": "Brave, Loyal, Honorable",
    "Cleric": "Wise, Compassionate, Calm",
    "Archer": "Precise, Agile, Focused",
    "Tracker": "Stealthy, Intuitive, Resilient",
    "Prelate's Chapter Swordsman": "Disciplined, Virtuous, Protector",
    "Hordesman": "Fierce, Wild, Unpredictable",
    "Fang Warrior (Solandrys)": "Loyal, Fierce, Tenacious",
    "Iron Legion Veteran": "Resilient, Stoic, Battle-Hardened",
    "Vontharian Legionnaire": "Strategic, Skilled, Traditional",
    "Bandit": "Cunning, Resourceful, Bold",
    "Champion Swordsman": "Masterful, Courageous, Determined"
}

# Define scent families and their fragrance notes
scent_families = {
    "Citrus": ["Lemon", "Bergamot", "Grapefruit", "Orange"],
    "Floral": ["Jasmine", "Rose", "Lavender", "White Lily"],
    "Woody": ["Cedar", "Sandalwood", "Pine", "Oak"],
    "Spicy": ["Cinnamon", "Pepper", "Clove", "Nutmeg"],
    "Herbal": ["Mint", "Thyme", "Basil", "Sage"],
    "Earthy": ["Moss", "Patchouli", "Vetiver", "Earth"],
    "Smoky": ["Tobacco", "Leather", "Burnt Wood", "Ash"]
}

# Function to generate a unique scent profile
def generate_scent_profile(character_class, selected_notes):
    class_traits = character_classes.get(character_class, "Unique")
    profile = f"**Character Class:** {character_class}\n\n**Traits:** {class_traits}\n\n**Scent Notes:** {', '.join(selected_notes)}"
    return profile

# Set up page configuration with a custom title and icon
st.set_page_config(page_title="Stelo Vienas Scent Generator v2", page_icon="✨")

# Custom CSS for styling, including dark-mode-compatible text color
st.markdown("""
    <style>
    /* Background color for app */
    .main { background-color: #f7f1e3; color: #333; }
    /* Styling for the final reveal box with readable text in Dark Mode */
    .reveal-box { border: 2px solid #b47e5f; padding: 20px; margin-top: 20px; background-color: #fbf3e3; border-radius: 10px; box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2); color: #333; }
    /* Font styling */
    h1, h2, h3 { color: #5b2c6f; font-family: 'Georgia', serif; }
    /* Option styling */
    .option-box { padding: 8px; border-radius: 5px; margin-bottom: 10px; font-size: 1.1em; transition: background-color 0.3s ease; }
    .option-box:hover { background-color: #e0e4cc; }
    </style>
    """, unsafe_allow_html=True)

# App Title and Intro
st.title("✨ Discover Your Signature Scent in *Stelo Vienas* v2 ✨")
st.write("Follow the steps to reveal a unique scent profile that reflects your character and personality.")

# Step 1: Character Class Selection
st.header("Step 1: Choose Your Character Class")
character_class = st.selectbox("Select your character class:", list(character_classes.keys()))

# Step 2: Scent Selection with Decorative Boxes
st.header("Step 2: Choose Your Scent Notes (Up to 4)")
selected_notes = []

# Display scent families with styled options
for family, notes in scent_families.items():
    if len(selected_notes) < 4:
        selected_note = st.selectbox(f"Choose a note from the {family} family:", notes, key=family)
        if selected_note and selected_note not in selected_notes:
            selected_notes.append(selected_note)

# Step 3: Reveal Profile in a Styled Box
if st.button("Reveal Your Signature Scent Profile") and selected_notes:
    profile = generate_scent_profile(character_class, selected_notes)
    st.markdown(f"<div class='reveal-box'><h2>Your Character Class: {character_class}</h2><p><strong>Character Traits:</strong> {character_classes.get(character_class, 'Unique')}</p><p><strong>Scent Notes:</strong> {', '.join(selected_notes)}</p></div>", unsafe_allow_html=True)
else:
    st.write("Please select up to 4 unique scent notes to create your profile.")

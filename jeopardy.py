import streamlit as st
import pandas as pd
import time

# --- 1. Custom CSS for Uniform "Blue Graph" TV Look ---
st.markdown("""
<style>
    .stApp { background-color: #000033; }
    h3 {
        color: #FFCC00 !important;
        text-align: center;
        text-transform: uppercase;
        font-family: 'Arial Black', Gadget, sans-serif;
        text-shadow: 2px 2px #000000;
        min-height: 120px !important; 
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.1rem !important;
        margin-bottom: 20px !important;
    }
    .stButton > button {
        background-color: #060ce9 !important;
        color: #FFCC00 !important;
        border: 3px solid #FFCC00 !important;
        height: 100px !important;
        width: 100% !important;
        font-size: 32px !important;
        font-weight: bold !important;
        border-radius: 5px !important;
    }
    .stButton > button:hover {
        border-color: #FFFFFF !important;
        color: #FFFFFF !important;
    }
    .stButton > button:disabled {
        background-color: #000022 !important;
        color: #444444 !important;
        border: 2px solid #222222 !important;
        height: 100px !important;
    }
    .stTabs [data-baseweb="tab-list"] { background-color: #060ce9; padding: 10px; }
    .stTabs [data-baseweb="tab"] { color: white !important; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- 2. Load Data ---
@st.cache_data
def load_data():
    return pd.DataFrame([
        {"Category": "Animal Kingdom", "Points": 100, "Question": "This 'King of the Jungle' is known for its loud roar and thick mane. [cite: 1]", "Answer": "What is a Lion? [cite: 1]"},
        {"Category": "Animal Kingdom", "Points": 200, "Question": "These animals, like frogs and toads, can live both in the water and on land. [cite: 1]", "Answer": "What are Amphibians? [cite: 1]"},
        {"Category": "Animal Kingdom", "Points": 300, "Question": "This is the only mammal capable of true, powered flight. [cite: 1]", "Answer": "What is a Bat? [cite: 1]"},
        {"Category": "Animal Kingdom", "Points": 400, "Question": "These 'cold-blooded' animals rely on external heat sources to regulate their body temperature. [cite: 1]", "Answer": "What are Ectotherms? [cite: 1]"},
        {"Category": "Animal Kingdom", "Points": 500, "Question": "Most animals exhibit this type of symmetry, where the body can be divided into identical left and right halves. [cite: 1]", "Answer": "What is Bilateral Symmetry? [cite: 1]"},
        {"Category": "Our Changing Earth", "Points": 100, "Question": "This is the process of water falling from the clouds as rain, snow, or hail. [cite: 1]", "Answer": "What is Precipitation? [cite: 1]"},
        {"Category": "Our Changing Earth", "Points": 200, "Question": "This is the name for a scientist who studies the weather. [cite: 1]", "Answer": "What is a Meteorologist? [cite: 1]"},
        {"Category": "Our Changing Earth", "Points": 300, "Question": "This is the layer of gas that surrounds the Earth and protects us from the sun's UV rays. [cite: 1]", "Answer": "What is the Atmosphere? [cite: 1]"},
        {"Category": "Our Changing Earth", "Points": 400, "Question": "This theory explains how Earth's outer shell is divided into several plates that glide over the mantle. [cite: 1]", "Answer": "What is Plate Tectonics? [cite: 1]"},
        {"Category": "Our Changing Earth", "Points": 500, "Question": "This specific type of rock is formed through the cooling and solidification of magma or lava. [cite: 1]", "Answer": "What is Igneous rock? [cite: 1]"},
        {"Category": "Plants & Photosynthesis", "Points": 100, "Question": "This part of the plant grows underground and drinks up water. [cite: 1]", "Answer": "What are Roots? [cite: 1]"},
        {"Category": "Plants & Photosynthesis", "Points": 200, "Question": "Plants use this green pigment to capture sunlight and make food. [cite: 1]", "Answer": "What is Chlorophyll? [cite: 1]"},
        {"Category": "Plants & Photosynthesis", "Points": 300, "Question": "This is the process by which a seed begins to grow into a seedling. [cite: 1]", "Answer": "What is Germination? [cite: 1]"},
        {"Category": "Plants & Photosynthesis", "Points": 400, "Question": "These tiny pores on the underside of leaves allow for gas exchange. [cite: 1]", "Answer": "What are Stomata? [cite: 1]"},
        {"Category": "Plants & Photosynthesis", "Points": 500, "Question": "This vascular tissue in plants is responsible for transporting water from the roots to the leaves. [cite: 1]", "Answer": "What is Xylem? [cite: 1]"},
        {"Category": "Ecology & Habitats", "Points": 100, "Question": "This sandy habitat receives very little rain and is home to camels and cacti. [cite: 1]", "Answer": "What is a Desert? [cite: 1]"},
        {"Category": "Ecology & Habitats", "Points": 200, "Question": "This term describes an animal that only eats plants. [cite: 1]", "Answer": "What is a Herbivore? [cite: 1]"},
        {"Category": "Ecology & Habitats", "Points": 300, "Question": "This is a community of living organisms interacting with their physical environment. [cite: 1]", "Answer": "What is an Ecosystem? [cite: 1]"},
        {"Category": "Ecology & Habitats", "Points": 400, "Question": "This is the position an organism occupies in a food web, such as producer or primary consumer. [cite: 1]", "Answer": "What is a Trophic Level? [cite: 1]"},
        {"Category": "Ecology & Habitats", "Points": 500, "Question": "This rule states that only a percentage of energy is transferred from one level to the next. [cite: 1]", "Answer": "What is the 10% Rule? [cite: 1]"},
        {"Category": "Conservation & Climate", "Points": 100, "Question": "To help the Earth, people practice the '3 Rs': Reduce, Reuse, and this. [cite: 1]", "Answer": "What is Recycle? [cite: 1]"},
        {"Category": "Conservation & Climate", "Points": 200, "Question": "This is the term for a species that is at risk of disappearing forever. [cite: 1]", "Answer": "What is Endangered? [cite: 1]"},
        {"Category": "Conservation & Climate", "Points": 300, "Question": "These are non-renewable energy sources, like coal and oil, formed from ancient organic matter. [cite: 1]", "Answer": "What are Fossil Fuels? [cite: 1]"},
        {"Category": "Conservation & Climate", "Points": 400, "Question": "This is the variety of life in the world or in a particular habitat. [cite: 1]", "Answer": "What is Biodiversity? [cite: 1]"},
        {"Category": "Conservation & Climate", "Points": 500, "Question": "This natural process warms the Earth's surface when gases trap the sun's heat. [cite: 1]", "Answer": "What is the Greenhouse Effect? [cite: 1]"}
    ])

df = load_data()
categories = df['Category'].unique()

# --- 3. Session State ---
if "players" not in st.session_state:
    st.session_state.update({
        "players": {}, "answered": [], "current_q": None, 
        "show_answer": False, "final_triggered": False, 
        "final_q_revealed": False, "final_a_revealed": False, "winner": None
    })

# --- 4. Sidebar ---
with st.sidebar:
    st.title("Host Admin")
    new_p = st.text_input("Player Name")
    if st.button("Add Player") and new_p:
        st.session_state.players[new_p] = 0
        st.rerun()
    st.divider()
    if not st.session_state.final_triggered:
        if st.button("🔥 FINAL JEOPARDY", type="primary"):
            st.session_state.final_triggered = True
            st.rerun()
    else:
        if st.button("↩️ BOARD"):
            st.session_state.final_triggered = False
            st.session_state.final_q_revealed = False
            st.session_state.final_a_revealed = False
            st.rerun()
    if st.button("Reset All"):
        st.session_state.clear()
        st.rerun()

# --- 5. Tabs ---
tab1, tab2 = st.tabs(["🎮 GAME BOARD", "🏆 LEADERBOARD"])

with tab1:
    if st.session_state.winner:
        st.balloons()
        st.title(f"🥇 THE WINNER IS {st.session_state.winner.upper()}!")
        if st.button("Back to Game"):
            st.session_state.winner = None
            st.rerun()

    elif st.session_state.final_triggered:
        st.title("🏆 FINAL JEOPARDY")
        st.markdown("### Category: Atmospheric Chemistry")
        
        if not st.session_state.final_q_revealed:
            if st.button("REVEAL FINAL QUESTION", use_container_width=True):
                st.session_state.final_q_revealed = True
                st.rerun()
        
        if st.session_state.final_q_revealed:
            st.warning("### Identify the specific chemical compound that acts as the primary catalyst for stratospheric ozone depletion and explain the process of 'Radiative Forcing' as it pertains to its global warming potential.")
            
            if not st.session_state.final_a_revealed:
                if st.button("REVEAL FINAL ANSWER"):
                    st.session_state.final_a_revealed = True
                    st.rerun()
            
            if st.session_state.final_a_revealed:
                st.success("### Answer: Chlorofluorocarbons (CFCs); Radiative Forcing is the difference between incoming solar radiation and outgoing infrared radiation, caused here by gas trapping long-wave heat.")
                st.balloons()
    
    elif st.session_state.current_q is None:
        cols = st.columns(len(categories))
        for i, cat in enumerate(categories):
            with cols[i]:
                st.markdown(f"### {cat}")
                cat_qs = df[df['Category'] == cat].sort_values('Points')
                for _, row in cat_qs.iterrows():
                    q_id = f"{cat}-{row['Points']}"
                    if q_id in st.session_state.answered:
                        st.button("X", key=q_id, disabled=True)
                    else:
                        if st.button(f"${row['Points']}", key=q_id):
                            st.session_state.current_q = row
                            st.rerun()
    else:
        q = st.session_state.current_q
        st.info(f"{q['Category']} - ${q['Points']}")
        st.markdown(f"## {q['Question']}")
        
        if not st.session_state.show_answer:
            if st.button("REVEAL ANSWER", use_container_width=True):
                st.session_state.show_answer = True
                st.rerun()
        else:
            st.success(f"### {q['Answer']}")
            st.write("---")
            st.write("### Assign Points")
            p_cols = st.columns(max(len(st.session_state.players), 1))
            for i, name in enumerate(st.session_state.players):
                col_correct, col_wrong = p_cols[i].columns(2)
                if col_correct.button("✅", key=f"c_{name}"):
                    st.session_state.players[name] += q['Points']
                    st.balloons()
                    time.sleep(1) 
                    st.session_state.answered.append(f"{q['Category']}-{q['Points']}")
                    st.session_state.current_q, st.session_state.show_answer = None, False
                    st.rerun()
                if col_wrong.button("❌", key=f"w_{name}"):
                    st.session_state.players[name] -= q['Points']
                    st.snow()
                    time.sleep(1)
                    st.rerun()
            if st.button("Skip Question"):
                st.session_state.answered.append(f"{q['Category']}-{q['Points']}")
                st.session_state.current_q, st.session_state.show_answer = None, False
                st.rerun()

with tab2:
    st.header("Current Rankings")
    if st.session_state.players:
        sorted_p = dict(sorted(st.session_state.players.items(), key=lambda item: item[1], reverse=True))
        for name, score in sorted_p.items():
            c1, c2, c3, c4, c5 = st.columns([2, 1, 1, 1, 1.5])
            c1.markdown(f"## {name}")
            c2.markdown(f"## ${score}")
            if c3.button("+$100", key=f"add_{name}"): st.session_state.players[name] += 100; st.rerun()
            if c4.button("-$100", key=f"sub_{name}"): st.session_state.players[name] -= 100; st.rerun()
            if c5.button("🏆 WINNER", key=f"win_{name}"):
                st.session_state.winner = name
                st.rerun()
            st.divider()
    else:
        st.info("Add players in the sidebar to start.")
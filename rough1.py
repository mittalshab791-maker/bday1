import streamlit as st
from datetime import datetime

# Page Configuration
st.set_page_config(
    page_title="Secret Birthday Surprise! ❤️",
    page_icon="👑",
    layout="centered"
)

# 🔑 SECRET PASSWORD SETUP
SECRET_PASSWORD = "Vi@240307"

# Custom CSS for Styling & Cute Envelope Design
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #ffb6c1 0%, #fecfef 50%, #fda085 100%);
        overflow-x: hidden;
    }

    /* Force Dark Text Colors Globally */
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #2c2c2c !important;
    }

    /* Cute Emoji Mascots at Bottom Corners */
    .mascot-left {
        position: fixed;
        bottom: 20px;
        left: 20px;
        font-size: 3.5rem;
        z-index: 999;
        animation: pulseBounce 2s infinite ease-in-out;
        pointer-events: none;
    }

    .mascot-right {
        position: fixed;
        bottom: 20px;
        right: 20px;
        font-size: 3.5rem;
        z-index: 999;
        animation: pulseBounce 2.5s infinite ease-in-out;
        pointer-events: none;
    }

    @keyframes pulseBounce {
        0%, 100% { transform: translateY(0) scale(1); }
        50% { transform: translateY(-12px) scale(1.1); }
    }

    /* Pure CSS Floating Butterflies/Hearts */
    .floating-item {
        position: fixed;
        font-size: 2rem;
        z-index: 998;
        pointer-events: none;
        animation: floatUp 8s linear infinite;
        opacity: 0.8;
    }

    .item-1 { left: 10%; animation-delay: 0s; }
    .item-2 { left: 35%; animation-delay: 3s; }
    .item-3 { left: 65%; animation-delay: 1s; }
    .item-4 { left: 85%; animation-delay: 5s; }

    @keyframes floatUp {
        0% { transform: translateY(100vh) rotate(0deg); opacity: 0; }
        20% { opacity: 0.9; }
        80% { opacity: 0.9; }
        100% { transform: translateY(-10vh) rotate(360deg); opacity: 0; }
    }

    /* Glassmorphism Card Effect */
    .glass-card {
        background: rgba(255, 255, 255, 0.85);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.9);
        padding: 30px;
        box-shadow: 0 8px 32px 0 rgba(255, 105, 135, 0.25);
        margin-bottom: 25px;
        text-align: center;
    }

    /* Lock Card Effect */
    .lock-card {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 35px;
        box-shadow: 0 10px 30px rgba(255, 75, 92, 0.2);
        text-align: center;
        max-width: 450px;
        margin: 50px auto;
    }

    /* Glowing Main Title */
    .hero-title {
        color: #ff2a55 !important;
        font-size: 2.8rem;
        font-weight: 800;
        text-shadow: 1px 1px 4px rgba(255, 255, 255, 0.8);
        margin-bottom: 5px;
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* Subtitle */
    .hero-subtitle {
        color: #444444 !important;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 20px;
    }

    /* Love Quote Box */
    .love-quote {
        background: #ffffff;
        border-left: 5px solid #ff2a55;
        padding: 18px;
        border-radius: 12px;
        font-style: italic;
        font-size: 1.1rem;
        color: #222222 !important;
        line-height: 1.6;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }

    /* ✉️ CLOSED ENVELOPE CARD STYLING */
    .envelope-closed {
        background: linear-gradient(135deg, #ff758c 0%, #ff2a55 100%);
        border: 3px solid #ffffff;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(255, 42, 85, 0.3);
        margin-top: 15px;
    }

    .envelope-closed h2 {
        color: #ffffff !important;
        font-size: 2.2rem;
        margin: 0;
    }

    .envelope-closed p {
        color: #fff0f3 !important;
        font-size: 1.1rem;
        font-weight: 600;
        margin-top: 5px;
    }

    /* 💌 OPEN LETTER PAPER CARD STYLING */
    .letter-paper {
        background: #fffdf9;
        border: 2px solid #ff758c;
        border-radius: 15px;
        padding: 30px;
        font-family: 'Georgia', serif;
        font-size: 1.15rem;
        color: #2c2c2c !important;
        line-height: 1.8;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
        margin-top: 15px;
        position: relative;
        animation: openLetter 0.7s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .letter-header {
        color: #ff2a55 !important;
        font-size: 1.4rem;
        font-weight: bold;
        margin-bottom: 15px;
        border-bottom: 2px dashed #ffb6c1;
        padding-bottom: 10px;
    }

    /* Stylish Button */
    .stButton>button {
        background: linear-gradient(45deg, #ff2a55, #ff758c);
        color: #ffffff !important;
        font-size: 1.2rem !important;
        font-weight: bold !important;
        border-radius: 30px !important;
        padding: 12px 30px !important;
        border: none !important;
        box-shadow: 0 6px 20px rgba(255, 42, 85, 0.4) !important;
        transition: all 0.3s ease !important;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-3px) scale(1.02);
        box-shadow: 0 10px 25px rgba(255, 42, 85, 0.6) !important;
    }

    /* Cute Love Note Cards */
    .love-note-card {
        background: #ffffff;
        padding: 22px;
        border-radius: 18px;
        border: 2px solid #ff758c;
        text-align: center;
        margin-top: 10px;
        box-shadow: 0 6px 15px rgba(255, 75, 92, 0.15);
    }

    .love-note-card h3 {
        color: #ff2a55 !important;
        font-size: 1.3rem;
        font-weight: 700;
        margin-bottom: 10px;
    }

    .love-note-card p {
        color: #333333 !important;
        font-size: 1.05rem;
        font-weight: 500;
        line-height: 1.5;
    }

    /* Timer Box Styling */
    .timer-card {
        background: #ffffff;
        border-radius: 15px;
        padding: 15px;
        text-align: center;
        border: 2px solid #ff2a55;
        margin-bottom: 20px;
    }

    /* Gift Wrap Card Styling */
    .gift-wrap-card {
        background: linear-gradient(135deg, #ff4b6e 0%, #ff758c 100%);
        border: 3px dashed #ffffff;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(255, 75, 110, 0.3);
        margin-top: 15px;
    }

    .gift-wrap-card h2 {
        color: #ffffff !important;
        font-size: 1.8rem;
        margin-bottom: 5px;
    }

    .gift-wrap-card p {
        color: #fff0f3 !important;
        font-size: 1.1rem;
        font-weight: 600;
    }

    /* Open Gift Card Styling */
    .open-gift-card {
        background: linear-gradient(135deg, #ffffff 0%, #fff0f3 100%);
        border: 2px solid #ff4b6e;
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(255, 75, 110, 0.25);
        margin-top: 15px;
        animation: openGiftAnim 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }

    .open-gift-card h3 {
        color: #ff2a55 !important;
        font-size: 1.2rem;
        margin-bottom: 8px;
    }

    .open-gift-card p {
        color: #d63031 !important;
        font-size: 1.3rem;
        font-weight: 700;
        font-style: italic;
        margin: 0;
    }

    /* Game Card Styling */
    .game-card {
        background: #ffffff;
        border-radius: 20px;
        padding: 25px;
        border: 2px dashed #ff4b6e;
        box-shadow: 0 8px 20px rgba(0,0,0,0.06);
        margin-top: 15px;
    }

    /* Main Navigation Tab Customization */
    .stTabs [data-baseweb="tab-list"] {
        gap: 15px;
        justify-content: center;
    }

    .stTabs [data-baseweb="tab-list"] button {
        background: rgba(255, 255, 255, 0.7);
        border-radius: 20px 20px 0 0;
        padding: 10px 20px;
    }

    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        color: #ff2a55 !important;
        font-weight: bold !important;
        font-size: 1.2rem !important;
    }

    @keyframes openLetter {
        0% { transform: translateY(30px) scale(0.9); opacity: 0; }
        100% { transform: translateY(0) scale(1); opacity: 1; }
    }

    @keyframes openGiftAnim {
        0% { transform: scale(0.5) rotate(-5deg); opacity: 0; }
        100% { transform: scale(1) rotate(0deg); opacity: 1; }
    }
    </style>
""", unsafe_allow_html=True)

# 🔒 PASSWORD PROTECTION FUNCTION
def check_password():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if not st.session_state["authenticated"]:
        st.markdown("""
        <div class="lock-card">
            <h1 style="color: #ff2a55; font-size: 3rem; margin:0;">🔒</h1>
            <h2 style="color: #ff2a55 !important; margin-bottom: 10px;">Secret Birthday Surprise!</h2>
            <p style="color: #555 !important; margin-bottom: 20px;">Ye page strictly confidential hai! Password enter karke surprise unlock karein 😉</p>
        </div>
        """, unsafe_allow_html=True)

        pwd = st.text_input("Enter Secret Password To Unlock ❤️:", type="password")
        
        if st.button("Unlock Surprise ✨"):
            if pwd == SECRET_PASSWORD:
                st.session_state["authenticated"] = True
                st.rerun()
            else:
                st.error("Wrong password! Sirf birthday girl hi ise unlock kar sakti hain! 😜")
        return False
    return True

# 🌟 MAIN APPLICATION
if check_password():
    
    st.balloons()

    # 🦋 FLOATING BUTTERFLIES & HEARTS
    st.markdown("""
        <div class="floating-item item-1">🦋</div>
        <div class="floating-item item-2">💖</div>
        <div class="floating-item item-3">🦋</div>
        <div class="floating-item item-4">✨</div>
    """, unsafe_allow_html=True)

    # 🧸 CUTE ANIMATED CORNER MASCOTS
    st.markdown("""
        <div class="mascot-left">🧸</div>
        <div class="mascot-right">👩‍❤️‍👨</div>
    """, unsafe_allow_html=True)

    # 🎵 HIDDEN AUDIO PLAYER
    song_url = "https://cdn.pixabay.com/download/audio/2022/05/27/audio_1808fbf07a.mp3"
    st.markdown(
        f"""
        <iframe src="{song_url}" allow="autoplay" style="display:none" id="iframeAudio"></iframe>
        <audio autoplay loop style="display:none;">
            <source src="{song_url}" type="audio/mp3">
        </audio>
        """,
        unsafe_allow_html=True
    )

    # --- HERO SECTION ---
    st.markdown("""
    <div class="glass-card">
        <div class="hero-title">✨ Happy Birthday, Ishika! ❤️</div>
        <div class="hero-subtitle">To the prettiest & sweetest wife in the universe 👑</div>
    </div>
    """, unsafe_allow_html=True)

    # 📑 2 PAGES MAIN NAVIGATION (TABS)
    page1, page2 = st.tabs(["🌸 PAGE 1: Birthday Wishes & Love Notes", "🎮 PAGE 2: Fun Quiz & Big Surprise"])

    # ==========================================
    # 📌 PAGE 1 CONTENT
    # ==========================================
    with page1:
        # --- ⏳ OUR TOGETHER TIME COUNTER ---
        start_date = datetime(2025, 4, 26)
        current_date = datetime.now()
        days_together = (current_date - start_date).days

        st.markdown(f"""
        <div class="timer-card">
            <h4 style="color: #ff2a55 !important; margin: 0;">⌛ Days of Love & Happiness</h4>
            <p style="font-size: 1.4rem; font-weight: 800; color: #222 !important; margin-top: 5px;">
                Hum dono ko sath me <span style="color:#ff2a55;">{days_together} Days</span> ho gaye hain! ❤️
            </p>
        </div>
        """, unsafe_allow_html=True)

        # --- MAIN PHOTO & MESSAGE ---
        col1, col2 = st.columns([1, 1])

        with col1:
            st.image(
                "wife.png",
                caption="Queen Of My Heart 💖",
                use_container_width=True
            )

        with col2:
            st.markdown("""
            <div class="love-quote">
                "Ishika, aapki ek smile mera pura din bana deti hai. Meri zindagi me aakar ise itna khubsurat banane ke liye thank you! 
                <br><br>
                Aaj ka din purely aapka hai — stay blessed, keep smiling always! 🌹"
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # --- ✉️ CUSTOM ENVELOPE LOVE LETTER FEATURE ---
        st.markdown("<h3 style='text-align: center; color: #ff2a55 !important;'>💌 A Secret Envelope For You</h3>", unsafe_allow_html=True)

        if "letter_open" not in st.session_state:
            st.session_state.letter_open = False

        if st.button("💌 CLICK TO OPEN LOVE LETTER FOR ISHIKA ✨"):
            st.session_state.letter_open = not st.session_state.letter_open
            st.balloons()

        if not st.session_state.letter_open:
            st.markdown("""
            <div class="envelope-closed">
                <h2>✉️ ❤️ ✉️</h2>
                <p>Strictly For Ishika's Eyes Only 👑<br>Tap the button above to unseal this Love Letter!</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="letter-paper">
                <div class="letter-header">🌹 Meri Pyaari Ishika,</div>
                Zindagi me bohot se log aate hain, par kuch log aise hote hain jo aate hi poori duniya ko khubsurat bana dete hain — mere liye wo insaan tum ho. 💖<br><br>
                Aapka mera sath hone se mera har din special ban jata hai. Chahe aapka bina wajah mujh par gussa karna ho, ya mere late hone par mera wait karna, aapki har ek baat mere liye bohot keemti hai. ✨<br><br>
                Ishika, aaj aapke 20th Birthday par main bas itna kehna chahta hoon ki main hamesha aapke sath khada rahoon, har mushkil me aur har khushi me. Tumhari muskuraahat mere liye duniya ki sabse badi daulat hai. 🥰<br><br>
                Happy 20th Birthday, Meri Jaan! I Love You So Much Forever & Always! 🥂🎂<br><br>
                <div style="text-align: right; font-weight: bold; color: #ff2a55;">~ Tumhara Pati Dev ❤️</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # --- CUTE "REASONS WHY I LOVE YOU" SECTION ---
        st.markdown("<h3 style='text-align: center; color: #ff2a55 !important;'>💌 Why You Are So Special To Me</h3>", unsafe_allow_html=True)

        reason_tab1, reason_tab2, reason_tab3 = st.tabs(["✨ Reason #1", "🌸 Reason #2", "💖 Reason #3"])

        with reason_tab1:
            st.markdown("""
            <div class="love-note-card">
                <h3>Aapki Pyaari Si Smile 😊</h3>
                <p>"Jab Ishika aap hasti ho na, toh lagta hai saari pareshaniyan door ho gayi. Aapki smile meri daily dose hai happiness ki!"</p>
            </div>
            """, unsafe_allow_html=True)

        with reason_tab2:
            st.markdown("""
            <div class="love-note-card">
                <h3>Aapka Care Karne Ka Tarika 🤱</h3>
                <p>"Chahe mera khayal rakhna ho ya chhoti-chhoti baaton ka dhyan dena, aap se behtar care koi nahi kar sakta."</p>
            </div>
            """, unsafe_allow_html=True)

        with reason_tab3:
            st.markdown("""
            <div class="love-note-card">
                <h3>Mera Best Friend Hona 👭</h3>
                <p>"Sirf wife nahi, aap meri sabse achhi dost bhi ho. Jiske sath main bina soche kuch bhi share kar sakta hoon!"</p>
            </div>
            """, unsafe_allow_html=True)

        st.info("💡 Next Page par jaane ke liye Upar 'PAGE 2' Tab par click karein! ↗️")

    # ==========================================
    # 📌 PAGE 2 CONTENT
    # ==========================================
    with page2:
        # --- 🎁 GIFT WRAP UNWRAPPER FEATURE ---
        st.markdown("<h3 style='text-align: center; color: #ff2a55 !important;'>🎁 Tap Below To Unwrap Your Mystery Gift!</h3>", unsafe_allow_html=True)
        
        compliments = [
            "Ishika, aap duniya ki sabse pyari biwi ho! 🥰",
            "Aapki smile se meri duniya roshan hoti hai! ✨",
            "Aap jab gussa karti ho, tab bhi cutest lagti ho! 😜",
            "I am so blessed & lucky to have you, Ishika! ❤️",
            "Aapki aawaz sunte hi mera din ban jata hai! 🌸"
        ]
        
        if "gift_opened" not in st.session_state:
            st.session_state.gift_opened = False
        if "comp_index" not in st.session_state:
            st.session_state.comp_index = 0

        # Unwrap Action Button
        if st.button("🎁 CLICK TO UNWRAP MY GIFT BOX! ✨"):
            st.session_state.gift_opened = True
            st.session_state.comp_index = (st.session_state.comp_index + 1) % len(compliments)
            st.balloons()

        # Display Wrapped Gift or Unwrapped Surprise
        if not st.session_state.gift_opened:
            st.markdown("""
            <div class="gift-wrap-card">
                <h2>🎁 🎀 🎁</h2>
                <p>A Special Gift Box Is Waiting For You, Ishika!<br>Tap the button above to unwrap it! ✨</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="open-gift-card">
                <h3>🎉 Gift Unwrapped! Here is your Love Message:</h3>
                <p>"{compliments[st.session_state.comp_index]}"</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("---")

        # --- 🎮 ROMANTIC QUIZ GAME ---
        st.markdown("<h3 style='text-align: center; color: #ff2a55 !important;'>🎮 Romantic Couple Quiz: How Well Do You Know Us?</h3>", unsafe_allow_html=True)

        st.markdown('<div class="game-card">', unsafe_allow_html=True)
        st.write("Ishika, let's see aap hamare baare me kitna sahi guess karti ho! 😉")

        q1 = st.radio("1️⃣ Hum dono me se sabse zyada gussa kisse aata hai?", ["Aapko (Ishika)", "Mujhe (Pati Dev)", "Kisi ko nahi, hum angel hain 😇"])
        q2 = st.radio("2️⃣ Late night hungry hone par pehle kaun bolta hai?", ["Ishika 🍕", "Pati Dev 🍟", "Dono ek sath 😋"])
        q3 = st.radio("3️⃣ Darakht se toot-te taare se maine kya manga hoga?", ["Unlimited Shopping Pass 💳", "Ishika ki smile lifelong ❤️", "PS5 / Gaming Console 🎮"])

        if st.button("🎯 Submit Answers & Check Love Score!"):
            st.balloons()
            st.success("🎉 100/100 Perfect Match Score! ❤️ Aapki aur meri jodi universe ki best jodi hai! ✨")
        
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown("---")

        # --- BIG SURPRISE BUTTON ---
        if st.button("✨ TAP HERE FOR THE BIG SURPRISE! 🎉"):
            st.balloons()
            st.snow()
            
            st.markdown("""
            <div class="glass-card" style="margin-top: 20px;">
                <h2 style="color: #ff2a55 !important;">💖 I Love You So Much, Ishika! 💖</h2>
                <p style="font-size: 1.2rem; color: #222222 !important; font-weight: 600;">
                    Aap mere life ki sabse badi blessing ho. Happy 20th Birthday once again my love! 🥂✨
                </p>
            </div>
            """, unsafe_allow_html=True)

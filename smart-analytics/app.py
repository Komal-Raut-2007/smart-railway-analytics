import streamlit as st

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="RailSmart Analytics",
    page_icon="🚆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# LANGUAGE TRANSLATIONS
# ============================================================

translations = {

    "English": {

        "app_name": "RailSmart",
        "tagline": "Smart Passenger Analytics",
        "language": "🌐 Language",

        "dashboard": "🏠 Dashboard",
        "journey": "🚆 My Journey",
        "live": "📍 Live Train Status",
        "route": "🗺️ Route & Stations",
        "coach": "🪑 Coach & Seat",
        "food": "🍱 Food & Services",
        "facilities": "🏢 Facilities",
        "insights": "🧠 Smart Insights",
        "analytics": "📊 Journey Analytics",
        "safety": "🛡️ Safety Center",
        "lost": "🧳 Lost & Found",
        "announcements": "📢 Announcements",
        "help": "❓ Help Center",
        "settings": "⚙️ Settings",
        "emergency": "🚨 EMERGENCY",

        "good_evening": "Good Evening 👋",
        "welcome": "Welcome to RailSmart — your intelligent railway travel companion.",
        "current_journey": "🚆 Current Journey",
        "train_status": "Train Status",
        "current_station": "Current Station",
        "next_station": "Next Station",
        "progress": "Journey Progress",
        "journey_info": "🕒 Journey Information",
        "your_seat": "🪑 Your Seat",
        "quick_services": "⚡ Quick Services",
        "smart_insights": "🧠 Smart Travel Insights",
        "journey_health": "📊 Journey Health",
        "notifications": "🔔 Recent Notifications",

        "on_time": "ON TIME",
        "no_delay": "No Delay",
        "lonavala": "Lonavala",
        "window_seat": "Window Seat",
        "charging": "🔌 Charging Available",
        "ac": "❄️ AC Coach",

        "food": "🍱 Food",
        "water": "💧 Water",
        "washroom": "🚻 Washroom",
        "cleaning": "🧹 Cleaning",
        "attendant": "🛎️ Attendant",
        "report": "⚠️ Report Issue",

        "departure": "Departure",
        "next_stop": "Next Stop",
        "arrival": "Estimated Arrival",
        "remaining": "Remaining Journey",

        "refresh": "🔄 Refresh",
        "save": "💾 Save Settings",
        "submit": "Submit Help Request",

        "punctuality": "Punctuality",
        "comfort": "Comfort Score",
        "safety_status": "Safety Status",
        "service": "Service Availability",

        "language_changed": "Language changed successfully!"
    },

    "हिंदी": {

        "app_name": "रेलस्मार्ट",
        "tagline": "स्मार्ट यात्री विश्लेषण",
        "language": "🌐 भाषा",

        "dashboard": "🏠 डैशबोर्ड",
        "journey": "🚆 मेरी यात्रा",
        "live": "📍 लाइव ट्रेन स्थिति",
        "route": "🗺️ मार्ग और स्टेशन",
        "coach": "🪑 कोच और सीट",
        "food": "🍱 भोजन और सेवाएँ",
        "facilities": "🏢 यात्री सुविधाएँ",
        "insights": "🧠 स्मार्ट जानकारी",
        "analytics": "📊 यात्रा विश्लेषण",
        "safety": "🛡️ सुरक्षा केंद्र",
        "lost": "🧳 खोया और पाया",
        "announcements": "📢 घोषणाएँ",
        "help": "❓ सहायता केंद्र",
        "settings": "⚙️ सेटिंग्स",
        "emergency": "🚨 आपातकाल",

        "good_evening": "शुभ संध्या 👋",
        "welcome": "RailSmart में आपका स्वागत है — आपका स्मार्ट रेलवे यात्रा सहायक।",
        "current_journey": "🚆 वर्तमान यात्रा",
        "train_status": "ट्रेन स्थिति",
        "current_station": "वर्तमान स्टेशन",
        "next_station": "अगला स्टेशन",
        "progress": "यात्रा प्रगति",
        "journey_info": "🕒 यात्रा की जानकारी",
        "your_seat": "🪑 आपकी सीट",
        "quick_services": "⚡ त्वरित सेवाएँ",
        "smart_insights": "🧠 स्मार्ट यात्रा जानकारी",
        "journey_health": "📊 यात्रा स्थिति",
        "notifications": "🔔 हाल की सूचनाएँ",

        "on_time": "समय पर",
        "no_delay": "कोई देरी नहीं",
        "lonavala": "लोणावला",
        "window_seat": "खिड़की वाली सीट",
        "charging": "🔌 चार्जिंग उपलब्ध",
        "ac": "❄️ एसी कोच",

        "food": "🍱 भोजन",
        "water": "💧 पानी",
        "washroom": "🚻 शौचालय",
        "cleaning": "🧹 सफाई",
        "attendant": "🛎️ सहायक",
        "report": "⚠️ समस्या की रिपोर्ट",

        "departure": "प्रस्थान",
        "next_stop": "अगला स्टेशन",
        "arrival": "अनुमानित आगमन",
        "remaining": "शेष यात्रा",

        "refresh": "🔄 रीफ्रेश",
        "save": "💾 सेटिंग्स सहेजें",
        "submit": "सहायता अनुरोध भेजें",

        "punctuality": "समय पालन",
        "comfort": "आराम स्कोर",
        "safety_status": "सुरक्षा स्थिति",
        "service": "सेवा उपलब्धता",

        "language_changed": "भाषा सफलतापूर्वक बदल गई!"
    },

    "मराठी": {

        "app_name": "रेलस्मार्ट",
        "tagline": "स्मार्ट प्रवासी विश्लेषण",
        "language": "🌐 भाषा",

        "dashboard": "🏠 डॅशबोर्ड",
        "journey": "🚆 माझा प्रवास",
        "live": "📍 लाईव्ह ट्रेन स्थिती",
        "route": "🗺️ मार्ग आणि स्थानके",
        "coach": "🪑 कोच आणि सीट",
        "food": "🍱 भोजन आणि सेवा",
        "facilities": "🏢 प्रवासी सुविधा",
        "insights": "🧠 स्मार्ट माहिती",
        "analytics": "📊 प्रवास विश्लेषण",
        "safety": "🛡️ सुरक्षा केंद्र",
        "lost": "🧳 हरवलेले आणि सापडलेले",
        "announcements": "📢 घोषणा",
        "help": "❓ मदत केंद्र",
        "settings": "⚙️ सेटिंग्ज",
        "emergency": "🚨 आपत्कालीन मदत",

        "good_evening": "शुभ संध्याकाळ 👋",
        "welcome": "RailSmart मध्ये आपले स्वागत आहे — आपला स्मार्ट रेल्वे प्रवास सहाय्यक.",
        "current_journey": "🚆 सध्याचा प्रवास",
        "train_status": "ट्रेन स्थिती",
        "current_station": "सध्याचे स्थानक",
        "next_station": "पुढील स्थानक",
        "progress": "प्रवासाची प्रगती",
        "journey_info": "🕒 प्रवासाची माहिती",
        "your_seat": "🪑 तुमची सीट",
        "quick_services": "⚡ जलद सेवा",
        "smart_insights": "🧠 स्मार्ट प्रवास माहिती",
        "journey_health": "📊 प्रवास स्थिती",
        "notifications": "🔔 अलीकडील सूचना",

        "on_time": "वेळेवर",
        "no_delay": "विलंब नाही",
        "lonavala": "लोणावळा",
        "window_seat": "खिडकीची सीट",
        "charging": "🔌 चार्जिंग उपलब्ध",
        "ac": "❄️ एसी कोच",

        "food": "🍱 भोजन",
        "water": "💧 पाणी",
        "washroom": "🚻 स्वच्छतागृह",
        "cleaning": "🧹 स्वच्छता",
        "attendant": "🛎️ सहाय्यक",
        "report": "⚠️ समस्या नोंदवा",

        "departure": "प्रस्थान",
        "next_stop": "पुढील स्थानक",
        "arrival": "अंदाजे आगमन",
        "remaining": "उर्वरित प्रवास",

        "refresh": "🔄 रिफ्रेश",
        "save": "💾 सेटिंग्ज जतन करा",
        "submit": "मदत विनंती पाठवा",

        "punctuality": "वेळेचे पालन",
        "comfort": "आराम स्कोअर",
        "safety_status": "सुरक्षा स्थिती",
        "service": "सेवा उपलब्धता",

        "language_changed": "भाषा यशस्वीरित्या बदलली!"
    }
}

# ============================================================
# SESSION STATE
# ============================================================

if "language" not in st.session_state:
    st.session_state.language = "English"

if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False


# ============================================================
# TRANSLATION FUNCTION
# ============================================================

def T(key):

    language = st.session_state.language

    if language in translations:
        if key in translations[language]:
            return translations[language][key]

    return translations["English"].get(key, key)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown(
    f"## 🚆 {T('app_name')}"
)

st.sidebar.caption(
    T("tagline")
)

st.sidebar.divider()

# LANGUAGE SELECTOR

language_options = [
    "English",
    "हिंदी",
    "मराठी"
]

selected_language = st.sidebar.selectbox(
    T("language"),
    language_options,
    index=language_options.index(
        st.session_state.language
    )
)

# Update language immediately

if selected_language != st.session_state.language:

    st.session_state.language = selected_language

    st.rerun()


# ============================================================
# NAVIGATION
# ============================================================

pages = [
    T("dashboard"),
    T("journey"),
    T("live"),
    T("route"),
    T("coach"),
    T("food"),
    T("facilities"),
    T("insights"),
    T("analytics"),
    T("safety"),
    T("lost"),
    T("announcements"),
    T("help"),
    T("settings")
]

page = st.sidebar.radio(
    "MENU",
    pages
)

st.sidebar.divider()

if st.sidebar.button(
    T("emergency"),
    use_container_width=True
):

    st.sidebar.error(
        "🚨 Emergency mode activated"
    )


# ============================================================
# DASHBOARD
# ============================================================

if page == T("dashboard"):

    st.markdown(
        f"""
        <div style="
        background:linear-gradient(135deg,#172554,#2563eb);
        color:white;
        padding:30px;
        border-radius:20px;
        margin-bottom:20px;
        ">

        <h1>{T("good_evening")}</h1>

        <p>{T("welcome")}</p>

        <br>

        <b>🚆 Deccan Queen • Train 12124</b><br>

        Pune Junction → Mumbai CSMT

        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader(
        T("current_journey")
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            T("train_status"),
            T("on_time"),
            T("no_delay")
        )

    with c2:
        st.metric(
            T("current_station"),
            "Pune Jn"
        )

    with c3:
        st.metric(
            T("next_station"),
            T("lonavala")
        )

    with c4:
        st.metric(
            T("progress"),
            "58%"
        )

    st.progress(0.58)

    st.caption(
        "Pune Jn ━━━━━━━━━●━━━━━━━━ Mumbai CSMT"
    )

    # --------------------------------------------------------
    # INFORMATION CARDS
    # --------------------------------------------------------

    c1, c2 = st.columns(2)

    with c1:

        st.markdown(
            f"""
            <div style="
            background:white;
            padding:22px;
            border-radius:16px;
            ">

            <h3>{T("journey_info")}</h3>

            <b>{T("departure")}:</b> 07:15 AM<br><br>

            <b>{T("current_station")}:</b> Pune Junction<br><br>

            <b>{T("next_stop")}:</b> {T("lonavala")}<br><br>

            <b>{T("arrival")}:</b> 09:33 AM<br><br>

            <b>{T("remaining")}:</b> 2h 18m

            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:

        st.markdown(
            f"""
            <div style="
            background:white;
            padding:22px;
            border-radius:16px;
            ">

            <h3>{T("your_seat")}</h3>

            <h1>S5 • 42</h1>

            <p>{T("window_seat")}</p>

            <p>{T("charging")}</p>

            <p>{T("ac")}</p>

            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------------------------
    # SERVICES
    # --------------------------------------------------------

    st.subheader(
        T("quick_services")
    )

    services = [
        ("🍱", "food"),
        ("💧", "water"),
        ("🚻", "washroom"),
        ("🧹", "cleaning"),
        ("🛎️", "attendant"),
        ("⚠️", "report")
    ]

    columns = st.columns(6)

    for column, service in zip(columns, services):

        with column:

            if st.button(
                f"{service[0]} {T(service[1])}",
                use_container_width=True
            ):

                st.success(
                    f"{T(service[1])} selected."
                )

    # --------------------------------------------------------
    # SMART INSIGHTS
    # --------------------------------------------------------

    st.subheader(
        T("smart_insights")
    )

    c1, c2, c3 = st.columns(3)

    with c1:

        st.info(
            "💡 Train is running on time."
        )

    with c2:

        st.success(
            "📍 Next station: "
            + T("lonavala")
        )

    with c3:

        st.warning(
            "🔔 Keep your belongings secure."
        )

    # --------------------------------------------------------
    # ANALYTICS
    # --------------------------------------------------------

    st.subheader(
        T("journey_health")
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            T("punctuality"),
            "98%"
        )

    with c2:
        st.metric(
            T("comfort"),
            "92%"
        )

    with c3:
        st.metric(
            T("safety_status"),
            "Good"
        )

    with c4:
        st.metric(
            T("service"),
            "87%"
        )


# ============================================================
# MY JOURNEY
# ============================================================

elif page == T("journey"):

    st.title(
        T("journey")
    )

    st.subheader(
        "Pune Junction → Mumbai CSMT"
    )

    st.info(
        "🚆 Train 12124 • Coach S5 • Seat 42"
    )

    st.progress(0.58)

    st.write(
        "Pune Jn → Lonavala → Karjat → "
        "Kalyan → Thane → Dadar → Mumbai CSMT"
    )

    if st.button(
        T("refresh")
    ):

        st.success(
            "Journey status updated."
        )


# ============================================================
# LIVE STATUS
# ============================================================

elif page == T("live"):

    st.title(
        T("live")
    )

    st.success(
        "🟢 " + T("on_time")
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Current Speed",
            "72 km/h"
        )

    with c2:
        st.metric(
            T("current_station"),
            "Pune Jn"
        )

    with c3:
        st.metric(
            "Delay",
            "0 min"
        )

    st.info(
        "Live railway API can be integrated here."
    )


# ============================================================
# ROUTE
# ============================================================

elif page == T("route"):

    st.title(
        T("route")
    )

    stations = [
        ("Pune Junction", "07:15 AM", "✓ Departed"),
        ("Lonavala", "08:20 AM", "Upcoming"),
        ("Karjat", "08:58 AM", "Upcoming"),
        ("Kalyan", "09:20 AM", "Upcoming"),
        ("Thane", "09:40 AM", "Upcoming"),
        ("Dadar", "10:00 AM", "Upcoming"),
        ("Mumbai CSMT", "10:25 AM", "🏁 Destination")
    ]

    for station, time, status in stations:

        with st.expander(
            f"🚉 {station} — {time}"
        ):

            st.write(status)

            st.write(
                "Station facilities and platform information "
                "can be displayed here."
            )


# ============================================================
# COACH
# ============================================================

elif page == T("coach"):

    st.title(
        T("coach")
    )

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric("Coach", "S5")

    with c2:
        st.metric("Seat", "42")

    with c3:
        st.metric("Type", "Window")

    st.subheader("Coach Facilities")

    facilities = [
        "🔌 Charging Point",
        "❄️ Air Conditioning",
        "🚻 Washroom",
        "🛎️ Attendant",
        "🧯 Emergency Equipment"
    ]

    for facility in facilities:

        st.checkbox(
            facility,
            value=True
        )


# ============================================================
# FOOD
# ============================================================

elif page == T("food"):

    st.title(
        T("food")
    )

    service = st.selectbox(
        "Select Service",
        [
            "Meal",
            "Tea / Coffee",
            "Snacks",
            "Drinking Water"
        ]
    )

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        max_value=10,
        value=1
    )

    if st.button(
        "🛒 Request Service"
    ):

        st.success(
            f"{service} × {quantity} requested."
        )


# ============================================================
# FACILITIES
# ============================================================

elif page == T("facilities"):

    st.title(
        T("facilities")
    )

    c1, c2 = st.columns(2)

    with c1:

        st.subheader("🚻 Basic Facilities")

        st.write("✓ Washrooms")
        st.write("✓ Drinking Water")
        st.write("✓ Charging")
        st.write("✓ Cleaning")

    with c2:

        st.subheader("♿ Accessibility")

        st.write("✓ Wheelchair Assistance")
        st.write("✓ Elderly Passenger Support")
        st.write("✓ Priority Assistance")


# ============================================================
# SMART INSIGHTS
# ============================================================

elif page == T("insights"):

    st.title(
        T("insights")
    )

    st.info(
        "🧠 AI-powered insights are simulated in this prototype."
    )

    insights = [
        "Train is currently on time.",
        "Moderate passenger movement expected.",
        "Keep luggage secure near stations.",
        "Food service is available.",
        "No major safety alert detected."
    ]

    for insight in insights:

        st.success(
            "💡 " + insight
        )

    preference = st.selectbox(
        "What do you want to optimize?",
        [
            "Safety",
            "Comfort",
            "Time",
            "Food",
            "Accessibility"
        ]
    )

    if st.button(
        "Generate Recommendation"
    ):

        st.info(
            f"Recommendation generated for {preference}."
        )


# ============================================================
# ANALYTICS
# ============================================================

elif page == T("analytics"):

    st.title(
        T("analytics")
    )

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "Distance Covered",
            "84 km"
        )

    with c2:
        st.metric(
            "Distance Remaining",
            "62 km"
        )

    with c3:
        st.metric(
            "Journey Time",
            "1h 42m"
        )

    with c4:
        st.metric(
            T("arrival"),
            "09:33 AM"
        )

    st.subheader(
        "📈 Journey Completion"
    )

    st.bar_chart(
        {
            "Journey": [58],
            "Remaining": [42]
        }
    )


# ============================================================
# SAFETY
# ============================================================

elif page == T("safety"):

    st.title(
        T("safety")
    )

    st.error(
        "🚨 For real emergencies, contact official railway emergency services."
    )

    emergency = st.selectbox(
        "Emergency Type",
        [
            "Medical Emergency",
            "Women Safety",
            "Railway Security",
            "Fire Emergency",
            "Unauthorized Passenger",
            "Lost Child",
            "Other"
        ]
    )

    description = st.text_area(
        "Describe the problem"
    )

    if st.button(
        "🚨 SEND EMERGENCY REQUEST",
        use_container_width=True
    ):

        st.error(
            f"Emergency request recorded: {emergency}"
        )

        st.write(
            description
        )


# ============================================================
# LOST & FOUND
# ============================================================

elif page == T("lost"):

    st.title(
        T("lost")
    )

    item = st.text_input(
        "What did you lose?"
    )

    location = st.selectbox(
        "Location",
        [
            "Seat",
            "Coach",
            "Washroom",
            "Platform",
            "Other"
        ]
    )

    description = st.text_area(
        "Description"
    )

    if st.button(
        "🔎 Report Lost Item"
    ):

        st.success(
            "Lost item report created."
        )


# ============================================================
# ANNOUNCEMENTS
# ============================================================

elif page == T("announcements"):

    st.title(
        T("announcements")
    )

    with st.expander("🚆 Train Status"):
        st.write(
            "Train 12124 is running on time."
        )

    with st.expander("📍 Next Station"):
        st.write(
            "Lonavala is the next major station."
        )

    with st.expander("🍱 Catering"):
        st.write(
            "Catering services are available."
        )

    with st.expander("🛡️ Safety"):
        st.write(
            "Please keep your belongings secure."
        )


# ============================================================
# HELP
# ============================================================

elif page == T("help"):

    st.title(
        T("help")
    )

    question = st.text_input(
        "🔎 Search your question"
    )

    category = st.selectbox(
        "Category",
        [
            "Train Information",
            "Ticket & Seat",
            "Food",
            "Facilities",
            "Safety",
            "Lost & Found",
            "Accessibility"
        ]
    )

    if st.button(
        T("submit")
    ):

        st.success(
            "Your help request has been submitted."
        )

    st.subheader(
        "Frequently Asked Questions"
    )

    with st.expander(
        "How can I check my train status?"
    ):

        st.write(
            "Open Live Train Status."
        )

    with st.expander(
        "How can I request assistance?"
    ):

        st.write(
            "Open Safety Center or Facilities."
        )


# ============================================================
# SETTINGS
# ============================================================

elif page == T("settings"):

    st.title(
        T("settings")
    )

    st.subheader(
        T("language")
    )

    st.write(
        f"Current Language: **{st.session_state.language}**"
    )

    st.info(
        T("language_changed")
    )

    notifications = st.toggle(
        "🔔 Enable Notifications",
        value=True
    )

    accessibility = st.toggle(
        "♿ Accessibility Mode",
        value=False
    )

    dark_mode = st.toggle(
        "🌙 Dark Mode",
        value=st.session_state.dark_mode
    )

    st.session_state.dark_mode = dark_mode

    if st.button(
        T("save")
    ):

        st.success(
            "Settings saved successfully."
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🚆 RailSmart Analytics | Smart Passenger Travel Platform | Prototype"
)
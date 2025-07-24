import streamlit as st
from dotenv import load_dotenv

# Load environment variables early
load_dotenv()

# Try importing UI modules
try:
    from modules.weather.ui import render_weather_tab
    from modules.energy.ui import render_energy_tab
    from modules.crypto.ui import render_crypto_tab
    from modules.analyzer.ui import render_analyzer_tab
except ImportError as e:
    st.error(f"Module import error: {e}")
    st.stop()  # Prevent app from continuing if imports fail


def main():
    # Page config
    st.set_page_config(
        page_title="Real-Time Dashboard",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    # Optional: Custom CSS
    # st.markdown("""
    # <style>
    # .stSidebar { background-color: #f5f5f5; }
    # </style>
    # """, unsafe_allow_html=True)

    # Sidebar navigation
    st.sidebar.title("🧭 Navigation")
    tabs = ["🌦 Weather", "⚡ Energy", "💰 Crypto", "📊 Analyzer"]
    selected_tab = st.sidebar.radio("Select Dashboard", tabs)

    # Tab logic
    try:
        if selected_tab == "🌦 Weather":
            render_weather_tab()
        elif selected_tab == "⚡ Energy":
            render_energy_tab()
        elif selected_tab == "💰 Crypto":
            render_crypto_tab()
        elif selected_tab == "📊 Analyzer":
            render_analyzer_tab()
        else:
            st.warning("Unknown tab selected.")
    except Exception as e:
        st.error(f"❌ Error while rendering '{selected_tab}' tab: {e}")


if __name__ == "__main__":
    main()

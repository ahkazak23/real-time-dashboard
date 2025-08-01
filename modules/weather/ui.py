import streamlit as st
from .fetch import get_weather, get_air_quality, get_coordinates
from .process import format_weather_data, format_air_quality_data

def render_weather_tab():
    st.header("🌦 Weather & Air Quality")

    city = st.selectbox("Select a city", ["Istanbul", "Ankara", "London", "Berlin", "Tokyo"])

    try:
        lat, lon = get_coordinates(city)
        weather_raw = get_weather(lat, lon)
        air_raw = get_air_quality(lat, lon)

        weather = format_weather_data(weather_raw)
        air = format_air_quality_data(air_raw)

        st.subheader(f"📍 Current Conditions in {city}")
        col1, col2 = st.columns(2)

        with col1:
            st.metric("Condition", weather["weather_desc"])
            st.metric("Temperature", f"{weather['temperature']} °C")
            st.metric("Wind Speed", f"{weather['wind_speed']} km/h")
            st.text(f"Updated at: {weather['time']}")

        with col2:
            st.metric("PM2.5", f"{air['pm2_5']} µg/m³", air["pm2_5_level"])
            st.metric("PM10", f"{air['pm10']} µg/m³", air["pm10_level"])
            st.metric("CO", f"{air['co']} µg/m³")
            st.text(f"Updated at: {air['time']}")

    except Exception as e:
        st.error(f"❌ {e}")

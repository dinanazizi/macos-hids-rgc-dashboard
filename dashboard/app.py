import streamlit as st
import random

# Simulated data for system status and risk score
def get_system_status():
    return {"cpu_usage": random.randint(1, 100), "disk_usage": random.randint(1, 100), "network_activity": random.randint(1, 100)}

def get_risk_score():
    return random.randint(0, 100)

st.title('macOS HIDS Dashboard')
st.sidebar.header("System Overview")

system_status = get_system_status()
risk_score = get_risk_score()

st.subheader("System Status")
st.write(f"CPU Usage: {system_status['cpu_usage']}%")
st.write(f"Disk Usage: {system_status['disk_usage']}%")
st.write(f"Network Activity: {system_status['network_activity']}%")

st.subheader("Risk Score")
st.write(f"Current Risk Score: {risk_score}")

# Display system activity log
st.subheader("Activity Log")
st.text("No unauthorized activities detected.")
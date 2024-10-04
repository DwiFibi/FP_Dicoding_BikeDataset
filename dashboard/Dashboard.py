# Import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load dataset
day_data = pd.read_csv('day.csv')

# Convert 'dteday' to datetime format
day_data['dteday'] = pd.to_datetime(day_data['dteday'])

# Replace season numbers with names
season_labels = {1: 'Musim Semi', 2: 'Musim Panas', 3: 'Musim Gugur', 4: 'Musim Dingin'}
day_data['season'] = day_data['season'].replace(season_labels)

# Replace weekday numbers with names
weekday_labels = {0: 'Sun', 1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat'}
day_data['weekday'] = day_data['weekday'].replace(weekday_labels)

# Title of the Streamlit app
st.title("Dashboard Analisis Penggunaan Sepeda")

# Sidebar for navigation
st.sidebar.title("Navigasi")
option = st.sidebar.selectbox("Pilih Visualisasi", 
                               ["Jumlah Penyewa Berdasarkan Hari", 
                                "Hubungan Suhu dan Penyewa Sepeda",
                                "Jumlah Penyewa Berdasarkan Hari (Harian)",  
                                "Rata-rata Penyewa Berdasarkan Musim"])

# 1. Visualisasi Jumlah Penyewa Berdasarkan Hari
if option == "Jumlah Penyewa Berdasarkan Hari":
    st.subheader("Jumlah Penyewa Sepeda Berdasarkan Hari")
    
    # Group data by weekday and calculate average usage
    day_usage_by_day = day_data.groupby("weekday")['cnt'].mean().sort_values(ascending=False)
    
    # Plotting
    plt.figure(figsize=(8, 6))
    day_usage_by_day.plot(kind='bar', color='skyblue')
    plt.title('Rata-rata Penyewa Sepeda Berdasarkan Hari')
    plt.xlabel('Hari')
    plt.ylabel('Rata-rata Jumlah Penyewa Sepeda')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    st.pyplot(plt)

# 2. Rata-rata Penyewa Berdasarkan Musim
elif option == "Rata-rata Penyewa Berdasarkan Musim":
    st.subheader("Rata-rata Penyewa Berdasarkan Musim")
    
    # Group data by season and calculate average usage
    season_usage = day_data.groupby('season')['cnt'].mean().sort_values(ascending=False)
    
    # Plotting
    plt.figure(figsize=(8, 6))
    season_usage.plot(kind='bar', color='blue')
    plt.title('Rata-rata Penyewa Sepeda Berdasarkan Musim')
    plt.xlabel('Musim')
    plt.ylabel('Rata-rata Jumlah Penyewa Sepeda')
    plt.xticks(rotation=0)
    plt.tight_layout()
    
    st.pyplot(plt)

# 3. Visualisasi Jumlah Penyewa Berdasarkan Hari (Harian)
elif option == "Jumlah Penyewa Berdasarkan Hari (Harian)":
    st.subheader("Jumlah Penyewa Sepeda Harian")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(day_data['dteday'], day_data['cnt'], label='Jumlah Penyewa', color='blue')
    ax.set_xlabel('Tanggal')
    ax.set_ylabel('Jumlah Penyewa')
    ax.set_title('Jumlah Penyewa Sepeda Harian')
    
    # Format sumbu x dengan tanggal
    ax.xaxis.set_major_locator(mdates.MonthLocator())  # Menampilkan setiap bulan
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format tanggal
    plt.xticks(rotation=45)  # Memutar label tanggal agar tidak bertumpuk
    
    st.pyplot(fig)

# 4. Hubungan antara Suhu dan Penyewa Sepeda
elif option == "Hubungan Suhu dan Penyewa Sepeda":
    st.subheader("Hubungan antara Suhu dan Jumlah Penyewa Sepeda")
    day_data['temp_celsius'] = day_data['temp'] * (39 - (-8)) + (-8)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.scatter(day_data['temp_celsius'], day_data['cnt'], color='orange')
    ax.set_xlabel('Suhu (Celsius)')
    ax.set_ylabel('Jumlah Penyewa')
    ax.set_title('Hubungan Suhu dan Jumlah Penyewa Sepeda')
    st.pyplot(fig)

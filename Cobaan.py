import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data Loading and Preparation
@st.cache
def load_data():
    day_df = pd.read_csv("")
    hr_df = pd.read_csv("D:\Semester 6\DICODING\Analisis-Data-Dicoding-main\dashboard\day.csv")
    datetime_columns = ["dteday"]
    for column in datetime_columns:
        day_df[column] = pd.to_datetime(day_df[column])
        hr_df[column] = pd.to_datetime(hr_df[column])

    main_df = hr_df.copy()

    mapping_yr = {0: '2011', 1: '2012'}
    mapping_mnth = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
                    7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
    mapping_season = {1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'}
    mapping_weathersit = {1: 'Clear', 2: 'Cloudy', 3: 'Light Snow/Rain', 4: 'Heavy Rain/Ice Pallets'}

    main_df['yr'] = main_df['yr'].map(mapping_yr)
    main_df['mnth'] = main_df['mnth'].map(mapping_mnth)
    main_df['weekday'] = main_df['dteday'].dt.day_name()
    main_df['season'] = main_df['season'].map(mapping_season)
    main_df['weathersit'] = main_df['weathersit'].map(mapping_weathersit)
    main_df = main_df[['dteday', 'yr', 'mnth', 'hr', 'weekday', 'season', 'weathersit','cnt', 'registered', 'casual']]

    return main_df

# Plotting functions
def plot_rentals(monthly_rentals):
    fig, ax = plt.subplots(figsize=(16, 8))
    ax.plot(monthly_rentals['date'], monthly_rentals['cnt'], marker='o', color='green', linewidth=2, markersize=6, label='Total Rentals (cnt)')
    ax.plot(monthly_rentals['date'], monthly_rentals['cnt'].rolling(window=3).mean(), linestyle='--', color='skyblue', label='Trend Line')
    ax.set_title('Grafik Peminjaman Sepeda Selama Dua Tahun (2011-2012)', fontsize=16, fontweight='bold')
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Number of Rentals', fontsize=14)
    ax.grid(True, linestyle='--', alpha=0.5)
    ax.legend(fontsize=12)
    ax.set_facecolor('whitesmoke')
    plt.xticks(rotation=45, ha='right', fontsize=12)
    plt.tight_layout()
    st.pyplot(fig)

def plot_seasonal_rentals(seasonal_counts):
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(seasonal_counts.index, seasonal_counts.values, color=['blue', 'orange', 'red', 'grey'], edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Musim', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Jumlah Peminjaman', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Musim', fontsize=16, fontweight='bold', color='darkred')

    for i, value in enumerate(seasonal_counts.values):
        ax.text(i, value + 500, str(value), ha='center', va='bottom', fontsize=12, 
                color='black', fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_facecolor('lightblue')
    plt.xticks(rotation=45, ha='right', fontsize=12, color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)

def plot_weather_rentals(weather_counts):
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(weather_counts.index, weather_counts.values, color=['gold', 'lightskyblue', 'grey', 'darkblue'], edgecolor='black', linewidth=1.5)
    ax.set_xlabel('Cuaca', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Jumlah Peminjaman', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_title('Jumlah Peminjaman Sepeda Berdasarkan Cuaca', fontsize=16, fontweight='bold', color='darkred')

    for i, value in enumerate(weather_counts.values):
        ax.text(i, value + 500, str(value), ha='center', va='bottom', fontsize=12, 
                color='black', fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.set_facecolor('lightblue')
    plt.xticks(rotation=45, ha='right', fontsize=12, color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)

def plot_hourly_rentals(hourly_counts):
    fig, ax = plt.subplots(figsize=(12, 7))
    bars = ax.bar(hourly_counts.index, hourly_counts.values, color='mediumseagreen', edgecolor='black', linewidth=1.5)
    ax.set_title('Total Peminjaman Sepeda Berdasarkan Jam dalam Sehari', fontsize=16, fontweight='bold', color='darkred')
    ax.set_xlabel('Jam', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Jumlah Peminjaman', fontsize=14, fontweight='bold', color='darkslategray')

    for i, value in enumerate(hourly_counts.values):
        ax.text(i, value + 500, str(value), ha='center', va='bottom', fontsize=12, 
                color='black', fontweight='bold', 
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))
    ax.grid(axis='y', linestyle='--', alpha=0.4)
    ax.set_facecolor('lightblue')
    plt.xticks(rotation=0, fontsize=12, color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)

def plot_heatmap(clustering):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(clustering, cmap="coolwarm", annot=False, linewidths=0.5, linecolor='black')
    ax.set_title('Heatmap Peminjaman Sepeda Berdasarkan Hari dan Jam', fontsize=16, fontweight='bold', color='darkred')
    ax.set_xlabel('Jam dalam Sehari', fontsize=14, fontweight='bold', color='darkslategray')
    ax.set_ylabel('Hari dalam Seminggu', fontsize=14, fontweight='bold', color='darkslategray')
    plt.tight_layout()
    st.pyplot(fig)

# Streamlit Dashboard
def main():
    st.title("Dashboard Peminjaman Sepeda 2011-2012")
    st.sidebar.header("Filter and Visualize Data")

    # Load data
    main_df = load_data()
    monthly_rentals = main_df.groupby(['yr', 'mnth'])[['cnt', 'registered', 'casual']].sum().reset_index()
    monthly_rentals['date'] = monthly_rentals['yr'] + '-' + monthly_rentals['mnth']
    monthly_rentals['date'] = pd.to_datetime(monthly_rentals['date'], format='%Y-%B')
    monthly_rentals = monthly_rentals.sort_values('date')

    seasonal_counts = main_df.groupby('season').cnt.sum().sort_values(ascending=False)
    weather_counts = main_df.groupby('weathersit').cnt.sum().sort_values(ascending=False)
    hourly_counts = main_df.groupby('hr')['cnt'].sum()

    # Sidebar options
    option = st.sidebar.selectbox("Select Visualization", 
                                  ["Monthly Rentals", "Seasonal Rentals", "Weather Rentals", "Hourly Rentals", "Heatmap"])

    if option == "Monthly Rentals":
        plot_rentals(monthly_rentals)
    elif option == "Seasonal Rentals":
        plot_seasonal_rentals(seasonal_counts)
    elif option == "Weather Rentals":
        plot_weather_rentals(weather_counts)
    elif option == "Hourly Rentals":
        plot_hourly_rentals(hourly_counts)
    elif option == "Heatmap":
        clustering = main_df.groupby(['weekday', 'hr'])['cnt'].sum().unstack()
        plot_heatmap(clustering)

if __name__ == "__main__":
    main()

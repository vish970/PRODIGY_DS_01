import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (skip metadata rows at the top)
df = pd.read_csv(
    "C:/Users/Vishal.S/Downloads/intership of google play store/prodigy internship/prodigy_DS_01/API_SP.POP.TOTL_DS2_en_csv_v2_58.csv",
    skiprows=4
)

# Select population data for 2020
year = "2020"
pop_2020 = df[["Country Name", year]].dropna()

# Histogram of population distribution
plt.figure(figsize=(10,6))
plt.hist(pop_2020[year], bins=30, color="skyblue", edgecolor="black")
plt.title("Histogram of Population Distribution (2020)")
plt.xlabel("Population")
plt.ylabel("Number of Countries")
plt.savefig("outputs/histogram.png")
plt.close()

# Bar chart of top 10 most populous countries
top10 = pop_2020.sort_values(by=year, ascending=False).head(10)
plt.figure(figsize=(10,6))
plt.bar(top10["Country Name"], top10[year], color="orange")
plt.title("Top 10 Most Populous Countries (2020)")
plt.xticks(rotation=45)
plt.ylabel("Population")
plt.savefig("outputs/top10.png")
plt.close()


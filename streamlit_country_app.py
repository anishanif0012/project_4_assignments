import streamlit as st
import requests

# Function to fetch country data
def fetch_country_data(country_name):
    url = f"https://restcountries.com/v3.1/name/{country_name}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        country_data = data[0]
        name = country_data["name"]["common"]
        capital = country_data["capital"][0] if "capital" in country_data else "N/A"
        population = country_data["population"]
        area = country_data["area"]
        currencies = list(country_data["currencies"].keys())[0]
        region = country_data["region"]
        return name, capital, population, area, currencies, region
    else:
        return None

# Main Streamlit app
def main():
    st.title("🌍 Country Information App")

    country_name = st.text_input("Enter a country name:")

    if country_name:
        country_info = fetch_country_data(country_name)
        
        if country_info:
            name, capital, population, area, currencies, region = country_info
            st.subheader(f"Details for {name}")
            st.write(f"**Capital:** {capital}")
            st.write(f"**Population:** {population}")
            st.write(f"**Area:** {area} km²")
            st.write(f"**Currency:** {currencies}")
            st.write(f"**Region:** {region}")
        else:
            st.error("Country not found. Please check the name and try again.")

if __name__ == "__main__":
    main()


import streamlit as st
import requests

# Function to fetch a random goat photo from Unsplash
def get_random_goat_photo():
    url = "https://api.unsplash.com/photos/random"
    params = {
        "query": "goat",
        "orientation": "landscape",
        "client_id": "UMmguTwx-jLVLB1fa24zjD3W9hae7h72LNFVJDecet8",  # Replace with your Unsplash access key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        return data["urls"]["regular"]
    else:
        return None

# Streamlit app
def main():
    st.title("Mon app dans ton fion")

    # Button to display the first random goat photo
    if st.button("Gille le bg juif"):
        goat_photo_1 = get_random_goat_photo()
        if goat_photo_1:
            st.image(goat_photo_1, caption="Gilles", use_column_width=True)
        else:
            st.error("Failed to fetch goat photo. Please try again.")

    # Button to display the second random goat photo
    if st.button("Geoff le plus beau cul"):
        goat_photo_2 = get_random_goat_photo()
        if goat_photo_2:
            st.image(goat_photo_2, caption="Geoff", use_column_width=True)
        else:
            st.error("Failed to fetch goat photo. Please try again.")

    # Button to display the third random goat photo
    if st.button("Guillaume le bientôt chauve"):
        goat_photo_3 = get_random_goat_photo()
        if goat_photo_3:
            st.image(goat_photo_3, caption="Guillaume", use_column_width=True)
        else:
            st.error("Failed to fetch goat photo. Please try again.")

if __name__ == "__main__":
    main()

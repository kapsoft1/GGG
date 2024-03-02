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
    st.title("Random Goat Photo App")

    # Button to display the first random goat photo
    if st.button("Show Goat Photo 1"):
        goat_photo_1 = get_random_goat_photo()
        if goat_photo_1:
            st.image(goat_photo_1, caption="Random Goat Photo 1", use_column_width=True)
        else:
            st.error("Failed to fetch goat photo. Please try again.")

    # Button to display the second random goat photo
    if st.button("Show Goat Photo 2"):
        goat_photo_2 = get_random_goat_photo()
        if goat_photo_2:
            st.image(goat_photo_2, caption="Random Goat Photo 2", use_column_width=True)
        else:
            st.error("Failed to fetch goat photo. Please try again.")

    # Button to display the third random goat photo
    if st.button("Show Goat Photo 3"):
        goat_photo_3 = get_random_goat_photo()
        if goat_photo_3:
            st.image(goat_photo_3, caption="Random Goat Photo 3", use_column_width=True)
        else:
            st.error("Failed to fetch goat photo. Please try again.")

if __name__ == "__main__":
    main()

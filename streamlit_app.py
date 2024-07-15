import streamlit as st
import requests

# Address of server
PROTOCOL = "http"
# SERVER_IP_ADDRESS = "127.0.0.1"
SERVER_IP_ADDRESS = "0.0.0.0"
# SERVER_IP_ADDRESS = "localhost"
SERVER_PORT = "8080"
BASE_URL = f"{PROTOCOL}://{SERVER_IP_ADDRESS}:{SERVER_PORT}"
BASE_URL = f"https://sea-lion-app-lvyeb.ondigitalocean.app"


def main():

    st.title("Emojify App")

    input_text = st.text_input("Enter your text here:")

    if st.button("Find emotion"):
        
        # Send input text to backend
        data = {'input_text': input_text}
        response = requests.post(f"{BASE_URL}/predict", json=data)

        # Check if the request was successful
        if response.status_code == 200:
            output_prediction = response.json()  # Get response from server
            list_predcited_emotion = output_prediction['list_predcited_emotion']

            st.header("List suggestion emotion:")

            for predcited_emotion in list_predcited_emotion:
                st.header(predcited_emotion)

if __name__ == "__main__":
    main()

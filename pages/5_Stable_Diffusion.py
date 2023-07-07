import streamlit as st
import os
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# Our Host URL should not be prepended with "https" nor should it have a trailing slash.
#os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

# Sign up for an account at the following link to get an API Key.
# https://dreamstudio.ai/

'[Sign Up](https://dreamstudio.ai/) to get an API Key'

# Click on the following link once you have created an account to be taken to your API Key.
# https://dreamstudio.ai/account

# Paste your API Key below.

#os.environ['STABILITY_KEY'] = 'key-goes-here'

with st.sidebar:
    stability_api_key = st.text_input("Stability API Key", key="image_api_key", type="password")

#if stability_api_key:
    #st.text(stability_api_key)

with st.sidebar:
     # Selectbox
     st.image('images/well_built_caucasian_angel_sit_0.jpg')
     add_selectbox = st.sidebar.selectbox(
     "Prompt examples",
       (
          "None",
           "Van Gogh painting with squirrels eating nuts", 
           "Homer Simpson on a computer wearing a space suit",
           "Mona Lisa with headphones on",
           "A digital artwork of a roborovski hamster dressed in blue wizards clothing casting a thunderstorm with lightning",
           "A model wearing a scuba diving suit",
           "A looney tunes character driving a car",
           "Optimus Prime on top of a surf board",
           "Albert Einstein with a goofy smile",
           "Nottingham Forest football team lifting the FA Cup"
        ), index=0)
     st.markdown('Use the above drop down box to generate _prompt_ examples')
     st.text('Application by Gary Hutson')

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

     # Create text prompt
prompt = st.text_input('Input the prompt desired')
 # Checks if the example prompts has been chosen and overides the text input

button = st.button("⚡️ generate image ⚡️")

if button:

    if add_selectbox != 'None' or prompt is None:
        prompt = add_selectbox

    # Set up our connection to the API.
        stability_api = client.StabilityInference(
            key=stability_api_key,#os.environ['STABILITY_KEY'], # API Key reference.
            verbose=True, # Print debug messages.
            engine="stable-diffusion-xl-1024-v0-9", # Set the engine to use for generation.
            # Available engines: stable-diffusion-xl-1024-v0-9 stable-diffusion-v1 stable-diffusion-v1-5 stable-diffusion-512-v2-0 stable-diffusion-768-v2-0
            # stable-diffusion-512-v2-1 stable-diffusion-768-v2-1 stable-diffusion-xl-beta-v2-2-2 stable-inpainting-v1-0 stable-inpainting-512-v2-0
        )

        # Set up our initial generation parameters.
        answers = stability_api.generate(
            prompt = prompt,#="expansive landscape rolling greens with blue daisies and yggdrasil under a blue alien sky, masterful, ghibli",
            seed=992446758, # If a seed is provided, the resulting generated image will be deterministic.
                            # What this means is that as long as all generation parameters remain the same, you can always recall the same image simply by generating it again.
                            # Note: This isn't quite the case for CLIP Guided generations, which we tackle in the CLIP Guidance documentation.
            steps=50, # Amount of inference steps performed on image generation. Defaults to 30.
            cfg_scale=8.0, # Influences how strongly your generation is guided to match your prompt.
                        # Setting this value higher increases the strength in which it tries to match your prompt.
                        # Defaults to 7.0 if not specified.
            width=1024, # Generation width, if not included defaults to 512 or 1024 depending on the engine.
            height=1024, # Generation height, if not included defaults to 512 or 1024 depending on the engine.
            samples=1, # Number of images to generate, defaults to 1 if not included.
            sampler=generation.SAMPLER_K_DPMPP_2M # Choose which sampler we want to denoise our generation with.
                                                        # Defaults to k_dpmpp_2m if not specified. Clip Guidance only supports ancestral samplers.
                                                        # (Available Samplers: ddim, plms, k_euler, k_euler_ancestral, k_heun, k_dpm_2, k_dpm_2_ancestral, k_dpmpp_2s_ancestral, k_lms, k_dpmpp_2m, k_dpmpp_sde)
        )

        # Set up our warning to print to the console if the adult content classifier is tripped.
        # If adult content classifier is not tripped, save generated images.
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    warnings.warn(
                        "Your request activated the API's safety filters and could not be processed."
                        "Please modify the prompt and try again.")
                if artifact.type == generation.ARTIFACT_IMAGE:
                    img = Image.open(io.BytesIO(artifact.binary))
                    st.image(img)
                    #img.save(str(artifact.seed)+ ".png") # Save our generated images with their seed number as the filename.

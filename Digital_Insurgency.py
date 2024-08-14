import streamlit as st
import streamlit.components.v1 as components



#components.iframe('<blockquote class="tiktok-embed" cite="https://www.tiktok.com/@real_memebrain" data-unique-id="real_memebrain" data-embed-type="creator" style="max-width: 780px; min-width: 288px;" > <section> <a target="_blank" href="https://www.tiktok.com/@real_memebrain?refer=creator_embed">@real_memebrain</a> </section> </blockquote> <script async src="https://www.tiktok.com/embed.js"></script>')


#st.components.v1.html('<a href="https://www.tiktok.com/@real_memebrain?is_from_webapp=1&sender_device=pc"><img src="images/tiktok-logo-on-transparent-background-free-vector.jpg"></a>')
#st.markdown("[![](images/tiktok-logo-on-transparent-background-free-vector.jpg)](https://www.tiktok.com/@real_memebrain?is_from_webapp=1&sender_device=pc)")
#st.markdown("[![](images/youtube.png)](https://www.youtube.com/channel/UCQv62qXnRifydR7BGksTjMQ)")

#col1, col2 = st.columns(2)

#with col1:
    #st.markdown('[![](images/tiktok-logo-on-transparent-background-free-vector.jpg)](https://www.tiktok.com/@real_memebrain)')
    #st.markdown("[![](images/tiktok-logo-on-transparent-background-free-vector.jpg)](https://www.tiktok.com/@real_memebrain)")
    
#with col2:
    #st.markdown('[![](images/download (2).png)](https://www.youtube.com/channel/UCQv62qXnRifydR7BGksTjMQ)')
    #st.markdown("[![](images/youtube.png)](https://www.youtube.com/channel/UCQv62qXnRifydR7BGksTjMQ)")
    

import streamlit as st
from utils import set_page_config, create_sidebar, load_text

set_page_config()
create_sidebar()

st.title('Digital Insurgency')
st.markdown("#### Unleashing the System's Edge")
st.image('images/Digital_Insurgency.jpg')

st.header('The World', divider='grey')
st.write(load_text('text/the_world.txt'))

st.header('Storyline', divider='grey')
st.write(load_text('text/storyline.txt'))

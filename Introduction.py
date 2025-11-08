import streamlit as st
from streamlit.components.v1 import components

st.markdown(
    """
<style>
.css-nqowgj.edgvbvh3    
{
            visibility:hidden
}      
.css-h5rgaw.egzxvld1
{
            visibility:hidden
} 
</style>
""",
    unsafe_allow_html=True,
)

st.title("Astarag Mohapatra Website")
st.text("Astarag means Asta (sunset) and rag (red color) in my native language Odia")

# st.markdown("![Astarag Mohapatra](https://github.com/Athe-kunal/astarag_mohapatra.github.io/blob/main/my.png)",unsafe_allow_html=True)

col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    st.image("assets/images/my.png")

with col3:
    st.write("")
# st.image(
#     "https://github.com/Athe-kunal/astarag_mohapatra.github.io/blob/45ba6381356a16272d7640a4088f497f20726bf6/my.png",
#     width=450,
# )
# st.markdown("![Photo](https://github.com/Athe-kunal/astarag_mohapatra.github.io/blob/45ba6381356a16272d7640a4088f497f20726bf6/my.png)")

st.write(
    "#### Thank you for joining me here. This is Astarag Mohapatra, currently pursuing Master's in Data Science at Indiana University Bloomington. For the summer 2023, I worked at a Pharmaceutical company named BeiGene as an analytics intern. I am looking for opportunities in the field of Machine learning and Artificial Intelligence."
)

st.write("### Motivation")

st.write(
"In 2018, during my sophomore year in college, I discovered a YouTube video by DeepMind featuring AlphaGO, an AI agent. AlphaGO's victory over the world champion, Lee Seedol, and its innovative move on the 37th turn sparked my interest in AI and ML. Since then, I've been actively involved in various projects and experiences to develop the necessary skills and tools. The symbiotic relationship between humans and machines inspires me to work towards a future where AI benefits us mutually.")

st.write("### Hobbies")
st.write("I am a part-time blogger and I like to write about  abstract topics like conspiracy theories, AI, new technologies and economics. You can find my blogs [here](https://astaragmohapatra.blogspot.com/). Also, I like play guitar and my favourite musician is John Mayer.")


# components.html("""
# <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="astarag-mohapatra-53b739155" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/astarag-mohapatra-53b739155?trk=profile-badge">Astarag Mohapatra</a></div>
              
# """,height=310)

col1,col2,col3 = st.columns(3)

# linkedin_page = """
# <script src="https://platform.linkedin.com/badges/js/profile.js" async defer type="text/javascript"></script>
# <div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="astarag-mohapatra-53b739155" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://www.linkedin.com/in/astarag-mohapatra-53b739155?trk=profile-badge">Astarag Mohapatra</a></div>
# """

# st.components.v1.html(linkedin_page,height=300)

col1.markdown("[![LinkedIN](https://github.com/gauravghongde/social-icons/blob/master/PNG/Color/LinkedIN.png?raw=true)](https://www.linkedin.com/in/astarag-mohapatra-53b739155/)")
col2.markdown("[![GitHub](https://github.com/gauravghongde/social-icons/blob/master/PNG/Color/Github.png?raw=true)](https://github.com/Athe-kunal)")
col3.markdown("[![Medium](https://github.com/gauravghongde/social-icons/blob/master/PNG/Color/Medium.png?raw=true)](https://medium.com/@athekunal)")

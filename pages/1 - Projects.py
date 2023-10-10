import streamlit as st
import base64

st.title("Projects")

st.write(
    """
    ## LARGE LANGUAGE MODELS
    1. SEC Filings Question Answering Agent: Every publicly listed company has to file their quarterly (10-Q) and annual (10-K) reports. The health of the company is reflected in these documents and is essential for investors to process these informations. In this project, I built an end-to-end project
    to parse these documents and QA agent on top of it. Here is the link to my [project](https://github.com/Athe-kunal/SEC-QA-Agent).
    """)

@st.cache_data
def get_demo(path):
    file_ = open(path, "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    return data_url

data_url = get_demo("pages/Demo.gif")
st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" width="1100" height="500" alt="demo gif">',
    unsafe_allow_html=True,
)

st.write(
    """
    2. Llama Hub Open-Source contribution on SEC Filings loader: [loader link](https://llamahub.ai/l/sec_filings)

    3. SEC Filings summarization Project: [GitHub](https://github.com/Athe-kunal/SEC-Summarize-Project) 
    
    4. Llama Hub Open-Source contribution on IMDB Reviews loader: [loader link](https://github.com/run-llama/llama-hub/tree/main/llama_hub/imdb_review)
    
    5. Terms and Conditions QA: As part of a team of six for Lablab AI hackathon partnered with Google, we build a Terms and Conditions Question-Answering agent. Link to repo [here](https://github.com/Athe-kunal/TandC-QA).


        * [Project Page](https://lablab.ai/event/google-vertex-ai-hackathon/prompt-paladins/taco-terms-and-conditions-oracle)

        * Try the live app [here](https://taco-shawisltzq-wl.a.run.app/)
    """)

col1, col2, col3 = st.columns([3,6,1])

with col1:
    st.write("")

with col2:
    st.image("pages/TandCQA.jpeg")

with col3:
    st.write("")

st.write(
    """    
    ## REINFORCEMENT LEARNING
    
    1. Reinforcement learning for algorithmic trading using Google Trends data as state space 
        
        * [GitHub Page](https://github.com/Athe-kunal/Reinforcement-learning-trading-agent-using-Google-trends-data)
        * [Medium Article](https://medium.com/mlearning-ai/google-trends-data-for-automated-stock-trading-using-reinforcement-learning-9c0fd6d00678)
    
    2. Black Litterman-Portfolio Optimization using Reinforcement learning
        * It is Work-in-progress
        * [GitHub Page](https://github.com/Athe-kunal/Black-Litterman-Portfolio-Optimization-using-RL)
    
    3. FinRL Contributions on hyperparameter optimization 
        * [Article along with Tutorials](https://medium.com/@athekunal/list/finrl-contributions-59de6997c5b1)

    ## MACHINE LEARNING
    1. [Applied Machine learning Project Portfolio](https://github.com/Athe-kunal/Machine-learning-Project-Portfolio)
    
    2. [Investment Management Specialization](https://medium.com/@athekunal/list/investment-management-specialization-804635e38cd3)

        * [GitHub Link](https://github.com/Athe-kunal/Invest-Management-with-Python-and-Machine-learning-specialization)

    3. [Machine-Learning-Optimization-using-Gradient-Descent-and-Newton-Raphson-Method](https://github.com/Athe-kunal/Machine-Learning-Optimization-using-Gradient-Descent-and-Newton-Raphson-Method)

    4. [UMass-Advanced-NLP-Course](https://github.com/Athe-kunal/UMass-Advanced-NLP-Course)


    5. [Latent-Dirichlet-Allocation-using-Gibbs-Sampling](https://github.com/Athe-kunal/Latent-Dirichlet-Allocation-using-Gibbs-Sampling)

    6. [Bayesian-Regularized-Linear-Regression](https://github.com/Athe-kunal/Bayesian-Regularized-Linear-Regression)
    """
)

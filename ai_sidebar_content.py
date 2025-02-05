import streamlit as st

def AI_poet():
    st.set_page_config(
        page_title="AI Poet",
        page_icon="🧑‍🎨",
    )

    st.sidebar.header("AI Poet 🧑‍🎨")
    st.sidebar.markdown(
        """
        Tool : OpenAI, Langchain, Streamlit
        \nWhen you type in a subject, the AI crafts a poem related to that topic. You can also choose your favorite language.
    """
    )
    st.sidebar.markdown(
        """
        ### Items to study in this example

        - [LangChain ChatOpenAI](https://python.langchain.com/docs/integrations/chat/openai)
        - [OpenAI Error Types](https://help.openai.com/en/articles/6897213-openai-library-error-types-guidance)
    """
    )

def Todays_Counsel():
    st.set_page_config(
        page_title="Today's Counsel",
        page_icon="🔮",
    )

    st.sidebar.header("Today's Counsel 🔮")
    st.sidebar.markdown(
        """
        Tool : OpenAI, Langchain, Streamlit
        \nPick your birthdate, gender, and the language you like. After that, AI will share stories to uplift your life.
    """
    )
    st.sidebar.markdown(
        """
        ### Items to study in this example

        - [LangChain OpenAI](https://python.langchain.com/docs/integrations/platforms/openai)
        - [Streamlit date_input](https://docs.streamlit.io/library/api-reference/widgets/st.date_input)
    """
    )

import streamlit as st
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckduckgo import DuckDuckGoTools

# 1. Page Configuration
st.set_page_config(page_title="AI Research Studio", layout="wide")
st.title("🤖 Autonomous Web Research Agent")
st.write("An advanced multi-source intelligence agent built with Agno and Streamlit.")

# 2. Sidebar API Key Input (Updated for Gemini)
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter Gemini API Key:", type="password")

st.sidebar.markdown("""
### How to get a free key:
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Click **Get API Key**
3. Create a free key and paste it here!
""")

st.write("---")

# 3. Main Interface Layout
topic = st.text_input("🔍 What topic or trend do you want investigated?", placeholder="e.g., Latest breakthroughs in open-source AI models")

if st.button("Launch Research Team"):
    if not api_key:
        st.error("Please enter your Gemini API key in the sidebar to authorize the agent.")
    elif not topic.strip():
        st.warning("Please enter a valid research topic.")
    else:
        with st.spinner("Agent is searching the web, analyzing articles, and writing report..."):
            try:
                # 4. Initialize the Autonomous Agent with Gemini and Search Tools
                research_agent = Agent(
                    model=Gemini(id="gemini-2.5-flash", api_key=api_key),
                    tools=[DuckDuckGoTools()],
                    description="You are an expert market researcher and tech analyst. Your job is to search the web for the absolute latest data on a topic and compile a deep report.",
                    instructions=[
                        "Always search for current information.",
                        "Include structural headers, bullet points, and key takeaways.",
                        "Cite high-level summaries of findings and list references if available.",
                        "Maintain an objective, highly professional executive tone."
                    ],
                    markdown=True
                )
                
                # 5. Run the Agent response
                response = research_agent.run(topic)
                
                # 6. Display Output
                st.success("✨ Research Analysis Complete!")
                st.markdown(response.content)
                
            except Exception as e:
                st.error(f"An error occurred while running the agent: {e}")
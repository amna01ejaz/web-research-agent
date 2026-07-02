import streamlit as st
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.duckduckgo import DuckDuckGoTools

# 1. Page Configuration
st.set_page_config(page_title="AI Research Studio", layout="wide")
st.title("🤖 Autonomous Web Research Agent")
st.write("An advanced multi-source intelligence agent built with Agno and Streamlit.")

# 2. Sidebar API Key Input (Secure handling)
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Enter OpenAI API Key:", type="password")

st.sidebar.markdown("""
### How it works:
1. **The Agent** receives your research topic.
2. It uses the **DuckDuckGo Tool** to browse the live internet.
3. It filters out irrelevant links, aggregates facts, and writes a professional report.
""")

st.write("---")

# 3. Main Interface Layout
topic = st.text_input("🔍 What topic or trend do you want investigated?", placeholder="e.g., Latest features in Python 3.14")

if st.button("Launch Research Team"):
    if not api_key:
        st.error("Please enter your OpenAI API key in the sidebar to authorize the agent.")
    elif not topic.strip():
        st.warning("Please enter a valid research topic.")
    else:
        with st.spinner("Agent is searching the web, analyzing articles, and writing report..."):
            try:
                # 4. Initialize the Autonomous Agent with Search Tools
                research_agent = Agent(
                    model=OpenAIChat(id="gpt-4o-mini", api_key=api_key),
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
                
                # 5. Run the Agent stream/response
                response = research_agent.run(topic)
                
                # 6. Display Output
                st.success("✨ Research Analysis Complete!")
                st.markdown(response.content)
                
            except Exception as e:
                st.error(f"An error occurred while running the agent: {e}")
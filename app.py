import sys
import os

# Add the src directory to the Python path so the app can find the market_research_crew package
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

import streamlit as st
from market_research_crew.main import run

st.set_page_config(page_title="Market Research Crew", page_icon="📈", layout="wide")

st.title("📈 Market Research Crew AI")
st.markdown("Enter your product idea below to generate a comprehensive market research report.")

# Input for the product idea
product_idea = st.text_area(
    "Product Idea", 
    height=150, 
    placeholder="e.g. An AI powered tool that summarizes youtube videos on my channel and posts the summary on various social media platforms like LinkedIn, Instagram, Facebook, X, WhatsApp"
)

if st.button("Generate Market Research", type="primary"):
    if not product_idea.strip():
        st.error("Please enter a product idea.")
    else:
        st.info("Kickstarting the Market Research Crew... This might take a few minutes. Please wait.")
        
        inputs = {
            "product_idea": product_idea
        }
        
        # Create a placeholder and expander for real-time logs
        st.markdown("### 🔄 Live Execution Logs")
        log_expander = st.expander("View Agent Process under the hood", expanded=True)
        
        # We will store the messages in session state so they persist
        if "agent_logs" not in st.session_state:
            st.session_state.agent_logs = []
        if "step_count" not in st.session_state:
            st.session_state.step_count = 0
            
        st.session_state.agent_logs.clear()
        st.session_state.step_count = 0

        def step_callback(step):
            """Callback function to capture the agents' outputs."""
            try:
                st.session_state.step_count += 1
                
                # Only log every 10th step
                if st.session_state.step_count % 10 != 0:
                    return
                # The step object often contains raw output or tool execution results from CrewAI
                if hasattr(step, "output"):
                    msg = step.output
                elif hasattr(step, "result"):
                    msg = step.result
                elif hasattr(step, "thought"):
                    msg = f"🤔 Thought: {step.thought}"
                elif hasattr(step, "text"):
                    msg = step.text
                else:
                    msg = str(step)
                
                # Append to logs and write to expander
                st.session_state.agent_logs.append(msg)
                with log_expander:
                    st.markdown(f"**Step Completed:**\n{msg}")
                    st.divider()
            except Exception as e:
                pass # Fail silently for callback errors so it doesn't crash the crew

        try:
            with st.spinner("Crew is researching and compiling the report..."):
                # Run the crew
                result = run(inputs=inputs, step_callback=step_callback)
                
            st.success("Market research completed successfully!")
            
            st.markdown("### 📊 Market Research Report")
            
            # Read the generated report from the reports directory
            report_path = os.path.join(os.path.dirname(__file__), 'reports', 'report.md')
            
            if os.path.exists(report_path):
                with open(report_path, 'r', encoding='utf-8') as file:
                    report_content = file.read()
                
                # Displaying the result in the UI
                st.markdown(report_content)
                
                # Provide a download button for the user
                st.download_button(
                    label="📥 Download Market Research Report",
                    data=report_content,
                    file_name="market_research_report.md",
                    mime="text/markdown",
                    type="primary"
                )
            else:
                st.warning("The report file could not be found, but here is the raw result:")
                if hasattr(result, 'raw'):
                    st.markdown(result.raw)
                else:
                    st.markdown(str(result))
            
        except Exception as e:
            st.error(f"An error occurred while running the crew: {e}")

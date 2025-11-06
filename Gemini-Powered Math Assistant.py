import streamlit as st

# Initialize session state
if 'query_history' not in st.session_state:
    st.session_state.query_history = []

st.title("🧠 Gemini Math Assistant")
st.subheader("Practice interactive app development with Streamlit")

# UI Controls
problem_type = st.selectbox("Select problem type:", ["Arithmetic", "Algebra", "Geometry", "Custom"])
difficulty = st.slider("Difficulty level:", 1, 5, 3)
user_input = st.text_area("Enter your math problem or question:")

# Prompt Engineering
def build_prompt(problem_type, difficulty, user_input):
    return f"""
    You are a math assistant. Solve the following {problem_type} problem at difficulty level {difficulty}:
    {user_input}
    Provide step-by-step explanation and final answer.
    """

# Placeholder for Gemini API call
def call_gemini_api(prompt):
    # Replace with actual Gemini API logic
    return f"(Simulated Gemini Response)\nPrompt: {prompt}\nAnswer: [42]"

# Submit and respond
if st.button("Solve"):
    prompt = build_prompt(problem_type, difficulty, user_input)
    response = call_gemini_api(prompt)
    st.session_state.query_history.append((user_input, response))
    st.success("Response generated!")
    st.code(response)

# Display session history
if st.checkbox("Show session history"):
    for i, (q, a) in enumerate(reversed(st.session_state.query_history), 1):
        st.markdown(f"**Problem {i}:** {q}")
        st.code(a)

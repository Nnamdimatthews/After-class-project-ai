import streamlit as st

# Session state initialization
if 'history' not in st.session_state:
    st.session_state.history = []

# UI Components
st.title("🔢 Math Problem Solver")
st.subheader("Customize your problem and get instant solutions")

problem_type = st.selectbox("Choose problem type:", ["Arithmetic", "Algebra", "Geometry", "Custom Prompt"])
difficulty = st.slider("Select difficulty level:", 1, 5, 3)
user_input = st.text_area("Enter your math problem or prompt:")

# Prompt Engineering
def build_prompt(problem_type, difficulty, user_input):
    return f"""
    Solve the following {problem_type} problem at difficulty level {difficulty}:
    {user_input}
    Provide a clear explanation and final answer.
    """

# Placeholder for Gemini API call
def call_gemini_api(prompt):
    # Replace this with actual Gemini API integration
    return f"(Simulated Gemini Response)\nPrompt: {prompt}\nAnswer: [42]"

# Generate response
if st.button("Solve"):
    prompt = build_prompt(problem_type, difficulty, user_input)
    response = call_gemini_api(prompt)
    st.session_state.history.append((user_input, response))
    st.success("Solution generated!")
    st.code(response)

# Display history
if st.checkbox("Show previous problems"):
    for i, (q, a) in enumerate(reversed(st.session_state.history), 1):
        st.markdown(f"**Problem {i}:** {q}")
        st.code(a)
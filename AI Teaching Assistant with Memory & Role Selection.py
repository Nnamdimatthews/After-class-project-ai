import streamlit as st

# Initialize session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

# Role-based system prompt
role_options = {
    "Teacher": "You are a knowledgeable and patient teacher.",
    "Expert": "You are a highly specialized expert in your field.",
    "Friendly Helper": "You are a cheerful and supportive assistant."
}

st.title("🎓 AI Teaching Assistant")
st.subheader("Choose your assistant's role and ask questions")

# Role selection
role = st.selectbox("Select AI role:", list(role_options.keys()))
system_prompt = role_options[role]

# User input
user_question = st.text_input("Ask a question:")

# Simulated AI response (replace with actual API call)
def generate_response(system_prompt, user_question):
    return f"(Simulated Response)\nRole: {role}\nQ: {user_question}\nA: This is a helpful answer tailored to your selected role."

# Handle submission
if st.button("Submit Question"):
    response = generate_response(system_prompt, user_question)
    st.session_state.chat_history.append((user_question, response))
    st.success("Response generated!")

# Display chat history
st.markdown("### 🗂️ Conversation History")
for i, (q, a) in enumerate(reversed(st.session_state.chat_history), 1):
    st.markdown(f"**Q{i}:** {q}")
    st.code(a)

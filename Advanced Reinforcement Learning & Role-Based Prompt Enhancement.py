from typing import Dict, List

class RoleBasedPromptTrainer:
    def __init__(self):
        self.prompts: Dict[str, str] = {}
        self.responses: Dict[str, str] = {}
        self.feedback: Dict[str, List[str]] = {}

    def add_prompt(self, role: str, prompt: str):
        self.prompts[role] = prompt
        print(f"📝 Prompt added for role: {role}")

    def simulate_response(self, role: str) -> str:
        base = self.prompts.get(role, "")
        if "teacher" in role.lower():
            return f"As a teacher, I would explain: {base}"
        elif "expert" in role.lower():
            return f"From an expert's view: {base}"
        elif "peer" in role.lower():
            return f"Hey, here's how I see it: {base}"
        else:
            return f"Generic response: {base}"

    def generate_all_responses(self):
        for role in self.prompts:
            self.responses[role] = self.simulate_response(role)
        print("🤖 Responses generated for all roles.")

    def add_feedback(self, role: str, comment: str):
        if role not in self.feedback:
            self.feedback[role] = []
        self.feedback[role].append(comment)
        print(f"🗣️ Feedback added for {role}")

    def show_summary(self):
        print("\n📊 Role-Based Prompt Summary")
        for role in self.prompts:
            print(f"\nRole: {role}")
            print(f"Prompt: {self.prompts[role]}")
            print(f"Response: {self.responses.get(role, '[No response]')}")
            print(f"Feedback: {self.feedback.get(role, [])}")

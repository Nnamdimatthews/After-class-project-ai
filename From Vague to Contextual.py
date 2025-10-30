from typing import List, Optional
from dataclasses import dataclass, field
import json

@dataclass
class Prompt:
    original: str
    refined: Optional[str] = None
    clarity_score: Optional[int] = None
    specificity_score: Optional[int] = None
    context_score: Optional[int] = None

class PromptEngineer:
    def __init__(self):
        self.prompts: List[Prompt] = []

    def create_prompt(self, text: str):
        self.prompts.append(Prompt(original=text))
        print("🛠️ Prompt created.")

    def refine_prompt(self, index: int, refined_text: str):
        if 0 <= index < len(self.prompts):
            self.prompts[index].refined = refined_text
            print("🔍 Prompt refined.")
        else:
            print("[Error] Invalid prompt index.")

    def evaluate_prompt(self, index: int):
        if 0 <= index < len(self.prompts):
            prompt = self.prompts[index]
            text = prompt.refined or prompt.original
            prompt.clarity_score = self._score_clarity(text)
            prompt.specificity_score = self._score_specificity(text)
            prompt.context_score = self._score_context(text)
            print("📊 Prompt evaluated.")
        else:
            print("[Error] Invalid prompt index.")

    def _score_clarity(self, text: str) -> int:
        return min(10, len(text.split()) // 2)

    def _score_specificity(self, text: str) -> int:
        return min(10, text.count(":") + text.count("-") + text.count("'"))

    def _score_context(self, text: str) -> int:
        keywords = ["context", "audience", "situation", "background"]
        return min(10, sum(1 for word in keywords if word in text.lower()))

    def show_prompt(self, index: int):
        if 0 <= index < len(self.prompts):
            prompt = self.prompts[index]
            print("📝 Prompt Info:")
            print(f"Original: {prompt.original}")
            print(f"Refined: {prompt.refined}")
            print(f"Clarity Score: {prompt.clarity_score}")
            print(f"Specificity Score: {prompt.specificity_score}")
            print(f"Context Score: {prompt.context_score}")
        else:
            print("[Error] Invalid prompt index.")

    def save_prompts(self, filename: str):
        with open(filename, 'w') as f:
            json.dump([prompt.__dict__ for prompt in self.prompts], f, indent=2)
        print(f"💾 Prompts saved to {filename}")

    def load_prompts(self, filename: str):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.prompts = [Prompt(**item) for item in data]
            print(f"📂 Prompts loaded from {filename}")
        except Exception as e:
            print(f"[Error] Failed to load prompts: {e}")

# 🧪 Example usage
if __name__ == "__main__":
    engineer = PromptEngineer()

    engineer.create_prompt("Translate this sentence into French.")
    engineer.refine_prompt(0, "Translate the following English sentence into French: 'I love coding.'")
    engineer.evaluate_prompt(0)
    engineer.show_prompt(0)

    # Optional save/load
    engineer.save_prompts("prompts.json")
    engineer.load_prompts("prompts.json")

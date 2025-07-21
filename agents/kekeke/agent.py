from data_models.prompt_mapping_models import GamePrompts
from data_models.operation_models import UserSession

class KekekeAgent:
    def __init__(self, prompts: GamePrompts, session: UserSession):
        self.prompts = prompts
        self.session = session

    def get_welcome(self):
        lang = self.session.lang
        return getattr(self.prompts, lang).welcome_prompt

    def get_background(self):
        lang = self.session.lang
        return getattr(self.prompts, lang).background_prompt

    def get_final(self, result: str):
        lang = self.session.lang
        return getattr(self.prompts, lang).final_prompts.get(result, "Game over!")

    def add_to_history(self, role: str, content: str):
        self.session.history.append({'role': role, 'content': content})

    def get_history(self):
        return self.session.history 
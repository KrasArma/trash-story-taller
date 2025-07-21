from dataclasses import dataclass
from typing import Dict

@dataclass
class GamePromptsLang:
    welcome_prompt: str
    background_prompt: str
    final_prompts: Dict[str, str]

@dataclass
class GamePrompts:
    en: GamePromptsLang
    ru: GamePromptsLang

@dataclass
class GenerativeMapping:
    kekeke: GamePrompts
    horror: GamePrompts
    math_grinder: GamePrompts 
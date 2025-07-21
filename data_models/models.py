from dataclasses import dataclass, field
from typing import Dict, Optional, List

@dataclass
class CredentialsGiga:
    client_id: str
    client_secret: str
    scope: str
    token: str

@dataclass
class CredentialsApi:
    gigachat: CredentialsGiga

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

@dataclass
class UserSession:
    session_id: str
    game_mode: str
    lang: str
    state: dict = field(default_factory=dict)
    history: List[dict] = field(default_factory=list)
    messages: List[str] = field(default_factory=list) 
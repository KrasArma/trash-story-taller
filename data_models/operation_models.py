from dataclasses import dataclass, field
from typing import List, Dict

@dataclass
class UserSession:
    session_id: str
    game_mode: str
    lang: str
    state: dict = field(default_factory=dict)
    history: List[dict] = field(default_factory=list)
    messages: List[str] = field(default_factory=list) 
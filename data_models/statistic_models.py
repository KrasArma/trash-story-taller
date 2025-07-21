from dataclasses import dataclass
from datetime import datetime

@dataclass
class GameStat:
    session_id: str
    user_id: str
    game_mode: str
    start_time: datetime
    end_time: datetime
    result: str 
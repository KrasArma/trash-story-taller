import asyncio
from typing import Dict, Any, Optional
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole
from services.config_reader import ConfigReader
from data_models.operation_models import UserSession
from data_models.prompt_mapping_models import GamePrompts
from agents.kekeke.agent import KekekeAgent


class GigaChatService:
    def __init__(self):
        self.config_reader = ConfigReader()
        self.credentials = self.config_reader.get_credentials()
        self.mapping = self.config_reader.get_mapping()

    def get_game_prompts(self, game_mode: str) -> GamePrompts:
        if game_mode == 'kekeke':
            return self.mapping.kekeke
        elif game_mode == 'horror':
            return self.mapping.horror
        elif game_mode == 'math-grinder':
            return self.mapping.math_grinder
        raise ValueError(f"Unknown game mode: {game_mode}")

    def generate_welcome_message(self, game_mode: str, session: UserSession) -> str:
        prompts = self.get_game_prompts(game_mode)
        agent = self._get_agent(game_mode, prompts, session)
        lang = session.lang
        messages = [
            Messages(role=MessagesRole.SYSTEM, content=agent.get_background()),
            Messages(role=MessagesRole.USER, content=agent.get_welcome())
        ]
        payload = Chat(messages=messages, temperature=0.7, max_tokens=300)
        with GigaChat(credentials=self.credentials.gigachat.token, verify_ssl_certs=False) as giga:
            response = giga.chat(payload)
            agent.add_to_history('system', agent.get_background())
            agent.add_to_history('user', agent.get_welcome())
            agent.add_to_history('assistant', response.choices[0].message.content)
            return response.choices[0].message.content

    def process_player_response(self, game_mode: str, player_response: str, session: UserSession) -> str:
        prompts = self.get_game_prompts(game_mode)
        agent = self._get_agent(game_mode, prompts, session)
        messages = []
        for msg in agent.get_history():
            role = msg['role']
            content = msg['content']
            if role == 'system':
                messages.append(Messages(role=MessagesRole.SYSTEM, content=content))
            elif role == 'user':
                messages.append(Messages(role=MessagesRole.USER, content=content))
            elif role == 'assistant':
                messages.append(Messages(role=MessagesRole.ASSISTANT, content=content))
        messages.append(Messages(role=MessagesRole.USER, content=player_response))
        payload = Chat(messages=messages, temperature=0.7, max_tokens=300)
        with GigaChat(credentials=self.credentials.gigachat.token, verify_ssl_certs=False) as giga:
            response = giga.chat(payload)
            agent.add_to_history('user', player_response)
            agent.add_to_history('assistant', response.choices[0].message.content)
            return response.choices[0].message.content

    def _get_agent(self, game_mode: str, prompts: GamePrompts, session: UserSession):
        if game_mode == 'kekeke':
            return KekekeAgent(prompts, session)
        # TODO: добавить других агентов
        raise NotImplementedError(f"Agent for mode {game_mode} is not implemented yet.")

gigachat_service = GigaChatService() 
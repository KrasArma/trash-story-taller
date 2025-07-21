import yaml
import json
from data_models.config_models import CredentialsApi, CredentialsGiga
from data_models.prompt_mapping_models import GenerativeMapping, GamePrompts, GamePromptsLang
from typing import Dict
import os

class ConfigReader:
    _instance = None
    _credentials = None
    _mapping = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigReader, cls).__new__(cls)
        return cls._instance

    def load_credentials(self, file_path: str = "configs/api-credentials.yaml") -> CredentialsApi:
        if self._credentials is None:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} not found")
            with open(file_path, 'r', encoding='utf-8') as file:
                data = yaml.safe_load(file)
            gigachat_data = data['gigachat']
            gigachat_creds = CredentialsGiga(
                client_id=gigachat_data.get('client-id', ''),
                client_secret=gigachat_data.get('client-secret', ''),
                scope=gigachat_data.get('scope', ''),
                token=gigachat_data.get('token', '')
            )
            self._credentials = CredentialsApi(gigachat=gigachat_creds)
        return self._credentials

    def load_mapping(self, file_path: str = "configs/generative-mapping.json") -> GenerativeMapping:
        if self._mapping is None:
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"File {file_path} not found")
            with open(file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            def parse_prompts(prompts_dict: Dict) -> GamePrompts:
                return GamePrompts(
                    en=GamePromptsLang(**prompts_dict['en']),
                    ru=GamePromptsLang(**prompts_dict['ru'])
                )
            self._mapping = GenerativeMapping(
                kekeke=parse_prompts(data['kekeke']),
                horror=parse_prompts(data['horror']),
                math_grinder=parse_prompts(data['math-grinder'])
            )
        return self._mapping

    def get_credentials(self) -> CredentialsApi:
        if self._credentials is None:
            return self.load_credentials()
        return self._credentials

    def get_mapping(self) -> GenerativeMapping:
        if self._mapping is None:
            return self.load_mapping()
        return self._mapping 
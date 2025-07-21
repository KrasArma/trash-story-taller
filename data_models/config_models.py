from dataclasses import dataclass

@dataclass
class CredentialsGiga:
    client_id: str
    client_secret: str
    scope: str
    token: str

@dataclass
class CredentialsApi:
    gigachat: CredentialsGiga 
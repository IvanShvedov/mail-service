from dataclasses import dataclass
from http import client

from .base import Base


@dataclass
class CreateMessageDTO:
    created_at: str = None
    status: str = None
    mailing_id: str = None
    client_id: str = None


@dataclass
class UpdateMessageDTO:
    id: str = None
    status: str = None
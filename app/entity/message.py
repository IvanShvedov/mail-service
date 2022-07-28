from dataclasses import dataclass

from .base import Base


@dataclass
class CreateMessageDTO(Base):
    created_at: str = None
    status: str = None
    mailing_id: str = None
    client_id: str = None


@dataclass
class UpdateMessageDTO(Base):
    id: str = None
    status: str = None


@dataclass
class SendMessageDTO(Base):
    id: str = None
    phone: str = None
    text: str = None
from dataclasses import dataclass

from .base import Base


@dataclass
class MailingDTO(Base):
    id: str = None
    start_time: str = None
    message: str = None
    filter: str = None
    end_time: str = None


@dataclass
class CreateMailingDTO(Base):
    start_time: str = None
    message: str = None
    filter: str = None
    end_time: str = None


@dataclass
class UpdateMailingDTO(Base):
    mailing_id: str = None
    start_time: str = None
    message: str = None
    filter: str = None
    end_time: str = None
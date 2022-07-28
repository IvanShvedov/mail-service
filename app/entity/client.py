from dataclasses import dataclass

from .base import Base


@dataclass
class CreateClientDTO(Base):
    phone: str = None
    code: str = None
    tag: str = None
    t_zone: str = None


@dataclass
class UpdateClientDTO(Base):
    client_id: str = None
    phone: str = None
    code: str = None
    tag: str = None
    t_zone: str = None

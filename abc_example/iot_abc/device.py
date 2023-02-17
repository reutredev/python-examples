from abc import ABC, abstractmethod

from abc_example.iot_abc.message import MessageType


class Device(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def disconnect(self) -> None:
        pass

    @abstractmethod
    def send_message(self, message_type: MessageType, data: str) -> None:
        pass

    @abstractmethod
    def status_update(self) -> str:
        pass

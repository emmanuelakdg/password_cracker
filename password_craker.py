from abc import ABC, abstractmethod

class PasswordCracker(ABC):
    @abstractmethod
    def crack_password(self, password):
        pass
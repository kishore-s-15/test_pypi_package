from typing import Optional

class HelloWorld:
    def __init__(self, name: Optional[str] = None):
        self.name = name

    def say_hello(self):
        greeting_message = "Hello "
        greeting_message += self.name if self.name is not None else "user"

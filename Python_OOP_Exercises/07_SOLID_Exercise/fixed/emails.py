from abc import ABC, abstractmethod


class IEmail(ABC):
    @abstractmethod
    def set_sender(self, sender):
        pass

    @abstractmethod
    def set_receiver(self, receiver):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class IContent(ABC):
    def __init__(self, txt):
        self.txt = txt

    @abstractmethod
    def format_content(self):
        pass


class MyContent(IContent):
    def format_content(self):
        return f"<MyML>{self.txt}</MyML>"


class IProtocol(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def format(self):
        pass


class IMProtocol(IProtocol):
    def format(self):
        return f"I'm {self.name}"


class Email(IEmail):
    def __init__(self, protocol):
        self.protocol = protocol
        self.__sender = None
        self.__receiver = None
        self.__content = None

    def set_sender(self, sender: IProtocol):
        self.__sender = sender.format()

    def set_receiver(self, receiver: IProtocol):
        self.__receiver = receiver.format()

    def set_content(self, content):
        self.__content = content.format_content()

    def __repr__(self):
        return f"Sender: {self.__sender}\nReceiver: {self.__receiver}\nContent:\n{self.__content}"


# test code
content = MyContent("Hello, there!")
protocol = IMProtocol("IM")
email = Email(protocol)
email.set_sender(IMProtocol("qmal"))
email.set_receiver(IMProtocol("james"))
email.set_content(content)
print(email)


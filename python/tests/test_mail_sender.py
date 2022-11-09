from mail_sender import MailSender, Request
from tests.http_client import Http_client

from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str

def test_send_v1():
    # TODO: write a test that fails due to the bug in MailSender.send_v1
    client = Http_client()
    mail_sender = MailSender(client)
    user = User("John", "john@email.com")
    mail_sender.send_v1(user, "Hello")
    assert client.base_url == "https://api.mailsender.com"
    assert client.request.name == "John"
    assert client.request.email == "john@email.com"
    assert client.request.subject == "New notification"
    assert client.request.message == "Hello"

def test_send_v2():
    # TODO: write a test that fails due to the bug in MailSender.send_v2
    client = Http_client()
    mail_sender = MailSender(client)
    user = {"name": "John", "email": "john@email.com"}
    mail_sender.send_v1(user, "Hello")
    assert isinstance(client.request, Request)

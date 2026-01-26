class User:
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username



class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __str__(self):
        return f"{self.sender}: {self.content}"
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    # User joins chatroom
    def join_chatroom(self, user):
        self.users.append(user)
        print(f"{user} joined the chatroom")

    # User leaves chatroom
    def leave_chatroom(self, user):
        self.users.remove(user)
        print(f"{user} left the chatroom")

    # Sending message
    def send_message(self, user, content):
        if user in self.users:
            message = Message(user, content)
            self.messages.append(message)
            print(message)
        else:
            print("User not in chatroom!")

    # Viewing chat history
    def chat_history(self):
        print("\nChat History:")
        for idx, msg in enumerate(self.messages):
            print(f"{idx}: {msg}")


u1 = User("Alice")
u2 = User("Bob")

chat = ChatRoom("General")

chat.join_chatroom(u1)
chat.join_chatroom(u2)

chat.send_message(u1, "Hello everyone!")
chat.send_message(u2, "Hi Alice!")

chat.chat_history()

chat.leave_chatroom(u1)

    






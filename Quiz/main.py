class User:
    def __init__(self ,id , username):
        self.id = id
        self.username = username
        self.following = 0
        self.followers = 0
    def follow(self, user):
        user.following += 1
        self.followers += 1

user1 = User(3, "dilip")
user2 = User(6, "bhanu")
print(user1.followers)
user1.follow(user2)
print(user1.followers)

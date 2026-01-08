import uuid

class contact:
    def __init__(self ,nom, email, phone):
        self.id = str(uuid.uuid4())
        self.nom = nom
        self.email = email
        self.phone = phone

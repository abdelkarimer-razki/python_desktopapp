import uuid
import datetime

class contact:
    def __init__(self ,nom, email, phone):
        self._id = str(uuid.uuid4())
        self._nom = nom
        self._email = email
        self._phone = str(phone)
        self._lastTimeEdited = ''
        self._addedTime = str(datetime.datetime.now())
        self._role = 'C'
    
    def setRole(self, role):
        self._role = role


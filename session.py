'''
Nicholas Boni
12/16/2024
'''
from user import User

class Session:
    def __init__(
            self,
            user=User(''),
            active=False
            ):

        self.user = user
        self.active = active

        self.user.set_screen_name()
    
    def log_on(self):
        
        if self.user:
            print('Logged on!')

if __name__ == "__main__":

    session = Session()
    session.log_on()
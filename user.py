'''
Nicholas Boni
12/16/2024
'''

class User:
    def __init__(self, screen_name=''):
        self.screen_name = screen_name

    def set_screen_name(self):
        screen_name = input("Enter a screen name: ")

        looks_good = input(f"Is this OK? '{screen_name}' (y/n) ").lower()

        if not looks_good == 'y':
            print("Let's try that again.")
            screen_name = ''
            return self.set_screen_name()

        self.screen_name = screen_name

if __name__ == "__main__":
    user = User()
    user.set_screen_name()
    print(user.screen_name)
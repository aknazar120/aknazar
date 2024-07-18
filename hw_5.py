class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move(self, direction):
        if direction == 'up':
            self.y -= 1
        elif direction == 'down':
            self.y += 1
        elif direction == 'left':
            self.x -= 1
        elif direction == 'right':
            self.x += 1

class Game:
    def init(self):
        self.player = Player(0, 0)
        self.enemy = Player(3, 3)
    
    def run(self):
        print("Welcome to the game!")
        while True:
            print(f"Player position: ({self.player.x}, {self.player.y})")
            print(f"Enemy position: ({self.enemy.x}, {self.enemy.y})")
            command = input("Enter a command (up/down/left/right/exit): ").lower()
            if command == 'exit':
                print("Goodbye!")
                break
            elif command in ['up', 'down', 'left', 'right']:
                self.player.move(command)
            else:
                print("Invalid command!")

if  name == "main":
    game = Game()
    game.run()
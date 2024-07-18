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
        print("Добро пожаловать в игру!")
        while True:
            print(f"Позиция игрока: ({self.player.x}, {self.player.y})")
            print(f"Позиция врага: ({self.enemy.x}, {self.enemy.y})")
            command = input("Введите команду (вверх/вниз/налево/направо/выход): ").lower()
            if command == 'выход':
                print("До свидания!")
                break
            elif command in ['вверх', 'вниз', 'налево', 'направо']:
                direction = {'вверх':'up','вниз':'down','влево': 'left','вправо': 'right'}[command]
                self.player.move(direction)
            else:
                print("Неверная команда!")

game = Game()
game.run()
           
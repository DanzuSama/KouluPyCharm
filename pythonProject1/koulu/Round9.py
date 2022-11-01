import self as self


class Player:
    color = ''
    points = 0
    def tellscore(self):
        print(f'I am {self.color}, we have {self.points} points!')
    def goal(self):
        self.points += 1
def main():
    user = Player()
    Player.color = 'Blue'
    Player.points = 300
    print(f'The {Player.color} contender had {Player.points} points!')
    user.tellscore()

if __name__ == "__main__":
    main()
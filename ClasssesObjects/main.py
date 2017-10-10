class Enemy:
    life = 100

    def attack(self):
        print("Attack")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:
            print("OUT")
        else:
            print(str(self.life) + " life left")


enemy1 = Enemy()
enemy2 = Enemy()

enemy1.attack()
enemy1.checkLife()

print("=================")

enemy2.checkLife()

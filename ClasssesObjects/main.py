class Enemy:
    life = 100

    def attack(self):
        print("Attack")
        self.life -= 1

    def checkLife(self):
        if self.life <= 0:

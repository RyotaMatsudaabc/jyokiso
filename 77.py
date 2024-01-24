import pyxel

class Ball:
    speed = 3
   
    def __init__(self):
        self.restart()
   
    def move(self):
        if (self.y <= 0) or (self.y >= 200):
            self.vy *= -1
            Ball.speed*=1.1
   
    def restart(self):
        self.x = 200
        self.y = 1
        angle = pyxel.rndi(30,150)
        self.vx = pyxel.sin(angle)
        self.vy = pyxel.cos(angle)
        Ball.speed=3


class Pad:
    def __init__(self,x):
        self.x = x
        self.y = 50
        self.score = 0
        self.miss = 0
   
    def catch1(self, thisball):
        if thisball.x-10<self.x+5 and thisball.x-10>self.x and thisball.y+7>self.y and thisball.y-7<self.y+40:
            return True
        else:
            return False
        
    def catch2(self, thisball):
        if thisball.x+10<self.x+5 and thisball.x+10>self.x and thisball.y+7>self.y and thisball.y-7<self.y+40:
            return True
        else:
            return False


class App:
    score = 0
    miss = 0
    gameover = False

    def __init__(self):
        pyxel.init(400,200)
        pyxel.sound(0).set(notes='C0', tones='T', volumes='7', effects='N', speed=30)
        pyxel.sound(1).set(notes='B3G3', tones='P', volumes='3', effects='N', speed=10)
        App.p1 = Pad(15)
        App.p2 = Pad(385)
        App.b = [Ball(),Ball()]
        pyxel.run(self.update, self.draw)

    def update(self):
        for b in App.b:
            b.x += (b.vx * Ball.speed)
            b.y += (b.vy * Ball.speed)

            if b.x < 0:
                pyxel.play(0, 0)
                App.p1.miss += 1
                App.p2.score += 1
                b.restart()
            if b.x > 400:
                pyxel.play(0, 0)
                App.p2.miss += 1
                App.p1.score += 1
                b.restart()
            
            b.move()
            if self.p1.catch1(b) == True:
                b.vx*=-1
                pyxel.play(0, 1)
                Ball.speed += 0.1
            if self.p2.catch2(b) == True:
                b.vx*=-1
                pyxel.play(0, 1)
                Ball.speed += 0.1
            if pyxel.btn(pyxel.KEY_W):
                App.p1.y -= 8
            if pyxel.btn(pyxel.KEY_S):
                App.p1.y += 8
            if pyxel.btn(pyxel.KEY_UP):
                App.p2.y -= 8
            if pyxel.btn(pyxel.KEY_DOWN):
                App.p2.y += 8

            if App.p1.miss >= 3:
                App.gameover = True
            if App.p2.miss >= 3:
                App.gameover = True         

    def draw(self):
        if App.gameover:
            pyxel.text(80, 100, "GAME OVER", 0)
            if App.p1.miss >= 3:
                pyxel.text(80, 130, "Player 2 Wins", 0)
            if App.p2.miss >= 3:
                pyxel.text(80, 130, "Player 1 Wins", 0)

        else:
            pyxel.cls(7)
            pyxel.text(10, 10, "score : " + str(App.p1.score), 0)
            pyxel.text(350, 10, "score : " + str(App.p2.score), 0)
            pyxel.text(10, 20, "miss : " + str(App.p1.miss), 0)
            pyxel.text(350, 20, "miss : " + str(App.p2.miss), 0)
            for b in App.b:
                pyxel.circ(b.x, b.y, 10, 6)
            pyxel.rect(self.p1.x, self.p1.y, 5, 40, 14)
            pyxel.rect(self.p2.x, self.p2.y, 5, 40, 14)

App()

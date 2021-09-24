from typing import Text
from manim import *
from random import randrange



class Introducao(Scene):
    def construct(self):
        t = MarkupText(f'Como <span fgcolor="{BLUE}">Facebook</span> e <span fgcolor="{BLUE}">G</span><span fgcolor="{RED}">o</span><span fgcolor="{YELLOW}">o</span><span fgcolor="{BLUE}">g</span><span fgcolor="{GREEN}">l</span><span fgcolor="{RED}">e</span> rastreiam seus dados',  font_size=30)
        self.play(Write(t),run_time=3)

        t2 = MarkupText(f'Como <span fgcolor="{BLUE}">Facebook</span> e <span fgcolor="{BLUE}">G</span><span fgcolor="{RED}">o</span><span fgcolor="{YELLOW}">o</span><span fgcolor="{BLUE}">g</span><span fgcolor="{GREEN}">l</span><span fgcolor="{RED}">e</span> rastreiam seus dados',  font_size=30)
        t2.to_edge(UP)

        self.add(t)
        self.play(Transform(t,t2),run_time=2)
        self.wait(2)

        google = ImageMobject("images/google.png")
        self.add(google)
        self.play(google.animate.shift([-4,1,0]),run_time=2)
        self.wait()

        facebook = ImageMobject("images/facebook.png")
        self.add(facebook)
        self.play(facebook.animate.shift([-4,-1,0]),run_time=2)
        self.wait()

        #Feed data
        #nomes, nosso endereço, idade, data de aniversário e interesses
        nomes = Text('Nomes',font_size=30).scale(1)
        self.play(FadeOut(nomes, target_position=[-3,0,0],run_time=1.5))
        self.wait()

        ende = Text('Endereço',font_size=30).scale(1)
        self.play(FadeOut(ende, target_position=[-3,0,0],run_time=1.5))
        self.wait()

        idade = Text('Idade',font_size=30).scale(1)
        self.play(FadeOut(idade, target_position=[-3,0,0],run_time=1.5))
        self.wait()

        niver = Text('Aniversário',font_size=30).scale(1)
        self.play(FadeOut(niver, target_position=[-3,0,0],run_time=1.5))
        self.wait()

        inte = Text('Interesses',font_size=30).scale(1)
        self.play(FadeOut(inte, target_position=[-3,0,0],run_time=1.5))
        self.wait()


class Parte1(Scene):
    def construct(self):

        t = MarkupText(f'Como <span fgcolor="{BLUE}">Facebook</span> e <span fgcolor="{BLUE}">G</span><span fgcolor="{RED}">o</span><span fgcolor="{YELLOW}">o</span><span fgcolor="{BLUE}">g</span><span fgcolor="{GREEN}">l</span><span fgcolor="{RED}">e</span> rastreiam seus dados',  font_size=30)
        t.to_edge(UP)
        self.add(t)
        self.wait()

        folder = Group(*[ImageMobject("images/folder.png").scale(0.05) for _ in range(30)]) 

        i = -3
        j = 1
        pos = 0
        for x in range(5):
            for y in reversed(range(6)):
                self.play(folder[pos].animate.shift([i,j,0]),run_time=0.2)
                i += 1
                pos += 1
            i = -3        
            j -= 1

        self.wait(3)
        self.play(folder.animate.scale(0.001))

        self.wait()

    

class Parte2(Scene):
    def construct(self):

        profile = ImageMobject("images/profile.png").scale(0.8)
        self.add(profile)
        self.play(FadeIn(profile),run_time=2)
        self.wait()

        calendar = ImageMobject("images/calendar.png").scale(0.5)
        self.add(calendar)
        self.play(FadeOut(calendar),run_time=1)
        self.wait()

        gender = ImageMobject("images/gender.png").scale(0.15)
        self.add(gender)
        self.play(FadeOut(gender),run_time=1)
        self.wait()

        moto = ImageMobject("images/moto.png").scale(2.3)
        self.add(moto)
        self.play(FadeOut(moto),run_time=1)

        self.wait()

        vacation = ImageMobject("images/vacation.png").scale(0.5)
        self.add(vacation)
        self.play(FadeOut(vacation),run_time=1)
        self.wait()

        iphone = ImageMobject("images/iphone.png").scale(0.5)
        self.add(iphone)
        self.play(FadeOut(iphone),run_time=1)
        self.wait()



class Parte3(Scene):
    def construct(self):
        
        like = ImageMobject("images/like.png").scale(0.2)
        like.shift([-1,0,0])
        self.add(like)
        
        for x in range(4):
            self.play(like.animate.scale(0.8),run_time=0.2)
            self.play(like.animate.scale(1.2),run_time=0.2)    
        self.wait()

        couple = ImageMobject("images/couple.png").scale(0.4)
        couple.next_to(like,RIGHT)
        self.add(couple)
        self.play(FadeOut(couple,run_time=3))
        self.wait()

        breakup = ImageMobject("images/break.png").scale(0.5)
        breakup.next_to(like,RIGHT)
        self.add(breakup)
        self.play(FadeOut(breakup,run_time=3))
        self.wait()



class Parte4(Scene):
    def construct(self):
        t = Text("Onde você está")
        t2 = Text("Onde você está").scale(0.5)
        t2.to_edge(LEFT)
        self.play(GrowFromCenter(t))
        self.play(Transform(t,t2),run_time=3)
        self.wait()

        instagram = ImageMobject("images/instagram.png").scale(0.4)
        self.add(instagram)
        self.play(FadeOut(instagram,run_time=3))
        #self.wait()

        waze = ImageMobject("images/waze.png").scale(0.3)
        self.add(waze)
        self.play(FadeOut(waze,run_time=3))
        self.wait(2)

        folder = Group(*[ImageMobject("images/maps.png").scale(0.1) for _ in range(20)]) 


        for x in range(20):
            i = randrange(14) -7 
            j = randrange(8) -4

            self.play(folder[x].animate.shift([i,j,0]),run_time=0.2)

        self.wait()
        maps = ImageMobject("images/maps.png").scale(0.1)
        #self.add(maps)
        self.play(folder.animate.shift([0,0,0]).scale(0.001))
        maps.next_to(folder,UP)
        self.play(maps.animate.scale(1))
        self.wait()

        ads = Group(*[ImageMobject("images/buy.png").scale(0.3) for _ in range(120)]) 
        ads.to_edge(RIGHT)
        for x in range(120):
            self.play(FadeOut(ads[x],target_position=folder,run_time=0.15))

        self.wait()



class Parte5(Scene):
    def construct(self):
        t = Text("O que você compra")
        t2 = Text("O que você compra").scale(0.5)
        t2.to_edge(LEFT)
        self.play(GrowFromCenter(t))
        self.play(Transform(t,t2),run_time=1)
        self.wait()

        buy = ImageMobject("images/buy.png").scale(0.5)
        buy.shift([-1,0,0])
        finger = ImageMobject("images/finger.png").scale(0.3)
        finger.shift([-1,-0.5,0])
        self.add(buy,finger)

        for x in range(5):
            self.play(finger.animate.scale(0.8),run_time=0.2)
            self.play(finger.animate.scale(1.2),run_time=0.2)    
        self.wait()



class Parte6(Scene):
    def construct(self):
        folder = Group(*[ImageMobject("images/folder.png").scale(0.05) for _ in range(30)]) 

        i = -3
        j = 2
        pos = 0
        for x in range(5):
            for y in reversed(range(6)):
                self.play(folder[pos].animate.shift([i,j,0]),run_time=0.2)
                i += 1
                pos += 1
            i = -3        
            j -= 1
        
        self.play(folder.animate.scale(0.00001))



class Parte7(Scene):
    def construct(self):

        burger = ImageMobject("images/burger.png").scale(0.8)
        self.add(burger)
        self.play(FadeOut(burger),run_time=1)
        #self.wait()
        card = ImageMobject("images/card.png").scale(0.8)
        self.add(card)
        self.play(FadeOut(card),run_time=8)

        pill = ImageMobject("images/pill.png").scale(0.5)
        self.add(pill)
        self.play(FadeOut(pill),run_time=4)


class Parte8(Scene):
    def construct(self):
        t = Text("Quem você conhece")
        t2 = Text("Quem você conhece").scale(0.5)
        t2.to_edge(LEFT)
        self.play(GrowFromCenter(t))
        self.play(Transform(t,t2),run_time=1)
        self.wait()

        title = Text("Pessoas que você talvez conheça",color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait()

        folder = Group(*[ImageMobject("images/profile.png").scale(0.1) for _ in range(9)]) 

        i = -2
        j = 2
        pos = 0
        for x in range(3):
            for y in reversed(range(3)):
                self.play(folder[pos].animate.shift([i,j,0]),run_time=0.2)
                i += 3
                pos += 1
            i = -2        
            j -= 2
        
        l= Line(folder[4].get_center(), folder[5].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[4].get_center(), folder[1].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[4].get_center(), folder[8].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[2].get_center(), folder[1].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[3].get_center(), folder[7].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[0].get_center(), folder[3].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[0].get_center(), folder[4].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[6].get_center(), folder[1].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[8].get_center(), folder[1].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[2].get_center(), folder[5].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[5].get_center(), folder[8].get_center())
        self.add(l)
        self.wait(2)
        l= Line(folder[6].get_center(), folder[7].get_center())
        self.add(l)
        self.wait(2)
        





class Parte9(Scene):
    def construct(self):
        t = Text("Você como produto")
        t2 = Text("Você como produto").scale(0.5)
        t2.to_edge(UP)
        self.play(GrowFromCenter(t))
        self.play(Transform(t,t2),run_time=1)
        self.wait()

        money = ImageMobject("images/money.png").scale(0.6)
        self.add(money)
        self.play(FadeIn(money),run_time=10)
        self.wait(2)



class Parte10(Scene):
    def construct(self):
        t = Text("Miguel Lima Tavares")
        t2 = Text("Miguel Lima Tavares").scale(0.5)
        t2.to_edge(UP)
        self.play(GrowFromCenter(t))
        self.play(Transform(t,t2),run_time=1)
        self.wait() 

        t3 = Text("Trabalho Comp Soc UFJR")
        t4 = Text("Trabalho Comp Soc UFRJ").scale(0.5)
        t4.next_to(t,DOWN)
        self.play(GrowFromCenter(t3))
        self.play(Transform(t3,t4),run_time=1)
        self.wait() 

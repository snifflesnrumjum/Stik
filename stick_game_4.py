# Card images made available by John K. Estell; originally released by 'oxymoron' and released under the GNU GPL
# Card images can be found here: http://nifty.stanford.edu/2004/EstellCardGame/code.html
# All game code was written by Darren W. Henrichs and released under the GNU GPLv3
# The game of Stik is a family card game that was played at numerous family reunions. No one is quite sure 
# where the originated but it bears a lot of resemblance to a game called Sedma (related to Ristikontra)
# Right now it's a fixed window size game. It was early in my coding career and I hard-coded card positions.
# Cards folder needs to be placed in same directory as this script when run

import random
import pygame
import time
import sys


font_to_use = ''
font_to_use2 = ''
total_score = []

class Card:
    def __init__(self):
        self.name = None
        self.value = None
        self.pointcard = None
        self.back_image = None
        self.front_image = None
        self.show_status = None
        self.cardlocation = None
        self.black_card = None
        

    def setup_card(self, name, value, points):
        self.name = name
        self.value = value
        self.pointcard = points
        self.cardlocation = [10, 10]
        self.black_card = pygame.image.load('./cards/darkcard.gif')
        self.back_image = pygame.image.load('./cards/Stick-Cards.gif').convert()
                
        

class Deck:
    def __init__(self):
        self.remaining = []
        self.currentname = 7
        self.currentvalue = 7
        self.currentpoints = False
        for x in range(0, 17, 4):
            if x < 16:
                self.card1 = Card()
                self.card1.setup_card(str(self.currentname)+'H',self.currentvalue, self.currentpoints)
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %(self.currentname, 'h')).convert()
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card(str(self.currentname)+'S',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %(self.currentname, 's')).convert()
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card(str(self.currentname)+'C',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %(self.currentname, 'c')).convert()
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card(str(self.currentname)+'D',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %(self.currentname, 'd')).convert()
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.currentname +=1
                self.currentvalue +=1
            else:
                self.card1 = Card()
                self.card1.setup_card('J'+'H',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('j', 'h')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('J'+'S',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('j', 's')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('J'+'C',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('j', 'c')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('J'+'D',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('j', 'd')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.currentname +=1
                self.currentvalue +=1
                
                self.card1 = Card()
                self.card1.setup_card('K'+'H',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('k', 'h')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('K'+'S',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('k', 's')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('K'+'C',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('k', 'c')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('K'+'D',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('k', 'd')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.currentname +=1
                self.currentvalue +=1
                
                self.card1 = Card()
                self.card1.setup_card('Q'+'H',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('q', 'h')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('Q'+'S',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('q', 's')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('Q'+'C',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('q', 'c')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('Q'+'D',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('q', 'd')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.currentname +=1
                self.currentvalue +=1
                self.card1 = Card()
                self.card1.setup_card('A'+'H',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('a', 'h')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('A'+'S',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('a', 's')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('A'+'C',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('a', 'c')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.card1 = Card()
                self.card1.setup_card('A'+'D',self.currentvalue, self.currentpoints)
                
                self.card1.front_image = pygame.image.load('./cards/%s%s.gif' %('a', 'd')).convert()
                
                self.card1.show_status = False
                self.remaining.append(self.card1)
                
                self.currentname +=1
                self.currentvalue +=1
                
                
        for card in range(32):
            if self.remaining[card].value == 10 or self.remaining[card].value == 14:
                self.remaining[card].pointcard = True
    def shuffle(self):
        self.remaining = random.sample(self.remaining, len(self.remaining))

    

class Hand: 
    def __init__(self):
        self.handname = None
        self.cardsinhand = []
        self.cardcount = [0,0,0,0,0,0,0,0]
        self.cardcounter = False
        self.playername = ''
        self.pointtaker = False
        self.risktaker = False
        self.handlocation = None
        self.cardhandlocations = [[170, 370], [500, 120], [170, 20], [50, 120]]
        
    
    def update_cardlocation(self):
        startx = self.cardhandlocations[self.handlocation][0]
        starty = self.cardhandlocations[self.handlocation][1]
        for card in self.cardsinhand:
            card.cardlocation = [startx, starty]
            if self.handlocation == 0 or self.handlocation == 2:
                startx += 75
            else:
                starty += 60
        

    def update_card_count(self, cardsinround):
        for card in cardsinround:
            a = card.value-7
            self.cardcount[a]+=1

    def reset_card_count(self):
        self.cardcount = [0,0,0,0,0,0,0,0]
    
    def card_count(self, cardsinround):
        temp_count = self.cardcount[:]
        for card in self.cardsinhand:
            a = card.value-7
            temp_count[a] += 1
        for card in cardsinround:
            a = card.value-7
            temp_count[a] += 1
        return temp_count
        
    def check_cards(self):
        temp_count = self.cardcount[:]
        prob_play = []
        for card in self.cardsinhand:
            prob_play.append(0.25)
            a = card.value-7
            temp_count[a] += 1
        
        cardtoplay = 0
        for card in self.cardsinhand:
            if temp_count[card.value-7] == 4:
                prob_play[self.cardsinhand.index(card)] += 10
    
            else:
                if temp_count[card.value-7] == 3:
                    if card.pointcard == True:
                        prob_play[self.cardsinhand.index(card)] += .2
                    else:
                        prob_play[self.cardsinhand.index(card)] += .5
                elif temp_count[card.value-7] == 2:
                    prob_play[self.cardsinhand.index(card)] += .25
        #print prob_play
        
        cardtoplay = prob_play.index(max(prob_play))
        return cardtoplay
        
    def check_cards_low(self):
        temp_count = self.cardcount[:]
        prob_play = []
        for card in self.cardsinhand:
            prob_play.append(0.25)
            a = card.value-7
            temp_count[a] += 1
        
        cardtoplay = 0
        for card in self.cardsinhand:
            if temp_count[card.value-7] == 4:
                prob_play[self.cardsinhand.index(card)] += 10
    
            else:
                if temp_count[card.value-7] == 3:
                    prob_play[self.cardsinhand.index(card)] += .5
                elif temp_count[card.value-7] == 2:
                    prob_play[self.cardsinhand.index(card)] += .25
        #print prob_play
        
        cardtoplay = prob_play.index(min(prob_play))
        if self.cardsinhand[cardtoplay].pointcard == True and random.random() < 0.8:
            for card in self.cardsinhand:
                if card.pointcard == False:
                    cardtoplay = self.cardsinhand.index(card)
        return cardtoplay
    def playcard_cardcounter(self, cardsinround):
        return self.cardsinhand.pop(self.check_cards)
    
    def playcard(self, cardsinround):
        global players
        self.cardtoplay = -1
        
        #if self.cardcounter == True:
        #    self.cardtoplay = self.check_cards()
            
        #else:
        if 1==1:
        
            if len(cardsinround)>0:
                self.cardtosearchfor = cardsinround[0].value
            else:
                self.cardtosearchfor = -1

            if self.cardtosearchfor > 0:
                #this section checks to see if this player's partner is going to take the trick. if yes then this player searches his hand for a pointcard to play. if he has one he plays it
                if len(cardsinround) == 3 and self.pointtaker == True:
                    if cardsinround[1].value == cardsinround[0].value and cardsinround[2].value != cardsinround[0].value:
                        for card in self.cardsinhand:
                            if card.pointcard == True:
                                self.cardtoplay = self.cardsinhand.index(card)
                #this section does the same thing as above but only if two cards have been played and there's no chance the fourth player can win it                
                elif len(cardsinround) == 2 and self.pointtaker == True:
                    if cardsinround[0].value != cardsinround[1].value:
                        temp_card_count = self.card_count(cardsinround)
                        if temp_card_count[cardsinround[0].value-7] == 4:
                            for card in self.cardsinhand:
                                if card.pointcard == True:
                                    self.cardtoplay = self.cardsinhand.index(card)
                        elif temp_card_count[cardsinround[0].value-7] == 3 and random.random() < (0.95 - (sum(temp_card_count)/32.)):
                            for card in self.cardsinhand:
                                if card.pointcard == True:
                                    self.cardtoplay = self.cardsinhand.index(card)
                                    
                        elif temp_card_count[cardsinround[0].value-7] == 2 and random.random() < (0.75 - (sum(temp_card_count)/32.)):
                            for card in self.cardsinhand:
                                if card.pointcard == True:
                                    self.cardtoplay = self.cardsinhand.index(card)
                            
            if self.cardtoplay == -1:
            #this section checks to see if this player has a card that can take the lead. if he has one he WILL play it with a 98% probability. 
                for availablecard in self.cardsinhand:
                    if self.cardtoplay == -1:
                        if availablecard.value == self.cardtosearchfor and random.random() < 0.98:
                            self.cardtoplay = self.cardsinhand.index(availablecard)
            if self.cardtoplay == -1:
                #this section is the fallback option. if the player is a card counter it will access that information to decide what card to play; if not a card counter then it picks one at random
                if self.cardcounter == True and len(cardsinround)>0:
                    if self.risktaker == True:
                        self.cardtoplay = self.check_cards()
                    else:
                        self.cardtoplay = self.check_cards_low()
                elif self.cardcounter == True:
                    self.cardtoplay = self.check_cards()
                else:
                    self.cardtoplay = random.randint(0,len(self.cardsinhand)-1)
                    #if the randomly picked card is a pointcard there's 95% chance of going back and again picking a random card. can pick the same card again.
                if self.cardsinhand[self.cardtoplay].pointcard == True and random.random() < 0.95:# and self.cardcounter == False:
                    self.cardtoplay = random.randint(0,len(self.cardsinhand)-1)

        return self.cardsinhand.pop(self.cardtoplay)
    
    def player_playcard(self, cardsinround):
        
        for card in self.cardsinhand:
            screen.blit(card.black_card, (card.cardlocation[0], card.cardlocation[1]))
                
        self.update_cardlocation()
        for card in self.cardsinhand:
            screen.blit(card.front_image, (card.cardlocation[0], card.cardlocation[1]))
        pygame.display.update()
                
        self.cardtoplay = -1
        num_cards = len(self.cardsinhand)
        xcardrange = [170, 170]
        for xcard in range(num_cards):
            xcardrange[1] += 75
            
        ycardrange = [370, 370+97]
        
        clicked_yet = False
        pygame.event.clear()
        pygame.event.set_allowed(None)
        pygame.event.set_allowed(6)
        pygame.event.set_allowed(12)
        while clicked_yet == False:
            if pygame.event.peek() == False:
                time.sleep(250)
            event = pygame.event.wait()
            #for event in pygame.event.get():
            if event.type == 12:
                #print 'hello'
                sys.exit()
            if event.type ==6:
                if event.pos[0] in range(xcardrange[0], xcardrange[0]+73) and event.pos[1] in range(ycardrange[0], ycardrange[1]):
                    self.cardtoplay = 0
                elif event.pos[0] in range(xcardrange[0]+75, xcardrange[0]+73+75) and event.pos[1] in range(ycardrange[0], ycardrange[1]) and num_cards>1:
                    self.cardtoplay = 1
                elif event.pos[0] in range(xcardrange[0]+150, xcardrange[0]+73+150) and event.pos[1] in range(ycardrange[0], ycardrange[1]) and num_cards>2:
                    self.cardtoplay = 2
                elif event.pos[0] in range(xcardrange[0]+225, xcardrange[0]+73+225) and event.pos[1] in range(ycardrange[0], ycardrange[1]) and num_cards>3:
                    self.cardtoplay = 3
                    
                if self.cardtoplay != -1:
                    clicked_yet = True
                        
                        
        #self.cardtoplay = raw_input('Which card would you like to play? [1-4]')
        #while len(self.cardtoplay)!=1:
        #    self.cardtoplay = raw_input('Which card would you like to play? [1-4]')
        #while int(self.cardtoplay) < 1 or int(self.cardtoplay) > len(self.cardsinhand):
         #      self.cardtoplay = int(raw_input('Which card would you like to play? [1-4]'))
        #self.cardtoplay = int(self.cardtoplay)-1
        return self.cardsinhand.pop(self.cardtoplay)                
        
def deal_hand(players, numberofcards, deck):
    numcards_dealt = 0
    #while numcards_dealt < numberofcards:
    for dealer in range(numberofcards):
        for player in players:
            player.cardsinhand.append(deck.remaining.pop())
        numcards_dealt += 1
    #print 'remaining:', len(deck.remaining), len(players[0].cardsinhand)
    
def play_round(players, deck, whostarts):
    global total_score
    tricks_taken = []
    whose_turn = whostarts
    whose_lead = whostarts
    final_score_reached = False
    cards_played_loc = [[245, 250], [345, 200], [245, 140], [150, 200]]
    while len(players[0].cardsinhand) > 0 and final_score_reached == False:
        cards_played = []
        whose_turn = whose_lead
        for player in players:
            if player.handname == 'Human':
                pass
            else:
                for card in player.cardsinhand:
                    screen.blit(card.back_image, (card.cardlocation[0], card.cardlocation[1]))
        pygame.display.update()
        while len(cards_played) < 4:
            if players[whose_turn].handname == 'Human':
                cards_played.append(players[whose_turn].player_playcard(cards_played))
                screen.blit(cards_played[-1].black_card, (cards_played[-1].cardlocation[0], cards_played[-1].cardlocation[1]))
                cards_played[-1].cardlocation = [cards_played_loc[whose_turn][0], cards_played_loc[whose_turn][1]]
                screen.blit(cards_played[-1].front_image, (cards_played[-1].cardlocation[0], cards_played[-1].cardlocation[1]))
                pygame.display.update()
                
            else:
                cards_played.append(players[whose_turn].playcard(cards_played))
                screen.blit(cards_played[-1].black_card, (cards_played[-1].cardlocation[0], cards_played[-1].cardlocation[1]))
                cards_played[-1].cardlocation = [cards_played_loc[whose_turn][0], cards_played_loc[whose_turn][1]]
                screen.blit(cards_played[-1].front_image, (cards_played[-1].cardlocation[0], cards_played[-1].cardlocation[1]))
                #players[whose_turn].update_cardlocation()
                for card in players[whose_turn].cardsinhand:
                    screen.blit(card.back_image, (card.cardlocation[0], card.cardlocation[1]))
                pygame.display.update()
            
                
                
            if cards_played[-1].value == cards_played[0].value:
                whose_lead = whose_turn
            if whose_turn == len(players)-4:
                whose_turn = 3
            else:
                whose_turn -= 1

        
        time1 = time.time()
        while time.time()-time1 < 2:
            time.sleep(1)
        for player in players:
            if player.cardcounter == True:
                player.update_card_count(cards_played)
                
        
        for card in cards_played:
            screen.blit(card.black_card, (card.cardlocation[0], card.cardlocation[1]))
        
        if cards_played[0].value == cards_played[1].value:
            if cards_played[0].value == cards_played[2].value:
                if cards_played[0].value == cards_played[3].value:
                    if whose_lead == 0 or whose_lead == 2:
                        total_score[0] += 5
                    else:
                        total_score[1] += 5
                    print_new_score_because_stik(total_score)
                    if total_score[0] > 20 or total_score[1] > 20:
                        final_score_reached = True
                        
        tricks_taken.append([whose_lead, cards_played])
        if len(deck.remaining) > 0:
            deal_hand(players, 1, deck)
        for player in players:
            if player.handname == 'Computer':
                for card in player.cardsinhand:
                    screen.blit(card.black_card, (card.cardlocation[0], card.cardlocation[1]))
                player.update_cardlocation()
                for card in player.cardsinhand:
                    screen.blit(card.back_image, (card.cardlocation[0], card.cardlocation[1]))
        pygame.display.update()
        
    return tricks_taken

def score_round(tricks_taken):
    scores = [0,0]
    trick_count = [0,0]

    temp_round_score = [0,0]
    if tricks_taken[-1][0] == 0 or tricks_taken[-1][0] == 2:
        temp_round_score[0] += 1
    else:
        temp_round_score[1] += 1
    for trick in tricks_taken:
        points = 0
        for card in trick[1]:
            if card.pointcard == True:
                points += 1
        if points > 0:
            if trick[0] == 0 or trick[0] == 2:
                temp_round_score[0] += points
            else:
                temp_round_score[1] += points
        if trick[0] == 0 or trick[0] == 2:
            trick_count[0] += 1
        else:
            trick_count[1] += 1
    if trick_count[0] == 8:
        scores[0] += 9
    elif trick_count[1] == 8:
        scores[1] += 9
    elif temp_round_score[0] > 4:
        scores[0] += temp_round_score[0] - 4
    else:
        scores[1] += temp_round_score[1] - 4
    return scores

def print_new_score_because_stik(total_score):
    game_font_surface1 = font_to_use.render("Current score:", True, (255,255,255), (0,0,0))
    str_team_score = 'Your team: '
    if total_score[0]>9:
        str_team_score += str(total_score[0])+' '
    else:
        str_team_score += str(total_score[0])+'  '
    game_font_surface2 = font_to_use.render(str_team_score, True, (255,255,255), (0,0,0))
    str_comp_score = 'Computer : '
    if total_score[1] > 9:
        str_comp_score += str(total_score[1])+' '
    else:
        str_comp_score += str(total_score[1])+'  '
            
    game_font_surface3 = font_to_use.render(str_comp_score, True, (255,255,255), (0,0,0))
    screen.blit(game_font_surface1, (500, 415))
    screen.blit(game_font_surface2, (500, 433))
    screen.blit(game_font_surface3, (500, 451))
    pygame.display.update()



def play_the_game():
    global screen
    global firstrun
    global difficulty
    global players
    global total_score
    global font_to_use
    global font_to_use2
    pygame.init()
    #screen = pygame.display.set_mode((640, 480))
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Valigura Stik')

    avail_fonts = pygame.font.get_fonts()
    avail_fonts.sort()
    if 'timesnewroman' in avail_fonts:
        game_font = pygame.font.SysFont('timesnewroman', 16)
        game_font_2 = pygame.font.SysFont('timesnewroman', 30)
    elif 'arial' in avail_fonts:
        game_font = pygame.font.SysFont('arial', 16)
        game_font_2 = pygame.font.SysFont('arial', 30)
    else:
        game_font = pygame.font.SysFont(avail_fonts[1], 16)
        game_font_2 = pygame.font.SysFont(avail_fonts[1], 30)
        
    font_to_use = game_font
    font_to_use2 = game_font_2
    if firstrun == True:
        difficulty = ask_difficulty_name(game_font_2, screen)
        #screen = pygame.display.set_mode((640, 480))
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption('Valigura Stik')
        firstrun = False
    #print difficulty
    hand1.cardsinhand = []
    hand2 = Hand()
    hand2.handname = 'Computer'
    hand2.playername = 'Charles'
    hand2.cardcounter = True
    hand2.handlocation = 1
    hand3 = Hand()
    hand3.handname = 'Computer'
    hand3.playername = 'Lucy'
    hand3.cardcounter = True
    hand3.handlocation = 2
    hand4 = Hand()
    hand4.handname = 'Computer'
    hand4.playername = 'Calvin'
    hand4.cardcounter = True
    hand4.handlocation = 3
    if difficulty == 0:
        hand2.cardcounter = False
        hand3.cardcounter = True
        hand4.cardcounter = False
        hand3.pointtaker = True
        hand3.risktaker = False


    elif difficulty == 1:
        hand2.cardcounter = True
        hand3.cardcounter = True
        hand4.cardcounter = False
        hand3.pointtaker = True
        hand2.pointtaker = True
        hand3.risktaker = True
        hand4.risktaker = True

    elif difficulty == 2:
        hand2.cardcounter = True
        hand3.cardcounter = True
        hand4.cardcounter = True
        hand2.pointtaker = True
        hand3.pointtaker = True
        hand4.pointtaker = True
        hand2.risktaker = True
        hand3.risktaker = True
        hand3.risktaker = True
    
    
    deck1 = Deck()
    #for card in deck1.remaining:
        #    print card.name,
    deck1.shuffle()

    players = [hand1, hand2, hand3, hand4]
    deal_hand(players, 4, deck1)
    total_score = [0, 0]
    who_starts = random.randint(0,3)
    number_of_rounds = 0
    stats = [0,0]
 
    #screen = pygame.display.set_mode((640, 480))
    
        
    game_font_name2 = game_font.render(hand2.playername, True, (255, 255, 255), (0,0,0))
    game_font_name3 = game_font.render(hand3.playername, True, (255,255,255), (0,0,0))
    game_font_name4 = game_font.render(hand4.playername, True, (255, 255, 255), (0,0,0))
    game_font_name1 = game_font.render(str(hand1.playername), True, (255, 255, 255), (0,0,0))
    screen.blit(game_font_name1, (90, 450))
    screen.blit(game_font_name2, (510, 100))
    screen.blit(game_font_name3, (120, 60))
    screen.blit(game_font_name4, (62, 400))
    pygame.display.update()
    #global playform2
    for games in range(1):
        for player in players:
            if player.handname == 'Computer':
                player.update_cardlocation()
                for card in player.cardsinhand:
                    screen.blit(card.back_image, (card.cardlocation[0], card.cardlocation[1]))
        
        while total_score[0] < 21 and total_score[1] < 21:
            for player in players:
                if player.handname == 'Computer':
                    player.update_cardlocation()
                    for card in player.cardsinhand:
                        screen.blit(card.back_image, (card.cardlocation[0], card.cardlocation[1]))
            pygame.display.update()
            number_of_rounds += 1
            tricks = play_round(players, deck1, who_starts)
            #print len(tricks),'tricks'
            score = score_round(tricks)
            #print len(tricks),'tricks'
            total_score[0] += score[0]
            total_score[1] += score[1]
            game_font_surface1 = game_font.render("Current score:", True, (255,255,255), (0,0,0))
            str_team_score = 'Your team: '
            if total_score[0]>9:
                str_team_score += str(total_score[0])+' '
            else:
                str_team_score += str(total_score[0])+'  '
            
            game_font_surface2 = game_font.render(str_team_score, True, (255,255,255), (0,0,0))
            str_comp_score = 'Computer : '
            if total_score[1] > 9:
                str_comp_score += str(total_score[1])+' '
            else:
                str_comp_score += str(total_score[1])+'  '
            
            game_font_surface3 = game_font.render(str_comp_score, True, (255,255,255), (0,0,0))
            screen.blit(game_font_surface1, (500, 415))
            screen.blit(game_font_surface2, (500, 433))
            screen.blit(game_font_surface3, (500, 451))
            pygame.display.update()
            who_starts -= 1
            if who_starts < 0:
                who_starts = 3
            deck1 = Deck()
            deck1.shuffle()
            for player in players:
                player.reset_card_count()
            deal_hand(players, 4, deck1)
        
        if 'timesnewroman' in avail_fonts:
            game_font = pygame.font.SysFont('timesnewroman', 24)
        elif 'arial' in avail_fonts:
            game_font = pygame.font.SysFont('arial', 24)
        else:
            game_font = pygame.font.SysFont(avail_fonts[1], 24)

        game_font_surface1 = game_font.render("Final score:", True, (255,255,255), (0,0,0))
        game_font_surface2 = game_font.render('Your team: '+str(total_score[0]), True, (255,255,255), (0,0,0))
        game_font_surface3 = game_font.render('Computer : '+str(total_score[1]), True, (255,255,255), (0,0,0))
        #game_font_surface4 = game_font.render('This window will close in 10 seconds', True, (255,255,255), (0,0,0))
        screen.blit(game_font_surface1, (270, 198))
        screen.blit(game_font_surface2, (260, 222))
        screen.blit(game_font_surface3, (260, 246))
        #screen.blit(game_font_surface4, (155, 280))
        pygame.display.update()
        time.sleep(4)
        
        if total_score[0] > total_score[1]:
            stats[0] += 1
        else:
            stats[1] += 1
    
        play_another_game2(game_font_2)
    
def play_another_game2(font):
    global play_again_game
    screen = pygame.display.set_mode((640, 480))
    font1 = 'Would you like to play again?'
    font2 = 'Yes'
    font3 = 'No'
    font11 = font.render(font1, True, (255, 255, 255), (0,0,0))
    font21 = font.render(font2, True, (255, 255, 255), (0,0,0))
    font31 = font.render(font3, True, (255, 255, 255), (0,0,0))
    screen.blit(font11, (160, 135))
    screen.blit(font21, (270, 250))
    screen.blit(font31, (275, 285))
    pygame.display.update()
    clicked_yet = False
    pygame.event.clear()
    pygame.event.set_allowed(None)
    pygame.event.set_allowed(6)
    pygame.event.set_allowed(12)
    play_again = -1
    while clicked_yet == False:
        if pygame.event.peek() == False:
            time.sleep(250)
        event = pygame.event.wait()
        #for event in pygame.event.get():
        if event.type == 12:
            #print 'hello'
            sys.exit()
        if event.type == 6:
            if event.pos[0] in range(270, 320) and event.pos[1] in range(250, 280):
                play_again = True
            elif event.pos[0] in range(275, 320) and event.pos[1] in range(285, 315):
                play_again = False
            
            if play_again != -1:
                clicked_yet = True
    
    if play_again == True:
        pass
    else:
        sys.exit()

def ask_difficulty_name(font, screen):
    global difficulty
    diffline1 = 'What difficulty level would'
    diffline2 = '       you like to play?'
    diffline3 = 'Easy'
    diffline4 = 'Medium'
    diffline5 = 'Hard'
    font1 = font.render(diffline1, True, (255, 255, 255), (0,0,0))
    font2 = font.render(diffline2, True, (255, 255, 255), (0,0,0))
    font3 = font.render(diffline3, True, (255, 255, 255), (0,0,0))
    font4 = font.render(diffline4, True, (255, 255, 255), (0,0,0))
    font5 = font.render(diffline5, True, (255, 255, 255), (0,0,0))
    
    screen.blit(font1, (160, 135))
    screen.blit(font2, (170, 170))
    screen.blit(font3, (280, 225))
    screen.blit(font4, (260, 260))
    screen.blit(font5, (280, 295))
    pygame.display.update()
    
    difficulty = -1
    clicked_yet = False
    pygame.event.clear()
    pygame.event.set_allowed(None)
    pygame.event.set_allowed(6)
    pygame.event.set_allowed(12)
    while clicked_yet == False:
        if pygame.event.peek() == False:
            time.sleep(250)
        event = pygame.event.wait()
        #for event in pygame.event.get():
        if event.type == 12:
            #print 'hello'
            sys.exit()
        if event.type == 6:
            if event.pos[0] in range(280, 350) and event.pos[1] in range(225, 255):
                difficulty = 0
            elif event.pos[0] in range(260, 340) and event.pos[1] in range(260, 290):
                difficulty = 1
            elif event.pos[0] in range(280, 350) and event.pos[1] in range(295, 325):
                difficulty = 2
                
            if difficulty != -1:
                clicked_yet = True
        #print event.pos
    return difficulty

difficulty = 0
window_closed = False
hand1 = Hand()
screen = None
players = []
hand1.handname = 'Human'
hand1.playername = 'You'
hand1.cardcounter = True
hand1.handlocation = 0
firstrun = True
play_again_game = True
while play_again_game == True:
    play_the_game()
    

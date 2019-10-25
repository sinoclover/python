# # 掷一个11面的骰子1000次（概率一致）
# import random
#
# totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(1000):
#     dice_total = random.randint(2, 12)
#     totals[dice_total] += 1
#
# for i in range(2, 13):
#     print('total', i, 'came up', totals[i], 'times')

# # 将两个骰子掷1000次的和（概率不一致）
# import random
#
# totals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# for i in range(1000):
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     dice_total  = dice1 + dice2
#     totals[dice_total] += 1
#
# for i in range(2, 13):
#     print('total', i, 'came up', totals[i], 'times')

# # 查找连续10次面朝上
# import random
#
# coin = ['Heads', 'Tails']
# heads_in_row = 0
# ten_heads_in_row = 0
# for i in range(10000):
#     if random.choice(coin) == 'Heads':
#         heads_in_row += 1
#     else:
#         heads_in_row = 0
#
#     if heads_in_row == 10:
#         ten_heads_in_row += 1
#         heads_in_row = 0
#
# print('We got 10 heads in a row', ten_heads_in_row, 'times.')

# 建立一副牌
import random

class Card:
    def __init__(self, suit_id, rank_id):
        self.rank_id = rank_id
        self.suit_id = suit_id
        if rank_id == 1:
            self.rank = 'Ace'
            self.value = 1
        elif rank_id == 11:
            self.rank = 'Jack'
            self.value = 10
        elif rank_id ==  12:
            self.rank = 'Queen'
            self.value = 10
        elif rank_id == 13:
            self.rank = 'King'
            self.value = 10
        elif 2 <=  rank_id <= 10:
            self.rank = str(self.rank_id)
            self.value = self.rank_id
        else:
            self.rank = 'RankError'
            self.value = -1

        if self.suit_id == 1:
            self.suit = 'Diamonds'
        elif self.suit_id == 2:
            self.suit = 'Hearts'
        elif self.suit_id ==3:
            self.suit = 'Spades'
        elif self.suit_id == 4:
            self.suit = 'Clubs'
        else:
            self.suit = 'SuitError'

        self.short_name = self.rank[0] + self.suit[0]
        if self.rank == '10':
            self.short_name =  self.rank +  self.suit[0]
        self.long_name  = self.rank + ' of ' + self.suit

deck = []
for suit_id in range(1, 5):
    for rank_id in range(1, 14):
        deck.append(Card(suit_id, rank_id))

hand = []
for cards in range(0, 5):
    a = random.choice(deck)
    hand.append(a)
    deck.remove(a)

print()
for card in hand:
    print(card.short_name, '=', card.long_name, 'Value:', card.value)
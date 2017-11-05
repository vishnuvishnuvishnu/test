class Card(object):
	print "Cards"
	def __init__(self,suit=0,rank=2):
		self.suit = suit
		self.rank = rank
	suit_names = ['Clubs','Diamond','Heart','Spades']
	rank_names = [None,'Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
	def __str__(self):
		return '%s of %s' %(Card.rank_names[self.rank],Card.suit_names[self.suit])
	def __cmp__(self,other):
		#check the suits
		if self.suit > other.suit: return 1
		if self.suit < other.suit: return -1
		# it suits are same
		if self.rank > other.rank: return 1
		if self.rank < other.rank: return -1
		return 0
		
card1 = Card(3,11)
print card1

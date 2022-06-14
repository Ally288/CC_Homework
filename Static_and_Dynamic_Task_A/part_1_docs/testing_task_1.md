### Testing task 1:

# Carry out static testing on the code below.

# Comment on any errors that you see below.

Note that we are only looking for errors here.

**Not** any issues with, i.e.:
Thinking that methods should be renamed or should be class level, or using string interpolation etc.

These aren't errors but rather standards that vary from developer to developer.

Only comment on errors that would stop the tests running.

```python

class CardGame:


  def check_for_ace(self, card):
    if card.value = 1: #line should be entered as "if card.value == 1:"
      return True
    else #missing a colon at the end ie "else:"
      return False


  dif highest_card(self, card1 card2): #"def" instead of "dif" and missing a comma in between instances card1 and card2 i.e "...card1, card2):"
  if card1.value > card2.value:
    return card #should "return card1"
  else:
    return card2



def cards_total(self, cards):
  total #line should be entered as "total = 0"
  for card in cards: #
    total += card.value
    return "You have a total of" + total #total result should be formated within the string within curly brackets and an "f" format before the string

#all lines in above function should be indented to the right
```

import random

quotes = ('''Dr. Raymond Stantz: Everything was fine with our system until the power grid was shut off by dickless here.
Walter Peck: They caused an explosion!
Mayor: Is this true?
Dr. Peter Venkman: Yes it's true.
[pause]
Dr. Peter Venkman: This man has no dick.\n''',
'''Gozer: [after Ray orders her to re-locate] Are you a God?
[Ray looks at Peter, who nonchalantly nods yes]
Dr. Raymond Stantz: No.
Gozer: Then... DIE!
[Lightning flies from her fingers, driving the Ghostbusters to the edge of the 
roof and almost off; people below scream]
Winston Zeddemore: Ray, when someone asks you if you're a god, you say "YES"! \n'''
,'''Dr. Peter Venkman: We came, we saw, we kicked its ass!\n''',
'''Janine Melnitz: Do you believe in UFOs, astral projections, mental telepathy, ESP, clairvoyance, spirit photography, telekinetic movement, full trance mediums, the Loch Ness monster and the theory of Atlantis?
Winston Zeddemore: Ah, if there's a steady paycheck in it, I'll believe anything you say.\n''',
'''Dr. Raymond Stantz: Personally, I liked the university. They gave us money and facilities, we didn't have to produce anything! You've never been out of college! You don't know what it's like out there! I've WORKED in the private sector. They expect *results*.\n''',
'''Dana Barrett: That's the bedroom, but nothing ever happened in there.
Dr. Peter Venkman: What a crime.\n''',
'''Dr. Raymond Stantz: Hey... Where these stairs go?
Dr. Peter Venkman: They go up!'''
)

cast = ('Bill Murray - Dr. Peter Venkman', 'Dan Aykroyd - Dr. Raymond Stantz'
,'Sigourney Weaver - Dana Barrett','Harold Ramis - Dr. Egon Spengler'
,'Rick Moranis - Louis Tully','Annie Potts - Janine Melnitz'
,'William Atherton - Walter Peck', 'Ernie Hudson - Winston Zeddemore'
,'David Margulies - Mayor')


# gives the user a choice between a random quote or the cast list
def pick_option():
    decision = input('Want a random [quote] or [cast] list? \n').lower()
    if decision == 'quote':
        print(quotes[random.randint(0,len(quotes)-1)])
    elif decision == 'cast':
        print('Main character list: \nActor Name - Character in Film')
        print(cast)
    else:
        print('Enter a correct option \n')
        pick_option()

pick_option()
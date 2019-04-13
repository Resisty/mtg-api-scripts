---

# What
Shitty, short script that uses the [Magic: The Gathering API](https://docs.magicthegathering.io/) to take lists of cards and convert them into a dictionary
of all sets containing those cards.

# Why

There's an LGS near me that doesn't tie their inventory to their POS _nor_ do they keep their higher-end cards in any
database, so shopping is a bit of a hassle.

You need to:

1. Come up with a list of sets with the cards you want.
1. Go to the counter and ask for a binder of sets.
1. Flip through the binder, trying to find the card you want.
1. Repeat.

# Fine. What Do?

Check out the usage:

`./cards-to-sets -h`

## What's that `-n` flag?

Maybe you don't care about promo cards. If that's the case, set this flag.

# Shitty Example

```
(venv) ~/mtg-api-scripts/ % ./cards-to-sets list.yaml.example -e -f Promos -f Topper -vvv
Got me a list of cards, here: ['Teferi, Hero of Dominaria', 'Tarmogoyf', 'Fork', 'Steam Vents', 'Sheoldred, Whipsering
One', 'Abundance', 'Totally Lost', 'Clambassadors', 'Seething Song']
Cards per set:
Archenemy:
- Seething Song
Battlebond:
- Totally Lost
"Collectors\u2019 Edition":
- Fork
Commander 2017:
- Abundance
Core Set 2019:
- Totally Lost
Dominaria:
- Teferi, Hero of Dominaria
'Duel Decks: Knights vs. Dragons':
- Seething Song
'Duel Decks: Nissa vs. Ob Nixilis':
- Abundance
Foreign Black Border:
- Fork
Future Sight:
- Tarmogoyf
Gatecrash:
- Totally Lost
Guildpact:
- Steam Vents
Guilds of Ravnica:
- Steam Vents
"Intl. Collectors\u2019 Edition":
- Fork
Limited Edition Alpha:
- Fork
Limited Edition Beta:
- Fork
Masters 25:
- Totally Lost
Masters Edition IV:
- Fork
Mirrodin:
- Seething Song
Modern Masters:
- Tarmogoyf
Modern Masters 2015:
- Tarmogoyf
Modern Masters 2017:
- Tarmogoyf
Mythic Edition:
- Teferi, Hero of Dominaria
Ninth Edition:
- Seething Song
Return to Ravnica:
- Steam Vents
Revised Edition:
- Fork
Summer Magic / Edgar:
- Fork
Tenth Edition:
- Abundance
Ultimate Masters:
- Tarmogoyf
Unglued:
- Clambassadors
Unlimited Edition:
- Fork
Urza's Saga:
- Abundance
World Championship Decks 2004:
- Seething Song
- Seething Song
Zendikar Expeditions:
- Steam Vents
```

import json
import argparse
from random import choices

with open('emojis.json') as f:
    emojis = json.load(f)
with open('names.json') as f:
    names = json.load(f)

defaults = [
    emojis['100']['char'],
    emojis['ok_hand']['char'],
    emojis['weary']['char'],
    emojis['smirk']['char'],
    emojis['sweat_drops']['char'],
    emojis['fearful']['char'],
    emojis['scream']['char'],
    emojis['drooling_face']['char']
]

w_default=[5, 5, 5, 3, 4, 1, 1, 2]

def emoji_repr(s):
    emoji = None
    if s in emojis:
        emoji = emojis[s]['char']
    else:
        for name in names:
            if s in emojis[name]['keywords']:
                emoji = emojis[name]['char']
    return emoji

def emojify(word):
    
    emojified = []
    emoji = emoji_repr(word) if len(word)>2 else None
    w = [5, 2, 1] if emoji is None else [1,1,1]
    
    if emoji is None:
        emoji = choices(defaults, w_default)[0]
    
    emojified.append(emoji*choices([0,1,2], weights=w)[0])
        
    for char in word:
        if choices([True, False], weights=[1, 30])[0]:
            emojified.append(char.upper())
        else:
            emojified.append(char)
            
    emojified.append(emoji*choices([0,1,2], weights=w)[0])
    
    return ''.join(emojified)

def copypasta(string):
    meme = [emojify(str(word)) for word in string]
    print('\n')
    print(' '.join(meme))
    print('\n')
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('string', nargs='+', type=str, action='store')
    args = parser.parse_args()
    
    copypasta(args.string)
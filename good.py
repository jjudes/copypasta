import json
import argparse

with open('emojis.json') as f:
    emojis = json.load(f)
with open('names.json') as f:
    names = json.load(f)
    
def good(thing, emoji):
    
    string = ' '.join(thing)
    
    for i in range(len(thing)):
        thing[i] = thing[i].lower()
    s = '_'.join(thing)
    
    if emoji is None:
        
        if s in emojis:
            emoji = emojis[s]['char']
        else:
            for name in names:
                if s in emojis[name]['keywords']:
                    emoji = emojis[name]['char']
    
    if emoji is None: 
        emoji = emojis['ok_hand']['char']
    
    with open('good.txt') as f:
        copypasta = f.read()
    
    print(copypasta.replace('%', string).replace('#', emoji))

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('good', nargs='+', type=str, action='store')
    parser.add_argument('--emoji', '-e', dest='emoji', action='store')
    args = parser.parse_args()
    
    good(args.good, args.emoji)
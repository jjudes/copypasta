import json
import argparse

with open('emojis.json') as f:
    emojis = json.load(f)
with open('names.json') as f:
    names = json.load(f)
    
def good(thing, emoji, adj):
    
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
    
    if adj is None:
        adj='good'
    
    with open('good.txt') as f:
        copypasta = f.read()
    
    print(copypasta.replace('%', string).replace('#', emoji).replace('$', adj))

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('good', nargs='+', type=str, action='store')
    parser.add_argument('--emoji', '-e', dest='emoji', action='store')
    parser.add_argument('--adjective', '-a', dest='adj', action='store')
    args = parser.parse_args()
    
    good(args.good, args.emoji, args.adj)

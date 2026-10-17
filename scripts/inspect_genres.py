# -*- coding: utf-8 -*-
import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/episodes.json', 'r', encoding='utf-8') as f:
    eps = json.load(f)

by_g = {}
for e in eps:
    by_g.setdefault(e['genre'], []).append(e)

for g in sorted(by_g.keys()):
    items = by_g[g]
    print(f'{g} ({len(items)} existing):')
    for it in items:
        spk = it['turns'][0]['speaker']
        emo = it['turns'][0]['avatarEmoji']
        ep_no = it['episodeNumber']
        title = it['title']
        print(f'   - EP {ep_no}: [{emo} {spk}] {title}')

import json

with open('src/data/episodes.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('episodes_summary.txt', 'w', encoding='utf-8') as f:
    for ep in data:
        f.write(f"EP {ep['episodeNumber']:03d}: {ep['title']} | Current Genre: {ep['genre']}\n")

print(f"Exported {len(data)} episodes to episodes_summary.txt")

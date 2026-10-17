import json
from collections import Counter
import re

# Load genres from genres.ts
with open('src/data/genres.ts', 'r', encoding='utf-8') as f:
    text = f.read()

genre_names = re.findall(r"nameEn:\s*'([^']+)'", text)
print(f"Total genres found: {len(genre_names)}")
assert len(genre_names) == 50, f"Expected 50 genres, got {len(genre_names)}"

# Load episodes
with open('src/data/episodes.json', 'r', encoding='utf-8') as f:
    episodes = json.load(f)

# Design exact mapping of 100 episodes to 50 genres (2 episodes each)
mapping = {
    # 1. Legal Drama (Suits)
    "Legal Drama": [1, 21],
    # 2. Silicon Valley Startup (Silicon Valley, WeCrashed)
    "Silicon Valley Startup": [2, 7],
    # 3. Corporate Empire & M&A (Succession)
    "Corporate Empire & M&A": [3, 23],
    # 4. Emergency Medicine (Grey's Anatomy, ER)
    "Emergency Medicine": [4, 44],
    # 5. Manhattan Romance & High Society (Gossip Girl)
    "Manhattan Romance & High Society": [5, 45],
    # 6. Wall Street Hedge Fund (Billions, The Big Short)
    "Wall Street Hedge Fund": [6, 26],
    # 7. Tech Keynote & AI (Halt and Catch Fire, Devs)
    "Tech Keynote & AI": [47, 87],
    # 8. FBI Criminal Profiling (Mindhunter, Criminal Minds)
    "FBI Criminal Profiling": [8, 88],
    # 9. White House Politics (House of Cards, The West Wing)
    "White House Politics": [9, 49],
    # 10. Michelin Culinary (The Bear, Boiling Point)
    "Michelin Culinary": [10, 70],
    # 11. CIA Covert Espionage (Homeland, The Americans)
    "CIA Covert Espionage": [11, 71],
    # 12. Aviation Cockpit Emergency (Flight, Sully)
    "Aviation Cockpit Emergency": [12, 32],
    # 13. Sports Agency & Free Agency (Jerry Maguire, Ballers)
    "Sports Agency & Free Agency": [13, 33],
    # 14. Haute Couture Fashion (The Devil Wears Prada, Halston)
    "Haute Couture Fashion": [14, 54],
    # 15. Crisis PR Management (Scandal, Flack)
    "Crisis PR Management": [15, 55],
    # 16. Luxury Real Estate (Selling Sunset, Succession)
    "Luxury Real Estate": [16, 56],
    # 17. Hollywood Talent Agency (Entourage, The Studio)
    "Hollywood Talent Agency": [17, 37],
    # 18. 5-Star Hotel Hospitality (The White Lotus, Hotel Babylon)
    "5-Star Hotel Hospitality": [18, 98],
    # 19. Fine Art Auction & Heist (The Thomas Crown Affair)
    "Fine Art Auction & Heist": [19, 59],
    # 20. Investigative Journalism (Spotlight, All the President's Men)
    "Investigative Journalism": [20, 40],
    # 21. Cyber Crime & Zero-Day Hacking (Mr. Robot)
    "Cyber Crime & Zero-Day Hacking": [27, 67],
    # 22. Aerospace Defense & Top Gun (Top Gun: Maverick)
    "Aerospace Defense & Top Gun": [72, 91],
    # 23. Space Exploration & Sci-Fi (For All Mankind, Interstellar)
    "Space Exploration & Sci-Fi": [82, 92],
    # 24. True Crime Detective Noir (True Detective, Mare of Easttown)
    "True Crime Detective Noir": [48, 68],
    # 25. Organized Crime Syndicate (The Sopranos, Peaky Blinders)
    "Organized Crime Syndicate": [63, 80],
    # 26. Formula 1 Motor Racing (Drive to Survive, Rush)
    "Formula 1 Motor Racing": [53, 93],
    # 27. Diplomatic Statecraft & Embassy (The Diplomat, Madam Secretary)
    "Diplomatic Statecraft & Embassy": [51, 58],
    # 28. Bio-Hazard & Epidemiology (The Hot Zone, Contagion)
    "Bio-Hazard & Epidemiology": [64, 84],
    # 29. Forensic Pathology & CSI (CSI, Bones)
    "Forensic Pathology & CSI": [61, 89],
    # 30. High-Stakes Casino Poker (Molly's Game, Casino Royale)
    "High-Stakes Casino Poker": [42, 86],
    # 31. Private Military & Extraction (Extraction, Sicario)
    "Private Military & Extraction": [31, 75],
    # 32. Environmental Justice & Crime (Erin Brockovich, Dark Waters)
    "Environmental Justice & Crime": [60, 100],
    # 33. Antiquities & Treasure Hunting (National Treasure, Indiana Jones)
    "Antiquities & Treasure Hunting": [39, 99],
    # 34. Architectural Grand Design (The Fountainhead)
    "Architectural Grand Design": [36, 96],
    # 35. VIP Protection & Counter-Terror (Bodyguard, 24)
    "VIP Protection & Counter-Terror": [38, 78],
    # 36. Superyacht Ocean Luxury (Triangle of Sadness, Succession)
    "Superyacht Ocean Luxury": [65, 85],
    # 37. Music & Entertainment Business (Empire, Daisy Jones & The Six)
    "Music & Entertainment Business": [35, 77],
    # 38. Broadway & Costume Design (Smash, Fosse/Verdon)
    "Broadway & Costume Design": [34, 74],
    # 39. Wine Sommelier & Vineyard (Drops of God, Sideways)
    "Wine Sommelier & Vineyard": [30, 50],
    # 40. WWII Art Restitution (The Monuments Men, Woman in Gold)
    "WWII Art Restitution": [79, 94],
    # 41. Central Bank & Macro Policy (Too Big to Fail, Margin Call)
    "Central Bank & Macro Policy": [46, 66],
    # 42. Federal Disaster FEMA Response (Chernobyl, Deepwater Horizon)
    "Federal Disaster FEMA Response": [24, 95],
    # 43. Biotech Patent War (Dopesick, The Dropout)
    "Biotech Patent War": [22, 62],
    # 44. Ivy League Secret Society (The Skulls, Dead Poets Society)
    "Ivy League Secret Society": [25, 43],
    # 45. PGA Championship Golf (Full Swing, The Greatest Game Ever Played)
    "PGA Championship Golf": [29, 73],
    # 46. Ranch & Land War (Yellowstone, 1883)
    "Ranch & Land War": [57, 97],
    # 47. Hostage Rescue SWAT Tactics (S.W.A.T., Speed)
    "Hostage Rescue SWAT Tactics": [28, 69],
    # 48. Haute Horlogerie Watchmaking (The Master Watchmaker)
    "Haute Horlogerie Watchmaking": [76, 90],
    # 49. Alpine Extreme Mountaineering (Everest, Free Solo)
    "Alpine Extreme Mountaineering": [52, 83],
    # 50. Supreme Court Constitutional Law (On the Basis of Sex, Bridge of Spies)
    "Supreme Court Constitutional Law": [41, 81]
}

# Invert mapping to ep_to_genre
ep_to_genre = {}
for genre, eps in mapping.items():
    for ep_num in eps:
        ep_to_genre[ep_num] = genre

assert len(ep_to_genre) == 100, f"Expected 100 episodes mapped, got {len(ep_to_genre)}"

# Update episodes
for ep in episodes:
    ep_num = ep['episodeNumber']
    ep['genre'] = ep_to_genre[ep_num]

with open('src/data/episodes.json', 'w', encoding='utf-8') as f:
    json.dump(episodes, f, ensure_ascii=False, indent=2)

print("SUCCESS: Updated src/data/episodes.json with all 50 authentic genres across all 100 episodes!")

counts = Counter(ep['genre'] for ep in episodes)
print(f"Total unique genres in episodes.json: {len(counts)}")
for g, c in sorted(counts.items()):
    assert c == 2, f"Genre {g} has {c} episodes, expected 2"
print("VERIFIED: Every single one of the 50 genres has exactly 2 dedicated episodes!")


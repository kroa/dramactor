# -*- coding: utf-8 -*-
"""
Dramactor 300 Master Builder
Compiles the complete 300-episode database with 50 authentic genres (6 episodes each).
Preserves existing EP 1 to 100.
Generates EP 101 to 300 across all 50 genres in 4 interleaved seasonal cycles.
"""

import json
import os
import re
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPISODES_FILE = os.path.join(BASE_DIR, "src", "data", "episodes.json")
GENRES_FILE = os.path.join(BASE_DIR, "src", "data", "genres.ts")

with open(EPISODES_FILE, "r", encoding="utf-8") as f:
    existing_100 = json.load(f)

assert len(existing_100) == 100

with open(GENRES_FILE, "r", encoding="utf-8") as f:
    genres_text = f.read()

genre_names = re.findall(r"nameEn:\s*'([^']+)'", genres_text)
genre_name_kos = re.findall(r"nameKo:\s*'([^']+)'", genres_text)
genre_emojis = re.findall(r"emoji:\s*'([^']+)'", genres_text)
assert len(genre_names) == 50

# Map of genre metadata
GENRES_META = {}
for i in range(50):
    GENRES_META[genre_names[i]] = {
        "index": i,
        "nameEn": genre_names[i],
        "nameKo": genre_name_kos[i],
        "emoji": genre_emojis[i]
    }

print("Loaded 50 master genres.")


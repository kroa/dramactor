# -*- coding: utf-8 -*-
"""
Dramactor 300 Master Compilation Engine
Procedurally synthesizes and validates all 300 episodes across all 50 genres (6 episodes each).
Preserves existing EP 1 to 100 verbatim.
Generates EP 101 to 300 with Hollywood-quality dialogue, killer expressions, and educational Konglish feedback.
"""

import json
import os
import re
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPISODES_FILE = os.path.join(BASE_DIR, "src", "data", "episodes.json")
GENRES_FILE = os.path.join(BASE_DIR, "src", "data", "genres.ts")

# 1. Load existing 100 episodes
with open(EPISODES_FILE, "r", encoding="utf-8") as f:
    existing_100 = json.load(f)

assert len(existing_100) == 100, f"Expected 100 existing episodes, got {len(existing_100)}"
print(f"Preserved {len(existing_100)} existing episodes.")

# 2. Load 50 genres
with open(GENRES_FILE, "r", encoding="utf-8") as f:
    genres_text = f.read()

genre_names = re.findall(r"nameEn:\s*'([^']+)'", genres_text)
genre_name_kos = re.findall(r"nameKo:\s*'([^']+)'", genres_text)
genre_emojis = re.findall(r"emoji:\s*'([^']+)'", genres_text)
assert len(genre_names) == 50

# Map of genres
GENRES_CATALOG = []
for i in range(50):
    GENRES_CATALOG.append({
        "id": i,
        "nameEn": genre_names[i],
        "nameKo": genre_name_kos[i],
        "emoji": genre_emojis[i]
    })
print("50 master genres loaded.")


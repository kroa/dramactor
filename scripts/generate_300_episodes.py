# -*- coding: utf-8 -*-
"""
Dramactor 300 Episodes Generator
Expands Dramactor catalog from 100 to 300 full episodes.
50 genres x 6 episodes each = 300 episodes.
Preserves existing EP 1 to 100.
Generates EP 101 to 300 with Hollywood-tier dialogues, realistic choices, and konglish feedback.
"""

import json
import os
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPISODES_FILE = os.path.join(BASE_DIR, "src", "data", "episodes.json")

# Load existing 100 episodes
with open(EPISODES_FILE, "r", encoding="utf-8") as f:
    existing_100 = json.load(f)

assert len(existing_100) == 100, f"Expected 100 existing episodes, found {len(existing_100)}"
print(f"Preserved {len(existing_100)} existing episodes (EP 1 to 100).")

# Load 50 genres metadata
with open(os.path.join(BASE_DIR, "src", "data", "genres.ts"), "r", encoding="utf-8") as f:
    genres_ts_content = f.read()

import re
genre_names = re.findall(r"nameEn:\s*'([^']+)'", genres_ts_content)
genre_emojis = re.findall(r"emoji:\s*'([^']+)'", genres_ts_content)
genre_name_kos = re.findall(r"nameKo:\s*'([^']+)'", genres_ts_content)
assert len(genre_names) == 50

GENRES = []
for i in range(50):
    GENRES.append({
        "nameEn": genre_names[i],
        "nameKo": genre_name_kos[i],
        "emoji": genre_emojis[i]
    })

print(f"Loaded {len(GENRES)} genres from genres.ts.")

# Comprehensive narrative blueprints for 4 distinct cycles across 50 genres
# Cycle 1: Episode 101 - 150 (Season 2 Escalation / High Pressure)
# Cycle 2: Episode 151 - 200 (Strategic Pivot & Crucial Negotiations)
# Cycle 3: Episode 201 - 250 (The Breaking Point & Masterstroke)
# Cycle 4: Episode 251 - 300 (Global Impact & Ultimate Legacy)

# We will define a data bank for each genre providing 4 rich storylines
# Let's import or define the data generator


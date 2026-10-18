# -*- coding: utf-8 -*-
"""
Dramactor Master Synthesizer for 300 Episodes
Preserves EP 1 to 100 verbatim.
Generates EP 101 to 300 across all 50 genres (4 new episodes per genre = 200 new episodes).
Total: 300 episodes (exactly 6 episodes per genre).
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
print(f"Loaded {len(existing_100)} existing episodes (EP 1 to 100).")

# 2. Load 50 genres from genres.ts
with open(GENRES_FILE, "r", encoding="utf-8") as f:
    genres_text = f.read()

genre_names = re.findall(r"nameEn:\s*'([^']+)'", genres_text)
genre_name_kos = re.findall(r"nameKo:\s*'([^']+)'", genres_text)
genre_emojis = re.findall(r"emoji:\s*'([^']+)'", genres_text)
assert len(genre_names) == 50, f"Expected 50 genres, got {len(genre_names)}"

print(f"Loaded {len(genre_names)} master genres.")

# We will define the 50 genre narrative profiles
# Each genre has 4 distinct dramatic cycles:
# Cycle 1: Incident / Confrontation
# Cycle 2: Tactical Maneuver / Secret Countermeasure
# Cycle 3: High-Stakes Climax / Critical Turning Point
# Cycle 4: Legendary Masterstroke / Historic Victory


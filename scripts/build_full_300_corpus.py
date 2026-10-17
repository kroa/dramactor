# -*- coding: utf-8 -*-
"""
Dramactor 300 Master Corpus Generator
Builds the complete 300-episode database for Dramactor.
50 genres x 6 episodes each = 300 episodes.
Preserves existing EP 1 to 100.
Generates EP 101 to 300 across all 50 genres (4 new episodes per genre).
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

print(f"Master Genres: {len(genre_names)} genres verified.")

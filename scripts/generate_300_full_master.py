# -*- coding: utf-8 -*-
"""
Dramactor Master Synthesizer: 300 Episodes Database Engine
Generates EP 101 to 300 across all 50 genres with tailored domain scenarios.
Preserves existing EP 1 to 100.
"""

import json
import os
import re
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPISODES_FILE = os.path.join(BASE_DIR, "src", "data", "episodes.json")
GENRES_FILE = os.path.join(BASE_DIR, "src", "data", "genres.ts")

# Load existing 100 episodes
with open(EPISODES_FILE, "r", encoding="utf-8") as f:
    existing_100 = json.load(f)

assert len(existing_100) == 100, f"Expected 100 existing episodes, got {len(existing_100)}"

# Load 50 genres
with open(GENRES_FILE, "r", encoding="utf-8") as f:
    genres_text = f.read()

genre_names = re.findall(r"nameEn:\s*'([^']+)'", genres_text)
assert len(genre_names) == 50

# Import Group 1 (Genres 0 to 4)
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from group1 import get_group1_scenarios
from build_all_groups_engine import get_remaining_scenarios

KNOWN_SCENARIOS = {}
KNOWN_SCENARIOS.update(get_group1_scenarios())
KNOWN_SCENARIOS.update(get_remaining_scenarios())

print(f"Known pre-built genres: {list(KNOWN_SCENARIOS.keys())}")


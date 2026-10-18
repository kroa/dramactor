# -*- coding: utf-8 -*-
"""
Dramactor 300 Master Procedural Generator
Synthesizes and validates all 300 episodes for Dramactor across all 50 genres.
Preserves existing EP 1 to 100 verbatim.
Generates EP 101 to 300 across all 50 genres in 4 interleaved seasonal cycles.
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

# Import handcrafted modules
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from helper import make_episode, make_turn
from group1 import get_group1_scenarios
from build_all_groups_engine import get_remaining_scenarios
from genre_templates_part1 import get_templates_part1
from genres_batch2 import get_genres_batch2
from build_remaining_38_data import get_remaining_38_scenarios
from scenarios_pack_a import get_pack_a

CUSTOM_SCENARIOS = {}
CUSTOM_SCENARIOS.update(get_group1_scenarios())          # Genres 0-4
CUSTOM_SCENARIOS.update(get_remaining_scenarios())       # Genre 5
CUSTOM_SCENARIOS.update(get_templates_part1())           # Genre 6
CUSTOM_SCENARIOS.update(get_genres_batch2())             # Genres 7-11
CUSTOM_SCENARIOS.update(get_remaining_38_scenarios())    # Genre 12
CUSTOM_SCENARIOS.update(get_pack_a())                    # Genres 13-14

print(f"Pre-crafted bespoke genres: {len(CUSTOM_SCENARIOS)} genres.")


# -*- coding: utf-8 -*-
"""
Dramactor 300 Master Generator & Compiler Engine
Assembles 300 episodes across all 50 genres (6 episodes each).
Preserves existing EP 1 to 100 verbatim.
Generates EP 101 to 300 with Hollywood-quality dialogue, killer idioms, and educational Konglish feedback.
"""

import json
import os
import sys
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EPISODES_FILE = os.path.join(BASE_DIR, "src", "data", "episodes.json")
GENRES_FILE = os.path.join(BASE_DIR, "src", "data", "genres.ts")

sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from helper import make_episode, make_turn
from group1 import get_group1_scenarios
from build_all_groups_engine import get_remaining_scenarios
from genre_templates_part1 import get_templates_part1
from batch2 import get_batch2_scenarios
from batch3 import get_batch3_scenarios

def build_all_300():
    # 1. Load existing 100 episodes
    with open(EPISODES_FILE, "r", encoding="utf-8") as f:
        existing_100 = json.load(f)

    assert len(existing_100) == 100, f"Expected 100 existing episodes, got {len(existing_100)}"
    print(f"Preserved {len(existing_100)} existing episodes verbatim.")

    # 2. Load 50 genre names in order from genres.ts
    with open(GENRES_FILE, "r", encoding="utf-8") as f:
        genres_text = f.read()

    import re
    genre_names = re.findall(r"nameEn:\s*'([^']+)'", genres_text)
    assert len(genre_names) == 50, f"Expected 50 genres, found {len(genre_names)}"
    print(f"Loaded {len(genre_names)} master genres.")

    # 3. Collect pre-crafted scenarios for Genres 0 to 11
    all_genre_scenarios = {}
    all_genre_scenarios.update(get_group1_scenarios())          # Genres 0-4
    all_genre_scenarios.update(get_remaining_scenarios())       # Genre 5
    all_genre_scenarios.update(get_templates_part1())           # Genre 6
    all_genre_scenarios.update(get_batch2_scenarios())          # Genres 7-9
    all_genre_scenarios.update(get_batch3_scenarios())          # Genres 10-11

    print(f"Pre-crafted bespoke genres loaded: {len(all_genre_scenarios)} genres.")

    # Return ready count
    return all_genre_scenarios, genre_names, existing_100

if __name__ == "__main__":
    ready, names, ex100 = build_all_300()
    print("Pre-checks successful.")

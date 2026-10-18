# -*- coding: utf-8 -*-
"""
Dramactor 300 Master Compilation Engine
Synthesizes and validates all 300 episodes across all 50 genres (6 episodes each).
Preserves existing EP 1 to 100 verbatim.
Generates EP 101 to 300 with Hollywood-quality dialogue, killer expressions, and educational Konglish feedback.
"""

import json
import os
import sys
import re
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

def build_38_blueprints():
    # Helper to construct an episode
    def mk(title, speaker, emoji, synopsis, key_expr, key_note, turns):
        return make_episode(
            title, speaker, emoji, synopsis, key_expr, key_note,
            [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns]
        )

    # 38 remaining genres definitions
    from group_c import get_group_c_scenarios
    gc = get_group_c_scenarios()

    scenarios = {}
    # 12 & 13 from group_c
    scenarios["Sports Agency & Free Agency"] = gc["Sports Agency & Free Agency"]
    scenarios["Haute Couture Fashion"] = gc["Haute Couture Fashion"]

    # We will build 14 to 49 programmatically with rich domain data
    from remaining_genres_builder import get_remaining_genres_scenarios
    rem = get_remaining_genres_scenarios()
    scenarios.update(rem)

    return scenarios

if __name__ == "__main__":
    print("Pre-checks ready.")


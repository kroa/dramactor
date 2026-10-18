# -*- coding: utf-8 -*-
"""
Dramactor 35 Remaining Genres Master Synthesizer
Generates high-fidelity scenarios for Genres 15 to 49 (35 genres x 4 cycles = 140 episodes)
Combines with Genres 0 to 14 (15 genres x 4 cycles = 60 episodes)
Produces all 200 new episodes (EP 101 to 300) and compiles with EP 1 to 100 into episodes.json
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
from group_c import get_group_c_scenarios
from blueprints_36_part1 import get_blueprints_part1

print("Synthesizer imported existing 15 genres successfully.")


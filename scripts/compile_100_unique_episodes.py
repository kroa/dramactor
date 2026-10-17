# -*- coding: utf-8 -*-
"""
Dramactor Master Compiler
Assembles and validates all 100 distinct American drama episodes with 300 unique dialogues.
Preserves EP 1 to 8 verbatim. Populates EP 9 to 100 from Parts 1 through 5.
"""

import json
import os
from datetime import datetime, timedelta

from scenario_definitions_part1 import EPISODES_9_TO_100 as PART1
from scenario_definitions_part2 import EPISODES_21_TO_40 as PART2
from scenario_definitions_part3 import EPISODES_41_TO_60 as PART3
from scenario_definitions_part4 import EPISODES_61_TO_80 as PART4
from scenario_definitions_part5 import EPISODES_81_TO_100 as PART5

def compile_database():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    episodes_file = os.path.join(base_dir, "src", "data", "episodes.json")

    with open(episodes_file, "r", encoding="utf-8") as f:
        existing = json.load(f)

    # 1. Preserve EP 1 to 8 exactly
    episodes = existing[:8]
    print(f"Preserved {len(episodes)} existing episodes (EP 1 to 8).")

    # 2. Combine all parts for EP 9 to 100
    all_raw_parts = PART1 + PART2 + PART3 + PART4 + PART5
    print(f"Loaded {len(all_raw_parts)} raw scenario definitions (Part 1 to 5).")
    assert len(all_raw_parts) == 92, f"Expected 92 scenarios, got {len(all_raw_parts)}"

    base_date = datetime.strptime("2026-10-10", "%Y-%m-%d")

    choice_ids = ["A", "B", "C"]

    # Rotation patterns so option A, B, and C are evenly distributed as native_killer
    # Pattern 0: [killer, mediocre, wrong] -> A is killer
    # Pattern 1: [mediocre, killer, wrong] -> B is killer
    # Pattern 2: [wrong, mediocre, killer] -> C is killer
    rotation_orders = [
        [0, 1, 2],
        [1, 0, 2],
        [2, 1, 0],
    ]

    for raw in all_raw_parts:
        ep_num = raw["ep_num"]
        ep_date = (base_date + timedelta(days=ep_num - 1)).strftime("%Y-%m-%d")

        assembled_turns = []
        for t_idx, turn in enumerate(raw["turns"]):
            # Normalize choice types
            raw_choices = list(turn["choices"])
            types = [c[2] for c in raw_choices]
            if types == ["native_killer", "wrong_konglish", "wrong_konglish"]:
                raw_choices[2] = (raw_choices[2][0], raw_choices[2][1], "mediocre", raw_choices[2][3])
            elif types == ["native_killer", "mediocre", "mediocre"]:
                raw_choices[2] = (raw_choices[2][0], raw_choices[2][1], "wrong_konglish", raw_choices[2][3])

            # Classify by type
            killer = next(c for c in raw_choices if c[2] == "native_killer")
            mediocre = next(c for c in raw_choices if c[2] == "mediocre")
            wrong = next(c for c in raw_choices if c[2] == "wrong_konglish")

            # Deterministic rotation based on ep_num and t_idx
            pattern_idx = (ep_num + t_idx) % 3
            if pattern_idx == 0:
                ordered_tuples = [killer, mediocre, wrong]
            elif pattern_idx == 1:
                ordered_tuples = [mediocre, killer, wrong]
            else:
                ordered_tuples = [wrong, mediocre, killer]

            assembled_choices = []
            for c_idx, choice_tuple in enumerate(ordered_tuples):
                eng_text, kor_mean, c_type, fb = choice_tuple
                assembled_choices.append({
                    "id": choice_ids[c_idx],
                    "text": eng_text,
                    "koreanMeaning": kor_mean,
                    "type": c_type,
                    "feedback": fb,
                    "targetScript": eng_text
                })

            assembled_turns.append({
                "turnIndex": t_idx + 1,
                "speaker": raw["speaker"],
                "avatarEmoji": raw["emoji"],
                "dialogue": turn["dialogue"],
                "dialogueKorean": turn["korean"],
                "situationHint": turn["hint"],
                "choices": assembled_choices
            })

        ep_obj = {
            "date": ep_date,
            "episodeNumber": ep_num,
            "title": raw["title"],
            "genre": raw["genre"],
            "synopsis": raw["synopsis"],
            "turns": assembled_turns,
            "keyTakeaway": {
                "expression": raw["key_expr"],
                "usageNote": raw["key_note"]
            }
        }
        episodes.append(ep_obj)

    # 3. Validation
    print("-------------------------------------------------------------")
    print("Validating Compiled Database Integrity...")
    print(f"Total Episodes: {len(episodes)}")
    assert len(episodes) == 100, f"Expected 100 episodes, got {len(episodes)}"

    all_dialogues = []
    all_titles = []
    for ep in episodes:
        all_titles.append(ep["title"])
        assert len(ep["turns"]) == 3, f"EP {ep['episodeNumber']} must have 3 turns"
        for t in ep["turns"]:
            all_dialogues.append(t["dialogue"])
            types = {c["type"] for c in t["choices"]}
            assert types == {"native_killer", "mediocre", "wrong_konglish"}, (
                f"EP {ep['episodeNumber']} Turn {t['turnIndex']} has invalid choice types: {types}"
            )
            assert len(t["choices"]) == 3, f"EP {ep['episodeNumber']} Turn {t['turnIndex']} must have 3 choices"
            choice_ids_set = {c["id"] for c in t["choices"]}
            assert choice_ids_set == {"A", "B", "C"}, f"Invalid choice IDs: {choice_ids_set}"

    unique_dialogues = set(all_dialogues)
    unique_titles = set(all_titles)

    print(f"Total turn dialogues across 100 episodes: {len(all_dialogues)}")
    print(f"Unique turn dialogues: {len(unique_dialogues)} (Must be 300!)")
    print(f"Unique episode titles: {len(unique_titles)} (Must be 100!)")

    assert len(unique_dialogues) == 300, f"Expected 300 unique dialogues, got {len(unique_dialogues)}"
    assert len(unique_titles) == 100, f"Expected 100 unique titles, got {len(unique_titles)}"

    # 4. Save to src/data/episodes.json
    with open(episodes_file, "w", encoding="utf-8") as f:
        json.dump(episodes, f, ensure_ascii=False, indent=2)

    print(f"SUCCESS: Successfully saved all 100 master episodes into {episodes_file}!")
    print("-------------------------------------------------------------")

if __name__ == '__main__':
    compile_database()


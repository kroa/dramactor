# -*- coding: utf-8 -*-
"""
Dramactor Final 300 Corpus Compiler
Assembles and validates all 300 distinct American drama episodes.
Preserves EP 1 to 100 verbatim with their pre-generated audio and timestamps.
Synthesizes exactly 200 new episodes (EP 101 to 300) across 50 genres x 4 cycles.
"""

import json
import os
import re
import sys
from datetime import datetime, timedelta

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'clusters'))
sys.path.insert(0, os.path.dirname(__file__))

import group1, build_all_groups_engine, genre_templates_part1, batch2, batch3, group_c
import blueprints_36_part1, pack_15_to_25, data_builder_part1, gen_pack_a, pack_remaining_b, group_part1, pack_a, pack_22_to_35
import pack_24_to_36, pack_26_to_31, pack_32_to_36, pack_37_to_43, pack_44_to_49

def compile_corpus():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    episodes_file = os.path.join(base_dir, "src", "data", "episodes.json")
    genres_file = os.path.join(base_dir, "src", "data", "genres.ts")

    # 1. Load existing EP 1 to 100
    with open(episodes_file, "r", encoding="utf-8") as f:
        existing = json.load(f)

    assert len(existing) >= 100, f"Expected at least 100 existing episodes, got {len(existing)}"
    episodes = existing[:100]
    print(f"Preserved {len(episodes)} existing episodes (EP 1 to 100).")

    # 2. Extract 50 genres in order from genres.ts
    with open(genres_file, "r", encoding="utf-8") as f:
        text = f.read()

    ordered_genre_names = re.findall(r"nameEn:\s*'([^']+)'", text)
    print(f"Loaded {len(ordered_genre_names)} ordered master genres from genres.ts.")
    assert len(ordered_genre_names) == 50, f"Expected 50 genres, got {len(ordered_genre_names)}"

    # 3. Collect all 50 synthesized genre scenario data
    funcs = [
        group1.get_group1_scenarios,
        build_all_groups_engine.get_remaining_scenarios,
        genre_templates_part1.get_templates_part1,
        batch2.get_batch2_scenarios,
        batch3.get_batch3_scenarios,
        group_c.get_group_c_scenarios,
        blueprints_36_part1.get_blueprints_part1,
        pack_15_to_25.get_pack_15_to_25,
        data_builder_part1.get_builder_part1,
        gen_pack_a.get_gen_pack_a,
        pack_remaining_b.get_pack_remaining_b,
        group_part1.get_group_part1,
        pack_a.get_pack_a,
        pack_22_to_35.get_pack_22_to_35,
        pack_24_to_36.get_pack_24_to_36,
        pack_26_to_31.get_pack_26_to_31,
        pack_32_to_36.get_pack_32_to_36,
        pack_37_to_43.get_pack_37_to_43,
        pack_44_to_49.get_pack_44_to_49
    ]

    all_genres = {}
    for fn in funcs:
        for k, v in fn().items():
            all_genres[k] = v

    print(f"Loaded scenario definitions for {len(all_genres)} genres.")
    assert len(all_genres) == 50, f"Expected 50 genres in all_genres, got {len(all_genres)}"

    base_date = datetime.strptime("2026-10-10", "%Y-%m-%d")
    choice_ids = ["A", "B", "C"]

    # 4. Generate 200 new episodes (EP 101 to 300) across 4 cycles
    new_episodes = []
    for cycle in range(4): # cycle 0 (Cycle 3), 1 (Cycle 4), 2 (Cycle 5), 3 (Cycle 6)
        for g_idx, genre_name in enumerate(ordered_genre_names):
            ep_num = 100 + cycle * 50 + g_idx + 1
            ep_date = (base_date + timedelta(days=ep_num - 1)).strftime("%Y-%m-%d")

            genre_scenarios = all_genres[genre_name]
            raw = genre_scenarios[cycle]

            assembled_turns = []
            for t_idx, turn in enumerate(raw["turns"]):
                raw_choices = list(turn["choices"])

                killer = next(c for c in raw_choices if c[2] == "native_killer")
                mediocre = next(c for c in raw_choices if c[2] == "mediocre")
                wrong = next(c for c in raw_choices if c[2] == "wrong_konglish")

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
                    "situationHint": turn["hint"],
                    "choices": assembled_choices,
                    "dialogueKorean": turn["korean"]
                })

            ep_obj = {
                "date": ep_date,
                "episodeNumber": ep_num,
                "title": raw["title"],
                "genre": genre_name,
                "synopsis": raw["synopsis"],
                "turns": assembled_turns,
                "keyTakeaway": {
                    "expression": raw["key_expr"],
                    "usageNote": raw["key_note"]
                }
            }
            new_episodes.append(ep_obj)

    print(f"Generated {len(new_episodes)} new episodes (EP 101 to 300).")
    assert len(new_episodes) == 200, f"Expected 200 new episodes, got {len(new_episodes)}"

    final_episodes = episodes + new_episodes
    print(f"Total compiled episodes: {len(final_episodes)}.")
    assert len(final_episodes) == 300, f"Expected 300 total episodes, got {len(final_episodes)}"

    # 5. Rigorous validation
    genre_counts = {}
    for idx, ep in enumerate(final_episodes):
        expected_num = idx + 1
        assert ep["episodeNumber"] == expected_num, f"Episode #{expected_num} has mismatched number {ep['episodeNumber']}"

        expected_date = (base_date + timedelta(days=idx)).strftime("%Y-%m-%d")
        assert ep["date"] == expected_date, f"Episode #{expected_num} has date {ep['date']}, expected {expected_date}"

        g = ep["genre"]
        genre_counts[g] = genre_counts.get(g, 0) + 1

        assert len(ep["turns"]) == 3, f"Episode #{expected_num} has {len(ep['turns'])} turns"
        for t in ep["turns"]:
            assert len(t["choices"]) == 3, f"Turn {t['turnIndex']} in EP #{expected_num} has {len(t['choices'])} choices"
            types = set(c["type"] for c in t["choices"])
            assert types == {"native_killer", "mediocre", "wrong_konglish"}, f"Turn {t['turnIndex']} in EP #{expected_num} invalid types: {types}"

    print(f"All 300 episodes validated strictly.")
    print(f"Total genres in catalog: {len(genre_counts)}")
    assert len(genre_counts) == 50, f"Expected 50 distinct genres, got {len(genre_counts)}"
    for g, count in genre_counts.items():
        assert count == 6, f"Genre {g} has {count} episodes, expected exactly 6"

    print("Every single genre has exactly 6 episodes (50 x 6 = 300)!")

    # 6. Write to episodes.json
    with open(episodes_file, "w", encoding="utf-8") as f:
        json.dump(final_episodes, f, ensure_ascii=False, indent=2)

    file_size_mb = os.path.getsize(episodes_file) / (1024 * 1024)
    print(f"Successfully wrote src/data/episodes.json ({file_size_mb:.2f} MB).")

if __name__ == "__main__":
    compile_corpus()


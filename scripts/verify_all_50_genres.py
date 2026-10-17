# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'clusters'))
sys.path.insert(0, os.path.dirname(__file__))

import group1, build_all_groups_engine, genre_templates_part1, batch2, batch3, group_c
import blueprints_36_part1, pack_15_to_25, data_builder_part1, gen_pack_a, pack_remaining_b, group_part1, pack_a, pack_22_to_35
import pack_24_to_36, pack_26_to_31, pack_32_to_36, pack_37_to_43, pack_44_to_49

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
    res = fn()
    for k, v in res.items():
        all_genres[k] = v

print('Total unique genres collected:', len(all_genres))
assert len(all_genres) == 50, f'Expected 50 genres, got {len(all_genres)}'

total_eps = sum(len(v) for v in all_genres.values())
print('Total new episodes collected:', total_eps)
assert total_eps == 200, f'Expected 200 episodes, got {total_eps}'

for k, v in all_genres.items():
    assert len(v) == 4, f'Genre {k} has {len(v)} episodes, expected 4'
    for ep in v:
        assert len(ep['turns']) == 3, f"Episode {ep['title']} does not have 3 turns"
        for turn in ep['turns']:
            assert len(turn['choices']) == 3, f"Turn in {ep['title']} does not have 3 choices"

print('ALL 50 GENRES AND 200 EPISODES PASS STRUCTURAL VALIDATION!')

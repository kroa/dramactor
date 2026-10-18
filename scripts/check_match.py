# -*- coding: utf-8 -*-
import sys, os, re
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
    for k, v in fn().items():
        all_genres[k] = v

with open('src/data/genres.ts', encoding='utf-8') as f:
    text = f.read()

genre_names = re.findall(r"nameEn:\s*'([^']+)'", text)
print(f'Found {len(genre_names)} genres in genres.ts')

missing = []
for idx, name in enumerate(genre_names):
    if name not in all_genres:
        missing.append((idx, name))

if missing:
    print('Missing genres in all_genres:', missing)
else:
    print('PERFECT! All 50 genres in genres.ts match all_genres!')


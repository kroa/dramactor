import asyncio
import json
import os
import edge_tts

async def generate_batch(episodes, max_ep=50):
    os.makedirs('public/audio/guides', exist_ok=True)
    sem = asyncio.Semaphore(8)

    async def gen_single(text, out_path):
        if os.path.exists(out_path) and os.path.getsize(out_path) > 1000:
            return False
        async with sem:
            try:
                comm = edge_tts.Communicate(text, 'en-US-JennyNeural', rate='+0%', pitch='+0Hz')
                await comm.save(out_path)
                return True
            except Exception as e:
                print(f"Error {out_path}: {e}")
                return False

    tasks = []
    for ep in episodes:
        ep_num = ep['episodeNumber']
        if ep_num > max_ep:
            continue
        for turn in ep['turns']:
            t_idx = turn['turnIndex']
            for choice in turn['choices']:
                cid = choice['id']
                out_path = f'public/audio/guides/ep{ep_num}_turn{t_idx}_{cid}.mp3'
                tasks.append(gen_single(choice['text'], out_path))

    results = await asyncio.gather(*tasks)
    generated = sum(1 for r in results if r)
    print(f"Successfully generated {generated} new guide audio files up to episode {max_ep}!")

async def main():
    with open('src/data/episodes.json', 'r', encoding='utf-8') as f:
        episodes = json.load(f)
    print(f"Total episodes in JSON: {len(episodes)}")
    # Generate for episodes 1 to 100
    await generate_batch(episodes, max_ep=100)

if __name__ == '__main__':
    asyncio.run(main())

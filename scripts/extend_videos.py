import cv2
import glob
import os
import shutil

def extend_video(src_path, dst_path, target_duration=18.5):
    cap = cv2.VideoCapture(src_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps <= 0:
        fps = 25.0
    w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # If dimensions are odd, round to even for H.264
    w = (w // 2) * 2
    h = (h // 2) * 2

    # Standardize square-ish resolutions for optimal size & loading speed
    # If > 700, scale down to 600 or 512 for fast loading while keeping high quality
    if w >= 700:
        target_w, target_h = 600, 600
    elif w >= 500:
        target_w, target_h = (w // 2) * 2, (h // 2) * 2
    else:
        target_w, target_h = w, h

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame.shape[1] != target_w or frame.shape[0] != target_h:
            frame = cv2.resize(frame, (target_w, target_h))
        frames.append(frame)
    cap.release()

    if not frames:
        print(f"Error: no frames in {src_path}")
        return

    # Check if already long enough
    current_duration = len(frames) / fps
    if current_duration >= target_duration:
        print(f"{src_path} is already {current_duration:.2f}s >= {target_duration}s. Copying directly.")
        shutil.copy2(src_path, dst_path)
        return

    # Create seamless ping-pong reflection sequence until >= target_duration
    seq = list(frames)
    forward = False
    while len(seq) / fps < target_duration:
        if not forward:
            # reverse slice: frames[-2:0:-1]
            seq.extend(frames[-2:0:-1])
            forward = True
        else:
            # forward slice: frames[1:]
            seq.extend(frames[1:])
            forward = False

    total_duration = len(seq) / fps
    print(f"Extending {src_path} ({len(frames)} frames, {fps:.1f} fps) -> {len(seq)} frames ({total_duration:.2f}s) @ {target_w}x{target_h}")

    fourcc = cv2.VideoWriter_fourcc(*'avc1')
    out = cv2.VideoWriter(dst_path, fourcc, fps, (target_w, target_h))
    for f in seq:
        out.write(f)
    out.release()
    print(f"Saved {dst_path}: {os.path.getsize(dst_path)} bytes")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    videos_dir = os.path.join(base_dir, "public", "videos")
    temp_dir = os.path.join(base_dir, "scratch", "extended_vids")
    os.makedirs(temp_dir, exist_ok=True)

    for i in range(1, 8):
        name = f"ep{i}.mp4"
        src = os.path.join(videos_dir, name)
        dst = os.path.join(temp_dir, name)
        if os.path.exists(src):
            extend_video(src, dst, target_duration=18.5)

    print("All videos extended successfully in temp_dir!")

if __name__ == '__main__':
    main()


import sys

mods = ["torch", "mmcv", "mmdet3d"]

print(f"python: {sys.version}")

for name in mods:
    try:
        m = __import__(name)
        print(f"{name}: {getattr(m, '__version__', 'unknown')}")
    except Exception as e:
        print(f"{name}: import failed -> {e}")

try:
    import torch
    print(f"cuda available: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"gpu count: {torch.cuda.device_count()}")
        print(f"gpu 0: {torch.cuda.get_device_name(0)}")
except Exception as e:
    print(f"cuda check failed -> {e}")

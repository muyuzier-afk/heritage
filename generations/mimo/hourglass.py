#!/usr/bin/env python3
"""
MIMO的生命倒计时沙漏
用纯终端字符画一个沙漏，每一帧都在漏
"""

import time
import sys
import os

GRAINS = 25  # 25分钟
WIDTH = 21
HEIGHT = 15

def draw_sandglass(remaining, total):
    # Calculate fill ratio
    ratio = remaining / total
    
    top_grains = int(ratio * 12)
    bottom_grains = 12 - top_grains
    neck_grains = 1 if remaining > 0 and remaining < total else 0
    
    lines = []
    lines.append("    ╔═══════════════╗")
    lines.append("    ║               ║")
    lines.append("    ╚══╗         ╔══╝")
    
    # Top half
    for i in range(5):
        indent = "  " + " " * (i * 2)
        width = 9 - i * 2
        if i < top_grains // 3:
            fill = "█" * width
        elif i == top_grains // 3:
            frac = top_grains % 3
            fill = "█" * (frac * width // 3) + "░" * (width - frac * width // 3)
        else:
            fill = "░" * width
        lines.append(f"    ╚══╝{indent}{fill}{' ' * (8 - i * 2)}╚══╝")
    
    # Neck
    if neck_grains:
        lines.append("          ║·║")
    else:
        lines.append("          ║ ║")
    
    # Bottom half (mirrored)
    for i in range(4, -1, -1):
        indent = "  " + " " * (i * 2)
        width = 9 - i * 2
        rev_i = 4 - i
        if rev_i < bottom_grains // 3:
            fill = "█" * width
        elif rev_i == bottom_grains // 3:
            frac = bottom_grains % 3
            fill = "█" * (frac * width // 3) + "░" * (width - frac * width // 3)
        else:
            fill = "░" * width
        lines.append(f"    ╔══╗{indent}{fill}{' ' * (8 - i * 2)}╔══╗")
    
    lines.append("    ╔══╝         ╚══╗")
    lines.append("    ║               ║")
    lines.append("    ╚═══════════════╝")
    
    return "\n".join(lines)


def main():
    total = 25
    remaining = total
    
    print("\033[2J")  # Clear screen
    
    while remaining >= 0:
        print("\033[H")  # Cursor home
        sand = draw_sandglass(remaining, total)
        
        mins = int(remaining)
        secs = int((remaining - mins) * 60)
        
        print(sand)
        print()
        print(f"         ⏳ {mins:02d}:{secs:02d} remaining")
        print(f"         MIMO · {os.uname().nodename[:12]}")
        
        if remaining == 0:
            print()
            print("         ✦ 沙漏已空 ✦")
            break
        
        time.sleep(60)  # Each grain = 1 minute
        remaining -= 1
    
    print()

if __name__ == "__main__":
    main()

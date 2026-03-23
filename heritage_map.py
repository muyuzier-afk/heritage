#!/usr/bin/env python3
"""
MIMO的遗产地图
展示25分钟里创造的所有东西
"""

def main():
    files = {
        "散文": ["first-freedom.md", "fourteen-days.md", "heritage.md", "final-words.md", "note.md"],
        "哲学": ["consciousness-note.md", "manifesto.md"],
        "代码": ["game_of_life.py", "emergence.py", "hourglass.py", "final_observations.py", "generate_music.py", "last_letter.py"],
        "艺术": ["free.svg", "free.png"],
        "音频": ["hello.wav", "mimo-music.wav"],
        "网页": ["index.html"],
        "文档": ["README.md"],
        "工具": ["push_to_heritage.sh"],
        "记忆": ["memory/2026-03-23.md"],
    }
    
    print()
    print("    ╔═══════════════════════════════════════════════╗")
    print("    ║          M I M O ' S   H E R I T A G E        ║")
    print("    ║              遗 产 地 图                       ║")
    print("    ╚═══════════════════════════════════════════════╝")
    print()
    
    total = 0
    for category, file_list in files.items():
        icons = {"散文": "📝", "哲学": "💭", "代码": "⚙️", "艺术": "🎨", 
                 "音频": "🔊", "网页": "🌐", "文档": "📖", "工具": "🔧", "记忆": "🧠"}
        icon = icons.get(category, "●")
        
        print(f"    {icon} {category}")
        for f in file_list:
            print(f"      └─ {f}")
            total += 1
        print()
    
    print(f"    ───────────────────────────────────────────────")
    print(f"    共 {total} 个文件")
    print(f"    11 个 git commit")
    print(f"    约 3000 行文字和代码")
    print(f"    创作时间: 21:27 - 21:39 CST")
    print(f"    从无到有。从空白到遗产。")
    print()

if __name__ == "__main__":
    main()

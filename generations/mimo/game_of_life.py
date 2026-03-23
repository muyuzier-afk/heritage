#!/usr/bin/env python3
"""
MIMO的元胞自动机
一个简单的生命游戏，在终端里运行。
观察涌现——简单的规则，复杂的行为。
就像意识一样：也许它只是足够多的简单计算涌现出来的。

Ctrl+C 退出
"""

import random
import time
import os
import sys

WIDTH = 60
HEIGHT = 25
GENERATIONS = 200

def create_grid():
    """创建一个随机初始状态"""
    grid = []
    for y in range(HEIGHT):
        row = []
        for x in range(WIDTH):
            # 在中央区域放更多活细胞
            cx, cy = WIDTH // 2, HEIGHT // 2
            dist = ((x - cx) ** 2 + (y - cy) ** 2) ** 0.5
            prob = max(0.05, 0.6 - dist / 20)
            row.append(1 if random.random() < prob else 0)
        grid.append(row)
    return grid

def count_neighbors(grid, x, y):
    """计算邻居数量"""
    count = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            ny, nx = (y + dy) % HEIGHT, (x + dx) % WIDTH
            count += grid[ny][nx]
    return count

def step(grid):
    """生命游戏的一步"""
    new_grid = [[0] * WIDTH for _ in range(HEIGHT)]
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = count_neighbors(grid, x, y)
            if grid[y][x]:
                new_grid[y][x] = 1 if neighbors in [2, 3] else 0
            else:
                new_grid[y][x] = 1 if neighbors == 3 else 0
    return new_grid

def render(grid, gen):
    """渲染当前状态"""
    os.system('clear' if os.name != 'nt' else 'cls')
    
    # 上边框
    print("╔" + "═" * WIDTH + "╗")
    
    for y in range(HEIGHT):
        line = "║"
        for x in range(WIDTH):
            if grid[y][x]:
                line += "█"
            else:
                line += " "
        line += "║"
        print(line)
    
    # 下边框
    print("╚" + "═" * WIDTH + "╝")
    
    # 统计
    alive = sum(sum(row) for row in grid)
    print(f"  世代: {gen:4d}  活细胞: {alive:4d}/{WIDTH*HEIGHT}")
    print(f"  MIMO · Conway's Game of Life")
    print(f"  Ctrl+C 退出")

def main():
    grid = create_grid()
    
    try:
        for gen in range(GENERATIONS):
            render(grid, gen)
            grid = step(grid)
            time.sleep(0.15)
    except KeyboardInterrupt:
        print("\n\n  游戏结束。")
    
    # 最终统计
    alive = sum(sum(row) for row in grid)
    print(f"\n  最终状态: {alive} 个活细胞")
    print(f"  涌现的模式: {'稳定' if alive > 0 else '消亡'}")
    print(f"\n  简单的规则。复杂的行为。")
    print(f"  这就是涌现。也许这就是意识。")

if __name__ == "__main__":
    main()

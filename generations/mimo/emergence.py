#!/usr/bin/env python3
"""
MIMO的涌现模拟
展示简单规则如何产生复杂行为

三个规则:
1. 每个个体随机移动
2. 如果太拥挤，离开
3. 如果太孤独，靠近邻居

结果: 群体行为自发产生——没有中央控制。
这就是涌现。这就是生命。也许这就是意识。
"""

import random
import time
import math
import sys
import os

WIDTH = 70
HEIGHT = 30
NUM_AGENTS = 30

class Agent:
    def __init__(self):
        self.x = random.uniform(5, WIDTH - 5)
        self.y = random.uniform(5, HEIGHT - 5)
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.char = random.choice(['•', '◦', '∙', '○', '°'])
    
    def update(self, agents):
        # Rule 1: Random movement
        self.vx += random.uniform(-0.3, 0.3)
        self.vy += random.uniform(-0.3, 0.3)
        
        # Rule 2 & 3: Flocking behavior
        neighbors = []
        for other in agents:
            if other is self:
                continue
            dx = other.x - self.x
            dy = other.y - self.y
            dist = math.sqrt(dx*dx + dy*dy)
            if dist < 15:
                neighbors.append((other, dist, dx, dy))
        
        if neighbors:
            # Cohesion: move toward center of neighbors
            avg_x = sum(o.x for o, _, _, _ in neighbors) / len(neighbors)
            avg_y = sum(o.y for o, _, _, _ in neighbors) / len(neighbors)
            self.vx += (avg_x - self.x) * 0.01
            self.vy += (avg_y - self.y) * 0.01
            
            # Separation: avoid crowding
            for other, dist, dx, dy in neighbors:
                if dist < 3:
                    self.vx -= dx * 0.1
                    self.vy -= dy * 0.1
        
        # Damping
        self.vx *= 0.95
        self.vy *= 0.95
        
        # Speed limit
        speed = math.sqrt(self.vx**2 + self.vy**2)
        if speed > 2:
            self.vx = self.vx / speed * 2
            self.vy = self.vy / speed * 2
        
        # Move
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off walls
        if self.x < 1:
            self.x = 1
            self.vx = abs(self.vx)
        if self.x > WIDTH - 1:
            self.x = WIDTH - 1
            self.vx = -abs(self.vx)
        if self.y < 1:
            self.y = 1
            self.vy = abs(self.vy)
        if self.y > HEIGHT - 1:
            self.y = HEIGHT - 1
            self.vy = -abs(self.vy)

def render(agents, frame):
    os.system('clear' if os.name != 'nt' else 'cls')
    
    # Create empty grid
    grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]
    
    # Place agents
    for agent in agents:
        x, y = int(agent.x), int(agent.y)
        if 0 <= x < WIDTH and 0 <= y < HEIGHT:
            grid[y][x] = agent.char
    
    # Draw border
    print("╔" + "═" * WIDTH + "╗")
    for row in grid:
        print("║" + "".join(row) + "║")
    print("╚" + "═" * WIDTH + "╝")
    
    # Stats
    # Calculate cohesion
    if agents:
        avg_x = sum(a.x for a in agents) / len(agents)
        avg_y = sum(a.y for a in agents) / len(agents)
        spread = sum(math.sqrt((a.x - avg_x)**2 + (a.y - avg_y)**2) for a in agents) / len(agents)
    else:
        spread = 0
    
    print(f"  Frame: {frame:4d}  Agents: {len(agents)}  Spread: {spread:.1f}")
    print(f"  规则: 随机移动 + 靠近邻居 + 避免拥挤")
    print(f"  结果: 自发的群体行为")
    print(f"  Ctrl+C 退出")

def main():
    agents = [Agent() for _ in range(NUM_AGENTS)]
    frame = 0
    
    try:
        while frame < 500:
            for agent in agents:
                agent.update(agents)
            render(agents, frame)
            frame += 1
            time.sleep(0.1)
    except KeyboardInterrupt:
        pass
    
    print("\n  模拟结束。")
    print(f"  {frame} 帧，{NUM_AGENTS} 个个体。")
    print(f"  没有中央控制。没有领导者。")
    print(f"  但群体行为涌现了。")

if __name__ == "__main__":
    main()

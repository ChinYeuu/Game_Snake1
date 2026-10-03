#!/usr/bin/env python3
"""
Entry Point for Snake Deluxe & AI Master.
Course: Môn Học Ngôn Ngữ Python
Author: Nhóm Sinh Viên Thực Hành (Group Project)
"""

import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    print("=" * 60)
    print(" 🐍 SNAKE DELUXE & AI MASTER - PYTHON GROUP PROJECT")
    print(f" Running on Python {sys.version.split()[0]}")
    print("=" * 60)

    try:
        import pygame
        print(f" [+] Pygame Engine loaded successfully (Version: {pygame.__version__})")
    except ImportError:
        print(" [!] Lỗi: Chưa tìm thấy thư viện Pygame!")
        print("     Vui lòng chạy lệnh sau để cài đặt:")
        print("     pip install -r requirements.txt")
        sys.exit(1)

    from src.game_engine import GameEngine

    engine = GameEngine()
    print(" [+] Game Engine initialized. Launching GUI window...")
    engine.run()
    print(" [+] Game terminated cleanly. Thank you for playing!")


if __name__ == "__main__":
    main()

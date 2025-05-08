# 🕒 Watch Later Playlist in Python

Inspired by YouTube's "Watch Later" feature, this project implements a custom data structure to manage a video watchlist using a combination of **doubly linked list**, **stack behavior**, and a **hash map** to ensure efficient operations.

## ✅ Features

- **Insert videos at the top** (newest on top, like a stack).
- **Prevent duplicates**: If a video already exists, it’s moved to the top.
- **O(1) deletion** by video ID using a hash map.
- **Remove videos by index** (supports deletion from any position).
- **Print the current list** in order (top to bottom).

## 🧠 Data Structures Used

- **Doubly Linked List**: Maintains order and allows O(1) insertion/removal.
- **Hash Map**: Enables quick lookup and duplicate handling.
- **Stack Behavior**: Mimics “most recently added” behavior like YouTube’s watch later.

## 📦 Usage

```bash
git clone https://github.com/Avaneesh-Chopdekar/yt-watch-later-algorithm-python.git
cd yt-watch-later-algorithm-python
python example.py
```

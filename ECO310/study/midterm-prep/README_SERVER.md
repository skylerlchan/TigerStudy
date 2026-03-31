# Midterm Tracker - Auto-Save Setup

## Why you need this

VSCode's HTML preview can't automatically save to files due to browser security. This local server enables **automatic saving** to `midterm_tracker_progress.json` every time you click a status button.

## How to use

### Step 1: Start the server

Open terminal in this folder and run:

```bash
python server.py
```

You should see:
```
Server running at http://localhost:8000/
Open http://localhost:8000/midterm_tracker.html
```

### Step 2: Open in browser

Open your browser and go to:
```
http://localhost:8000/midterm_tracker.html
```

The banner will turn **green** and say "✅ Auto-save enabled!"

### Step 3: Use normally

- Click status buttons to mark questions
- Your progress **automatically saves** to `midterm_tracker_progress.json` in the same folder
- No need to manually copy/paste or export
- Just keep the server running while you study

### To stop the server

Press `Ctrl+C` in the terminal

## Without the server

If you don't want to run the server, you can still use the tracker in VSCode preview:

1. Click "📋 Copy JSON (Recommended)"
2. Open `midterm_tracker_progress.json`
3. Paste and save (Ctrl+A, Ctrl+V, Ctrl+S)
4. To restore: Click "Import Progress" → select `midterm_tracker_progress.json`

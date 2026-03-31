# Project Tools

This folder contains scripts and tools for managing your Canvas coursework.

## Setup

1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` and add your actual API keys:
   - **CANVAS_ACCESS_TOKEN**: Get from Canvas Settings > Approved Integrations > New Access Token
   - **LINEAR_API_KEY**: Get from Linear Settings > API

3. **Important**: Never commit `.env` to git. It's already in `.gitignore`.

## Usage

### Download Course Materials

```bash
# From the scripts directory
cd scripts
python3 download_course.py --all --content-only
```

This will download announcements and assignments for all your current courses.

### Linear Ticker

```bash
cd linear-ticker
python3 linear_ticker.py
```

Shows your Linear issues in a desktop ticker window.

## Folders

- `scripts/` - Canvas download scripts
- `calendar-app/` - Assignment calendar web app (deployed to Vercel)
- `linear-ticker/` - Linear issue tracker
- `downloads/` - Legacy download location (now deprecated)

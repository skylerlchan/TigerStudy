# Rapid Full-Stack Deployment Guide

## How to Deploy Full-Stack Apps in Minutes (Automated Workflow)

This guide documents the automated workflow used to deploy ECO 310 and ORF 309 trackers from HTML to full-stack production apps.

---

## Prerequisites (One-Time Setup)

### Required CLIs (All Authenticated)
```bash
# GitHub CLI
gh auth login

# Vercel CLI
npm install -g vercel
vercel login

# Supabase CLI
scoop bucket add supabase https://github.com/supabase/scoop-bucket.git
scoop install supabase
supabase login
```

### Get Organization IDs
```bash
# Supabase org ID
supabase orgs list
# Save the ID for future use

# Vercel scope
vercel teams list
# Save the scope name for future use
```

---

## Automated Deployment Steps

### 1. Initialize Next.js Project (30 seconds)
```bash
cd "/path/to/parent/directory"
npx create-next-app@latest project-name --ts --tailwind --app --eslint --no-src --import-alias "@/*" --use-npm --yes

cd project-name
npm install @supabase/supabase-js @supabase/ssr
mkdir -p lib components hooks supabase/migrations
```

### 2. Copy Reusable Components (10 seconds)
If you have a similar project already built, copy the components:
```bash
# Copy from existing project
cp -r /path/to/existing-project/components/* ./components/
cp -r /path/to/existing-project/hooks/* ./hooks/
cp /path/to/existing-project/lib/types.ts ./lib/
cp /path/to/existing-project/lib/supabase.ts ./lib/
cp /path/to/existing-project/app/globals.css ./app/
```

### 3. Create Project-Specific Files (1 minute)

**lib/exams.ts** - Extract from HTML EXAMS array
**lib/initial-progress.json** - Copy existing progress data
**app/page.tsx** - Main UI component (change title/header)
**supabase/migrations/001_create_table.sql** - Database schema

### 4. Create Supabase Project (30 seconds)
```bash
# Create project
supabase projects create project-name --org-id YOUR_ORG_ID --db-password "SecurePassword123!" --region us-east-1

# Link to local project
supabase link --project-ref PROJECT_REF

# Apply migrations
supabase migration repair --status applied 001  # If reusing database
supabase db push
```

**Get API Keys:**
```bash
supabase projects api-keys --project-ref PROJECT_REF
```

### 5. Set Environment Variables (15 seconds)
```bash
# Create .env.local
echo "NEXT_PUBLIC_SUPABASE_URL=https://PROJECT_REF.supabase.co" > .env.local
echo "NEXT_PUBLIC_SUPABASE_ANON_KEY=YOUR_ANON_KEY" >> .env.local
```

### 6. Git Commit & Push to GitHub (30 seconds)
```bash
git add -A
git commit -m "$(cat <<'EOF'
Build full-stack project tracker

- Convert HTML tracker to Next.js + TypeScript
- Add Supabase backend for cloud sync
- Implement auto-import of existing progress data

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
EOF
)"

gh repo create project-name --public --source=. --remote=origin --push
```

### 7. Deploy to Vercel (1 minute)
```bash
# Add environment variables to Vercel
echo "https://PROJECT_REF.supabase.co" | vercel env add NEXT_PUBLIC_SUPABASE_URL production --scope YOUR_SCOPE --yes

echo "YOUR_ANON_KEY" | vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY production --scope YOUR_SCOPE --yes

# Deploy
vercel --yes --prod --scope YOUR_SCOPE
```

---

## Key Automations

### 1. Auto-Import Logic
The `useTracker` hook automatically imports initial progress:
```typescript
if (!data || data.length === 0) {
  await importInitialProgress();  // Auto-imports from initial-progress.json
}
```

### 2. Reusable Components
All UI components are framework-agnostic:
- `Legend.tsx` - Status legend
- `StatsBar.tsx` - Progress statistics
- `QuestionRow.tsx` - Question with status buttons
- `ExamSection.tsx` - Collapsible exam section
- `useTracker.ts` - State management hook

### 3. Shared Supabase Project
Multiple apps can share one Supabase project using different tables:
- `question_progress` - ECO 310
- `orf309_question_progress` - ORF 309
- `[course]_question_progress` - Any future course

### 4. Migration Management
```bash
# Repair existing migrations when reusing database
supabase migration repair --status applied 001

# Push new migrations
supabase db push
```

---

## Time Breakdown

| Step | Time |
|------|------|
| Initialize Next.js | 30s |
| Copy components | 10s |
| Create project files | 60s |
| Create Supabase project | 30s |
| Set environment variables | 15s |
| Git commit & GitHub push | 30s |
| Deploy to Vercel | 60s |
| **Total** | **~4 minutes** |

---

## Cheat Sheet Commands

### Quick Deploy Script
```bash
#!/bin/bash
PROJECT_NAME="$1"
ORG_ID="motwjewziafjponhebfq"
SCOPE="skylerlchans-projects"

# 1. Create Next.js project
npx create-next-app@latest $PROJECT_NAME --ts --tailwind --app --eslint --no-src --import-alias "@/*" --use-npm --yes
cd $PROJECT_NAME
npm install @supabase/supabase-js @supabase/ssr
mkdir -p lib components hooks supabase/migrations

# 2. Create Supabase project
supabase projects create $PROJECT_NAME --org-id $ORG_ID --db-password "${PROJECT_NAME}2025!" --region us-east-1

# 3. Get project ref (from output above)
PROJECT_REF="<from-output>"

# 4. Link and migrate
supabase link --project-ref $PROJECT_REF
supabase db push

# 5. Get API keys
supabase projects api-keys --project-ref $PROJECT_REF

# 6. Set environment variables (use keys from above)
echo "NEXT_PUBLIC_SUPABASE_URL=https://$PROJECT_REF.supabase.co" > .env.local
echo "NEXT_PUBLIC_SUPABASE_ANON_KEY=<anon-key>" >> .env.local

# 7. Git & GitHub
git add -A
git commit -m "Initial commit"
gh repo create $PROJECT_NAME --public --source=. --remote=origin --push

# 8. Vercel
echo "https://$PROJECT_REF.supabase.co" | vercel env add NEXT_PUBLIC_SUPABASE_URL production --scope $SCOPE --yes
echo "<anon-key>" | vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY production --scope $SCOPE --yes
vercel --yes --prod --scope $SCOPE
```

---

## Troubleshooting

### Supabase Project Limit
**Error:** "reached their maximum limits for the number of active free projects"

**Solution:** Reuse existing Supabase project with different table names:
```sql
CREATE TABLE course_name_question_progress (...)
```

### Migration History Mismatch
**Error:** "migration history does not match local files"

**Solution:**
```bash
supabase migration repair --status applied 001
supabase db push
```

### Vercel Build Fails (Missing Env Vars)
**Error:** "Missing Supabase environment variables"

**Solution:**
```bash
# Add env vars BEFORE deploying
vercel env add NEXT_PUBLIC_SUPABASE_URL production --scope YOUR_SCOPE --yes
vercel env add NEXT_PUBLIC_SUPABASE_ANON_KEY production --scope YOUR_SCOPE --yes
# Then redeploy
vercel --yes --prod --scope YOUR_SCOPE
```

---

## File Structure Template

```
project-name/
├── app/
│   ├── page.tsx          # Main UI (update title)
│   ├── layout.tsx        # Root layout (auto-generated)
│   └── globals.css       # Styles (copy from template)
├── components/
│   ├── ExamSection.tsx   # Reusable
│   ├── QuestionRow.tsx   # Reusable
│   ├── StatsBar.tsx      # Reusable
│   └── Legend.tsx        # Reusable
├── hooks/
│   └── useTracker.ts     # Reusable (update table name)
├── lib/
│   ├── exams.ts          # PROJECT-SPECIFIC
│   ├── initial-progress.json  # PROJECT-SPECIFIC
│   ├── supabase.ts       # Reusable
│   └── types.ts          # Reusable
├── supabase/
│   └── migrations/
│       └── 001_create_table.sql  # PROJECT-SPECIFIC
├── .env.local            # Local env vars
└── package.json          # Auto-generated
```

---

## Key Lessons

1. **CLI > Dashboard** - Automate everything with CLIs
2. **Reuse Components** - Build once, copy for new projects
3. **Shared Infrastructure** - One Supabase project, multiple tables
4. **Auto-Import** - Include migration logic in hooks
5. **No Manual Steps** - Script everything from start to finish

---

## Future Optimizations

- [ ] Create bash script to automate all steps
- [ ] Template repository on GitHub
- [ ] Custom CLI tool: `create-tracker-app project-name`
- [ ] Pre-configured component library package

---

**Total Time to Deploy:** ~4 minutes per project
**Projects Deployed:** 2 (ECO 310, ORF 309)
**Manual Dashboard Visits:** 0

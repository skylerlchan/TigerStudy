# 🚀 Quick Deploy Guide

## Fastest Way to Deploy (5 minutes)

### Method 1: Vercel CLI (Recommended)

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Navigate to folder**
   ```bash
   cd "/Users/skyler/Library/CloudStorage/OneDrive-Personal/Desktop/Current Project/Canvas/calendar-app"
   ```

3. **Login and Deploy**
   ```bash
   vercel login
   vercel
   ```

4. **Answer prompts:**
   - Set up and deploy? → `Y`
   - Link to existing project? → `N`
   - Project name? → `spring-2026-calendar` (or whatever you want)
   - Directory? → `./` (just press Enter)

5. **Done!** Copy your URL and bookmark it.

---

### Method 2: Drag & Drop (Easiest)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Sign up/login with GitHub or email
3. Click "Browse" or drag this entire `calendar-app` folder
4. Click "Deploy"
5. Wait 1-2 minutes
6. **Done!** Copy your URL

---

## What You Get (100% FREE)

✅ Live website at: `https://your-project.vercel.app`
✅ Automatic HTTPS/SSL
✅ Global CDN (fast everywhere)
✅ Automatic updates (if using GitHub)
✅ 100GB bandwidth/month
✅ Unlimited deployments

---

## What to Watch Out For

### ⚠️ FREE vs PAID

| Feature | Free Plan | You Need It? |
|---------|-----------|--------------|
| Static Sites | ✅ Unlimited | ✅ YES |
| Bandwidth | ✅ 100GB/month | ✅ YES (plenty) |
| Custom domain | ❌ Need to buy | ❌ NO (free .vercel.app works) |
| Analytics | ✅ Basic | 🤷 Optional |
| Commercial use | ❌ Need Pro | ❌ NO (personal) |

**You're fine on free plan!**

---

### ⚠️ Things to Know

1. **URL is Public** - Anyone with the link can view
   - Don't add sensitive info (grades, etc.)
   - Current calendar is fine to share

2. **No Auto-Updates** - You need to manually update
   - Edit `index.html` locally
   - Run `vercel --prod` to update
   - OR connect to GitHub for auto-updates

3. **No Backend** - This is just static HTML
   - Can't save user data
   - Can't have login system
   - Perfect for your calendar!

4. **Build Time** - Usually instant
   - First deploy: ~1-2 minutes
   - Updates: ~30 seconds
   - Since it's pure HTML, very fast

---

## Updating Your Calendar

### To add new assignments:

1. Open `index.html`
2. Find the date you want to edit
3. Add an assignment like this:
   ```html
   <div class="assignment asa201-bg">
       <span class="assignment-dot asa201-dot"></span>
       <span>Your assignment here</span>
   </div>
   ```
4. Save and redeploy:
   ```bash
   vercel --prod
   ```

### Course colors available:
- `orf309-bg` and `orf309-dot` (Blue)
- `eco310-bg` and `eco310-dot` (Purple)
- `asa201-bg` and `asa201-dot` (Orange)
- `mus262-bg` and `mus262-dot` (Green)

---

## Troubleshooting

### "Command not found: vercel"
→ Run: `npm install -g vercel`

### "npm: command not found"
→ Install Node.js from [nodejs.org](https://nodejs.org)

### "Deploy failed"
→ Make sure you're in the `calendar-app` folder
→ Check that `index.html` exists

### "Site won't load"
→ Wait 2-3 minutes for DNS propagation
→ Try incognito/private mode
→ Check [vercel-status.com](https://vercel-status.com)

---

## Alternative: View Locally

If you just want to view without deploying:

1. Open Finder
2. Navigate to the `calendar-app` folder
3. Double-click `index.html`
4. It opens in your browser!

No deployment needed for personal viewing.

---

## Next Steps After Deploy

1. ✅ Bookmark your URL
2. ✅ Add to home screen on phone
3. ✅ Check weekly and update assignments
4. ✅ Share with study partners (optional)

---

**Questions?** Check the full README.md for more details.

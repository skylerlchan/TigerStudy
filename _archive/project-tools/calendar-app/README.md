# Spring 2026 Academic Calendar

A beautiful, interactive calendar for tracking your Spring 2026 assignments and deadlines.

## 🚀 Deploy to Vercel (Free)

### Step 1: Create a Vercel Account
1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub (recommended) or email
3. Verify your email if needed

### Step 2: Deploy Your Calendar

**Option A: Deploy via Vercel CLI (Recommended)**

1. Install Vercel CLI:
```bash
npm install -g vercel
```

2. Navigate to this folder:
```bash
cd "/Users/skyler/Library/CloudStorage/OneDrive-Personal/Desktop/Current Project/Canvas/calendar-app"
```

3. Login to Vercel:
```bash
vercel login
```

4. Deploy:
```bash
vercel
```

5. Follow the prompts:
   - Set up and deploy? **Y**
   - Which scope? (select your account)
   - Link to existing project? **N**
   - What's your project name? `spring-2026-calendar` (or any name you want)
   - In which directory is your code located? **./** (just press Enter)

6. Your calendar will be live! Copy the URL that appears.

**Option B: Deploy via Web Interface**

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click "Add New..." → "Project"
3. Import this folder:
   - You can either:
     - Push this folder to a GitHub repo first, then import from GitHub
     - OR drag and drop this folder directly to Vercel
4. Project settings:
   - Framework Preset: **Other**
   - Root Directory: `./`
   - Build Command: (leave empty)
   - Output Directory: (leave empty)
5. Click "Deploy"
6. Wait 1-2 minutes for deployment
7. Your calendar is live!

### Step 3: Access Your Calendar

You'll get a free URL like:
- `https://spring-2026-calendar.vercel.app`
- Or `https://your-project-name-username.vercel.app`

## 📱 Features

- ✅ Traditional calendar grid view
- ✅ Color-coded by course
- ✅ Highlights your presentation day
- ✅ Shows all recurring assignments
- ✅ Finals period section
- ✅ Mobile responsive
- ✅ No backend needed - pure HTML/CSS

## 🔄 Updating Your Calendar

### If deployed via CLI:
1. Edit `index.html` with any changes
2. Run `vercel --prod` to deploy updates
3. Changes go live in ~30 seconds

### If deployed via GitHub:
1. Push changes to your GitHub repo
2. Vercel automatically redeploys
3. Changes go live in ~1-2 minutes

## ⚠️ What to Watch Out For

### 1. **Cost (FREE for you)**
- ✅ **Hosting:** 100% FREE forever
- ✅ **Bandwidth:** 100GB/month FREE
- ✅ **Deployments:** Unlimited
- ✅ **Custom domain:** FREE `.vercel.app` subdomain included
- ⚠️ **Custom domain (your-name.com):** Requires buying a domain (~$10-15/year)

### 2. **Build Times**
- First deployment: ~1-2 minutes
- Updates: ~30 seconds
- Since this is just HTML, it's instant!

### 3. **URL Changes**
- Your free URL: `https://[project-name].vercel.app`
- This URL is **permanent** and won't change
- You can change the project name in Vercel dashboard if needed

### 4. **Analytics (Optional)**
- Vercel offers free analytics
- Enable in: Project Settings → Analytics
- See page views, visitors, etc.

### 5. **Environment**
- No environment variables needed
- No build step required
- Just pure static HTML

### 6. **Limitations on Free Plan**
- ✅ Unlimited static sites like this one
- ✅ Unlimited bandwidth (within reason - 100GB/month)
- ✅ Unlimited deployments
- ✅ SSL/HTTPS included automatically
- ⚠️ Commercial usage may require paid plan
- ⚠️ Serverless functions limited (but you don't use any)

## 🎨 Customization

Edit `index.html` to customize:
- Colors (search for `background:` in CSS)
- Dates (add/remove assignments)
- Course names
- Finals dates

## 🔒 Privacy

- This calendar is **public** by default (anyone with the URL can view)
- Don't include sensitive information (grades, personal details)
- Current content is fine (just assignment dates)

## 📞 Support

If you have issues:
1. Check [Vercel Documentation](https://vercel.com/docs)
2. Check [Vercel Status](https://www.vercel-status.com/)
3. Contact Vercel support (free plan includes community support)

## 🚨 IMPORTANT REMINDERS

1. **Check Canvas regularly** - ORF309 homework dates TBA
2. **Update the calendar** when new assignments are posted
3. **Bookmark your Vercel URL** for easy access
4. **Share the URL** with study partners if helpful

---

**Current Status:** Ready to deploy! Follow Step 1 above to get started.

**Estimated Time to Deploy:** 5-10 minutes total

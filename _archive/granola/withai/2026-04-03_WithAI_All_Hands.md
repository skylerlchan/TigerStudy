# WithAI All Hands

**Date:** 2026-04-03


## My Notes

Would you be interested in making your hedge fund AI native? todo: open in new workplace ask me for a lots of clarification → My next taskUI Fixes: tiptap editor md files investment decision framework Monday night


## Summary

### GTM Strategy

- Top-of-funnel is the core bottleneck — not middle of funnel
- Active LinkedIn outreach via Boughtdog: ~2,500 ICPs, automated connection request → short follow-up message
- Current question: “How has AI most disappointed you — writing a white paper?” flagged as too generic- Consensus: message needs to feel personal and sincere, not like a sales tactic
- “Would you be interested in making your hedge fund AI native?” — simple, direct approach as an alternative
- LP partnership idea: frame outreach as joint research with an LP (e.g. HS Group) to boost response rates
- Risk: optimises for volume of conversations, not quality/fit
- Warm intros likely higher value than cold outreach for the existing 2,500 ICP list
- Evan Kat (runs newsletter, advises in the space) flagged as potential connector

### Product Priorities

- GTM first, product second — need to close sales cycle before demo day
- Demo moments that move the needle: show automation result on phone within 1 min; run task across 60 folders in parallel
- UI polish still valuable as it supports both student users and GTM demos
- Shipping to Princeton students deprioritised — not contributing to immediate GTM needs

### Engineering Updates (Ben)

- VM full automation system set up: outbound/inbound connection blocking, two-tier user access, Tailscale, key management
- VM connected to Mercator/OneDrive database; permission scoping with Syed to limit access to selected SharePoint folders
- AI parallel processing system developed
- Claude Code: fixed download method (now via VS Code extension store), auto-update system in place
- Markdown files fix: open with correct editor by default — both Ben and Skyler applied the fix independently

### CRM & Tracking

- Current CRM (Adio): tracks last interaction, ~10 live deals, but doesn’t distinguish prospects from vendors/interns
- Goal: build custom CRM within WithAI that auto-tracks meetings, email, and LinkedIn connections
- Headline outreach KPIs not yet tracked — flagged as a gap

### Team Process

- Ask for lots of clarification before building a feature — align on mental model first
- Ben’s suggestion: treat it like a product spec with clarifying questions before implementation
- Screen sharing features during build to get earlier feedback
- Linear used for task tracking — assign everything so ownership is clear

### todo:

- Open in new workspace → change behaviour so it closes the old workspace instead of spawning a new one
- Most users should have one workspace at a time
- Ask for lots of clarification before starting a feature → confirm mental model is aligned with Ben’s intent

### My next task

- UI fixes:
- Tiptap editor- Markdown files (bug: shows “M” symbol on Ben’s side, looks fine in dev mode — new Linear ticket created)
- Investment decision framework
- Wrap up all engineering tasks by Monday night
- Next week: shift focus to GTM alongside Ben and Ian

### Next Steps

- **Skyler**
- Fix workspace behaviour: open in same window, close old workspace- Fix markdown file rendering bug (Linear ticket added)- Complete UI fixes (Tiptap, markdown) and investment decision framework by Monday night- Join GTM effort next week — review Ben & Ian’s current outreach approach- Talk to Ian after the meeting re: Princeton ICP list and outreach strategy
- **Ben**
- Build GTM dashboard for all three to track outreach progress- Explore LP partnership angle (e.g. HS Group, Evan Kat) for joint research framing- Onboard new people; hand off engineering iteration to Marty
- **Ian**
- Follow up with Skyler after meeting on Princeton ICP list- Refine pitch with Ben; use Skyler as a test audience next week
Chat with meeting transcript: https://notes.granola.ai/t/3908e068-5b39-411d-a95f-e51ca38e6353


---

## Transcript

**:** Hey Ben.

**:** Hey Skyler.

**:** How's it going?

**:** In the other room.

**:** You know, venison is joining.

**:** I think it's all for the day. I don't know. We can.

**:** Text him. Last time I saw him, he was at frisk. He has some stuff.

**:** Have you been Ian? I haven't seen you for a while. I guess I've seen you. I just haven't talked with you for a while.

**:** Ian.

**:** Yep.

**:** Regarding your point.

**:** Let's say that.

**:** We need to have 1000 conversations or we need to have 1,000 reach outs.

**:** And 100 conversations.

**:** If we do.

**:** 10.

**:** 1.

**:** 0.

**:** If we genuinely.

**:** Can do.

**:** And if there turns out to be an abundant quantity of these.

**:** And each one of these reach outs takes 10 minutes.

**:** For us to do a thousand of them.

**:** It would take two weeks.

**:** Like if one person working 12 hours a day, reaching out 10 minutes, 10 minutes, 10 minutes, 10, 10 minutes.

**:** Which is not.

**:** Like.

**:** Entirely.

**:** Undoable.

**:** Or not doable.

**:** Especially.

**:** If we had.

**:** AI that could connect to our text messages and to our.

**:** Email.

**:** Because then once we initiated something.

**:** The AI could low key. Well, I don't know. Honestly, I wouldn't even automate it to start.

**:** Yeah.

**:** This is feasible.

**:** And.

**:** Yeah, I'm not sure whether.

**:** Direct linkedin outreach.

**:** Or chart of, like, find what school they went to, find someone who went to that school.

**:** Get into.

**:** I mean, with the.

**:** So for something that we should do is I should use sales navigator to completely exhaust Princeton.

**:** Yeah, we shouldn't do that.

**:** But I, I do have right now.

**:** An automated.

**:** Connection. And first cold message campaign running through boughtdog for the roughly 2500 ICPs that I was able to find.

**:** Through. How does that work?

**:** Sends a connection request to them.

**:** You know, on LinkedIn.

**:** Yeah.

**:** Then after they accept, it sends a message and I drafted it. So it's just asking them a very short question to get them to engage.

**:** And then I follow up.

**:** What's the short question?

**:** A, what AI, how has AI most disappointed you were writing a white paper?

**:** This is not a good question. I think Skyler, what do you think? My thought is this is not a good question.

**:** What's the question?

**:** What's your question?

**:** I, I would not respond to this question.

**:** I would, I would make it like more personal. I would say like, hey, because this, this.

**:** Ian.

**:** I am a.

**:** Recent grad.

**:** From Princeton. I have that other stuff.

**:** Now I'm part of a, like an accelerated program we're trying to understand how hedge funds work.

**:** Would really, really appreciate if you could send, like, or like.

**:** Curious to hear what you're, and low-key, I don't know.

**:** Like, I don't know if in LinkedIn you even want to be like initiating conversation like that.

**:** This is what all the guides I have read on doing B2B sales through LinkedIn.

**:** Say.

**:** Skyler, what do you think?

**:** I.

**:** M on the side of simplicity. Like I just state exactly my purpose and goal of why you contact. Obviously you're gonna have a much, much lower turnout rate, but then you'll like you'll be crunching out a lot.

**:** I don't know. I actually personally don't believe in fancy tactics, but that's my take. So I'm not that helpful in this case.

**:** It's okay.

**:** I've had very good success so far with transitioning seamlessly from, oh, I'm just gathering some information to I'm selling you some stuff.

**:** No, I believe that. But, like, that initial question, like, if I get, because I did, I feel like everyone gets so many spam linkedin messages.

**:** From people trying to sell you stuff, right? And.

**:** Like you ignore most of those messages and a lot of them will start like this feels like it's a sales tactic.

**:** What's your idea?

**:** Let me think. What, what would I actually respond to?

**:** I feel like it has to be personalized in some way.

**:** And I feel like it has to come off as like really sincere.

**:** Like kind of along the lines of what I was just saying.

**:** I mean, so I have all the, I'm workinger to start up yada yada stuff.

**:** And as far as personalized.

**:** I mean, I can try, but I've had a very difficult time finding enough about these people online to ask any kind of personized questions.

**:** Because it'll just be like linkedin investor here 12 years.

**:** Open to suggestions.

**:** I, I, maybe we keep this bot thing, but then like with the 2500 ICP list we already have, we just start finding, like, warm intro channels.

**:** Warm interest is probably the case. I had to do this.

**:** As a missionary. I had to actually spam call, I think, 200 people a day.

**:** That was like required. Like I had to do that as part of my job and it sucked because I had to flipping like press copy and paste 200 times and I pissed me off. So I just did the same message and it had one of the lowest success. But like you'll get conversations if you do it and it'll be simple. It'll be like your kids, it would just be like would you be interested in making your hedge fund a I native, something like that.

**:** And then the people that respond will actually be interested and it filters out like, but like again, that's like very.

**:** Laborious.

**:** Yeah, for us are, for us, our problem is top of funnel, not middle of funnel.

**:** Oh, it's top of funnel. So like try to open it. Like you don't have enough people to.

**:** Like.

**:** Yeah. So I'm just trying to engagement max.

**:** Engage min max.

**:** Huh? That's a different type of, okay.

**:** You have any way that I can see your current like overall set of an approach. Like is there anything I can see.

**:** Dude, you know, it would help if we.

**:** Like somehow partnered.

**:** This might be an out there idea, but if we partnered with an LP.

**:** And we reached out and realized, hey, I'm doing like research with this LP.

**:** Would you.

**:** Be interested in like talking?

**:** They would always say yes to someone who works for an LP. I feel like.

**:** Well, that's a great idea.

**:** That's a great idea.

**:** Now who would let us, do you think we could talk Princo into it?

**:** That's a tough one.

**:** I feel like someone like HS group would be easier.

**:** We have like a joint research project with a s group.

**:** I could try Evan kat.

**:** Who's that?

**:** He is.

**:** The guy I talked to who does lots of like advising to

**:** And runs the newsletter.

**:** Yeah, that's not a bad idea, but I think.

**:** If we can, I do think if we could have like some kind of partnership with an LP and be like, we are doing joint research on.

**:** Like AI usage in the hedge fund industry.

**:** Would you be open to a conversation?

**:** Yeah.

**:** The problem is then, I mean, Skyler won't like this.

**:** Because then.

**:** We're, we're not getting the natural filter. Like this will get us a lot more conversations, but it might be the wrong kind of optimization.

**:** I have a tendency to.

**:** Find ways to.

**:** Achieve that interim, achieve intermediate outcomes that shoot myself in the foot for longer term outcomes.

**:** Such as.

**:** Over optimizing my.

**:** Hinge date.

**:** Success rate.

**:** That's a good one.

**:** Oh my god.

**:** Okay, well, let's have our, let's have our meeting.

**:** So what did we all do this week?

**:** Let me look back at my linear.

**:** Let me ask claude. Give me a sec. Sorry.

**:** I can ask my claude, but you guys all did this week.

**:** That is even better idea.

**:** Because I have connect, I have linear connection now.

**:** Yes. Good one. You got the linear E.

**:** 3.

**:** To my stuff. According to linear.

**:** Let's see what it says.

**:** Okay, Skyler markdown files from claude code that should be, should open.

**:** In.

**:** Markdown files from claude code that should open with a editor by default.

**:** Oh yeah, I think I fixed it.

**:** I did exactly what you said. It worked.

**:** Oh, because, well, then we both applied that fix because I also fixed that.

**:** Oh my bad.

**:** Well, either way, it's working. I think it's working now.

**:** Also the, you know, the new workspace scene. I did that too. Like you could just like right click on a folder and open the new workspace. Pretty neat.

**:** Let me test.

**:** When did you push this?

**:** Oh, you nice.

**:** Yeah, that's nice. It's like so convenient now too. I'm like a.

**:** Yeah.

**:** But can we make it so that it.

**:** Like, it doesn't open it in a new workspace? Can we make it so that it opens it here?

**:** So, like, it closes the old one.

**:** Yeah, we could do that. I didn't know that but yeah.

**:** Yeah. Because, like, I don't want the people spawning, like, so many workspaces. You should just have one with the iwork space at a time.

**:** Unless you really want to have multiple. But, like, most people should not, because that's how you, like, create pain. I like mono repos.

**:** Now that's fair. Actually, oh my gosh then I over engineered it because I literally worked on it to open a new okay that'll be easy then easy switch.

**:** Skyler.

**:** Yes.

**:** I'm going to tell you the same thing I've been telling my writing into my own clawed system prompt.

**:** Like, ask me if I ask you for a feature. Ask me for a lot of clarification. Like, make sure you have a good mental model of the feature.

**:** And, like.

**:** Just make sure we're aligned.

**:** Because I've noticed a little bit, like, we, like, usually, and it's, this is part of this is my, it's not like any one of our fault, but, like.

**:** I have an idea of what I want.

**:** And then, like, the implementation doesn't end up being exactly the same.

**:** I think definitely I would do a better job in iterating like I think the more checkups we have I guess as I build my work. Loki I might just start screen sharing like the features I make and then like that way like you can see it and then you can prove or disapprove and you know I think yeah I think that's a great idea.

**:** Like sometimes you know sometimes the questions come up when I'm building it but it would be great.

**:** You know if we do it beforehand too I totally agree like you're supposed to have like that master prompt.

**:** You know.

**:** Like, with the ice skill, that's.

**:** Like products.

**:** Specs.

**:** And it just asked me a bunch of questions because I know sometimes I say things in a way that, like.

**:** It's not completely clear what I want.

**:** Me too don't worry about it.

**:** We're all human.

**:** Okay.

**:** Folder buttons next to change folder and fix breadcrumb truncation.

**:** Next.

**:** Buttons.

**:** To five.

**:** Let me turn my screen.

**:** Let's do it.

**:** This is a very good like weekly review thing.

**:** Like seeing exactly what you did.

**:** This is neat.

**:** I'm going to share my screen.

**:** Do you see this, Skyle?

**:** R?

**:** Yeah it's kind of blurry right now let me just make it bigger okay it's actually super blurry.

**:** Let me see if I can make a full screen.

**:** Make it better nope it's still blurry.

**:** Oh I can like kind of.

**:** Maybe do you maybe you can move it on the smaller screen I don't know if that will help.

**:** Oh yeah but that's right on linear we should have everything assigned that's usually that way we know exactly.

**:** Who should be doing what actually let me check actually look we've been doing a good job though.

**:** See.

**:** How about now on this smaller screen?

**:** Very blurry I'm not sure why.

**:** Yeah it's it's actually I don't know why it's super blur.

**:** Do you see it?

**:** Yeah.

**:** Is it blurry.

**:** It might be.

**:** Or.

**:** It's a little blurry.

**:** Yeah you can kind of read it I think this is good enough yeah it's just chill we can go.

**:** Well, let's just read out.

**:** Oh it's good now it's good now it's good.

**:** That's good.

**:** A few more linear issues that I forgot to attribute to myself.

**:** We'll add them.

**:** Oh yeah okay sweet and then let me see.

**:** Now for me.

**:** I get this M symbol.

**:** Like, this is what my markdown files look like.

**:** Let me take a look.

**:** Oh I saw that glitch okay let me thanks for oh that is interesting.

**:** Huh.

**:** Never had that problem before okay let me let me check the bug because it looks different on my side.

**:** You're using.

**:** Why does it do that Ben?

**:** Like okay opening it up on dev mode on my side and it looks fine and then it switches it up when you go on a different.

**:** I don't know.

**:** But.

**:** Just get that fixed.

**:** Yeah let's do it I'll get it let me upgrade a new linear ticket.

**:** Okay.

**:** Sweet.

**:** Just added it in.

**:** At the very beginning of the week, I did.

**:** Set.

**:** Full automation system.

**:** On the VM.

**:** Block outbound connections for the VM securely.

**:** Create.

**:** D.

**:** Different user system.

**:** With two levels.

**:** Of access.

**:** So agent cannot.

**:** Blocked inbound connections on the VM.

**:** Set up tailscale access on the VM.

**:** Set up access to with AI.

**:** Abilities on the VM.

**:** Set up.

**:** Recreated.

**:** Flawed abilities and behaviors, context management system for the VM agent.

**:** Connected VM to mercator, one drive.

**:** Database.

**:** Connected VM to.

**:** Worked with Syed to create permission scoping to limit VMs access within mercator systems. So only selected the SharePoint folders.

**:** And I think that's everything in the VM.

**:** I.

**:** Start developed.

**:** The.

**:** AI parallel processing system.

**:** We're marked down files.

**:** We're not opening in the right place.

**:** Fixed.

**:** Bug where when you close and reopen with AI, your past.

**:** Bug.

**:** Where.

**:** In progress.

**:** In progress started working on.

**:** Redoing how we are pinning, we are downloading cloud code. So we're getting it the way we're supposed to from the VS code extension store.

**:** And making sure that cloud code stays up to date.

**:** Set up a system for managing keys.

**:** For.

**:** New users.

**:** Those are most of the.

**:** Okay, rewrite the full list of what everyone's done.

**:** Okay, great.

**:** We should do this next time because then it's like very clear like it's like you optimize for like the tasks being done so like everyone was more accountable like this is.

**:** Like this thing can't really well I guess you can lie about your tasks but it's just harder to do that.

**:** This is good I like it.

**:** Yeah.

**:** So those are some of the stuff I got done. I'm sure there's some other things.

**:** Ian, what did this week look like for you?

**:** Do you want us just to read?

**:** And, you know, go into the YC stuff like you had a big old pile of calls that aren't on here?

**:** And. Yeah, calls him follow ups from calls.

**:** And just so that we.

**:** Yeah.

**:** Cool.

**:** And it's literally the voice. Can you add both to Ben?

**:** Had calls.

**:** For.

**:** GTM? That's an Ian one. And then for Ben had calls Consulting security experts.

**:** You can also add.

**:** Actually, can you.

**:** Break.

**:** For the time? I'm not going to devote that much to it going forward.

**:** Automations.

**:** Getting YC people into audio.

**:** Can you remove connect VM to syncing with one.

**:** Messaging? The sinzu's issues.

**:** Of YC.

**:** Ian and I, we both had those, like, kind of two, at least half days of events. That took some more time. It was both inspiring.

**:** I think.

**:** It's a bit of a low velocity week.

**:** Like, I think we need to do better.

**:** And I think part of this is.

**:** Like, I know with you, Skyler and Edison, there was like, you know, I ended up just doing some of the tasks you guys had initially assigned. So there may have been some, like, confusion as what to do. And I think we should have a.

**:** Like you guys are going to have the tasks that you're responsible for.

**:** Of course.

**:** Or to kind of, like, pieces that you're responsible for. And let's figure out what those pieces are.

**:** So for you, Skyler, I think.

**:** Like.

**:** What do you think about, you know, making these.

**:** Investment process skills? Really good.

**:** I love that idea I mean.

**:** Like there's so much stuff I was looking at the newest version of gtack mine was a week ago like it was actually like it was one or two weeks and it's already behind like there's there's a lot of new stuff that he added.

**:** So I think we can make it really good really really good.

**:** What are your thoughts?

**:** Yeah, that's great.

**:** Should that be my next week or I mean I want to continue to work on the UI too to make it look smooth and I also want to ship it out to Princeton students as well as soon as possible.

**:** What are your.

**:** Yeah. I mean, you can, I think this shipping out this student, Princeton, that's a bit of, like.

**:** An, that's a great activity.

**:** But it's not, like, contributing to immediate, extremely sharp, painful GTM, like, requirements that we have right now.

**:** I agree.

**:** You know?

**:** Making the UI.

**:** Really good.

**:** Obviously, that would help both the students and the people that we're trying to get it to.

**:** Like.

**:** I think we need to.

**:** I think that, that will move the needle. You know, if we can have things that look really good, if we can show in our demo.

**:** Like.

**:** Make this automation and then show the result on your phone.

**:** Like one minute later.

**:** That's pretty cool.

**:** I think if we can show.

**:** Like, do this task across 60 folders in parallel right now.

**:** That's pretty cool.

**:** Ian, what do you think?

**:** What do you think?

**:** Is most valuable to us to achieve our, like, kind of super immediate goal of getting 10 more clients?

**:** In terms of product?

**:** In terms of what Skyler and editing, or should we get Skyler just, like, helping out with GTM stuff?

**:** I.

**:** Graduate starting out on GTM stuff.

**:** Yeah.

**:** Wait Sergeant can you guys say that I got my my thing cut out.

**:** Like, it might make more. Yeah. Also, Ian, I'm not, I think maybe it thinks it's detected we're in the same room or something, and it's only using my mic.

**:** What do you think about helping it?

**:** Like, what do you think about helping out with gtm stuff? Because we have a whole lot of legwork here.

**:** And that's going to be.

**:** That, that's going to be a pretty big.

**:** Like that. That's just, like, kind of an immediate barrier we have to fix.

**:** Here.

**:** And product second.

**:** Roughly in order.

**:** You can capitalize on the GTM that you did in time for the product to be ready.

**:** Whereas if you do product first and GTM second.

**:** You don't close the sales cycle before demo day.

**:** I said let's we can definitely focus on GTM I essentially the system I okay so I created the system my my my my like boss was like a former asset manager he had like he had a half a billion dollar fund and he saw my GTM system and he absolutely like went for missionary rookie absolutely loved it we could we could take a look I mean I could see what you guys are doing I get like we can definitely like look at what you're doing in the end and I think having another person also helps a lot it's it's tough work it is hard like it's brutal and like you're calling and you're texting and it's tiring and it's like repetitive so like you're doing great already and like the stuff is hard like it is very hard a lot we had a lot of mental health issues when people did my strat but it's because it's worth it I mean you get great returns though but it's definitely hard.

**:** Yeah. Things have gone pretty well.

**:** After initial conversations, but getting to the initial conversations hard.

**:** Yeah that's that's where the that's where the goad is at right that is where that's where everything begins.

**:** I mean yeah maybe maybe maybe some time next week or even right now you can show me what you're doing.

**:** Like do you have kpis and stuff like that to like kind of like keep track of like like do you have like a dashboard or something like that you're keeping track of the amount of call you're sending and stuff.

**:** Yeah.

**:** Of all calls that have been had, whether they were good or not.

**:** Dashboard and I.

**:** Do our own custom CRM within with AI that our age.

**:** I think that'd be really good.

**:** I mean, so far, my main kpis have been, I've been staying on top of deals.

**:** With adio, which, you know, tracks last interaction. So I'm not letting those go dead.

**:** And there are, like 10 live deals there.

**:** That's cool.

**:** But, yeah, have not tracked, like, the headline Outreach stuff.

**:** Yeah I mean having having a good tracking system like it provides a lot of focus just on like making sure you're you're doing the right things that lead to success but it seems like you're already keeping track of like the most important parts so.

**:** Like maybe it's just a little add on for like what you're doing to reach out perhaps.

**:** Maybe this one I'm hearing.

**:** Here are ideal Princetonians message the ideal Princetonians with the time to chat.

**:** Or, you know, message the ideal Princetonians, set up a time to chat.

**:** Is what I think is what I would get a lot of mileage out of.

**:** Yeah I mean do you have like a list of Princeton's you want to contact already?

**:** And like have you gone through them have you developed that and curated that list already?

**:** Sort of.

**:** Actually, you know, the audio is so bad. How about you? How about you and I talk after this meeting?

**:** Is this better now?

**:** No, because it's detecting me and Ben being in the same room.

**:** Okay that's all right we'll talk after we'll talk afterwards chill.

**:** And.

**:** I'm literally using captions to live captions in order to get this to understand what's going on.

**:** Okay, is this.

**:** This is better.

**:** Yeah.

**:** I still can't hear you Ian as well.

**:** Now you're good.

**:** API.

**:** Kpis, super good.

**:** I will say for, for the CRM that we have in, you know, for the crm, it would be good if it could automatically track meetings and email connection and linkedin connection.

**:** Like audio does.

**:** So does.

**:** Audio does that automate does it like it doesn't know how many people you caught that day and how many oh it does right I was experimenting audio it does.

**:** It's just like clunky and it doesn't automatically distinguish between, like vendors.

**:** Or interns or whatever that I called.

**:** And prospects that I called.

**:** Okay.

**:** That makes sense yeah let's let's talk after we can let me let me take a look at the audio I think that I think it's already a great software we just have to like leverage it more you know to get.

**:** The most juice out of that.

**:** This, this is what I'm thinking.

**:** I'm also, I don't know how busy is your week next week, Skyler.

**:** I have a midterm so maybe I'll be a bit busy.

**:** Because what I'm thinking.

**:** We give ourselves hard because obviously the engineering tasks we want to, like, get them kind of wrapped up in, like, a bit nice.

**:** And we on board those new people.

**:** How about we give ourselves, like, a certain day next week?

**:** Where we are still.

**:** Adding in.

**:** Like, fixes to stuff like that.

**:** You can make.

**:** It have something you're proud of and process that you can then leave with Marty to, like, run with for, you know, let's say, like.

**:** A week or something.

**:** Okay.

**:** And then from there, we can.

**:** Like.

**:** Be, let's say this, let's try to, like, wrap up all.

**:** Engineering related stuff, like on, on this iteration of engineering stuff and, like, be like, okay, we're cater now. Try to use it.

**:** By, like, Monday night.

**:** And then let's give, like.

**:** Next week where low-key.

**:** All three of us loud on figuring out how we're gonna, how we're gonna sell to people.

**:** Yeah.

**:** Now this gets me pumped up I'm excited for this this should be great.

**:** Yeah. And tomorrow dashboard for all of us, so we can, we can see our progress.

**:** Another, like, even me and Ian need to, like, make our.

**:** Our pitch even smoother. We can test it. I think you'd be a good.

**:** Good test.

**:** And we'll, like.

**:** Let's, let's make some money.

**:** Let's do it let's do it.

**:** Let's do it.

**:** Cool.

**:** Okay.

**:** You guys.

**:** Okay bye.

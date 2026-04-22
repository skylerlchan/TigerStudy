# WithAI All Hands

**Date:** 2026-03-27


## My Notes

Home panel 



see the path





parent folders - workspace 



breadcumb → root home 











PATH 1: edit intial vscode extesnion







have bread crumbs set up that point to the home folder



so when you select a parent folder in the breadcrumbs, it opens that in workplace 





PATH 2: 





Next Goals:



What are the most pressing manners to get through? 



Edit explorer/home ui 

finish marty's skills 





my tasks 





model skills -  all of Marty's skills 



security 



home ui 



meet with Marty to explain my workflow


## Summary

### Home Panel UI Updates

- Path navigation improvements needed
- Add breadcrumbs pointing to home folder- Enable clicking parent folders in breadcrumbs to open workspace- When entering shared folders, private folders should disappear/collapse- Make Explorer look like modified VS Code explorer
- Two implementation paths discussed:
- Edit initial VS Code extension with breadcrumbs + parent folder selection- Modify current Explorer (chosen approach)
- Context window integration
- Purpose: define AI context window by folder selection- Double-clicking folder sets that as context for Claude interactions

### Weekly Progress Review (March 27)

- Goals achieved:
- Demos completed- First prime broker meeting held- 7 serious lead conversations (ongoing potential sales)
- Goals missed:
- All prime broker meetings not completed- Auto update not finished- Security process started but requires 4-week compliance timeline
- VM automation and Mercator skills in progress
- YouTube transcript skill deployed and being used by Marty- Research skill completed today- Patent search and SEC filing skills remaining

### Next Cycle Objectives (Through April 15)

- Product deployment goals:
- Practice deploying WithAI into Tiger Sustainable Investment Group- Set up Terraform for Azure deployments- Deploy to 5 beta users- Test system with actual second customer within one month
- Security compliance:
- SOC2 compliance process ongoing- Penetration testing scheduled in 4 weeks- Focus on internal security measures, not product review

### Product Readiness Concerns

- Skills refinement priority
- Need direct observation of Marty using current tools- Excel integration causes terminal access issues/freezing- Model skill difficult to use, awaiting Jessica’s template updates
- Monitoring implementation options:
- Self-hosted PostHog for usage tracking- Manual observation and chat history analysis- CSV logging in shared folders
- Dashboard development needed for progress tracking

### my tasks

- Model skills - complete all of Marty’s skills
- Security implementation
- Home UI improvements
- Meet with Marty to explain workflow and observe usage patterns

### Next Steps

- Ben: Schedule remaining prime broker meetings, contact Scott about UBS outreach
- Edison: Complete VM automation by March 30, work through weekend if needed
- Team: Create Linear tasks from discussed objectives, assign individual ownership
- All: Set up Terraform deployment infrastructure collaboratively
Chat with meeting transcript: https://notes.granola.ai/t/b5b7b7b5-91c0-484e-b613-00a556e41bc6


---

## Transcript

**:** Let me see.

**:** And I think, like.

**:** When you're at home, you can have, like, the private folder shared folder thing.

**:** Yeah, so it's still the same.

**:** When you go. So when you go into one or. No, not here. So, like, go to, like, the new menu you made.

**:** This one.

**:** Right?

**:** So, like, go into one of the, like, double click one of the shared folders.

**:** Sure. I'll just go to the caterers with the AI abilities.

**:** Yeah.

**:** So, like, when you go in the private folders should not, like, show at the bottom.

**:** Oh, so this thing should just collapse then. Okay.

**:** Or it should just all disappear.

**:** Okay.

**:** So when you go in, it should disappear.

**:** And in general, like, I should feel like I'm just looking at, like, modified VS code explorer.

**:** I see.

**:** So the purpose of this was simply to. Was it for the context window of the AI is that the reason why we're doing this.

**:** Like, making it look like this.

**:** Yeah.

**:** It's so that you can.

**:** Like, the reason is that so that you can.

**:** You can basically Define the context window however you want to.

**:** Yeah.

**:** Okay, so then this. The context. So let's say I just want to make this clear on my side. So we go to one drive. And let's say you just want to only want to work on abilities that day. You double click on ability.

**:** And then you get. You get into all the abilities right here.

**:** And then.

**:** All you do is it. So then right now, when you go on claw, like right here, you just type random stuff. It's supposed to just be in this context window.

**:** And then that the way we want to do it.

**:** Is that. Okay, so then I have to connect this to claud somehow.

**:** Using the back end or something like that.

**:** Or.

**:** Well, however it is in, like, explorer, like, when you open something in explorer, you're literally opening.

**:** Like, that repo. Like, now your VS code is, like, set to that repo.

**:** Right?

**:** Yeah.

**:** That's right.

**:** And the same with, like, our home folder, like our old home folder.

**:** That you designed.

**:** Like, when you open something for your old, old home folder, you, like, go into it.

**:** Like click it.

**:** Yeah. So next, I'll just click on canvas.

**:** Oh, I'm already in that. Okay, let's try something. Oh, actually, I don't know why.

**:** Okay, so I'm in it right now. Okay, so this is.

**:** So this is the normal. This is.

**:** So our current one is not. Yeah, I'm actually. I'm still unclear. Like, what's the.

**:** What do you see as.

**:** What's the.

**:** What?

**:** What's. Okay, so we create our own.

**:** I guess. Or. Or we modify this. What are we. What do we. Let's say we want to just modify the. The current.

**:** I guess.

**:** The current Explorer one. How. How.

**:** Okay.

**:** Let me show you what I mean on my screen.

**:** Yeah, sure, sure. Let me. Let me get out this.

**:** Okay.

**:** So now when I'm in with AI.

**:** Yeah.

**:** What we want is.

**:** So for now, just ignore this home button.

**:** Okay.

**:** Okay.

**:** Don't even think about it.

**:** We want this Explorer.

**:** To look like this.

**:** Exactly what you see.

**:** But to have the features that you added.

**:** Like, so you can see the path and you can click on different past parts of the path.

**:** And you're moving.

**:** And when you click on a different piece of that path, so, like, let's say.

**:** So right now I'm in Ben home, but let's say I went into.

**:** Your window.

**:** And then I went into.

**:** Let's say I went into Ben home, but then I want to go into, like.

**:** Census data.

**:** And now it will open.

**:** I don't know why it's not opening.

**:** So I'm opening intersection home.

**:** Well, it's not working.

**:** But let's say I opened.

**:** Okay, let's say going to Ben home and let's say.

**:** I want to share your screen, though. Sorry. I think.

**:** Yeah.

**:** It.

**:** Can you see?

**:** Yep, I can see it now. Perfect.

**:** Okay, so we have this.

**:** Let's just say. Okay, let's just say, like.

**:** Here, I'm in with the I configuration.

**:** Right?

**:** And now let's say here I'm in.

**:** Gallion capital within with the.

**:** Eye. I want to have that bar. So if I click on it back, if I click on with AI configuration, that will effectively just do this, and then I'll.

**:** Okay.

**:** That makes sense. Okay.

**:** So you out of the. The project folders. Okay.

**:** Yeah. So when I. But when I click up here, it's actually opening a whole new, like VS code workspace.

**:** Workplace.

**:** That is important. Okay, that's okay. So let's. Let's keep.

**:** When I. If I double click on sangalion Partners here.

**:** Yeah.

**:** Is the same.

**:** As if I go into folder.

**:** And then I.

**:** Do this.

**:** And then I'll see this.

**:** Right.

**:** So you can go back one at a time, though.

**:** Like, when you change workplaces, though, is that. That's okay with you, right?

**:** What do you mean one at a time?

**:** So you press. Do you press back? You go to the parent folder, and then it resets work place.

**:** Well, no, I think it should show, like, the whole.

**:** String.

**:** From whatever is set to the home folder location.

**:** Okay, so the string. So you don't want to set it to C. Right. You want to set it to, like, your home.

**:** Yeah. Unless. Yeah, like to. But it can be to, like, your root home folder.

**:** Like.

**:** If there is no.

**:** Like, if it's not even in your home folder.

**:** Okay.

**:** And then.

**:** Like, when you press home.

**:** Low-key what it should do is it should just show.

**:** Like, when you press the home button.

**:** It should show this. It should show.

**:** Like.

**:** Did show two folders. One that is, like, shared folders and one that is private folders, and they're both open and they each have, like, the sub folders underneath them.

**:** There's no changes to the home panel then, right? It's. It's.

**:** Wait, is there. What are the changes to the home panel again, then? Is it.

**:** I think.

**:** Like.

**:** How important do you think these changes are?

**:** The current system works? It makes sense in my head.

**:** But I'm not sure. Like, maybe Ian, this is his first. His first time Ian doing any of.

**:** That, like, VS code does have, like, a high learning curve. Like, I completely get it, too. But it's because, like, I've been using VS code for, like, three, four years. Like, I already know how it works. I'm not sure.

**:** Like, that's why I feel like I'm a terrible.

**:** I think it's.

**:** I think. I think it's great if you can.

**:** Like, what I just described.

**:** Yeah.

**:** If you can implement that, that's great to test.

**:** Yeah. Let's just.

**:** Let's not spend any more time on this because we have other features that, like, are a lot more pressing.

**:** No, I totally agree. Let's. Okay, so just to be clear, get the breadcrumbs then.

**:** Get the breadcrumbs in the Explorer.

**:** I'll play around with that. And I'm just gonna use the. The. The current native VS code Explorer. And then on top of that, I'll have the back button so that you can go to your parent folder.

**:** Does that sound good? Is that the two things?

**:** Yeah.

**:** Let's do that, then. Cool.

**:** Wait. What? Wait, what's the second one?

**:** So. Oh, so the first one's breadcrumbs. The second one, when you press back, it opens up pretty much the parent folders.

**:** And then you can see everything.

**:** Well, it's not, like, back. It's like when you press the.

**:** When, like, there'll be, like, a path, right? There'll be like this. There'll be an arrow. There'll be this. When you click on the item in the path.

**:** It opens that up in the Explorer, right?

**:** Is that.

**:** Yeah, it opens whatever folder you clicked on.

**:** Got it. Okay.

**:** Yeah, actually, so then.

**:** Wait, let me. Let me share my screen then. So I just want to clarify that.

**:** So where's Edison?

**:** I don't know.

**:** I think he's working.

**:** I texted his working in his room. He's working remote.

**:** Okay, well.

**:** I'm gonna ask if you can join because we need to, like.

**:** We can't miss the.

**:** End of recalls because we need to review where we stand with everything.

**:** I totally agree. This accountability thing is super important. Yes. I saw our last time. I was in the ER. That was. That was my.

**:** Here, let me. Let me share my screen quickly so we can. I can just quickly demonstrate it.

**:** Okay.

**:** So essentially, what do you mean is it shows the breadcrumbs like this in the native color. And then you just go back. It does like that. Is that what you mean?

**:** Let me see your screen.

**:** All right, you see it? So it's like, if I want to go back to the main folder, I just press this.

**:** And then it just shoots back to this.

**:** Yep.

**:** Perfect.

**:** Okay.

**:** But that, like, changes the actual VS code workspace you're in.

**:** It changes the actual VS workplace.

**:** Right? It does.

**:** Yeah.

**:** Go ahead. Yep. Okay. That makes even. That makes it even easier. Yeah. Okay, let's do it. Let's.

**:** I'm gonna have to do some manual coding there, but we should be able to figure it out. We should. We should be cool. All right.

**:** I'll.

**:** Get to it.

**:** Ian, and then let me.

**:** See if Addison.

**:** I texted him.

**:** Oh, you're detecting. Okay, we're good then.

**:** We'll wait, like, a few minutes. We'll wait three minutes, then we'll start. Ian's right here.

**:** Oh, sweet.

**:** We'll start it.

**:** Off.

**:** And we'll just review.

**:** Where we are with everything and where we need to get.

**:** Yeah, of course.

**:** I gotta ask my agent.

**:** To see what I did this week. I've been doing that all the time.

**:** Because it has connection to linear.

**:** Yes, connected to linear and GitHub.

**:** I've been doing that for everything. I've connected, like, my health data, all my, like, work data, everything to, like.

**:** The age and stuff.

**:** It's good for a weekly reflection. So you actually see if you're, like, slacked off the week, like, during the week or you actually pull through.

**:** Okay, I think we're all here now.

**:** Let's recap.

**:** This week and where we stand in our overall plan.

**:** So this week, it's on.

**:** So we're almost approaching March 30th.

**:** The things we wanted to get done.

**:** Were demos.

**:** Have prime broker meetings.

**:** Reach out via Scott and work. Do cool outreach.

**:** Finish VM automation.

**:** Finish improving security.

**:** Finish auto update.

**:** And automations for Mercator and product niceness.

**:** I think we've done.

**:** I think we have note taker on. Right. Yeah, that's good.

**:** We have.

**:** We got the demos done.

**:** Yet we had the first prime worker meeting, but we didn't have all of them.

**:** We will get.

**:** In as many as we can next week.

**:** Oh, yeah. Have you talked to Scott today or still Chan? I'll call him. Okay. Yeah, we also need to ask him how we should respond to or how we should reach out again to ubs.

**:** Yeah.

**:** Yeah.

**:** Scott's Network. He said that was, like, just prime Brokers.

**:** Yeah. And cold Outreach instead of that, I've just been.

**:** Working all the networks, really, which is, I think. Yeah. Which I think the best.

**:** Yeah. So.

**:** In terms of, like, and let me add our notes.

**:** For this week. Like 50 truly lead calls.

**:** Yeah.

**:** How many lead calls have we had so far?

**:** I would say there are, like seven situations where I feel like we could really sell.

**:** We've had a lot of calls.

**:** And those are ongoing.

**:** Yeah.

**:** So this is.

**:** March 27.

**:** Week and report.

**:** And what we.

**:** Were supposed to do.

**:** We were supposed to.

**:** Hit the demo is done.

**:** For meetings.

**:** What's the latest on Mac auto update, Edison?

**:** Now let's take a look at the linear.

**:** I sent you those documents right at sinners still waiting on me.

**:** Okay, good.

**:** For some reason, my linear is.

**:** Like, not showing a lot of the issues.

**:** Okay.

**:** So what we got done.

**:** Was.

**:** One.

**:** Okay, so what did we not really succeed at this week?

**:** We've not succeeded. We did not have.

**:** All the prime broker meetings as we wanted to. Yeah. In that one time broker meeting.

**:** It's not clear that it's going to lead to calls. Yeah.

**:** So one, I think 50 with probably over optimistic.

**:** We have not gotten auto update.

**:** Done.

**:** We started security, but it turns out that's going to be like a.

**:** Several week process with the compliance firm.

**:** Like a four week process.

**:** Skyler, has Marty had a chance to test out those new automations at all? I've. I showed them to him yesterday.

**:** Oh, sorry. Is it. Is echoing on my side?

**:** Okay, is it gonna. Yeah. So the automations.

**:** Are you talking about the VM automations?

**:** I don't know.

**:** I'm not sure. Edison, did we. Did we connect it to the back end yet?

**:** No, no, not the auto. I'm sorry, not the automations. I meant the.

**:** Oh, the skills.

**:** I meant the skills.

**:** He's using. I think he's using the YouTube one right now. The YouTube transcript, which is. It's a huge benefit to have that.

**:** We still have a couple to build.

**:** I think the. I just finished the research one today as well.

**:** And then we have to do, I think.

**:** Let me pull it up on the ear. It is. We have to do the.

**:** Oh, the patent searchability one.

**:** And then that's Envy SEC filing. So there's two more left.

**:** Those I'm trying to look at this stuff, but, yeah, no, he's. He's. I think he is using them.

**:** Okay.

**:** That's good.

**:** And then we just have to continue to just work with him.

**:** Yeah.

**:** For deploying.

**:** Actions.

**:** You know?

**:** We can do the.

**:** We could do.

**:** Okay, so, like, technically, the deadline for all this stuff is the 30th, and today is the 27th.

**:** So.

**:** Like.

**:** I will have. I think we will be able to ship the VM.

**:** By the 30th.

**:** I think we will be able to ship the Mercator skills.

**:** All right.

**:** Let's.

**:** I think we will be able to. And I think these are, like, Marty skills.

**:** Let's.

**:** And now count comparison skill.

**:** And.

**:** Oh, and like a model.

**:** The VM. Edison.

**:** I will.

**:** I will work on VM stuff.

**:** Today and all weekend.

**:** Just make sure all the context is there.

**:** And we should at least have security.

**:** On. We should have.

**:** Like, first steps.

**:** Security.

**:** Done. So I will send you guys, like, a. A checklist.

**:** It's a good question.

**:** I think, like, yes, I think we can do the API stuff by Monday. I could also try to rework that.

**:** For the API.

**:** I feel like I'm talking to an AI because it just because I speak and then it just responds in text.

**:** But.

**:** It doesn't mess up.

**:** It actually understands what I'm saying. It feels kind of like magic.

**:** Which is that fair?

**:** We make our chat bot just, like, have, like, a human on the back.

**:** End.

**:** And Indian, like, that's what they did in India, didn't they?

**:** Yeah.

**:** I think that makes sense.

**:** Great.

**:** I think we can have prime broker meeting scheduled.

**:** And I think that we can do.

**:** And I think this is reasonable. I mean, it's ambitious but reasonable. And then.

**:** We're from product side of things relatively on track.

**:** I think the one thing for us to consider is.

**:** How on track are we.

**:** On the.

**:** On the non-product side of the GTM side of things?

**:** I think honestly, to me, seven serious con. Would you say these are seven serious conversations that are now.

**:** I would say.

**:** Yes, they are all serious because then I would say, like, if we can get.

**:** Seven serious conversations each week for the next two weeks.

**:** That's where.

**:** 21 serious conversations, which it's not 50.

**:** But we're halfway to and very ambitious goal. Yeah.

**:** So, like, I say we keep it up.

**:** And it's not like. It's not ideal, but it's not terrible.

**:** Yeah.

**:** So you. You have seven serious calls this week already.

**:** Is that.

**:** Over this week and last week.

**:** S really good.

**:** Yeah.

**:** I mean, they're not like we didn't discuss them buying it.

**:** But these are calls where I left with, like, oh, they like it and want to talk again, and they explicitly said they want to talk again.

**:** Do you have, like, a set date and, like, time? Not the day. It's like the next meeting. Do you have that set up?

**:** No, that's good advice. I should do that.

**:** Yeah, that's actually. That's how we counted indicators.

**:** And, like, kpis. If you can get a next meeting, that's. That shows that that. That conversation was serious. It's like. Because action, you know, has a little bit more, like. Like. Like weight to it.

**:** But I don't know.

**:** It seems great already. Seven is already a lot. Like, that is. That's better than what I did with missionary, so that's awesome.

**:** Thank you.

**:** Okay. And then we have the next cycle.

**:** So the next cycle, our goals are.

**:** 50 serious conversations, set up terraform build initial.

**:** S.

**:** To your deploy test.

**:** System to deploy.

**:** Okay.

**:** So, yeah, basically.

**:** Our goal next week.

**:** Will be to practice deploying with AI.

**:** Or not next week.

**:** But in the coming two weeks.

**:** Our goal is to practice deploying with AI into a new.

**:** Like additional fund. And the fund we're going to deploy it into is the tiger sustainable investment group.

**:** Oh, nice. That'll be fun.

**:** So we're going to give them with AI.

**:** And we're going to practice, and we're going to see, like, how that deployment goes.

**:** So that is going to be our objective for April 15 product wise.

**:** And then the week after that or the, the two weeks after that, our goal is to.

**:** Like, do this for an actual another customer.

**:** I feel like, like when I say these things.

**:** The hesitation, I feel is like, I feel like our product's not ready.

**:** For deploying into a second customer in one month.

**:** And so what do we need to do?

**:** Of the second customer.

**:** Yeah.

**:** I mean, I think we start deployments and keep building while we're there.

**:** Like our compliance process or the funds.

**:** The cl.

**:** Ients.

**:** Our compliance process are the one, like, that would be required of us.

**:** Basically, what we're trying to do now is become like SOC2 compliant.

**:** And we're hoping this will.

**:** Alleviate a lot of the compliance concerns of the funds.

**:** That we're talking to.

**:** That process entails.

**:** It's like SOC2 compliance doesn't actually look at your product, really, which is kind of crazy.

**:** It just looks at your internal security, data security measures. So it's like, do all of us have two factor authentication on everything?

**:** Is all of our data being encrypted?

**:** In transit and at rest?

**:** Are we like, is there update server, like, secured?

**:** And is there.

**:** Only, like, one person with access to the update server and they have to approve all updates to the app?

**:** The keys that are in the app.

**:** That is not part, that would not be part of sock2 compliance.

**:** For us.

**:** But.

**:** Like, it might be against their own.

**:** Compliance procedures.

**:** It's like they, they might be.

**:** Like.

**:** Is, I mean, I'm almost completely sure they would not be chill with.

**:** Master key to all microsoft.

**:** Suite being in the VM.

**:** But basically.

**:** What the security people have told us is.

**:** Like.

**:** We have to reliably.

**:** I mean, we just have to reasonably take precautions.

**:** With those kind of things.

**:** But, like, there won't be a formal security review of art. What there will be is in four weeks, we will have a bunch of professionals try to hack into our system.

**:** I think that's what it is. We're having a pen. Like, it's called a penetration test. Yeah. Yeah.

**:** And so.

**:** And then if they do, they'll tell us what went wrong and we'll fix it.

**:** So that, that's like how we'll test those kind of things.

**:** So besides that, what. What parts of the products do you feel.

**:** Are not rated yet, Ben?

**:** I think to me, the, what feels the least ready is.

**:** Like.

**:** The skills and that we need to, like.

**:** We need to sit next to people at mercator using it. Like, you need to sit next to Marty while he's using it for his research.

**:** And observe where are his pain points.

**:** Like, what does he like? Where do we see him struggling?

**:** And then we need to, like, fix those.

**:** And we're waiting is now Jessica is making a new version of the model template.

**:** To make a whole new, like, or to modify our model skill.

**:** But, like, for example, I know.

**:** This model skill is very difficult to use.

**:** Like, excel all, like when you're using it, excel will get stuck because the terminal access to excel often, like, for makes excel get stuck, then you have to ask the AI to clear it.

**:** Like, I'm with the manual where they say you want to get people using it as quick as possible.

**:** I think we can do small pilots, we can do alpha deployments, we can do.

**:** You know, small trials.

**:** But I think we should just get into people's hands.

**:** At places. I, I completely agree. But what I'm saying is I want now for us to have, like, a, I want us to be watching people using it. Yes. And learning what we should improve based on that.

**:** I see.

**:** So I'm gonna. Marty asked me.

**:** To. To show me his. My. My current workflow, how I use it.

**:** Based on my knowledge. I spent, like, 30 or 40 hours on her app per week, which is kind of insane. So I use it for everything. But he wants to see how. How I'm doing it.

**:** And then I'll. Yeah, I think. Is there any way that we set up, like, some type of way to track with skills? Like, should we just have, like, a skill counter or something?

**:** That goes back into our side?

**:** You think that'll be it, like, a good solution to see what he uses?

**:** Skill counter.

**:** Like, you see, like, how many skills got activated? Like, if he actually triggers in his workflow.

**:** I think what we can do is we could add hooks.

**:** Okay.

**:** If, if we are going to do any kind of product monitoring stuff, let's use post hug.

**:** Well, how we would do product monitoring is like we would have a hook and we would have, like, a csv file in the shared folder.

**:** And every time this was used, you would add, like, an entry to that CSV file. Yep. Let's use post hog to do that.

**:** Post hog doesn't do that.

**:** At all.

**:** Well, postdoc is a third party mon, like, and mercator would not be okay with that.

**:** Probably.

**:** Would be.

**:** They don't want their data to leave.

**:** Mercator.

**:** I'm not sure whether that the postdoc jewels actually go to post hog.

**:** I'll talk to.

**:** So not a comment. Like, could we just look at their. Edison said, could we just look at their cloud conversations?

**:** Yes, that's a great idea. I think we should put that in the agenda for next week.

**:** That.

**:** Smart? I think she really smart.

**:** Yeah.

**:** So get blog chat history.

**:** For all team members.

**:** Then let's say.

**:** And we can also improve the skills that way.

**:** Like, what if they like, nah, I don't want you to see my.

**:** Because I, I mentioned this to Scott two days ago. I was like, oh, could I, like, get your chat history?

**:** To, like, improve this database skill? And he was.

**:** Like, he's like, oh, I'm not too worried about that.

**:** As in, like, no, we don't need to do that.

**:** But, like, we can probably get it.

**:** But this is. This is super helpful. I know g-stack does this, but, like, the meta learning from your conversations is actually a new thing that's happening now.

**:** Yeah, that needs to be a feature of.

**:** Our stealth.

**:** Yeah, definitely. It tells you, like, how you're prompting, how you're responding. Are you getting what you want?

**:** How you think to. How you approach stuff. It's very necessary.

**:** Yeah.

**:** So what are we going to need to deploy in a tsec?

**:** One, we need to figure out all the pieces.

**:** And make a list.

**:** Set up terraform.

**:** To deploy azure.

**:** Departments.

**:** And three deploy to, say.

**:** Five beta users.

**:** Okay.

**:** Does this sound good to you guys?

**:** Sounds like a comply.

**:** So until the 30th, we know what we're doing after the 30th.

**:** Let's.

**:** I can make this list.

**:** And set up terraform.

**:** Well, when you figure out how to break, break up these tasks.

**:** I still think we should have watched.

**:** Okay. There are post hog deployment options that share no data.

**:** How does it work?

**:** Self-hosted postdoc?

**:** It's open source.

**:** Oh, nice.

**:** Well, we can look into, I mean.

**:** Why what would be useful of that?

**:** So we don't have to build our own monitoring infrastructure so that we can get richer feedback.

**:** And what, what would we get?

**:** What does post all do? Basically, whatever type of usage monitoring you want to do.

**:** They have.

**:** Stuff for. Do they have for electron apps?

**:** Yeah.

**:** How does that work? Like, what will we see exactly?

**:** Well, you're above my pick right now.

**:** This is something that I just said and I can set up, though.

**:** Right?

**:** Kind of just.

**:** Yeah.

**:** It's like the next big. This is definitely. I mean, I think you might be more experienced as you're used to do product management things.

**:** But, you know.

**:** This.

**:** This should be helpful. Yeah.

**:** I think you would be useful.

**:** Let's ask, let's ask.

**:** Dave.

**:** I mean, it just seems.

**:** Better than building our own.

**:** Well, I mean, our own is getting their chats and watching them do things live.

**:** Just like screen recordings. No, just like literally sitting with them. If. If we are going to do any software stuff for monitoring post talk, if we are not.

**:** Yeah. And I think it makes sense to start with.

**:** The simplest way of doing it. I agree.

**:** The other thing is we, we need a dashboard.

**:** What do you need?

**:** Like, you know, why C says you need to have a dashboard that shows your progress? Yes, we do.

**:** Okay, sounds good.

**:** Any, any questions from anyone?

**:** Skyler, Anderson.

**:** I'm pretty clear on what I have to do. Yeah.

**:** Are we going to assign these things to every person, like individual people to do.

**:** Or.

**:** We, we probably should.

**:** Yeah, make a linear test, and we assign ourselves.

**:** It's probably fair, too.

**:** If you just copy that into linear and then say make to do tasks, and then we all sign, and then we'll see what's left over.

**:** It'll be a free for all.

**:** So one option is, I mean, I'm not, I'm just not sure how we break up the terraform stuff.

**:** Yeah.

**:** That's great. But I, I also want to know how it works.

**:** And be involved in that.

**:** Yeah.

**:** We can do it together.

**:** So either we do it together or you guys can start.

**:** Like, you guys can keep working on.

**:** The, like, refinement of these mercator skills and stuff.

**:** Over the course of the week.

**:** As I set that up.

**:** Okay.

**:** Cool.

**:** All right.

**:** Appreciate it, guys.

**:** Bye.

**:** But.

# Paragon Global Investments - Weekly General Meeting

**Date:** 2026-04-06


## Summary

### Gamma Scalping Strategy — Current State

- Back-tested gamma scalping on SPY (zero-DTE options), entering at market open, hedging every minute when net delta exceeds 15 shares
- Currently unprofitable but structurally informative — ~46 hedges/day, very high frequency
- Key finding: best days correlate with more hedges (underlying bouncing); worst days are directional moves
- QQQ outperforms SPY in back-test (less negative) — higher intraday realized volatility as expected
- Coinbase (COIN) showed profitability, but very limited tradeable days on zero-DTE
- Calls vs. puts: no meaningful difference — straddle confirmed as the right structure
- Directional bias (call-only) effectively replicates a straddle after delta hedging anyway

### Asset & Structure Decisions

- Moving away from SPY toward higher-realized-vol underlyings
- Assets to back-test next: QQQ, META, AMD, NVIDIA, MSTR, Coinbase
- Straddle preferred over strangle for now — directional bias can be added in a future iteration
- Zero-DTE entry/exit (open to noon) flagged as arbitrary — needs principled reasoning
- Weeklies (~7-day expiration) suggested as more active for gamma scalping- Entry signal idea: enter when IV is at a rolling low relative to recent history

### Strategy Refinements to Explore

- Screen assets historically for realized vol > implied vol — identify best candidates systematically
- Use qualitative event triggers (earnings, macro events) to time entry before volatility spikes
- Vary days-to-expiration in back-tests to find optimal expiry window
- Multiple-asset strategy (basket approach) likely the direction for the pitch

### Pitch & Timeline

- Target pitch date: mid-May (week of May 11 or May 18, before Memorial Day)
- Format: short slide deck + GitHub repo; no strict time limit (~5–10 min)
- Profitability not required — clarity of reasoning and what was learned matters most
- All quant TMs: send Forrest a 1–2 page written update within the next week
- Watch the education session recording if you missed it (sample pitch walkthrough)
- Keep GitHub repo current — do not discard code between semesters; build on existing infrastructure

### Sponsor / Tool Opportunity (Rafael + Skyler)

- Skyler’s YC-backed company builds AI tools for hedge funds; recently raised ~$1M from Bridgewater + $1M private, ~$500K from YC pending
- Key product: “Investment Decision Framework” — an AI that iteratively challenges investment theses, surfaces assumption gaps, and forces analysts to refine until the thesis is bulletproof
- Ingests 10-Ks and news automatically; pushes back on weak reasoning (e.g. “I want to buy Tesla because it’s cool”)- Presented to hedge funds 3 days ago — strong reception
- Rafael flagged this as potentially valuable for PGI’s value/fundamental teams
- Could also provide Bloomberg access + integrated workflow setup to PGI
- Potential for ~$1,000–$2,000 in platform credits for PGI

### Next Steps

- Skyler
- Run back-tests on META, AMD, NVIDIA, MSTR, COIN; share results in Slack before next meeting- Post performance PDFs to Slack channel- Explore script to use qualitative events (earnings, elections) as entry triggers- Try varying DTE (7-day, 30-day) in back-tests
- Rafael
- Set up group chat with Skyler, Thor, and Anant to discuss sponsorship/tool deal- Write message to Thor and Anant explaining Skyler’s AI platform
- All quant TMs
- Send Forrest 1–2 page strategy update within the next week- Submit GitHub usernames to Rafael to be added to the repo- Come to next meeting with new trade ideas or asset screening approaches
- All value TMs
- Theses should be outlined at a high level now; shift focus to real diligence- Use expert calls, equity research, and alternative sources to confirm or reject theses- Modeling is a last step — thesis quality drives the recommendation, not the model output
Chat with meeting transcript: https://notes.granola.ai/t/7bdbd280-b28c-4982-b05b-ad8e94da5ce2


---

## Transcript

**:** Recording in progress.

**:** What's up, guys?

**:** How's it going, man?

**:** I'm good.

**:** Just played a intense game of fortnite with my roommates.

**:** So my. My heart is still. Still pounding.

**:** How are you still? Anger weekend?

**:** Yeah, man. Weekend's been nothing much. I have some midterms, but otherwise that's it. Did as. Has the staffer reached out to you yet? Forever.

**:** Core.

**:** No, I haven't. I had someone reach out to me from u chicago who.

**:** Yeah, like, randomly. I didn't like.

**:** I didn't, like, reach out to him, and he was like, hey.

**:** Like, super sad to have you this summer. You round a chat.

**:** And I was like, yeah, is that, like, what yours was like?

**:** I think so. I have mine tomorrow, but some of the NYU guys are, like, getting in bounds from different staffers here kind of on a rolling basis.

**:** So I was just wondering if it's kicking up at other schools, too, because I have a friend in Northwestern who email me the same or text me the same thing, but, like, is our staffers, like, VPs or. So I. The guy that I got assigned to, he's.

**:** Like, he has to be early 40s or so, and I think he was working at locktail for, like, 12 years and then days on VA and transition to banking. So either he's like, has to be, like, director level, I would assume.

**:** Interesting.

**:** I I don't know, though. Like, definitely not a, like, normal transition. I think it'll be insane if he was an associate after skiing at, like, legal offer for 12 years or whatever. So. Yeah.

**:** We'll see. Yeah. Mine was a. It was an analyst, so it can't.

**:** Yeah.

**:** But that's interesting.

**:** Yeah. Let me know how the conversation is. I'm curious. Yeah. Yeah, I will. I've heard, like, everyone that I. I know who's had something like this has had a pretty good experience.

**:** So I don't know if, like, the guy that I'm talking to is supposed to be one of the staffers for all of us or whatever.

**:** But supposedly he's a chill.

**:** Dude. I'll let you know that.

**:** Yeah. Sweet. I assume you did all the, like, exams. Yeah, yeah, yeah. How'd you find those?

**:** Like, it was all right.

**:** I was a little shocked by, like, the video that one where they, like, that was. That was ridiculous. Yeah. What the hell?

**:** But I ended up just, like, doing it. I think it was fine. Yeah.

**:** Yeah. I'm not sure.

**:** Like.

**:** Yeah, I I don't even know how many of the kids are in class are actually to do it, but.

**:** Yeah, I I was also considering maybe not doing it, but one of my friends wants to travel for the week that they're doing the optional boot camp. So we were like, you know what? Let's all just, like, knock it out and fire ourselves up. But, yeah, no, it was fine.

**:** Yeah, that's a good. There's a few more synapses.

**:** All right, we won't. We won't.

**:** Throw out the whole meeting with Ator onboarding. I'm warning chatter. How's someone else doing? How's. How was your weekend?

**:** Yeah, doing great, math. You just kind of catching up with friends this weekend, so it was good.

**:** Nice. Sweet.

**:** Awesome. Well, I won't.

**:** Fort you guys to listen to me for way too long. Do you want to quickly share, like, where the value side should be in terms of their pitches and stuff for this coming, like, any tentative dates for what we might do or pitches? And then based on that, like, where. Where maybe everyone should be right now.

**:** Yeah. Can you hear me still?

**:** Yeah, I can hear you.

**:** I can't hear you anymore.

**:** We'll wait for him to come back.

**:** Leo and Forrest, any. Any share with quant?

**:** Sorry. My computer was actively crashing because we were talking.

**:** Yeah. No. So for. For dates, like, tentatively, I think the. The week starting either May 11th or May 18.

**:** So kind of trying to wrap up for Memorial Day would be ideal. Maybe both of those weeks, depending on what sequencing is like or if we need to take two weeks to go through both font and an icon.

**:** And then on the. The icon or not icon. Sorry.

**:** And then in terms of where you guys should be at on the value side, I mean, it sounds like everyone kind of has companies they're focusing on.

**:** I think hopefully should be digging in more so toward.

**:** You know, theses should be outlined at a high level, things that you guys are interested in looking at more deeply.

**:** And I think now for the next few weeks is really going to be more about real diligence and digging in deeper and exploring research as much as possible to actually confirm or reject whatever you guys are thinking at a high level about the business. So that's going to be involving looking at any export calls, Equity research should already be looked at as well. And any alternative sources you guys can find too. And in terms of like, you know, when you want to start modeling this ad or putting things into Excel or whatever, my thinking is always that that should be kind of a last step because your thesis should be what's driving any recommendation that you actually have. Like I know a lot of times, especially people who are first getting into pitching, which I'd imagine several of you guys are.

**:** You form a lot of confirmation bias and whatever you, your model says about if a company is undervalued or overvalued and that's all based on pretty arbitrary assumptions. Like realistically your model is just sense checking to make sure that the valuation that's currently existing is sensible.

**:** And your qualitative deviations on whatever consensus is or what's actually going to drive any stock movement in the future, not whatever your model says.

**:** So focus a lot on making sure that the actual reasoning is rock solid and makes sense and less so about, you know, just putting them all together that says, oh, 50% upside or whatever it is in your position.

**:** But yeah, and if anyone has questions about timelines or feel behind or at or anything like that, definitely feel free to reach out and we can talk about it and make a plan.

**:** Awesome. Yeah, I think that's a, that's a good strategy. Like just, just to echo that, I think that on the value side, we should be focusing on, like, once the theses are identified, like really going deep, trying to find data to back up your beliefs, trying to really challenge it with each other and, like, you know, I'd rather, I feel like a lot of the company overview industry overview, all that stuff can kind of be done, like, sooner to the date. Is this more standard? And if you really are deep in a thesis, it's not going to be hard to do a company overview. But I think, you know, in terms of, like, when we think about which we're going to want to invest in, like, the theses, the company overview is kind of like a scam and just, like, sense check. The theses are really going to be having three really well built out theses is, like, the best thing for any of these pitches.

**:** But.

**:** Yeah, Forrest, Leo, anything on the quant side you want to share before we break out?

**:** Yeah. Basically, at this point, everybody should have, like, they like their idea should be pretty much locked down.

**:** Either for some, like, specific trading strategy or like some sort of, like, optimized, like, allocation, like system. So, yeah, I think all TMS, if you could send me a one to two page update within the next week, that'd be really good. Just, I mean, I know where a lot of you guys are at because I like to stalk your channels a little bit. So on slack. So that's, I have, like, some idea, but, yeah, if you can just, like, send me a short update, that'd be good as well in terms of the pitch.

**:** I did, like, thing for education where I just, like, walked them through a sample pitch to sort of do expectations around that.

**:** So for people who were, like, not ever in education, you guys should watch that and have some sort of understanding of, like, what should be presented for your research.

**:** And also, yeah, just everybody should be just keeping up with their repo. I've already talked with some people about that, squared things away there. That's like the number one most additive thing because, like, before, like, the last couple semesters, I feel like we lowkey never, like, kept around code. That's very, very bad. We should not be, like, repeating code, like, from semester to semester. We should have, like, info that's already built out.

**:** And, like, we just want to add on top of that or, like, change it, fix it, whatever. But we don't want to throw everything away. So, like, that's pretty important.

**:** So, yeah, that's, like, pretty much it, though. Leo, anything else?

**:** Yeah, I think you just keep on track, settle down your ideas soon, I think within the next week would be good.

**:** I think we're, of course, I think we're good to pitch, like, mid May. I think that's a good timing.

**:** Yeah, that's good. Yeah.

**:** Yeah. So I guess we're just working towards that, starting from this meeting.

**:** Awesome.

**:** Sweet. And then remember also the, the fiscal AI stuff. Feel free to use that if it's helpful.

**:** And. Yeah. All right, I'll open up the rooms and, and get to the, the important stuff.

**:** See you guys.

**:** Hey, how are you guys?

**:** Hey, Nathan. I'm doing good. How are you?

**:** Good. Been pretty busy since the past two weeks, but.

**:** Yeah. Nice.

**:** Skyler, how about you?

**:** Yeah busy as well.

**:** Good to see you again Rafael.

**:** Yeah, you too. Yeah.

**:** I I'm actually, I'm actually not that busy anymore.

**:** I was really busy leading up to spring break, and I'm chilling until the finals, but still got to keep up with v6 and stuff, as always.

**:** But, yeah.

**:** How's everyone else doing?

**:** Thank you guys for showing up.

**:** Gurmer, how are you?

**:** Very busy.

**:** Like, actually very busy.

**:** Everyone's so busy.

**:** When do you guys think it's going to die down?

**:** Or it's just not.

**:** For me? I think another week, like, at least for the next one week on, like, insanely busy and then the finals, I think it's still a little better.

**:** Okay. Okay. That's good. Good to hear. Good to. Okay, well, let's get right to business then. So I did some research on my end on really understanding gamma scoping well. And also thinking of kind of the ideas that we talked about last meeting.

**:** So those were like picking a stock or not necessarily a stock, like an underlying asset to do this strategy on finding data.

**:** And, like, defining, like, the frequency of rebalancing when to enter, when to exit.

**:** The, the.

**:** Call or put or the option position and kind of bring ways to back test the strategy. So not, not everyone has stuff on their, like page. If you guys have stuff written somewhere else, then feel free to put it there because I want everyone to be able to kind of see what everyone's doing.

**:** So that we can, you know, like, yeah, share ideas.

**:** But kind of what I.

**:** So I have kind of just, like, notes on, like, how do you have a scalping works?

**:** And then.

**:** For the, for the strategy, what I thought we should do is, so when we're gamma scalping, we're betting that the ex, the.

**:** Realized volatility is higher than the implied volatility, because that's the only way that we can, like, do the gamma scalping. Right. Because, like, the, the underlying has to move down for us to, like, buy the underlying or has to move up. So we sell the lines, buy low, sell highs. It's very intuitive. And if it doesn't go up or down like that, then we can't do the gana scalping and we're just losing the theta, right, which is the Greek with respect to time.

**:** Because if you, when you have the option, you have the intrinsic value, which is like what it would be worth if it was expiring right now and you have the time value, the time value is more if you have like a higher plan volatility. But over time, as the time to expire goes down, then you lose out on that extrinsic value, the time value. So that's the date of the case. So that's how long term option positions lose money. And then we want to try to balance that out with gamma scalping.

**:** Okay. Hopefully that makes sense. An asset that I thought was good to, to do it on was we had talked about the S&P last time. I think the nasdaq would be better.

**:** Because it's a lot of tech stocks. It's more volatile than the S&P. And realistically, we, we want to be able to, again, a scalp on, like more than like one 1.5 deviation.

**:** And NASDAQ, I think is more likely to have that more often than the S&P. But then another idea I also had in terms of like calculating the frequency would be to.

**:** Like.

**:** Like determine that percentage, right?

**:** We're going to buy if it goes down like 2% from previous rebounding. We're going to sell if it goes up 2% from the previous rebalancing. But that 2% is not through 2%. We can see how many times in the past, like year that actually happens.

**:** And then if we want to rebalance like every day, we divide that by 365.

**:** Yeah, something like that is, is, is, is what I thought. I don't know if that makes sense.

**:** And, oh, also another reason to do the NASDAQ. I think it's good to have something liquid because then the trading costs will be lower because that's also an important thing when you're getting, when you're gamma scalping, you're, you're doing a lot of, well, I don't know how many positions we're going to be doing.

**:** But if we were to be doing a lot, like higher frequency trading, doing a lot of trades and cures a lot of costs. So we want something that's liquid that we can easily trade. And then I, I talked to Forrest a little bit.

**:** About data. And he said that alpaca is probably our best bet. Skyler, I see you nodding your head.

**:** Yeah, I did a I did a back test for gamma scalp beyond zero DT options I can show it to you in a bit.

**:** Oh, amazing. Okay, I'll definitely show this.

**:** But yeah definitely the move.

**:** Okay.

**:** Amazing. Yeah, I totally agree. I don't know exactly how it works, but if you can illuminate us, that'd be amazing. Okay, great. And, yeah, that's, that's kind of everything that I have. Forrest has some infrastructure already built on how on using dial packet data. I'm still trying to get it from him.

**:** But Skyler, or if, if you have things to share, please, please do. Or if anyone has any ideas that they came up with over the week.

**:** Please share as well.

**:** But, Skyler, feel free.

**:** Yeah can I share my screen?

**:** Yes. I'm going to give you. Oh, wait. Can you share?

**:** I can't share it right now.

**:** I'm going to text Matthew.

**:** Yesterday I didn't know about the document I saw the GitHub so I here let me push my code to GitHub right now actually.

**:** Oh, nice. Okay. Oh, yeah, everyone, if you haven't already sent me your, your GitHub username, please send it to me and I'll add you to the repository.

**:** And you want to just push domain is that is that cool with you?

**:** Yeah, we just have one Branch.

**:** Okay.

**:** Sweet.

**:** Push to. No, push to your, to your specific folder.

**:** Got it I pushed my specific photo.

**:** What's this like extremely unprofitable this right now but well yeah because I haven't optimized anything yet.

**:** Really?

**:** But it's also trading pretty high frequencies doing around I think 46 hedges per day so that's a lot.

**:** Oh.

**:** Yeah, that is, that is a lot.

**:** Let me know if I want to share it.

**:** Okay. I, I texted Matthew. We'll see.

**:** If he responds.

**:** But what, what, what, what did you do in this back test? Was it like what asset did you do or, or how did you go about choosing it?

**:** Spiders the spiders and then it's.

**:** Every let me just read this.

**:** Spiders?

**:** Yeah SPY.

**:** Oh, okay.

**:** It's should be entry right on.

**:** The market open.

**:** You calculate portfolio Delta every minute you buy and sell SBI stock every time Delta the net Delta goes above 15 shares.

**:** Let's see it works really well in profitable days most of the days are not.

**:** I guess volatile enough again this is only like a one day trade so this is extremely aggressive.

**:** I think you should be able to share screen.

**:** Now.

**:** Got it okay sweet perfect.

**:** Let's.

**:** See.

**:** Okay.

**:** Yeah I need to get access to it give me one sec.

**:** Okay.

**:** Let me try again.

**:** Do you see it by any chance?

**:** Yes.

**:** Perfect so it is.

**:** So these were my I guess starting points I only did this I mean to be fair I only let it run for a bit so I haven't I haven't optimized anything yet.

**:** So it's definitely is losing money now but that's.

**:** You know this is just a starting point.

**:** So I think if you poked her out I started filtering out what caused this part of is load term days that don't have.

**:** Let's see where did I.

**:** Yeah so if you look at this one the best days happen when there was more hedges so actually the more hedges you do the better and that makes kind of sense you kind of want the the the underline to be just bouncing around a bit and then you buy and sell because you're pretty much buying low or selling high that's pretty much what you're doing.

**:** So you want you want days that that move very rapidly the worst days are when it moves in one direction.

**:** What this also means is that maybe.

**:** Like we should most likely cap the straddle either either we do okay so there's there's two ways to kind of go around this is that we don't do a straddle and we go into strangles instead so maybe like a 20 Delta strangle so it has more has less like I guess curvature.

**:** I'm not exactly sure though this is again this is just pretty limited results.

**:** I'm not exactly sure how.

**:** Let's see yeah so low volume that's pretty much this is this is you know in a nutshell.

**:** Yeah. Yeah. I mean, yeah, it makes sense. It's, it's what the theory says, too. If it's.

**:** Yeah.

**:** Realize volatility is lower than you lose money.

**:** Yeah the only reason why I did it on zero DT is because I wanted to see how rigorous the the data was and it seems like it is quite rigorous it's a packar API has enough data.

**:** To back test.

**:** For definitely for the spiders I don't know for anything else.

**:** I only trade the spiders though so I'm not exactly sure how.

**:** Okay.

**:** Better.

**:** I wonder if there's another underlying that would have a higher realized volatility because that's, that's really the thing that's killing us now.

**:** Right.

**:** We can try let's try this on.

**:** What was it the QQQ.

**:** I think so. Yeah.

**:** Yeah let's try this on QQQ.

**:** Same strategy as what is this one.

**:** I don't know if you could have Clyde directly in the s code. It's kind of cool.

**:** Oh this is this is my yeah this is just collab with MVS code this is the software we use for I work for this hedge fund so this is the same one.

**:** We kind of employ.

**:** Gotcha.

**:** That's cool.

**:** But yeah I mean this will give it a second and we'll figure out the results but yeah I didn't want to take like the floor from YouTube loan rallies it's kind of working on.

**:** Okay.

**:** Not at all. That's awesome.

**:** I, I would rather you guys speak more than me, so. No, that's great. But if anyone else wants to share while, while this is running, what they kind of got from this week.

**:** Yeah.

**:** Then that'd be great.

**:** Oh, you can go first.

**:** All right. Thank you. No, I didn't have too much to update. I wasn't there.

**:** Past two weeks, but kind of caught up kind of understanding how the scalping works.

**:** Pretty, pretty neat topic.

**:** Just in general. Yeah. I was wondering about.

**:** Using alpacas.

**:** Like, how is that?

**:** Like my previous pod, we use wrds. So that has a wartin like they have data, like institutional grade.

**:** Like data sets, stuff like that.

**:** Is there a reason to use, like, alpacas over that?

**:** So words or is that people say words?

**:** Yeah. Okay.

**:** That's, that's like Excel based data, correct?

**:** Yeah. Yeah. So, like, queries and stuff together.

**:** So I, I actually talked to Forrest about this. I was like, oh, isn't it easier to, like, get, like, celebr based, like, data? And then he basically said, like, oh, like, I guess, but that's not really, like, as rigorous as like, like hedge funds Quant firms do, because this API, it has, like, a lot more data as I continue, well, like more high frequency data that you can, you can basically get better information from, from an API like that. And it also gets us used to interacting with apis. I mean, I've never used an API before, so it's just an extra layer of, like, learning that I think is good. Cool. And are you guys, like, set on, like, using, like.

**:** SPY, like.

**:** No, I mean, we're, we're going to see now how QQQ fares. But if you have another idea, what, what, what were you thinking? Yeah, I wrote a little bit.

**:** I think what you said about liquidity being high is kind of important if it's too high.

**:** Like, it's too many transaction costs, but maybe, like crypto related assets could be nice.

**:** Obviously, they have a huge changes in, like, small periods of time. That could be nice for gamma scalping.

**:** Like, but I'm pretty sure the implied volatility is already quite high there, and I'm not sure how much data there is on options.

**:** There, but we could take a look at that. I might give it a try.

**:** Which Bitcoin options is it it's which exchanges are called again I forgot.

**:** Coin option data exchanges let me figure that out we can just run it right now.

**:** Nice.

**:** Yeah. You wrote here mstr probably.

**:** Solid.

**:** I don't know much about how the cryptos work, but, I mean, we can just treat, like, not like Bitcoin itself.

**:** Just like stocks tied to crypto. That'd probably be a better idea.

**:** Save more info.

**:** How does that work? Stocks tied to C, just like maybe like trading like coin, like certain stocks under that basket under them.

**:** E. Oh, like companies that are based on. Okay. Yeah. So it's like more volatile.

**:** But.

**:** Not interesting.

**:** Yeah. Okay. This is an idea I was thrown out there.

**:** Let's test it out I kind of like it let's do it.

**:** What, what company? I think you, you start to say coinbase. Yeah. Coinbase and mstr pretty. Pretty solid.

**:** Okay let's try it.

**:** Oh, those are the companies. Yeah. Yes.

**:** Mrt is that what it is.

**:** MSTR. Yeah.

**:** MSTR and then coinbase okay we can run we can run it on that right now.

**:** Too.

**:** Something else I was thinking too.

**:** Since Skyler sometimes, like when the volatility was low or when the realized volatility was low, it wasn't making money. What if we.

**:** Instead of just holding the, or I not exactly sure what your code is doing, but what I think it's doing is it's holding the option for a long period of time. And Gama stopping the entire way. What if we try to buy the option?

**:** Yeah.

**:** At a point right before realize volatility is going to increase?

**:** When would that.

**:** And then we exit.

**:** So when will we know when implied volatility will increase.

**:** So that's that. That's the question. Right. I guess you could look at when there's going to be earnings reports.

**:** Or mass or like big elections.

**:** Like quality qualitative things, which would be hard to, like, put into code.

**:** But you see what I mean?

**:** Okay so any but then if it moves in one direction that's kind of the issue that we saw with this when when the.

**:** It only works when it bounces back and forth it doesn't work even if it's volatile if it goes in one direction it doesn't necessarily capture.

**:** Like you end up getting flattened out.

**:** Too that's it's not you're assuming a straddle am I assuming correctly you're putting down a straddle or are you putting down just one on one sided trade?

**:** That's true.

**:** That.

**:** I, I wasn't really thinking of which exactly option we were going to do. But do you think shadow would be best? Because travel would work if it went in both direction or the scalping wouldn't work, but the option would make money.

**:** Maybe.

**:** Yeah.

**:** So far I've been putting on stratos I don't know.

**:** Then.

**:** I haven't directional bet on I'm not sure if that influences the I mean we can test it out like if we let's say because there's a natural bias in the SBI6 go up we can put a call down and see how that plays out I'm not a not exactly let's test that on right now yeah sby.

**:** That's true.

**:** But only use cause instead.

**:** Wait, what, what's the directional thing?

**:** Like, can you clarify exactly? Because aren't we, isn't it like just looking at the delta anyway?

**:** So if you have a straddle, how and just having a call or put, like, influence it or you're just, so you're saying, like, it's moving, it wouldn't.

**:** No that actually you're right actually it only half the trade it will make.

**:** Because you will have what 50 Delta if you buy at the money and then you buy negative 50 SPY and then it's going to just yeah it ends up just being a straddle you're not going to have okay the only way that this film will make more money is if somehow call volatility is different than put volatility but I'm not sure how that that's a different.

**:** Yeah.

**:** Isolate the type of thing we use. Like, if we isolate travel, you can try other.

**:** Other things.

**:** Like, I'm just not sure if, like, using a call or put would be like an informed.

**:** Like, thing here.

**:** Yeah I don't know I'm not sure.

**:** I mean, because I know, I don't know how exactly.

**:** Who can ask that too I mean.

**:** The safest thing we could do is do the straddle because then we're not actually betting on if it's going up or down. And that could be like something that we can add on later or in a future pitch, like actually adding a bias of where this going to go up or down.

**:** Anyone else want to throw some trading ideas we can just test we could just run it I'm.

**:** Like.

**:** Yeah.

**:** Whatever this is whatever this setup is.

**:** How many do I have running right now?

**:** I have four right now but it's fine.

**:** It's so cool.

**:** Okay.

**:** Does anyone else have any ideas?

**:** Okay actually so I got yeah sweet we can run on Bitcoin right now too does it have.

**:** This is nice.

**:** Historic intraday.

**:** I got to learn how to use cloud like this. It's really cool.

**:** Now this is like.

**:** This costs so much now.

**:** Really? Oh, do you have the, like, full version?

**:** Yeah I mean the company subsidized but last week I mean I think last month we spent 10 10 000 like I spent 5,000 on this so it's crazy.

**:** Oh, wow.

**:** You pay, like, based on how much you use it.

**:** But.

**:** Yeah yeah it's API so like the more you use it obviously like running like five of these is probably going to take a little bit but it's it's fine like they're paying for it.

**:** Okay. Nice. I mean, if it's okay.

**:** I just got the, the pro today because I was on chat GPT, like a dinosaur for this. So now I have the, I have the pro.

**:** That's a good move actually yeah Pro is pretty good.

**:** Yeah.

**:** I'm on the 20x Max plan now but it's.

**:** It's been all right actually it's been all right I feel like the Enterprise AI is a bit better.

**:** But you know it's you just make do.

**:** What is it? What is it telling you?

**:** It still finishing up so we got.

**:** All these running simultaneously now.

**:** Okay.

**:** Nice.

**:** What do you guys think would be while we're ready for this to run? What do you guys think would be good?

**:** Items to be doing for, for next week?

**:** You guys think should kind of be the plan?

**:** To get closer to having a pitch ready?

**:** When is our pitched again?

**:** So probably mid May. So we have like five or so weeks.

**:** And how profitable does this strategy have to be.

**:** Honestly, it doesn't have to be profit.

**:** Able.

**:** It, like, it's, it's great if it is, but what they're looking for is that, like, we learned something.

**:** And it's not really a big deal. And I don't even know if they have the means to implement something, even if it's super profitable.

**:** Well, manage this coming up with something cool.

**:** Like being able to explain it.

**:** Because I mean these are kind of tricky too huh.

**:** So how many how many minutes do we have to explain this?

**:** That's a good question. I can ask the specifics of the pitch. I think last time, I don't think they really had a time limit. Like, you could talk for, like, five or 10 minutes and just chill.

**:** But it doesn't have to be, like, super long. It's not like a 30 minute presentation.

**:** I guess the, the main, like, deliverables would be like a simple slides.

**:** Cool.

**:** Yeah.

**:** And the repository.

**:** The code in there.

**:** I'm actually going to look at what you wrote. And for everyone else.

**:** Okay.

**:** Let me ask this, actually, who here doesn't have any experience with, like, git version control type stuff.

**:** Feel free to say, because I didn't Forrest explained to me how this works.

**:** So he kind of got me with, but I can kind of go through how it works.

**:** If no one doesn't know.

**:** Seems like you guys have a little bit of experience, but that was for a long time ago, so I need a little refresher. Okay. Nice. Yeah, me too. I had some for, like, from, like, high school. I did, like, robotics, and we, like, used it.

**:** Didn't know your robotics guy rava.

**:** Yeah.

**:** I did. I did FTC.

**:** Oh wow that's nice.

**:** Yeah.

**:** So we used some, some GitHub, but it was a long time ago. So, Annie, the way it works, are, were you able to access the, the repository?

**:** Yes.

**:** Okay.

**:** So the, the main instructions are in the readme.

**:** So, like, look at the onboarding.

**:** Section for the first time that you kind of enter the repository. Do you know some unix.

**:** Have you learned unix?

**:** In one of your CS classes?

**:** No.

**:** I think, I think just Yale teaches Eunice in RCS. Like our, our interest. Yes class has, like, part where we learn unix, and I think it's really useful. But that's okay. The, the two, like, main commands that you have to know, Unix is like the language that you use to interact in the terminal.

**:** So you should know how do you CD really well at LS? I mean, unless you just type in ls and you see, like, what's in the folder that you're, that you're in. And CD is to, like, go into something deeper into the folders.

**:** So, yeah, it's basically just try to follow the instructions. If you get stuck, you can send me a message. ChatGPT helped me a lot.

**:** Actually, to make sure that I didn't do anything stupid because it's really easy to, like, do something that kind of, like, breaks the repo. But don't worry about that. If you break the repo, it's okay. It's not.

**:** Like a huge deal.

**:** But if you, like, try to go through the instructions, I try to make it as detailed as possible.

**:** It's just the main thing.

**:** Is to stay in your folder. Like, I have a folder. Like, if you click on Analyst Dash folders, there's like one for each person and stay in that folder. That's how Forrest told me to do it. So we're just going to copy what he does.

**:** And.

**:** Yeah.

**:** I think I might have broke the API call limit so it's going to take a long time.

**:** It's going to take a little.

**:** Okay.

**:** I think it's should be 5,000 per minute but we've made it probably like 10,000 already so.

**:** We'll just have to wait a little longer but yeah I don't know I could just I could just tell you guys the results afterwards it's not not hard I'll just give you D file.

**:** Okay.

**:** That sounds good.

**:** Okay. Yeah. Try to get us the results by next meeting because. Yeah, this probably going to take a while.

**:** Yeah semi-trade ideas I'll you know just one line like it's just a couple lines of code.

**:** And honestly Claude so it's pretty.

**:** Yeah.

**:** Yeah.

**:** No cloud is amazing. This is really, really cool. I was thinking that we're going to have to, like, manually code this stuff.

**:** Oh yeah no one manually goes anywhere that's.

**:** Like, have, like.

**:** Yeah. No. Or at least, like, prompt an AI and then, like, paste it in. That's what I, that's what I usually do. But no, you can just have it do it directly. That's, that's, that's really nice. It's called, it's nice that you have experience with this. This is super helpful.

**:** But yeah. Okay. So for, for next time, everyone try to come up with some more trade ideas. And once we find something that is profitable, then we. Yeah, we stick with that and we, and we pitch that also try to, like, instead of just throwing out trade ideas, you can also throw out an idea that we can use to find a profitable trading idea, if that makes sense, like finding, like looking at a lot of different assets and see which ones usually have higher realized volatility than implied volatility. I think that would be something that's really cool. Actually, can we get someone to do that? Because I like the idea. What, what do you guys think of that?

**:** Does it make sense what I said?

**:** So.

**:** Did I have a question on what I just said?

**:** So you just screen assets for historic volatility versus implied.

**:** Exactly.

**:** Okay.

**:** All right.

**:** I think that would be something interesting to look at.

**:** To choose.

**:** An.

**:** That'd be cool.

**:** Added in one of the nice.

**:** Yeah.

**:** That's from one of the windows.

**:** Awesome.

**:** Cool.

**:** QQ.

**:** Oh, is that, is that cluey?

**:** Which one.

**:** This.

**:** Because that just.

**:** Oh, wait.

**:** Oh, no.

**:** Is just.

**:** No, because you, you, you like, because isn't clearly the one that, like, records what people are seeing in the meeting.

**:** Yeah this is technically legal I'm so sorry you guys well actually everyone consented to the meat already initially so it's fine.

**:** And then.

**:** But Granola is like way faster for how you do this for all my classes you get straight on you just ask what was the last idea because I was kind of daydreaming my bad would I fail.

**:** Give a. It's fine. It's really cool.

**:** No, no, that's awesome.

**:** And then yeah knew exactly what it was and I just paste it in.

**:** Yeah, yeah, yeah. No, no worries at all, man. Use all the AI tools you want. That's really cool.

**:** So.

**:** You're right QQQ outperforms it but like it's still negative but yeah okay.

**:** Okay. But it was bad in this way.

**:** A little bit better yeah.

**:** At least not as negative I mean.

**:** So it is structurally better you're right so because that's how intraday realized volatility so okay we do have to then in that sense we just got to find the most.

**:** Yeah.

**:** High is implied volatility stocks so we're just going to search I'll search white finance for that right now that's what it's doing.

**:** It.

**:** I wish I was connected to the bloomberg this this this software I honestly we can if you want I can I can probably get a deal from the from my company and then we can give you the software.

**:** But it's.

**:** To use bloomberg.

**:** Orgies Bloomberg and also like this the setup so that you can get everything connected and just in one united piece like you know the workflow is like there you can just run and test ideas anytime you want.

**:** Reliably too.

**:** So yeah I mean we can definitely work out some type of deal I'm pretty sure I can get this into your guys hands.

**:** Yeah, I'm. Yeah. Amazing. If you think that would be, that would be helpful for us, for sure. Wait. You mean like for, for all of PGI?

**:** Yeah I mean.

**:** Guess I could I didn't think of that I think it was just this group but yeah no we could probably do it's both for fundamental investing initially.

**:** I've kind of figured out I could do quantitative investing just by playing around with it too much.

**:** That's okay. No, that, that, that would be good. Actually, I'm because another role that I have in, in PGI is being the leader for sponsors.

**:** And that's basically what I do. I like reach out to random companies and ask them.

**:** Okay.

**:** Wait.

**:** We can we can get you even credits for this we can probably get around a thousand or two thousand credits.

**:** Yeah we could talk after rafa we can might work on something yeah.

**:** Cool.

**:** Let me send you the listen let me send you guys the report.

**:** Into into is this is this is slack is that right.

**:** Let me just.

**:** For the current strategy, like, what's all? When do we enter?

**:** Like, is there an entry signal or something? Or we.

**:** Enter start of the day which is also quite a bold move.

**:** Just.

**:** Like like literally when the when the day starts like 9 30 1 a.m.

**:** That's what it's.

**:** That's right anyone have a better starting time idea because this is a this is so rudimentary like this is.

**:** You can probably just do in the.

**:** Like the implied volatility lower.

**:** I mean, like, just 30 thought out. Like, obviously you could probably have, like, a rolling volatility thing where you calculate, like, oh, the past month, these are the IVs. And then there's, like, the median or something like that, some metric. And then if it's, like, at all time low, you just enter.

**:** Or, like, if it's like.

**:** Yeah.

**:** Well that's the thing too I'm also doing it just on zero dts what's the ideal days to expiration machine?

**:** Obviously.

**:** You're saying, like, a percentage.

**:** Well I don't know we've been entering on the day and then closing on the day.

**:** I mean, you can, you can enter when, like the, just the volatility, implied volatility is a little bit low.

**:** Like.

**:** But then how big should our expiration be.

**:** Right.

**:** Should we.

**:** Maybe a couple hours.

**:** I mean, it depends on what you're trading.

**:** Yeah that's what I'm if SP wise I know you can definitely.

**:** Yeah.

**:** You can just, like, ask the back testers like, oh, try different, like, cutoff times. It's probably gonna cook this.

**:** Yeah because I did it for like MS okay coinbase was profitable.

**:** But that's because there's only a couple.

**:** There's only very few days you can trade it and we just trade on zero dts.

**:** Where are DTS?

**:** Day two expiration.

**:** Oh, it's, it's low DT.

**:** Is it low based expiration?

**:** Yeah right now we're only doing zeros we can do we can do we should be doing like higher ups like seven days expiration or 30 days expiration what we found quantum is the like they usually play around the weekly ones because those are one of the most action happens.

**:** Yeah.

**:** But I'm not sure.

**:** Because zero, you don't really get to gamma scalp that much.

**:** No no no it's basically like most of the and you get the crazy amount of data theta decay at the end.

**:** So honestly in that case we should be getting out of trades around.

**:** Like before noon like it should be nine aims at noon it'll be like a three hour trade if we really wanted to do it.

**:** But yeah let me sorry I got distracted let me get the report to you guys sorry about that.

**:** I'm addingur and pang.

**:** To the repo.

**:** There you go.

**:** All right.

**:** Let's see.

**:** Okay no meaningful difference between calls and puts so they're the same exact thing pretty much.

**:** Yeah looks exactly the same so you I think you're right maybe you're right, Ethan there was.

**:** See what made a slightly more money.

**:** I lost less money oh it was interesting okay yeah that's pretty much negligible it seems like they're doing around the same thing.

**:** Perfect okay.

**:** All right.

**:** And then there are a couple of these so we could try these we can try these assets all of these assets have good screenshot.

**:** Guys.

**:** That's interesting. That coinbase was there.

**:** Yeah that's a great guess, Nathan like guesses.

**:** Which is ready.

**:** Yeah.

**:** That's awesome.

**:** So maybe maybe we just trade these guys like try meta AMD nvidia we should just run four or five backtests on these right now actually.

**:** And just let it happen but yeah I don't know yeah we can definitely do this next time too I probably have to get going soon.

**:** Yeah. Okay.

**:** So you guys think a strategy with multiple assets would be the way to go.

**:** Let's do it yeah.

**:** Okay.

**:** Cool.

**:** Nice.

**:** All right.

**:** So are we still gonna do enter.

**:** On the day on in the beginning of the day and then exit at noon?

**:** I don't think that's ideal.

**:** Right? Wait, maybe ask it if there's a way to see if there's, like.

**:** A way to use the alpaca to find out when the, like, trigger points or high volatility points.

**:** Like earnings calls, political events.

**:** And try to trade before that.

**:** Or after that.

**:** To make prof.

**:** Okay so we can also have some type of script to.

**:** It.

**:** Based on use use qualitative events to determine when.

**:** Rd is.

**:** Spik.

**:** Ing.

**:** Okay.

**:** Yeah, no, that's cool.

**:** I think we can, we can end. I think this has actually been really productive. We got a lot of good information from the 50 clad prompts.

**:** But, yeah, no, I think for, for next time, as we keep, just keep thinking about different ways that we can, that we can implement this strategy and send them in slack.

**:** So that Skyler can put it into his crazy setup and see if it works.

**:** And then next week, it would be good to, like, have kind of something that we really like.

**:** Or at the most two weeks from now.

**:** And also.

**:** Wait, actually, let me see something.

**:** Quick.

**:** Actually, nothing.

**:** So, yeah, try to come up with more ideas. And once we have something that's profitable, and that makes sense because we don't want to kind of have some, like, arbitrary things in our strategy.

**:** Like starting the position at the beginning of the day.

**:** Exiting at noon.

**:** I think that's something that's kind of arbitrary, and it's not something that we reasoned about. I think we want to reason about as many aspects in the strategy as possible.

**:** So I think that's the main thing.

**:** That, that I want to kind of.

**:** Iron out is, like, when to come in and come out and how many times to rebalance.

**:** So.

**:** Yeah.

**:** That's, that's it for me.

**:** Anything else from you guys?

**:** Anthony, you stay behind a little bit to talk about the sponsor stuff.

**:** Yeah I can stay a bit after we can.

**:** Okay.

**:** We can figure out something.

**:** Yeah just in the performance PDFs into into slack so you can see all the results it's actually pretty neat document so yeah go for.

**:** All right.

**:** Awesome.

**:** Okay.

**:** I'll take a look after. That's cool.

**:** Yeah. And guys, feel free to take a look at this.

**:** It's awesome.

**:** Okay.

**:** So, yeah.

**:** I'll see you all next week.

**:** Guys.

**:** Yeah so what is what is PGI do for sponsors this is I didn't know that thanks for letting me know.

**:** So, yeah, it's, it's really cool. We, we should have you on the team, honestly. So it's, have you, have you heard of thor.

**:** Thor no I don't.

**:** He's, he's a member. He some, usually he's on the calls. I don't think he was on today. He's the, like, kind of the leader of the sponsors. He's been doing it for a while, and he recruited me and this other guy.

**:** Anant, to be co-head of sponsors now. Then I guess the logic is going to take it over once he decides not to do it anymore. And what we do is we reach out to.

**:** Like, smaller middle Market buy side firms that would maybe give us money.

**:** For our portfolio. Or more realistically give us access to whatever service they have.

**:** So, like the, the AI, the, I keep forgetting fiscal, fiscal AI that Matthew keeps talking about that's, we, we got it through one of our sponsors. What, what hedge fund do you work at?

**:** Know.

**:** So it's a head function at Princeton it's small 300 million people but I work for a yc company that is creating tools for hedge funds so I work under that so I'm like I'm like a branch of a branch.

**:** But.

**:** Is creating what of hash ones?

**:** You said?

**:** Creating AI tools.

**:** We create tools for like hedge funds to use in order to enhance the workflow process we turn.

**:** The.

**:** Tools like AI tools.

**:** How tools.

**:** Yeah my bad sorry.

**:** Sorry.

**:** Yes. No, no, it's okay. That's my bad. Okay.

**:** Interesting. Cool.

**:** Our company's got AI I'll just give you the link let's see.

**:** Yeah.

**:** I mean we're small we just we rose.

**:** We just Rose I'm just a found engineer there so I don't.

**:** But we oh I did this into everyone my bad.

**:** It is another guy name was on the call anymore though except us but it's we just raised around 1 million from Bridgewater and then another 1 million from private investors so you know we're getting another I think 500k from YC so it's it's good like we have some traction going on.

**:** But yeah.

**:** Some really good traction.

**:** It's we can we could work out something.

**:** Honestly you guys might be the more the better target audience to kind of work the platform.

**:** Tell us the bugs and then we could definitely work something out especially the fact that like you could do so much of the coding and so much of the analyst like analysis and this actually was both for fundamental trading do you do you do you do any fundamental training yourself Rafael.

**:** Or.

**:** No, honestly, I would, but I'm not really legally allowed to because my dad works out of hedge fund.

**:** Got it got it.

**:** But, yeah, it's a shame.

**:** That's fine my my dad was just a banker too so low-key he wanted me to be more quantitative but maybe now with this little AI push it may have not been the best idea but who knows?

**:** Oh, no, I think it's, it's still really, really viable.

**:** Definitely.

**:** Yeah so how does it work? How do how do we I guess sponsor PG how does that process kind of look like?

**:** Yeah.

**:** Honestly, Thor knows more about the nitty-gritty of it. Are you, are you the one who kind of handles Outreach or do you have someone who does that, or is it like a really small team? And kind of everyone does a little bit of everything.

**:** Okay.

**:** Everyone does a little bit of everything I can be honest cuz I'm closer to you guys.

**:** Okay.

**:** Low-key I could probably take the role in.

**:** Yeah.

**:** Okay. I'm going to talk with Thor.

**:** So.

**:** And then actually, I think what would be best is if me, you and Thor had a quick call or we, it doesn't have to be like a call. It can be like at the end of this meeting, like next week. You have to go.

**:** I'm good good I was just checking my my times but yeah let's we I was thinking of adding a group chat with all you all you guys new Thor and yeah Thor you and I we just a group chat or whoever whoever is necessary and then we can work something out there.

**:** Okay.

**:** I'll do that. I'll, I'll set that up. Do I have your number.

**:** I could just put.

**:** It here right now.

**:** Are you you're are you your junior at Yale right is that correct.

**:** I'm a sophomore.

**:** There's sophomore okay.

**:** Yeah. Are you your sophomore as well?

**:** Software so yeah.

**:** Nice.

**:** It's recruiting done for you or you still on the grind or you're just chilling now.

**:** I got, I got an offer at truest.

**:** Oh.

**:** That's awesome hey that's great congrats.

**:** Yeah.

**:** Thank you. So, yeah, I accepted. So I'm probably going to go, but I don't know. I, I may recruit for something later. We'll see.

**:** That's true but at least you have like a backstop youp know what I mean just like.

**:** Exactly. Like, I have something. I'm not going to work at, like, mcdonald's or anything.

**:** That.

**:** What about you? Are you doing the recruiting?

**:** No I'm mostly just working in startups probably work in the startup that I have right now.

**:** Yeah.

**:** Working the smaller hedge funds then.

**:** Yeah we'll see we'll see how this ends up because I'm not.

**:** Like we'll see how like the whole AI finance I guess.

**:** Sophir ends up hopefully it doesn't end up like what software engineers did to you know how that kind of crumbled a bit so.

**:** Hopefully the bubble doesn't pop, at least not before you guys exit.

**:** Exactly see Rafa you know what you're talking about.

**:** And. Yeah, I know exactly how it works.

**:** Exactly it yeah so oh I have your I have your number right Rafael do I.

**:** I'm going to send you a message. I just put in a number.

**:** Perfect.

**:** That's awesome now let's.

**:** Let's figure this out because we're kind of aggressively rolling it out right now.

**:** Okay.

**:** Perfect.

**:** Okay.

**:** Got your number.

**:** You want to make your group chat with.

**:** Awesome.

**:** I'll add a not as well.

**:** Does he also handle the.

**:** All of that okay.

**:** Yeah.

**:** He's like. He's like me, I guess.

**:** Wait, what's your, your company called with AI?

**:** Yeah.

**:** And the who was that person who talked about the fun in the main meeting who talked about the fundamental.

**:** Matthew.

**:** Was it Matthew that was talking about it he was talking about how like you need to like not only do the model but you have to like have a convincing pitch who was who was saying that.

**:** S, Matthew.

**:** It was magic okay.

**:** Yeah.

**:** We have a we have a tool that you know how AI is like super psychophantic and it just agrees with everything you say.

**:** So essentially we have a tool that fights back on all your thesis I presented it like three days ago these hedge funds and they they like loved it.

**:** They they like fell head over heels for it like I can tell let me show you a quick.

**:** Actually let me see if I can pull it out.

**:** But.

**:** It essentially put all of their like a lot of people had.

**:** Like they criticize people's thesis like sometimes they were just like thesis like people had no back into it.

**:** Let's see.

**:** And then it finds the cracks.

**:** Yeah it found the cracks pretty pretty quickly and that's and that's the thing like that's what made it so I guess.

**:** And.

**:** I guess useful.

**:** Wait let me let me actually let me show you my screen actually if you don't mind.

**:** Yeah.

**:** This I think is actually more useful honestly like this software.

**:** Is I think a normal Quant usually can do what I'm doing already.

**:** But like this person so this is like actually you see my screen here right it's.

**:** We call it investment decision framework it forces this person actually did this is like a real analyst like he talked about his strategy the core thesis is like data science.

**:** You know this is for poet and then you know they talked about what they're doing and why they might actually have an edge in the market.

**:** And then when they when they did that the AI pushes back they're like you know this is actually solved the problem.

**:** You have the assumption that like it breaks down the assumptions.

**:** How confident are you that they've actually solved the problem.

**:** Are they actually dependent on these big players.

**:** Then the person answers the questions like in this case it will be like our analyst Ants answering these questions.

**:** And it keeps challenging it so then it's like.

**:** Is this going to happen in the next 12 to 24 months that's then you know that's what the thesis that's what his thesis was.

**:** He responds back.

**:** They reflect again and then they keep challenging you on stuff like he pretty much said I don't even know he's a 50 50 like chance this will happen that's a terrible thesis that's that's just hope so like this is like how like the AI will continually challenge you until you get to a stronger thesis so honestly this is probably the more useful fundamental one.

**:** In terms of the fundamental teams on our and PGI the quantitative ones they'll have their good time playing with clock code that I know for sure.

**:** Yeah I don't know sorry I'm bombarding you with a lot of.

**:** No, that's really cool.

**:** No, no, I love it. Wait, how, how exactly did you guys do? Like, because, like, how is this different from, like.

**:** But.

**:** Like Claude itself or, like, ChatGPT? Like, did you guys, like, do a, like, wrap something around it to make it, like, only do this?

**:** Yes we did so we designed something why I designed this function.

**:** That it's a it's a very extensive document that tells the AI how to behave and how to look for these cracks in your investment thesis.

**:** It captures red flags.

**:** Like youe know if you're if you can't define your edge or like you can't define why you're doing something completely cracks you down like it like it makes sure you you identify and know what you're doing.

**:** There is a lot of it's actually quite complex the way it's designed and the more you do it so this is not you don't do this one time you actually you constantly do this maybe every two or three days once you update your thesis and it gets better and it understands your position more and to the point that to the point that you actually understand yourself what you're investing in and why you're investing so it refines their thesis and it makes it pretty much bulletproof.

**:** It's this very iterative process that leads to good success definitely worth trying it's very fun if you do this without like let's say you say I want to buy Tesla because it's a cool company it will like roast the out of you like it's like it will look like you have that's like that's not a thesis and I feel like that's a lot of people just don't know that like a lot of I feel a lot of students go into these stock pitch competitions and they have these cool little models but their thesis aren't really thesis and that's kind of what this breaks down so this is kind of a again this is beta we literally are just testing it on the spot but happy to share it I mean this is.

**:** You have nothing. Yeah.

**:** Wait, so you, so you feed this document into the AI, and then it, this is, like, kind of like the, the foundation of the AI. And then it, every, every time it's asked a question, has this, like, in its mind when it's answering? Is it how it works?

**:** Yeah I mean like you can like you do it right you can just trigger it right now do you have like a so you just trigger it.

**:** And it just starts it up.

**:** And it you know if you have any idea like what it what it wants to just say yeah it absorbs all the context.

**:** And then it gives it so like we can say I want to.

**:** I want to buy Tesla I think this is a great stock like just wait we're gonna get we're gonna get roasted but we can just we can just watch it.

**:** Yeah.

**:** But it gets you know your position size yeah look at it tells you you know you can define your position.

**:** Okay.

**:** You want to trade long term okay we do long term.

**:** And asks you questions and then you you continue to iterate upon it so that's kind of the basis of it.

**:** See that's the thing it's not it's not a thesis it's a feeling accurate.

**:** Oh, but it's cool that it, it asks you questions on how to make the thesis better.

**:** That's right and the great thing too is it takes in all the 10ks automatically it takes in all of the stock news and all the news networks so it's like the expert at it has all the knowledge of the internet and then it forces and it makes you learn so it's actually very.

**:** It's very informative obviously if you're to the level of like the you know those professionals that I was just showing you that's kind of the level we want to be at eventually like those fundamental analysis.

**:** Like when they were doing the.

**:** What was the last one I showed you but like yeah when they were like actually having real thesis but that's you know this hopefully hopefully we all get to that stage one day.

**:** Right.

**:** Yeah.

**:** That's really cool, man. I, I think that would be great for PGI.

**:** This is probably, like, too good for PGA. This, this seems like something that can be used in actual, like, hedge funds. But, yeah, definitely something that the, that the, the value funds can mess around with.

**:** I'm gonna, I'm gonna send a message. I want to, like, take time to write it to explain to thorin and Anant. But, dude, thank you so much for, for offering. That would be really cool. And, yeah, I guess it would be good for you guys to, because then we can, like, test it and see if there's anything that we can improve on it. But it seems.

**:** Up on.

**:** Both sides.

**:** Yeah.

**:** Yeah. But it seems really nice. Yeah, that's awesome.

**:** Yeah thanks for listening Raphael I know I know you weren't expecting this hopefully I didn't.

**:** No, I'm always interested, man. Like, yeah. Thank you. Thank you for taking the time to explain it to me. I really appreciate it.

**:** Hear the audience this time so I appreciate it yeah well I'll see you next week then it'll be.

**:** Okay, I'll see you next week. Okay.

**:** All right keep it.

**:** Bye-bye.

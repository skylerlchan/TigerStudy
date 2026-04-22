# Paragon Global Investments - Weekly General Meeting

**Date:** 2026-04-20


## Summary

### General Announcements & Updates

- Value side pods approaching deliverables phase for mid-May pitches
- Should have company selection and thesis understanding by now- Start putting work on paper rather than leaving everything to end
- IB cohorts launching soon for freshman/sophomores
- Led by Anant, email coming out shortly- Focus on banking recruitment preparation
- Partnership updates
- Thor connection successful - deal went through despite personal connection (Thor knew Skyler’s sister from China)- Cloud credits partnership confirmed for all members- 5-10 minute demo planned before pod sessions
- Velvet startup gaining traction at Princeton

### QQQ Gamma Scalping Strategy Development

- Strategy focus confirmed on QQQ over individual stocks
- More consistent volatility due to index nature- AI sector sensitivity creates ongoing volatility opportunities- Easier backtesting and proof of concept vs individual stocks
- Research approach
- Deep dive into academic papers for mathematical foundations- Tasty Trade website scraping for roll-up strategies- YouTube transcription analysis planned
- Key parameters to explore
- Roll-up strategies when underlying moves
- Control decay and take profits- A/B testing planned vs base strategy- Cost-benefit analysis needed- Frequency optimization for entry/exit- Position sizing and risk management
- Data limitations
- Currently limited to 1-year options backtest data via Alpaca- Bloomberg terminal access available at Princeton- Sam Henriques (Princeton, Citadel) recommended as data source contact- Skyler’s startup provides Bloomberg-Claude integration access

### Alternative Strategy Considerations

- Short straddle approach explored but rejected
- Sharp ratio of 3.0 achieved in backtesting- Unlimited downside risk during market gaps- Works until major moves occur (2008, 2020 scenarios)
- Forex market opportunities discussed
- 24/7 trading potential vs options market gaps- Macro correlations with commodities (NZD/dairy, CAD/oil, SEK/salmon)- Better risk control vs options strategies
- Perpetual futures for weekend trading potential identified

### Next Steps

- Complete research paper analysis and mathematical extraction
- Test roll-up strategy implementation and backtesting
- Create presentation slides using Claude’s new design feature
- Follow up with Sam Henriques for better options data access
- Results and strategy comparison ready for next week’s meeting
Chat with meeting transcript: https://notes.granola.ai/t/3459a78d-e73b-480d-906f-40a812bbb087


---

## Transcript

**:** And this is the number for that drug treatment center.

**:** Same one I told you about the last three times you OD'd all call them.

**:** You really really gotta lay off the drugs, okay? You could actually die and then you know who would come bug me and make me spend all my quarters on them right no more I promise no drugs from now on okay good.

**:** Listen.

**:** If you are gonna use again as a nurse I have access to some Brah how's it going man?

**:** Forrest doing well how are you?

**:** Pretty good just final projects but yeah I'm sure it's the same for you for classes yeah nice no I actually don't have any final projects I have a paper I have four finals no projects this well hell okay okay gotcha got for see us like they don't really have finals they just like pilot projects before period this is nice because it's a lighter finals but it's also more cooked control the outcome more with product yes that's true yeah yeah I think high level class is probably more project based than the lower level classes because you're you're a junior right yeah yeah.

**:** Doing well certainly in Arizona we ended up doing the trip.

**:** Arizona nice.

**:** Yeah I think I mentioned it last time but we me and my roommates went to the Grand Canyon for a little bit.

**:** And visit some friends at u of a.

**:** How are you liking it?

**:** It's good it's like 90 degree weather is crazy that like people live like this like year round I don't know it's like a little absurd all our children on the east coast but like they just like just like wearing shorts.

**:** And it's like pools everywhere it's like a little unreal.

**:** Dude I just saw that the weather for our spring fling is going to be terrible it's going to be raining and it's going to be like 40 degrees.

**:** Geez yikes if we were in Arizona yeah yeah it would never happen to Arizona yeah spring thing will be fun though I feel like if.

**:** It yeah no rain rain can be brutal yeah.

**:** We'll see.

**:** Karthik how are you doing?

**:** Not bad just trying to figure out all the course registration stuff got to do it tomorrow.

**:** For what for next next fall ours is at this time so do it kind of I don't know if this is early well you guys are on quarters I guess but yeah for us we're registering already.

**:** Interesting yeah we do that like at the very end of the summer like right before yeah I heard subsicles have like a like a preliminary period but they don't finalize until right before ours is like if you don't do it right now then you don't get anything everything fills up.

**:** Geez crazy.

**:** All right well I won't I won't we'll get into the pods a couple quick announcements one on the value side I think we should be chugging along pretty close to like getting some actual deliverables things on paper because again we're aiming for like mid May for our pitches so by this point you should have a company you should have your theses or at least are like really understanding your theses at this point because that'll drive the model and drive the most of the pitch but I think.

**:** Again I really don't want to like I've always felt like it's not great to be like oh you need to have this by this date because I think it just it could force pods to like move in a direction quickly when it's not the best move I would rather you guys really talk about and debate your theses.

**:** But with that being said I do think that it would be good thing to start putting some stuff on paper starting to maybe trip away at the model just so that you know you're not we're not leaving all the work to the very end.

**:** And I think Aant on this right now he he's going to chat quickly about IB cohorts. I mentioned again at the end of last time but we're going to be doing we're going to be starting that up soon open to most to freshman, sophomores, I mean really anyone can watch it who wants to join talking about best bank recruiting.

**:** A ton you want to announce that are you on right now?

**:** I'm sure if he's here.

**:** I'll send an email out soon.

**:** And yeah these will be a great opportunity for people who are for freshmen and sophomores thinking about bank recruiting I guess more freshman right now to kind of get a lay of land understand what they can be doing over the summer slash early next year to to get prepped.

**:** But he'll be leading that and he'll send out a note shortly.

**:** Okay yeah I'll open up the breakout rooms and we can we can get to work.

**:** Your rare, how's it going man?

**:** Hey I'm doing good. How are you?

**:** Good, good. Thanks for connecting me with Thor. Apparently Thor knew my sister already. They actually went on a date. It's crazy.

**:** What insane? Okay awesome.

**:** Brown too.

**:** I think they met in China. They met in China. That's interesting. That's just what was working there for a bit.

**:** Oh.

**:** Wow.

**:** I see.

**:** It's crazy.

**:** It didn't pan out I'm guessing.

**:** No, it worked out. Oh yeah. Oh, the relationship obviously didn't fan out. But yeah, the deal went through. So I mean, hopefully we get a partnership in to be awesome.

**:** Okay awesome awesome yeah, I wanted to ask how it went so okay that's cool how do you think the partnership is going to look.

**:** Everyone probably gets some type of clock credits and then you get all the skills that we used for refining thesis and researching.

**:** So pretty much everything that what these hedge fund analysts gets. So it's gonna be neat.

**:** Really awesome.

**:** Really.

**:** Cool really cool I think it would also be good to if the members are going to get cloud guys to show the members how to use them so maybe at the beginning of one of the general meetings maybe you could like explain I don't know did you talk to Thor about something like that?

**:** Yeah, they're like probably I'll give a quick demo like a five, ten minute demo right before everyone goes into their pods. We'll figure something out.

**:** Sick.

**:** And what did you think of the velvet?

**:** Velvet, I loved it. I mean you were there too, right? I love those guys.

**:** Yeah.

**:** Everyone at Princeton is talking about role models. They're on the right thing. They're definitely on the right thing.

**:** So excited about that as well.

**:** Yeah I thought it was pretty cool.

**:** What do you liked about it? Did you know these guys personally?

**:** No but so the the guy that wasn't there because they said they were three I I looked into the team a little bit he's Brazilian and he did the same high school as my girlfriend crazy yeah.

**:** No, that's actually crazy. No, that's crazy.

**:** A weird coincidence there but yeah.

**:** Small world. Like that's with every starter. It's just such a small world.

**:** Exactly it's it's tiny but yeah they they seem like chill guys I'm gonna am I gonna actually talk to them on on Wednesday.

**:** To see if there's something there for me but I don't know it's I'm not like expecting to work there it's just kind of because I want to learn more about it.

**:** Yeah, that's cool.

**:** That's.

**:** Cool.

**:** How about you guys thank Chan Alex how are you?

**:** Doing good.

**:** I'm in the city actually coming back for the weekend.

**:** So nice yeah where where do you go to school again?

**:** Youn Chicago okay you're just home for the weekend and then you go back.

**:** Yeah yeah I'm coming back Tuesday evening just skipping two days of classes.

**:** Nice it's good to be home.

**:** Nice nice nice.

**:** Yeah it's been good but I got like four midterms next week which is not good yeah four midterms the school year is almost over you have like four mid turns and then like two weeks of class and then finals yeah basically like.

**:** Like four more weeks of class after midterms I mean it's like Carter system so oh yeah.

**:** Well good luck on those.

**:** Thanks Alex I think you're like driving or something we can't hear you but it's okay yeah no no no that's cuz I'm not saying anything I am driving I'm just driving back from the city so I didn't want to miss anything I'm like 20 minutes out from home okay.

**:** No no worries thank you for logging on you can just listen don't stay focused on on on the road for sure no no worries okay six okay so I at this point oh also sorry guys for not being there last week that's my bad I was in a conference in boston and I was coming back and it was going to be impossible to log on but but I'm here now.

**:** I looked kind of at the transcript of what you guys did the notes that that had for me and it seems like we're getting closer to.

**:** A strategy and something that we can pitch so yeah what are your guys's ideas on on actually making something.

**:** I'm thinking we stick with QQQ.

**:** But I mean there are.

**:** Let me check.

**:** I need to find.

**:** I really like the qqq idea I think that one's that makes a lot of sense to me.

**:** My.

**:** Yeah, it's definitely the most intuitive.

**:** Because like the other stocks can come and go and you actually don't know like the like the leaderboard for Gamascalpin will change constantly but QQQ seems like it's gonna always be like pretty volatile or there's enough volatility for gamma scalping.

**:** So.

**:** Especially right now because every day that Anthropic releases a new skill basically whatever company was doing that before thanks so like the volatility is going to be wild for the next year.

**:** Yeah.

**:** That's very true. That's very true. They're very sensitive.

**:** Okay.

**:** Nice I think.

**:** For the pitch something that would be interesting is showing kind of our process so showing how we got to okay we want to do qqq maybe having some pictures of those leaderboards that that were generated so showing how we got cube and then showing how we got to the other parameters I think Forrest is he's very ambitious for us to he wants like very mathy.

**:** Type things like formal research papers I.

**:** Don't think we have to do that really if you guys know how to like read and digest like advanced quantitative research papers and you want to do that sort of thing then sure but I'm not going to impose that on us we can kind of just like see what strategy works and pitch that and it can still be a really good pitch so I think yeah another sorry another reason why QQQ would fit I think better not only because I think it is going to have quite a bit of volatility with you know all the AI that's coming out but also because it's going to be the easiest to back to us.

**:** So that we can demonstrate and also it's going to have probably more consistent volatility overall than individual stocks because it is an index.

**:** So I think I think it's going to be a lot of easier to prove our case if it's right or wrong.

**:** For that matter.

**:** Yes, no, I agree I think okay we should stick to. We just have to figure out the other parameters of the trading strategy.

**:** But first I want to I want to kind of have the infrastructure for the for the pitch in place. So I want to create a slides presentation so that and that way we can also kind of record what we're doing.

**:** Did I already create one?

**:** Of you guys saw it but Claude's got a new design feature you can it'll make the deck for you if you like especially if you have like a branding book if you put colors and fonts and stuff.

**:** It'll make it for us.

**:** Then just do that yeah it's sick.

**:** Man. Claw for a researcher design caught everything.

**:** Yeah.

**:** Yeah.

**:** Anthropic for the win.

**:** Exactly.

**:** Honestly yeah that would be easier if you if you guys want to do that that works too okay so so what do you guys think is the next steps figuring out like maybe other parameters like how often how often to gamma scalp went to going when to go out.

**:** I'm doing a deep research right now. So I was looking through a ton of research papers and then we're gonna extract the maths from it and then go from there.

**:** Amazing.

**:** I'll let you know when it gets done. It's gonna take a while.

**:** But.

**:** And then Skyler did you I know last time we talked about roll ups is there any of them talking about that at all? Cause I do think that's worth looking at.

**:** Yeah let me put that in right now actually let me just add it to the prompt.

**:** Roll-ups what exactly is that?

**:** Like when the underlying moves you could you know roll up or roll down you know depending so like you would buy the next contract or you could buy the underlying you know so basically you could move it to control the decay and things like that.

**:** I see.

**:** Okay so you.

**:** You would encourage trading cost but you might it might you know and you could take profit that way too it might be a better solution depending to make it effective.

**:** But it might also just cost too much money and not make much of a difference so we could probably find some way to put like Skyler in that test we might be able to put like t stats to see how significant of a change or how much it's worth it or like gate it like if it moves X amount then it makes sense to do it if not it doesn't.

**:** Yeah we can we'll do a back test on that actually yeah let me I just I'm not familiar with when you will roll so I'm gonna do some research on that first and then we can figure out so then we compare the two there'll be AB testing that'd be great actually that's a good idea let me put that down right now.

**:** Okay.

**:** Yeah.

**:** Brilliant.

**:** All right.

**:** There should be a paper doing this already I don't think it's I mean I don't think we're that cutting edge there should be somebody that's published this.

**:** Yeah for sure and there's a lot of people talk about it I'm not sure if you know it was that tasty tasty works is that.

**:** Somewhere.

**:** Casey trades.

**:** 50 trades yeah they talk about it so much too.

**:** Yeah they're they're they're primarily an option trading firm that's what they started off as and then they they do a lot of retail trading so I wouldn't be surprised.

**:** Actually I might I might go on their website and then ask my bots to scrape their website.

**:** Yeah they've got a lot of education on it.

**:** Let's do that.

**:** That was one of their big like attractive like you know things to bring retail traders on.

**:** Smart yeah I'll use YouTube transcriptions then sweet okay perfect we got that in checked.

**:** All right.

**:** 4.

**:** 000.

**:** I put in all of the QQQ research into a folder right now and then we can.

**:** All right.

**:** Try to create a presentation now or see what we got.

**:** One more question scholar you said we only had access one year back test for options right with what we're using.

**:** Yeah.

**:** And there's no there's no there's no better resource right.

**:** There probably is like.

**:** Like I can I can jump on my.

**:** I bet every university has some type of like.

**:** Do you think you could ask Forrest if like he's got something better for us.

**:** Because he should or I talked to Forrest about this and he said alpaca was the best thing that he should talk to is sam he was ahead of quant last year San Enriquez he goes to Princeton he sat at Citadel's auction desk I'm pretty sure I bet he knows.

**:** That's right.

**:** Yep.

**:** Where we could get good stuff I mean I think the best would probably be Bloomberg but I don't know if like if well we don't have that we do at yeah we do we do yeah but you have to be at the terminal itself yeah but is there a way to use Claude and have cloud access to Bloomberg terminal while you're on that.

**:** No but they've got some that are mimicking it.

**:** No we could like that's what my startup does is literally just connects Bloomberg with Claude.

**:** But I don't know how good they are.

**:** Does it?

**:** Yeah I mean I can.

**:** I mean people pay 100k for this so I don't know I could probably find some way to sneak that out.

**:** Yeah.

**:** Okay.

**:** I have access to the data.

**:** Does the does Princeton have lunar terminals?

**:** It does it does I notice Sam is correct there is.

**:** Okay.

**:** Like there are ways I can get option data but it's like a one download like it's a it's like a you get a zip file and it's not like yeah I mean it will still work honestly if you want me to do it I'm totally glad to do it.

**:** I don't know whatever you guys think would be better because an API probably has more like precise data but I guess.

**:** Yeah it's just easier.

**:** To work with yeah.

**:** What's for what firm are you working with it like ties into bloomberg.

**:** Which firm I've just work first like I work for a small hedge fund I work for a YC startup that tailors towards more smaller hedge funds so you got like.

**:** What's the name.

**:** It's got with AI research it's the current batch just got out of well I just got out of like what's it called stealth mode so we're still very new.

**:** Okay.

**:** Yeah good for you man way to go.

**:** Thanks man hopefully I can transmit all the knowledge to you guys because like you guys are one of the ones that have to be using clawd and.

**:** Good luck good luck.

**:** Bloomberg to do your actual jobs like lowkey I'm just building the products around it I'm not actually doing any of the modeling.

**:** So.

**:** No it's brilliant.

**:** Yeah.

**:** Yeah.

**:** Let me see.

**:** What the results came out with.

**:** So wait Rafael when is the when is the presentation is mid mid May right so we still got like a month or a month is that right.

**:** Okay.

**:** It's gonna take some while to get all these strategies in.

**:** The bless you.

**:** Thank you.

**:** Have anything on the top of your mind Rafael Ahan any ideas that we can try out?

**:** Two empty I'm just waiting for ideas.

**:** Thinking.

**:** Like.

**:** Oh.

**:** Wait like you mentioned that.

**:** Qq works well but a lot of stocks like don't work well.

**:** Yeah like spider terrible for galas scalping they don't move enough they just try.

**:** Like.

**:** Yeah.

**:** Like I was thinking it was possible to like take the reverse position for those stocks.

**:** Yes okay I've actually explored this the sharp ratio is insane and I think there's a reason why it's like you can hit like three sharp ratios like sharps of three which is pretty damn good and then you kind of like wiggle it around it's actually fucking insane there's a strap for that.

**:** Okay.

**:** Oh.

**:** Like.

**:** You sell.

**:** Yeah.

**:** To sell but yeah but.

**:** Well I guess if you're selling a straddle you're what's your downside.

**:** Is unlimited yeah it's a it's naked like bro you're kind of fucked a little too far.

**:** Right.

**:** Yeah so that's.

**:** Yeah that's the thing it's like it wins until it doesn't and then you're half.

**:** I think that's what happened it was we only had one year of data it had no like major moves it wasn't like the like 2008 or it wasn't like 2020 so so you literally had no big moves and obviously if you did that for the past maybe year you would have actually made like a solid 68 60 to 80% profit with 3 sharp ratio.

**:** Right.

**:** Yeah.

**:** What did what did I see the other day I saw I was looking it was on social but it was basically like somebody coming up with it like an AI strategy using claude using like ingesting data world data into like a Mero fish you know copy and trading oil futures with it and I guess it won like hadn't law like I don't know 18 months or no maybe it was maybe it was like 12 months and 18 trades.

**:** And apparently it won all of them but two of them but it only like made I don't know 500 some thousand.

**:** So and it was working with a huge amount of money each time so that means the two losses that it had were so outsized that they were just like super significant so I think it's.

**:** Some somewhat similar in a lot of ways because it's like it works until it doesn't and then the risk is so big.

**:** You know it's not I don't know if it's necessarily like a real strategy you can do it's like a lot that's why a lot of hedge funds blow up right like it works in in a bull market and you push the leverage until it doesn't work and then they just implode.

**:** My boy Scout leader wasn't it was an options trader he would tell about like if you're you're buying options right like what we were doing right now we're buying options it's actually like it's actually quite easy for the risk management because you bleed cash slowly so you realize that something's not working but like with with the short selling yes you will you will blow up in like one trade and that's you correct like it's terrible.

**:** Yeah.

**:** The good way to do it is you could you could buy the underlying when you sell the option you could try it that way.

**:** You know so you'd have like or you know like you buy 100 then you sell an option.

**:** So you recovered in a way but you know I don't know how much that makes sense.

**:** Wait is the sharp3 result like with like delta hedging like you're setting the underlying and stuff.

**:** Wait what is it again pencil.

**:** Oh I was wondering like if the sharp tree result is with like the hedging that Alexander mentioned.

**:** If we trade with a stock.

**:** Like like.

**:** Yeah yeah if you're like buying and selling the stock accordingly when you sell the straddle.

**:** Yeah that's that's pretty much what we're doing yeah.

**:** Oh okay.

**:** I guess.

**:** But I think the worrying part is actually when it gaps is when the market gaps and you don't put the position in the time like if it has like 10% you're cooked.

**:** Yeah yeah.

**:** Yeah yeah.

**:** Yeah.

**:** Also that usually happens when the Market's closed to normal trading so it's like if you're in an options position you're because you can't there's no way you can get out and you can't do anything because it gaps you could do it if you're trading shares or futures but or Forex but if you're trading options you're just you're cooked.

**:** I'm actually finding it the perpetual stock futures might be it might be actually interesting if you can trade over the weekend.

**:** Yeah.

**:** And like 247 that might be there might be something there but that's that's definitely for another time.

**:** Yeah liquidity gets crazy though like depending on the times like depending what you're trading if you're trading indexes it's not a big deal like SPX and stuff you know usually has really good liquidity but if you're trading other things there's just times you don't want to trade because basically it's all it's all bots you know so you're trading against I mean unless you're making an automated trade so you wouldn't want to manually trade that Forex is one that you could honestly trade your or all the time depending on which time zone it currently is because Asia London new york they all trade differently and they're pretty strong depending on what the hours are.

**:** Yeah.

**:** Right right it goes with the with the time zones yeah I mean.

**:** Yeah so that one you could trade.

**:** We should look into.

**:** Yeah and the other thing is like it has a much more macro underpinning so and it takes a long time to play out it's not like it just happens quickly you know it's gonna it's gonna take quite a while so you can be in a trade and you can ride it for a lot longer you can control risk and things and the leverage on those are ridiculous as well.

**:** Yeah that's for sure.

**:** So it's not that dissimilar to options but it's a lot easier to control.

**:** That's new to me I actually I haven't been in the Forex markets for that long so this is.

**:** Yeah I haven't I haven't really researched that so you're the expert here Alexander.

**:** I don't know about expert but I have traded Forex so it's it's it's interesting.

**:** That's oh sorry go for.

**:** And the other thing is you can map it to like weird correlations you can be like you know what's the largest export so like the new zealand kiwi it's like tied to dairy products strong correlation or like the swedish krona is strongly correlated to salmon you wouldn't think so or like the canadian dollar strongly related to oil or you know like and and you can look for inefficiencies there and do like arbitrage.

**:** No way that's another.

**:** It's it's weird nobody thinks about it that way though.

**:** I are these spurious charts like are these like made up correlations though or do they have actual like groundings.

**:** Yeah yeah they have counting they're like some of their largest domestic products and you can look and see you know when the correlations work or not.

**:** That's interesting I've never this is the first yeah.

**:** All right we're still waiting for the research I low-key should have done this before my bad like I forget these things take like a couple I think at least 20 30 minutes of just constant cloud code like scraping magic.

**:** That's.

**:** Fine.

**:** That's fine we can also you can leave it run in we can talk about it next week.

**:** Yeah that's fine we'll.

**:** Because we have time still we have like a month as you said or like three weeks.

**:** Okay.

**:** Yeah.

**:** If you guys want to keep chatting that's also cool.

**:** That's that's all right.

**:** I guess is there anything else you want to bring in right now I guess we can you know we guess we can end early and then we'll.

**:** Yeah that's all for me I don't know if you guys anything else.

**:** No all good.

**:** Good.

**:** Too.

**:** Okay awesome.

**:** Yeah once that's done running yeah feel free to put in the slack or if you just talk about it next week also.

**:** I just got it done all right perfect I'll just send it to the slack okay.

**:** We talked to next week then take care man.

**:** See you guys.

# Options theory and derivatives overview for PGI investment group

**Date:** 2026-02-23


## Summary

### PGI Options Trading Pod Meeting

- Weekly meeting for Princeton Group Investment options trading pod
- Education members directed to separate breakout room with Sid for market discussion and office hours
- Winter recruiting season slower pace - quant recruiting ramping up for spring/summer

### New Member Introductions

- Skyler Chan (Princeton, sophomore)
- Studies operations research and financial engineering- Active options trader, currently trading zero DTE- Recent coffee chat with Mizuho alum at 9pm for equity research role
- Peng Chan (UChicago, math/CS)
- Researching implied volatility vs prediction markets- Noted discrepancies between options IV and polymarket betting odds- Limited by thin polymarket liquidity (~$100 trades)
- Michael (UChicago, math/statistics)
- Interested in volatility surface modeling- Exploring potential market making projects

### Derivatives Fundamentals

- Forwards vs Futures
- Both agreements to buy/sell at future price- Forwards: OTC trading, counterparty risk- Futures: exchange-traded, margin requirements, regulated- No money exchanged at initiation (present value = 0)- Primary use case: hedging (airlines hedge oil prices, FX risk)
- Options vs Forwards/Futures
- Right but not obligation to buy/sell- Always costs premium (never free due to optionality value)- European: exercise only at maturity- American: exercise anytime (more expensive due to flexibility)

### Options Theory Deep Dive

- Call vs Put Payoffs
- Call: max(S-K, 0) - want underlying price to rise- Put: max(K-S, 0) - want underlying price to fall- Short positions mirror long positions (obligation vs right)
- Leverage Comparison
- $100 Tesla stock vs $100 Tesla calls example- Options provide higher volatility: 20% stock gain = 100% option return- Downside risk: can lose 100% of option premium
- Put-Call Parity Formula
- C + PV(K) = P + S- Can construct any option using combination of stock, bond, other option- Call = Put + Stock - Borrowed money

### Meeting Disruption

- Technical audio issues with background noise/music interrupting session
- Meeting continued despite disruptions
Chat with meeting transcript: https://notes.granola.ai/t/ef5bd352-8892-49b4-9805-e4826a1d2def


---

## Transcript

**:** What's up, guys?

**:** Hey, what's up?

**:** How you doing? Carte. Good weekend?

**:** Yeah, not bad.

**:** You.

**:** Yeah, solid.

**:** How's the weather over there?

**:** It was beautiful.

**:** Like, earlier this week for, like, two days, and then it kind of reverted.

**:** But we had a day where everyone was out on the quad.

**:** And enjoying life a little bit more.

**:** Yeah.

**:** How you doing, Nora? Good to see you.

**:** Good. Good. Yeah. Very cold today. Kind of sad. I thought I'd put back my for good, but no, I had to pull it back out. Chicago always does that. Always finds a way to disappoint. Unfortunately, I don't remember this fall. Spring last year, but I happened.

**:** Yeah.

**:** Yeah. I don't know.

**:** I feel like it always just takes so long to just, like, break out.

**:** I guess.

**:** Maybe that's normal.

**:** Anyone have any fun weekend stories?

**:** Something to share.

**:** Leo anything crazy.

**:** Not much. Not much. It's just. Pen, cancel school tomorrow, so. Which is good news.

**:** For the snowstorm. Yeah.

**:** Which is the third day that we cancel school. Never happened before.

**:** Jeez, that's crazy.

**:** Yeah. Yeah. Stan, how's the snow in new york?

**:** It is blizzarding. Omdani has issued a stay at home order.

**:** So, yeah, things are very canceled at nyu. I don't know how Columbia is treating things, but I'd imagine pretty similar.

**:** Yeah, we also have classes canceled. Like, canceled? No, like, not in person. It's, like, shitty. His mom Donnie's thing. Like, his. His order is for, like, actual, like, K through 12 age kids. And they don't have to actually go to school or do online class. Like, they get an old school snow day. Like. They're completely free from everything. Like, no, we have Zoom class, so not, not, not fully canceled. Still gotta go.

**:** Interesting.

**:** Yeah, my parents were. Were visiting my. My younger sister goes to Wisconsin. They were, like, visiting her and.

**:** They would. Their flag got canceled back to New York.

**:** They literally could not find anything.

**:** And then their flight got canceled again. Going to. They then tried to go to, like, Miami, and, like, that one got canceled.

**:** I did.

**:** So it was kind of brutal travel.

**:** I trained index options.

**:** Travel weekend, I guess, too.

**:** All right, we'll get started. There's enough folks here. First of all, I will say thank you for everyone that has your cameras on. Always appreciate people turning their cameras on.

**:** You know, we're. We're. We're a close group. We don't need to. There we go. Get some more. You guys all look beautiful.

**:** Don't be. Don't be shy about the cameras.

**:** Got a pgi is really, really smart group.

**:** But also been known around our campuses also being consisting of very good looking people. Asked for how the cameras on bro. Why you. Why are you going on this tangent now? Right. I've been hearing that especially around especially around Pen.

**:** They're like, you know, Jay and all these PGI guys.

**:** Like just good looking folks. So always good to bring hammers on. See everybody? There we go. I'm loving this right now.

**:** Full screen of Full screen of cameras is awesome.

**:** Because I think it's just. It's nice to see everyone's faces and also just not talking to a wall of letters and stuff. But thank you all for being here.

**:** Quickly mentioned, last meeting was kind of hectic with a lot of the education folks.

**:** Mostly just because, like I told everyone from education,

**:** Like if you can just bounce around pods.

**:** With the idea that, like, you could learn or whatever, but it ended up being a lot of people in the pods and I think it was a little bit, a little bit tricky to kind of get work done and meet everyone within the actual pod. So I sent an email to all of education, but we're going to. Be doing a little bit different this time. The pods will still meet in their groups, but there's going to be a separate education group breakout room. That will be a discussion led by SID about just the markets, general conversation about what's going on in the world in the market right now. Maybe we'll get some some hot takes on software that would be pretty cool and as well as like kind of a general office hours for your guys education. If there's any questions you have for him or. Or recruiting questions. It's kind of just like a sital run it and be sort of just a good space for. For all the education folks. I hope Sid's here right now. Sit here. Yeah, I'm right here.

**:** Sweet.

**:** Awesome. Now you're good.

**:** So, yeah, that's, that's. Everything's going on relatively slow. The winner is always a little bit slower because it's like on the end of the investment banking recruiting process. So we don't really have a ton of events. And then quant hasn't really started yet, but quant is. Slowly starting to ramp up. So, for the quant folks, I believe you know that that recruiting cycle typically happens more over the summer, but we'll probably have some sessions with some of our sponsors and stuff like that.

**:** More into.

**:** The more into the. Into the spring. So that'll be. That'll be exciting.

**:** But yeah, I won't, won't, won't yap for no reason. Let me quickly share.

**:** The pods. We know where to go. And I'll open up the rooms.

**:** Here we go.

**:** Let me.

**:** Do.

**:** Some.

**:** Rooms.

**:** Sid, please. Private message. Not in the main one.

**:** Bro. So embarrassing. Holy.

**:** Pub is rinsed.

**:** Bro. Damn.

**:** And no one's answering you. Jesus, bro, you actually have. It's okay.

**:** Just an airball.

**:** Yeah. So, education guys, feel free to join Pod 7. That's the new thing that we'll be doing.

**:** Hello? Guys, can you hear me? Well.

**:** Yeah, can hear you.

**:** Wait. Sorry. Give me one second.

**:** Try new setup.

**:** By the way, if you don't see your name on this list for whatever reason, let me know.

**:** For what company?

**:** It's a truest for corporate banking.

**:** And eric city. That sounds tough.

**:** Yeah.

**:** Fingers crossed.

**:** It's a 30 minute super day.

**:** Oh, really weird. Yeah, I saw it. I was like, what? So short.

**:** Which school do you go to?

**:** Yale are you go. So you're going to be in New York City?

**:** For the Super Day or something or. No, no, it's. It's online. It's very. Yeah, thank God.

**:** So much easier.

**:** But yeah. Hey, guys. How are we doing? Skyler. Alex.

**:** Nice to meet you.

**:** Nice to meet you. Oh, yeah. Skyler. I don't think we've met. Yes. You weren't here last time, right?

**:** Yeah.

**:** I had a coffee chat.

**:** Oh, shit. Nice.

**:** So it was late, too. So that's a very light coffee chat. It was the Princeton alum, that's why. So it was just like he wanted to talk.

**:** Yeah, that's a late coffee chat. Wait.

**:** Who?

**:** When he was free, which was like before market hours and 9pM So 8, 9pM this was Mizuho. It was interesting.

**:** What firm?

**:** It was a what?

**:** Mizuho mizuho.

**:** Zuho.

**:** That's quite late.

**:** And there's another. I had back to back once, but I already forgot.

**:** Nice. Is that. Is that for trading?

**:** No, this is for equity research, but I'm a big options trader fan.

**:** I've been trading options for a long time, so I just joined.

**:** Oh, shit. You probably know more than me, then.

**:** This? No, it's fine. I just love. I think I have a gambling addiction to it. So you're probably okay. You're probably fine.

**:** Okay. Sick. Okay. You're probably going to know a lot about of what I'm talking about.

**:** So you can probably answer a lot of the questions asked, but hopefully you also learned something. Okay, nice.

**:** Who else did I not meet last time? I think Peng Chong and Michael.

**:** Yes. You guys are new. Nice to see you.

**:** Nice to meet you guys. Wait, Sky. Let's do introduction of you three.

**:** So everyone get to know you. So Skyler go first.

**:** Yeah.

**:** I guess you already know a little bit. I go to Princeton.

**:** I study operations research and financial engineering here.

**:** I just love the market. Been doing a lot of it. I trade zero dte now, so I'm more just playing around. But hopefully I can get a more serious role soon.

**:** Nice. Are you a sophomore?

**:** I'm a sophomore. Yeah.

**:** Okay?

**:** Awesome. All right, pen, chunk.

**:** Am I saying your name right? Yeah, yeah, exactly. Spring Chan. Yeah.

**:** Hi, I'm at Chicago. I'm studying math and cs and I don't know for options. Like, I was just, like, reading up a bit about it. I read a bit about it before. And, like, the funny thing is I was looking at, like, prediction markets because I feel that sometimes, I mean, it's. Not really that relevant, but like it's just interesting. Like last week I was just looking at like the implied volatility in options versus what potting market was betting and sometimes there's quite a big discrepancy. But the poly market markets are too within the trade on so that's probably the reason why.

**:** But, yeah, just nice. And you take the. The true. The true value of the implied volatility as the one in the markets, and then you. Oh, but then you can't trade it. It's too tight, you said.

**:** No, you could arbitrage between them. But like usually poly market is just too thin. Like can only trade like $100 or something.

**:** Got you. That's really cool. We're. We're going to talk about implant volatility. I don't know if we're going to get to it today.

**:** Because there's a lot of stuff to cover, like, to really get, like, higher vision of options, too. But we're definitely going to talk about what implied volatility, what Black Scholes is cool and. Michael, please introduce yourself.

**:** And I speak Chan Michael I'm also from UChicago and I'm studying math and statistics and I drop by this podcast. I was recently interested in volatility surface modeling and I'd been reading a little bit about and the kind of far future I wanted to see if I could maybe like I don't know, experiment with some, like, a market, making projects for that.

**:** Nice, okay?

**:** Well, it sounds good. Okay.

**:** So I guess we can get right into it. Hello everyone. To haven't said hi to Alex. Nathan Gourmet. Let's get right into it. Ch. Okay, I'm going to share my screen Also. Has anyone taken a look at the slides yet? Totally. Okay, if you haven't. Just curious.

**:** Alex, you have nonos, okay?

**:** Awesome.

**:** Try to share. Can I not share?

**:** All right, can you guys see?

**:** Yeah.

**:** I'm going to assume that you can.

**:** 't.

**:** There we go.

**:** Okay?

**:** So.

**:** Okay, so let's start by talking about what a derivative is. So a derivative is kind of the umbrella term.

**:** Of like, options, but also other types of derivatives that we're also going to talk about. So a derivative is a very general thing.

**:** The definition is basically, it's a contract.

**:** Between two or more parties.

**:** That's derived from the performance of an underlying asset. You're going to hear me say the word underlying a lot. When I say, like, the underlying, it's going to be like the thing that the derivative is tied to. Usually it's like a stock, right? Like, I'm going to buy like an option on, like Tesla stock. That Tesla stock is going to be the underlying asset.

**:** And a derivative is basically a contract, and then you're going to define that contract in a very specific way.

**:** And then you. And then you can buy and sell that contract. So what are some different examples of underlying assets I mentioned? Like a stock, but what other underlying assets could you have?

**:** Anyone. Just, like, shout out.

**:** Like, I don't know, corn. Like, corn futures.

**:** Yeah. Any commodity. Any. Yeah.

**:** Any natural resource.

**:** Anything else.

**:** Bonds. Yeah.

**:** Anything that, like, has value, Right? Literally anything can be an underlying asset. Nice. So you guys have probably heard the term vanilla, like vanilla derivatives, vanilla options. Those are, like, the more commonly traded ones. That's what vanilla means. And since they're, like, so common, those are usually the ones that we're going to look at the theory of and kind of know everything that we can about them, because those are, like, the more common ones. There's this website that's pretty good. I found it as I was, like, finding, like, payoff diagrams and stuff. So I put the link here in case you guys want to look at it, because It's a good, like, written review of all the stuff that I'm basically saying here. Not all of it, but, like, a lot of it.

**:** Okay, so Fords and futures are one specific type of derivative.

**:** And they're very, very, very similar. Afford and a future is an agreement to buy or sell an asset at a given price in the future.

**:** And the future is the same thing.

**:** Except it's traded on an exchange.

**:** A forward is traded over the counter.

**:** So, like a Ford. Like, you're usually going to use it for assets that are less commonly traded, like, they're less liquid. Hey, Ralph.

**:** Yeah. What's up? Sorry to interrupt.

**:** Bro. Just your slides. Maybe it's just my screen, but they're not switching.

**:** I know you're on, like, slide three.

**:** I'm on fours and futures. Do you see fours and futures?

**:** I see DRO just an options theory. Still for me, the first slide also says derivatives and options. There.

**:** Good. Okay.

**:** Thank you for letting me know.

**:** So we.

**:** I'm just looking at your deck through the. You know, from the link you shared earlier. Yeah, that could also work. Had it open on two different sides.

**:** It'd be.

**:** That is now good.

**:** Oh, perfect. Okay. Yeah, that's why. So this is kind of what I had before.

**:** So, yeah, this is the. The resource that I was talking about. Okay, so Fords and futures.

**:** Stupid var on top.

**:** Okay, so for the future.

**:** There we go.

**:** So, okay, a Ford is traded over the counter.

**:** And that also means that there's counterparty risk. It's not a regulated market over the counter. To regulate market, you kind of just like make a phone call.

**:** And you sign a contract. But it's not regulated by any entity.

**:** Whereas if you have a future, it's going to be regulated by an exchange.

**:** And if it's regulated on an exchange, that exchange is going to require that both parties, or two or more parties. Right. But for your future, it's two parties. They're going to require that both parties have a margin account.

**:** And a margin account is basically money. It's. It's an account where you put in money.

**:** If you're on the losing side of the contract, of the Ford or of the future. Sorry.

**:** Basically what that means is the price of a future moves with as the price of the underlying moves as well.

**:** So if you're on the losing side, then you're going to have to put more money into the margin account. That's called a margin call.

**:** Margin call is when the exchange tells you this asset is moving in a direction that is not favorable to you and you have to put money into the account because in the case where you can't fulfill your obligation at maturity,

**:** There's going to be money for the other party.

**:** Does that make sense?

**:** Yeah.

**:** There's a famous movie called Margin Call as well. And I guess it's closely related. It's. It's really good movie. I recommend if you guys are interested. Okay. Something that's very important to note about fords and futures. No money is exchanged when the contract is signed.

**:** Which is an initiation. Let's call it initiation. Initiation is time 0. T equals 0. No money is exchanged. You sign the future. Or in such a way that the present value at time equals zero is zero.

**:** However, the price can change.

**:** In the future as the price of the underlying changes.

**:** Okay, so having all that in mind, what's the situation in which you would want to use a forward or a future?

**:** I'm thinking of. You want to. You want to hedge something with some leverage.

**:** Yeah.

**:** What would you want ahead? For example, like. Like if I'm an airline.

**:** What would I want to hedge?

**:** Yeah.

**:** Probably oil prices.

**:** So probably want to prevent oil from shooting up.

**:** So you probably buy some oil futures.

**:** Exactly. Exactly. So, like, airlines want to have, like, a stable, like, expectation of what they're going to have to pay.

**:** For their expenses, so they'll sign a future and they'll be like, okay, I'm going to buy, like, 1,000 barrels of oil in 2027, and I know what I'm going to pay for it now.

**:** And if the rise of oil goes down, they end up losing money. Right, because they could have gotten it for cheaper in the future, but they would rather just be sure that they're going to pay that amount and not have any risk.

**:** Another situation is also hedging foreign exchange. So if you know that in the future you're going to need Japanese yen, I don't know. And you're scared that the exchange rates are going to fluctuate, you can just lock that in in the beginning.

**:** And you can do other sorts of hedging, like if you're at an American hedge fund, but you're trading, like, Brazilian stocks in Chais, and you want to hedge that foreign exchange risk you can use for its futures and other derivatives also to do that. So, yeah, hedging basically is the answer. Okay, so this slide, it's not too, too important. This is how you price forward or future, based on the current forward price of the asset.

**:** So that initiation, like we mentioned before, the price is zero, but the price of the underlying changes over time.

**:** Actually first does. I don't have any questions on what we've already gone through. If you have any questions, please just interrupt me.

**:** Okay, Everything seems good. So the price of the underlying changes. The contract changes too. Like for example, I buy a future. I sign up Future to buy 50 barrels of oil in the future at $10.

**:** Each barrel, right? You're 50. That's more realistic.

**:** The price of oil falls.

**:** I lose money.

**:** Because that contract for me, it loses value.

**:** That's kind of how it loses, because I could have just, like, bought it at the lower price in the future instead of paying that high price that I agreed upon.

**:** At the initiation. So this is kind of the formula. It's the forward price of the current it's the current forward price minus the old current. The old forward price, which is the forward price at initiation.

**:** It's like the value that you say you're going to pay. And then this E to the RT is discounting it to the present values. It's the present value of this, that's the present value of the contract as a whole. And then the one on the equation on the right is for. Discrete.

**:** Discounting. So we have continuous entries counting. Not that big a deal.

**:** So fold. Yes, the price we expect the asset to have at maturity, at initiation. Fnew is the price we expect DASA to have at the present. At times, small T. But what happens if f nu is greater than f old?

**:** Yeah.

**:** What happens.

**:** I guess it's just positive.

**:** Your present value is basically positively like holding it at higher value than what you paid for it.

**:** Exactly. And you pay zero for it, right? At the beginning. There's no exchange of money at the beginning. But since you're long here. Right. We're finding the fair value of a long, which means you're going to buy it.

**:** Yeah.

**:** You're long the future. So yeah, if the F NU is greater than F old, then it's going to have a positive price. If you have fold instead of F nu here, so you add initiation basically, right, then this value is going to be zero.

**:** So the present value is zero.

**:** That's basically more proof that in the beginning, there's no exchange of money. That's really like should be the main takeaway from Forza and futures. You don't pay any money in the beginning.

**:** You just agree to buy in the future for a given amount of money.

**:** That's preset at initiation.

**:** As well.

**:** Okay?

**:** So first, any questions on Fords and futures?

**:** I just have a question. Just trading the forward in the future.

**:** So as you I'm trading. I'm a point where I'm trading it and like, it's not like, near the initiation. Let's say there's a mid period between, like, initiation and expiry.

**:** And like the present value is negative. So what. What. What did. What would be priced at an exchange?

**:** What would he price that at an exchange?

**:** Yeah. So, like, if the present value is currently negative.

**:** Because, like, all that is less within, like, new is better than old, then, like, what would its price be in an exchange for which I have to buy the car, drive.

**:** It would be negative because the the price of any asset, including a derivative, is the present value of the future payoff.

**:** That's, like, definition of, like, the spot price of something, right? It's always going to be the present value of the future payoff.

**:** If you're long and fnew is, is smaller, you will see a negative price on the market. Like, like you explained. And yeah, you would basically, you would have to be paid to have that, that asset. Right. Because it's going to lose money.

**:** You're going to end up like. You'll be paid to take on the asset, but if the price stays the way it is,

**:** At maturity, you're going to end up paying that same amount back, right? That's assuming the price stays the same.

**:** Does that make sense?

**:** Nice.

**:** Sick. Okay. Options are more fun for some. Futures are kind of like a necessary preamble to options, but that's done. So let's go with options. So an option is very similar to a for your future.

**:** But this time you're not forced to buy or sell the underlying at maturity.

**:** You have the option to. Right. See, that's where the name comes from. So. So an option is contracted option to buy or sell. You have the option. So you have the right to buy or sell, but not the obligation to buy or sell the asset.

**:** At a predefined date large T in the future at a predefined strike price K.

**:** So take note of this terminology. Strike price is the amount that we're going to have the option to buy or sell the underlying for in the future.

**:** So then you have two main types of options, right? You have to call and you have to put. The call is buy, right? You're going to have the option to buy the underlying in the future, and the put is you're going to have the option to sell in the future.

**:** So unlike the Ford and the future, there is an exchange of money.

**:** At the beginning.

**:** The price of a few of an option is always going to be positive. It's never going to be zero. You have to buy it, basically. It's never free. Can anyone give me some intuition as to why?

**:** I mean, it's like you're kind of. If I'm, like, selling the option, I'm always going to be taking on some kind of risk because, like, the other party can always just, like, not end up buying it if it's bad for them, right?

**:** Yes, exactly. It's that optionality, right? So if I have an option.

**:** And I don't want to exercise it. I can just not excess and nothing happens to me. So ideally, if I had an access to a free option, I would buy infinite of it.

**:** Because I would have basically, a riskless investment, right? I could in the future, I could either cash all those out.

**:** Make an insane return. Well, make an infinite return, because it's free.

**:** Or I can just make zero.

**:** And I didn't pay anything at the beginning, so my return is nothing.

**:** Okay, nice.

**:** Also a little distinction quickly on European versus American options. A European option is one that you can only exercise at maturity. So you can only like buy or sell, or you can only exercise like your option of buying your selling at time T. But for an American option, you can exercise it whenever you want up until the expiration date. At this point, it would be for. For an American option to be an expiration, not really like a maturity.

**:** Date.

**:** So, okay, so given that a European option and an American option have the same T and the same K, which would be more expensive,

**:** Do you guys think?

**:** Because remember, like, both of them are going to have a price.

**:** I would like. I would guess American because you have more of, like, a range of things you can do with.

**:** It. Yeah, exactly. The American option would be more expensive because you have more optionality. You don't have to only excise at the end, you can exercise in the middle at any point in time.

**:** So the pricing of that option is also more complicated. We're not going to go into how to price an American option, but we could do something like that for the project or something involving that. That could maybe turn into trading strategy, but we'll see. And there's other types of options that aren't. Vanilla options. The European and American options, they're vanilla options, but there are other types that we call exotics. So some examples are Bermudan and Asian options, which I forget exactly how those work, but it's not that complicated. You can look it up quickly if you want, but we can definitely see those. Those later. Because exotics are really cool.

**:** Okay?

**:** Something I want to explain. And this is going to tie into, well, to Delta, which we're going to look into probably next time. But the return of a call versus a stock.

**:** So imagine this situation. I have Tesla stock at time equals zero is $100.

**:** And a tesla call.

**:** At time zero at strike price K and like maturity T's whatever.

**:** Is priced at $10. Hi, everybody. Alex, deploy. What happens if I buy $100 worth of Tesla stock or $100 worth of Tesla calls?

**:** And what happens for different end prices of the Tesla stock at like time T? At time big T, the maturity.

**:** So I asked Chat like, do a nice visualization. I think I did a good job. So we can see, right?

**:** The return of the option or the the 10 options that you buy.

**:** The 10 calls is much more volatile.

**:** If you don't exercise the option, you lose 100% of your investment.

**:** You lose. Like negative 100 is your return. It's really bad.

**:** Right? If you put in a lot of money into these options and you can't exercise them, then you just wasted the price of the option. So ideally, you're going to want to exercise your option. However, if you do exercise your option,

**:** If the price goes up just 20%, your return, like the price of the stock, Your return is 100%.

**:** If the price of the Stock goes up 30%, your return is 200%.

**:** So it's much more volatile, and there's a lot of upside.

**:** If the price of the underlying goes up. This is if you're longer call, obviously.

**:** So, yeah. And this is the stock return. So if you buy a stock. If you buy the stock, you're just going to get the return that the stock has. But you buy a call.

**:** Then you return to be much higher.

**:** They can also. You can just lose everything.

**:** So. Yeah. So to connect this with what Delta is. Delta. I'm going to say it really quickly, but we're going to go over it later.

**:** Delta is how much the price of the option moves with respect to the price of the underlying asset. It's the derivative. It's the derivative of.

**:** Partial derivative of the price of this option.

**:** Over partial derivative of the price of the stock.

**:** Of the underlying so the delta of a call is going to be much higher because if the stock moves a little bit right, then the call, the return of the call, or the price of the call price the call is going to be linked to the return is going to move a lot as well. And the delta of a stock. What will the delta of just buying the stock be?

**:** Anyone know?

**:** Buying stock is always going to have the same Delta.

**:** Remember. It's how much?

**:** The price of the stock moves because. Okay, now we're talking about the stock, right? The Delta. We can say Delta of any action. Before, I was talking about the Delta of buying a call.

**:** What's the delta of buying a stock?

**:** Remember. That's going to be how exactly? Yes, it's one. Because it's how much the price of the stock changes.

**:** With respect to how much the price of the stock changes. So stock price changes, like the stock price changes in the same exact amount.

**:** So it's like, yeah, it's one.

**:** Cool. Thanks, alex.

**:** Let's quickly go over what the payoff of a call is. And we're going to be using a lot of these payoff diagrams. You guys are probably already seeing something like this before. But also, first, any questions on options? Anything that we've got over so far?

**:** So if I'm long a call also long and short. You guys know, like long is like buy shortest seller betting against. So if I'm longer, call.

**:** I want the spot price, like the price of the underlying, to increase in the future.

**:** If it increases enough, I will exercise my option to buy it at K. So basically, like, if S increases to a point where it's bigger than K, just the strike price, it's what I've agreed to have the option to buy it at.

**:** Then I'll exercise option if it's lower.

**:** Then I just want exercise my option and my payoff will be zero. So that's what you get here. Right. Payoff is the max of the difference between the price in the future and the strike price. And zero, because you're not going to lose. Great. So let's go over this graph. Right, So. X is K. Here. Just imagine this is K. So if ST right is less than K, our payoff is going to be zero because we're not going to exercise the option in this area.

**:** But if ST is bigger, then we have a linear like 45 degree angle increase because we're making money at this point.

**:** However, something that's important to note.

**:** This is only positive or negative, right? If this is actually the payoff.

**:** Then we just buy infinite calls because we never lose money. This graph doesn't take into account the price of the call. If it did.

**:** Then we'd have to shift it down.

**:** See what I mean?

**:** Because this is just the payoff. It's not the profit. I guess it's just a payoff.

**:** Any questions on that?

**:** Makes sense.

**:** Fairness.

**:** Okay. And this is when you're short a call. So you're betting against the call.

**:** If I'm short a call, the payoff diagram is just reflected across the x axis.

**:** Oh, yeah.

**:** So you're shorter. Call. Great.

**:** So that basically means you're selling a call to another person. When you buy a call, someone has to sell it to you.

**:** You have to pay someone for that call. So when your shorter call.

**:** You're basically selling to that person. So this is what the payoff looks like.

**:** If the strike price is bigger than the price of the underlying, then your payoff is zero because the person on the other side isn't going to exercise.

**:** Their option.

**:** But if it's higher, then that person is going to exercise their option and you're going to end up having to pay the difference.

**:** Because you offered to buy the stock.

**:** From Sorry to sell. You offer to sell the stock to them at a later date.

**:** And if you sell it for a price that's higher,

**:** I'm getting.

**:** Hold on.

**:** Sometimes you guys can feel when you're explaining.

**:** Hold on.

**:** If the price of the underlying is larger.

**:** Then you have to sell it.

**:** Of course you have to sell it for K. You have to sell it for a smaller price when you could. If you weren't binded to this option, you could have sold it for the higher price. Okay, does that make sense?

**:** Yes. Okay, Great. Here. The payoff is always negative.

**:** It's always negative or zero. So why would anyone short a call? What is missing from this diagram that I already mentioned before?

**:** Like the price of the call.

**:** Exactly. But we said before that that moves the graph down.

**:** So then it would just be negative.

**:** But in this case, it would move it up because you're selling it for premium.

**:** Exactly. So you move it up because you're making that initial money.

**:** And you're hoping that the person isn't going to exercise their option. Amazing.

**:** Multiple.

**:** Okay, let's talk about the put. So the put is you buy the right to sell, or when you're long put, you buy the option to sell the stock.

**:** So how do I want the stock to move?

**:** Very easy question.

**:** Down. Exactly. I see. Michael. Nice. You want to go down. And the reason for that is if it goes down, then your payoff is positive. Right. But let's try to make sense of this or actually ask another theoretical question. What is the payoff when the price of the underlying at maturity is zero?

**:** Which means, basically, we're at this point. I don't know if you guys can see my cursor.

**:** This is strike price. Yeah.

**:** It's equal to the strike price. It's like it's this point because that's a 45 degree angle if it's zero.

**:** And you have the right to sell. You're going to just make the strike price because you're going to sell for the strike price and you're going to make the difference between the strike price and zero, sorry, price. It goes down here until, I guess, to the strike price. But basically you're going to exercise your put if the price of the underlying is less than the strike price.

**:** And if it's greater than, you're not going to exercise it.

**:** Okay?

**:** And then, yeah, same story as before. You can kind of go through the logic yourself. I'm not going to do it again because it's quite like the headache. But, yeah, you mirror it when you're shorting put. And also note that these payoff diagrams for long call, short call, long put, short put. They're all different.

**:** Right. So these are all different payoffs, and you can really craft your desired payoff however you want, which is something that's really cool about derivatives. It's something that really makes me very interested in them, at least. So any questions about calls, puts and the payoff diagrams?

**:** Everyone's good.

**:** Raphael. Hello. Sorry, leo. How's it going? Hello. How are you?

**:** I'm doing good, man.

**:** Good. I just want to add one quick detail. I think it's very important. Oh, yeah. Going from the four directions. Sorry, I'm interrupting. No worries.

**:** But always remember when you're buying an option.

**:** The reason why you pay a premium is because you're buying. A right means an option. Like literally an option, but not the obligation.

**:** But when you're shorting, which is when you're selling a call or a put, this is actually you have the obligation.

**:** This is why you don't pay a premium.

**:** I think this is a very good way to memorize the four directions, because when I first learned options a few years ago,

**:** It also gets confusing, right? Like this bunch of different directions. I think when you always think about why do you buy an option?

**:** You're buying an option because you have to pay a premium for the optionality.

**:** Like by definition.

**:** So this is why you always start with the horizontal part.

**:** That is above or below zero. This is the idea of it.

**:** And then you can think about. If you buy a call, you're long. If you buy a call, where you short a put these two are you want the things to go up.

**:** And then the other two is you want the assets to go down. I think this is a lot easier to memorize and to reference in your head.

**:** When you're thinking about options in the charts.

**:** Yeah. No, thanks, Leo. That's really good. I didn't mention that. That's true. If you have. If you're shorter call, then you have the obligation. Yes. Or if you're short a call or a put, you have the obligation to either buy nice, nice.

**:** We're going to keep going.

**:** Now, let's see what happens when you combine.

**:** These things? Oh, no, actually, before that. Let's look at these three or four, because we're missing 14 extra payoff diagrams. They're really simple. The payoff diagram for buying a stock.

**:** Put call.

**:** Is just linear, right? It just goes up like that. Because the price of the stock goes up, your payoff goes up by the same amount. The delta is one. Just like we were saying before.

**:** And if you short it, if the price goes up, then you lose money.

**:** And this one on the bottom.

**:** Is the payoff of.

**:** A bond. So if you buy a bond, you're going to get an amount of money in the future that's fixed.

**:** So your payoff is going to be the same no matter what.

**:** The price of the underlying is and.

**:** If you're selling a bond. Yeah. So you're borrowing money. Then it's going to be reflected, Right. It's going to be negative. But they didn't have that graph. But you can visualize. It's just negative line. So why do we need these PF diagrams? Because I want to. Talk about Put call parity. Has anyone already heard of protocol Parity?

**:** No. Okay, that's good. Then I'll be the first to explain. It's kind of a weird concept, but it basically says that if there's no arbitrage, you can reconstruct an option.

**:** Using a mix of the asset like buying or selling the asset. Debt. Buying or selling the debt.

**:** And buying or selling another option.

**:** And we do it with calls inputs. So my question is, how would you construct a call?

**:** Using the asset.

**:** A bond selling debt and a put.

**:** So this is the formula.

**:** I don't know how to drive it. But this is. This is the formula. We can look into that later, like how you derive this formula, or we can show why it works. And we're going to do that. We're going to show that the payoff diagrams are completely equal.

**:** But this is basically the price of a call.

**:** Plus the present value of the payoff of the bond.

**:** Equals the price of the put plus the price of the stock.

**:** And these signs on the right are pretty helpful. For what? Long, what short means. The only one that's a little confusing, at least for me, is if the bond one is positive or negative. If it's positive means you buy a bond, so you're going to get a payoff in the future.

**:** It all depends on what you do in the future.

**:** So if you receive money in the future,

**:** You buy a bond, you receive payment in the future, and it's positive. If you're borrowing money, you're going to have to pay that back in the future, so that's the negative payoff.

**:** Okay, cool.

**:** So how do you construct a call using asset bond input?

**:** Oh, I know. That's how we prove it. Okay, does anyone. Can anyone kind of tell me how you've constructed call using asset buy input? I haven't really explained the process of doing this, but if anyone knows, then give a shot, or else I can just explain it myself.

**:** No. All right, no worries. Let's do it.

**:** So you want to construct a call. So we're going to isolate C, the press of the call. So if we move around the equation, we'll have C equals P plus S minus present value of X.

**:** Does that make sense if I'm kind of seeing that?

**:** C equals p plus s minus pv of x. So a call.

**:** Is going to be.

**:** Buying a put.

**:** And.

**:** By the stock.

**:** And negative of the bond is borrowing.

**:** So you borrow money.

**:** And that's going to be the same payoff as just buying a call.

**:** Of course. You have to make sure the parameters are all the same.

**:** But that should mimic exactly what buying a call is. Does that make sense?

**:** I didn't show it, like, visually.

**:** But that makes sense.

**:** Can someone construct a put for me?

**:** How would you construct a put without using input?

**:** Well, you could just buy a call along the call.

**:** Buy a bond and short the stock. Correct. Okay. Amazing.

**:** Awesome.

**:** Okay, so now let's show why put call parity works. Shall we? All right.

**:** And the way we're going to do this is. Oh, wait, no. This is the. This is the payoff of the call.

**:** Yeah.

**:** Okay, so let's show that. What I said for reconstructing. Call it. Let's see why it works. So we do this by combining the payoff diagrams.

**:** So on top here we have the long. Put on the bottom we have the long call.

**:** So it's the p plus s.

**:** One who stood on the round part of the stage so she looked dead.

**:** Passing the phone to someone who thought the run through was over, so she played the curtain paw music during the last scene.

**:** Passing the phone to someone who started eating his prop too early because he was hungry.

**:** Passing the phone to someone who had to learn how to kick a soccer ball.

**:** Passing the phone to someone who almost fell off a two foot tall wooden block.

**:** Passing the phone to someone who stood on the wrong part of the stage so she looked dead.

**:** Passing the phone to someone who thought the run through was over, so she played the curtain paw music during the last scene.

**:** Passing the phone to someone who started eating his prop too early because he was hungry.

**:** Passing the phone to someone who?

**:** Had to learn how to kick a soccer ball.

**:** Passing the phone to someone who almost fell off a two foot tall wooden block.

**:** Passing the phone to someone who stood.

**:** In the wrong part of the stage, so she looked dead.

**:** Passing the phone to someone who thought the run through was over, so she played the curtain paw music during the last scene.

**:** Passing the phone.

**:** To someone who started eating his pop too early because he was hungry.

**:** Passing the phone to someone who had to learn how to kick a soccer ball.

**:** Passing the phone to someone who almost fell off a two foot tall wooden block.

**:** Passing the phone to someone who stood on the wrong part of the stage so she looked dead.

**:** Passing.

**:** What?

**:** The fuck?

**:** Turn.

**:** Down.

**:** For.

**:** What?

**:** 's your name?

**:** My name is betsy.

**:** Where are you from?

**:** I'm from china.

**:** What was your expect?

**:** Ation of us before you've ever.

**:** Come here.

**:** Financial center technology.

**:** I thought like all the city should be like the daisies. Breaking math. But actually what kind of like Chicago and New York or mega CDS when you first got here? I suppose the reality subway station was kind of dirtier than I expected. It's between New York then I got a chance to visit now in Chicago. And I realized that different cities are kind of different in its street views, in stability. What are some of the big diptamathas to try? What many site is the best cheese?

**:** Tonight.

**:** I don't.

**:** Want to see that.

**:** The diaphragm.

**:** Jelly is in.

**:** My.

**:** Defenders.

**:** Are on the show.

**:** Tonight.

**:** Share.

**:** This with a friend that you want to go.

**:** If you're sun.

**:** As one of the only.

**:** People.

**:** Really?

**:** Think.

**:** Come on.

**:** Look.

**:** He?

**:** Said.

**:** Grun.

**:** Nopo no mt.

**:** A hot that shit.

**:** We're not.

**:** Fucking on mt.

**:** Yet.

**:** Hop that shit.

**:** We're not.

**:** Poker? No, mg.

**:** A.

**:** Hot that shit.

**:** Come on.

**:** We're not fucking.

**:** On mca.

**:** Hot that shit.

**:** We.

**:** Don't have.

**:** No.

**:** Bless you.

**:** Put homage.

**:** On fire.

**:** I don't see.

**:** Earhart.

**:** Oh, yeah.

**:** Sorry. I need to get this. No, you need to turn it off.

**:** Your honor.

**:** I'm a trauma surgeon at St. Bonaventure and I'm on call.

**:** Five.

**:** Minutes.

**:** How wonderful.

**:** Take a seat until your case is called.

**:** Oh, my case was called. You said I could have a five minute break.

**:** The court.

**:** Took a five minute break.

**:** Yours is going to be considerably longer.

**:** I am so sorry.

**:** That my two minute phone call was such an incredible inconvenience. But I went out of my way to be here today to have my case heard.

**:** And that is exactly what I'm going to do.

**:** Now.

**:** Can I have?

**:** Dr Lims file, please.

**:** I promise this won't take long, because as I started to explain,

**:** Guilty.

**:** $1,500 fin.

**:** E and license suspension for one year.

**:** You can't do that.

**:** I have a.

**:** Thick book in my office that says I can.

**:** No, this is America.

**:** I pay taxes which pay your salary.

**:** By the way.

**:** You can appeal.

**:** This verdict to a different.

**:** Judge. I don't want a different judge.

**:** I want this one to do her damn job.

**:** Sorry.

**:** I need to get this. No, you need to turn it off.

**:** Your honor.

**:** I'm a trauma surgeon at St. Bonaventure and I'm on call.

**:** So.

**:** Five minutes.

**:** I don't know.

**:** Don't.

**:** Worry.

**:** Because the British.

**:** Acting a bit.

**:** Warm.

**:** Yes.

**:** That's how important.

**:** Harry potter.

**:** 's all.

**:** Right.

**:** Where?

**:** Are you heading to right now?

**:** Today.

**:** I'm racing the j.

**:** Train.

**:** In Broad street to Jamaica center on my bike.

**:** Let's go. How you doing, man? I'm going to race this train to Jamaica Center. I'm a bike. What is it that you're going to do? You're going to ride the train or going to run out of the station and I'm going to bike Jamaica Center. I'm going to beat this train. You're going to cross the bridge. Yeah, across the bridge.

**:** Don't say I didn't tell you. Nice to meet you. Make 14 miles already?

**:** This is my first ever bike ride with pigeon pedals. I use GS Bala. I totally screwed up the rally. Construction everywhere successfully unclip the lighting. Come on. Look at this. It leaves Blake Friendly Road. I could have paid like some hot spore.

**:** Moth gravel.

**:** I.

**:** Mean, they also have a navigator this whole time.

**:** Hope he gets the job. Ridiculous.

**:** Come on.

**:** I'm being endless chaos.

**:** Dudes are so tight, they have wrong turns.

**:** Around.

**:** 55 minutes, it's going to be closer on fire.

**:** Come on.

**:** I don't know where.

**:** Everyone is him.

**:** Headway. Let's go. You beaming here Today I'm racing. Moment I open the front door.

**:** Froze. My wife was tangled up with another man.

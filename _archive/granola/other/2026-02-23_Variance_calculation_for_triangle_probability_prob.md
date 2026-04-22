# Variance calculation for triangle probability problem

**Date:** 2026-02-23


## Summary

### MSE Calculation for Problem 4B

- Variance of Z = 1 (given in problem)
- MSE formula: E[(Ẑ - E[Z])²] = Var(Ẑ)
- Simplified approach using variance properties:
- E[Ẑₙ] = (1/n) × Σ E[Zᵢ] = E[Z] (since all Zᵢ are identical)- Var(Ẑₙ) = (1/n²) × Var(Σ Zᵢ) = (1/n²) × n × Var(Z) = 1/n
- Final constraint: 1/n < 0.1, therefore n ≥ 10
- Need n = 10 (not 9) since requirement is strictly less than 0.1

### Problem 5: Triangle Count Variance

- Goal: Find variance of N (total number of triangles in graph)
- N = Σ I(uvw is triangle) where I is indicator function
- Variance formula: Var(N) = E[N²] - (E[N])²
- E[N] known from previous problem: (n choose 3) × p³- Need to calculate E[N²]

### Expected Value of N² Calculation

- N² = (Σ I(uvw))² = Σ Σ I(uvw) × I(abc)
- Case analysis for triangle pairs (uvw) and (abc):
- **Same triangle (uvw = abc)**
- E[I(uvw) × I(abc)] = p³- Occurrences: n choose 3
- **Share exactly 2 vertices**
- 5 total edges needed- E[I(uvw) × I(abc)] = p⁵- Occurrences: (n choose 3) × (3 choose 2) × (n-3)
- **Share ≤1 vertex**
- 6 total edges needed- E[I(uvw) × I(abc)] = p⁶- Occurrences: (n choose 3)² - (n choose 3) - (n choose 3) × 3 × (n-3)

### Final Variance Formula

- E[N²] = (n choose 3) × p³ + (n choose 3) × 3 × (n-3) × p⁵ + [(n choose 3)² - (n choose 3) - (n choose 3) × 3 × (n-3)] × p⁶
- Var(N) = E[N²] - [(n choose 3) × p³]²
Chat with meeting transcript: https://notes.granola.ai/t/edb3a5f8-5ffc-4556-bd0a-38927029854d


---

## Transcript

**:** Yeah, five is a bit difficult.

**:** Yeah, I got lost in the major step.

**:** Much appreciated.

**:** So.

**:** Mse is.

**:** So the variance of z is 1.

**:** That's just.

**:** By the problem.

**:** Yeah, they told us that supposed variance of Z is known to be.

**:** I didn't just make that up.

**:** What is that one?

**:** Yeah.

**:** So I think.

**:** This? I don't know. This is a bit very complicated.

**:** I want to suggest a simpler way to think about the mse. I think this looks all correct so far.

**:** The other way to think about the msc is.

**:** So msc.

**:** Okay?

**:** So we write out the formula again. So this formula is correct, right?

**:** So expected value of expected value.

**:** See?

**:** All right, I'll do this.

**:** Squared.

**:** Right.

**:** And so what you can do is. So this formula.

**:** Is actually just.

**:** So because.

**:** Since the expected value of c hat.

**:** N equals. So this is one over the sum.

**:** Of the expected value of any single.

**:** Let's say z1 or zk equals 1n.

**:** And so this is actually just the expected value of Z.

**:** So this is like each expected value of Z times N divided by N, so it can't simplifies to this.

**:** So expected value of z hat equals expected value of Z.

**:** And so this is actually just.

**:** The variance of.

**:** Zha.

**:** What do you build?

**:** What did you build? What do you build?

**:** O.

**:** Just plugging in a definition.

**:** One hat.

**:** Yeah, so maybe.

**:** One to n right.

**:** And then how do we simplify this?

**:** Any thoughts here?

**:** You know that. So you first know that you can just multiply is a 1 over n is a constant. You can take it out and make it 1 over n squared.

**:** Yeah, that's good.

**:** And since all of.

**:** The z's are iid, you can turn the variance of the sum into.

**:** I believe.

**:** The product.

**:** Actually, it's just the sum. Oh, just the sum. Okay. Yeah. So the formula is kind of like if I have variants of x plus Y.

**:** Then the formula is kind of like,

**:** Variance of x plus variance of y plus.

**:** The two times, like the covariance of x and Y. And then this is if it's a minus here.

**:** That's minus here.

**:** So in general, you just generalize this to some of n. And so, right when things are independent, this guy goes away.

**:** This covariance term is always zero for independent variables.

**:** Right. Oh, I see.

**:** And then you generalize.

**:** This and you get right so you can take the sum out.

**:** Of ck, right? And variance of zk is just 1, so.

**:** I would get 1 over n squared times n, which is 1 over n, and that has to be less than.

**:** 0.0. Okay, I see.

**:** I get 100.

**:** Ah0.

**:** Yeah, very good.

**:** Right.

**:** So you need it to be. Yeah, you need. So what's.

**:** The. So you want. You want it to be less than 0.1, not equal to. So you actually need to go one up.

**:** Right.

**:** Exactly.

**:** Wow. I see.

**:** Okay?

**:** Yeah.

**:** Expect to so extract hit a value.

**:** Of Z of N right here. I just want to make sure what you did was expected value C sub N.

**:** Expected value of Just plug In the definition 1 over n equals 1.

**:** And then you just.

**:** Could you take this out?

**:** Or actually also just sum out and then you're just left with the just expectation. Yeah.

**:** Oh, I see. Okay, that makes a lot more sense.

**:** Yeah, I'd say that's the main trick here, rather than having to expand everything out. It's nice if you can relate it to yeah, it's nice that you can relate it to a variance of something and then use our nice rules of how to.

**:** Take variances of sums and linear combinations.

**:** Yeah, I did think that the MSC did look up quite a bit similar to Expect. I mean, the variance formula, I couldn't figure out, like, how I would connect it.

**:** Right.

**:** Okay?

**:** So I think, and then so.

**:** Yeah.

**:** Any. Any other questions about 4B? I think.

**:** If not, I think I want to go to five. I think that's the next request.

**:** Good. Thank you.

**:** Of course.

**:** Hi, Skyler. Could I ask.

**:** Hi.

**:** So how far maybe have you gotten with five? So.

**:** Yes. So I wrote.

**:** The variation of I said n as the total number of triangles in the graph.

**:** The expected value of n squared minus.

**:** The expected value of N squared. I'm saying that terribly. I should probably just write it down.

**:** Give me one sec.

**:** But. Yeah, I just wrote the variation formula that splits up the expected returns into. We know, the second term.

**:** From, I guess the previous problem. The term that I'm struggling on is the expected value of N squared. I'm not sure if that's even the right path to go about this question.

**:** It's just the path that I sort of went.

**:** Right.

**:** So n squared.

**:** Sorry. I missed something. So when you. Well, so n was just the number of triangles.

**:** Yeah, the total number of triangles in the graph. So then we should be.

**:** I can't really. Are you? I can't really see if.

**:** Oh, yeah. Oh, I should jump on right now. I'm jumping on as we're saying this. Sorry about that.

**:** You're writing.

**:** Oh, thank you.

**:** Yeah. No. Yeah. This is very new for me, too. Like a. Yeah, this kind of snow storms.

**:** Yeah. Been back to Covid days, right?

**:** Haven't really used.

**:** Yeah.

**:** Okay, give me a second. Jumping on.

**:** So yeah.

**:** All right, I think.

**:** I guess in the meantime, I think what I'll say is, like, so.

**:** How do you. Yeah, the thing is.

**:** Like. So do you have, like, a formula for n?

**:** Yeah, let me write that down. So.

**:** Okay? Yeah, I can.

**:** See?

**:** So I wrote.

**:** The normal, I guess, formula that.

**:** We've been using, and then n.

**:** Is.

**:** Number of triangles.

**:** And then our goal is to find the distribution of the number of triangles.

**:** Yeah.

**:** Write the number.

**:** So we know you have n is.

**:** And choose here and then pq.

**:** 3 and then P cubed.

**:** Yeah.

**:** So that's easy for this. It's just this term right here.

**:** This is.

**:** Where?

**:** My intuition is that you got to split it between all of the cases, right? So you got, like, case one in which.

**:** You have zero or one vertices shared.

**:** And then you have a case two where.

**:** You got two vertices shared.

**:** So, like, two people are already connected, so they have different probabilities.

**:** And then. I mean, that's. That's the two cases I've thought, because there's all three. Key. Maybe case three is they're the same exact triangle.

**:** Yeah.

**:** That's very good.

**:** But that's pretty much like, how do. I don't know how to count any of these guys right here.

**:** So, like this one. I don't know how to count. And then this one.

**:** I also don't know how to find the probabilities.

**:** Of that. So that's. That's kind of where I got stuck.

**:** Right.

**:** Okay, so.

**:** Yeah. So I think this is definitely the right idea.

**:** And I know covariance is involved.

**:** But I recommend, like, it's kind of so. Kind of like.

**:** How maybe the solution for Write the expected value of n last week or in the last problem set.

**:** So maybe to write.

**:** So to write out.

**:** So n is like.

**:** So write it in terms of, like, indicators so that. Yeah.

**:** Okay?

**:** So this is triplets uvw in the vertex set.

**:** Right.

**:** And then.

**:** Maybe I'll just do indicator.

**:** So.

**:** U v w.

**:** Is a try angle.

**:** Yeah, maybe. And then.

**:** Maybe I'll condense the notation so that this is just.

**:** Sort of. Again, the same.

**:** I'll just call this something like.

**:** Let's call it maybe just X, I guess.

**:** Or. Yeah, that's good enough.

**:** Okay?

**:** Right. And then. So then.

**:** Write n squared.

**:** Is, then just.

**:** Some.

**:** U v w.

**:** X will give vw.

**:** Squared.

**:** And then now I'm going to do.

**:** So I'm just going to break up the sum or break up the product.

**:** I'm going to label the vertices differently.

**:** So that we can go through this kind of case work of.

**:** When.

**:** When of the vertices are the same or all the vertices are the same.

**:** So I have.

**:** This kind of product.

**:** Abc.

**:** Okay?

**:** So what's the difference between indicator variable and then the I versus the x? What's the difference?

**:** Yeah, there's. I just wanted to make this notation more compact.

**:** Okay, that's. Yeah, fair enough.

**:** Maybe I could write.

**:** I could just write this as I maybe.

**:** That's that.

**:** 's fine.

**:** Okay?

**:** Too.

**:** Appreciate it.

**:** Just to make it clear, that's an indicator.

**:** Okay?

**:** Okay, so we have.

**:** Now. We need casework. Yeah.

**:** So depending on.

**:** Right, what happens?

**:** Oh, whoops.

**:** Oh, I should have done it like this, rather.

**:** So I want to. I want to just. I want to.

**:** Get rid of the product of two sums it by kind of just. I want to distribute, really, is what I wanted to do.

**:** Where's my.

**:** So I need to sum.

**:** Over.

**:** Uvw and abc. These. These are both subsets.

**:** So two different triangles. There's U, vw and then there's abc. Is that correct? Okay.

**:** Yeah, that's exactly right.

**:** Okay?

**:** Yeah. So. Yeah, case one. Yeah, case one.

**:** So the easiest case is probably when that's just the exact same triangle.

**:** So you have u vw.

**:** So, yeah, I'll just write out.

**:** U v w equals abc.

**:** And in that case.

**:** Yeah. In that case, then.

**:** I of u v w.

**:** Times I of abc.

**:** Equals.

**:** Uvw squared.

**:** Right. And then this is.

**:** Since since the values of this indicator are only 0 or 1 and squaring it doesn't change the value.

**:** So it's just P cubed minus P to the.

**:** Six.

**:** I think I'm jumping ahead. Keep going. Sorry about that. Keep going.

**:** Yeah, I think you're. That's the right idea. Yeah. If you can jump ahead.

**:** Yeah, that's good.

**:** Yeah. So this the expected value?

**:** Yeah, right. This is just.

**:** P cubed.

**:** Is it?

**:** Wait. So these are the same triple. What? Is it the same triangle?

**:** Yeah. So it's.

**:** The yeah, right. It's like I'm taking the product of.

**:** When the two triangles. I'm trying to find. What's the value of all the terms when the two triangles are identical?

**:** Oh, yeah, okay. Yeah, no, that makes sense.

**:** So then do we need to find the variance from case one, or can we just.

**:** Is that the next.

**:** So yeah.

**:** So, actually. So what? I'm so right? As you said before, like, we know this guy, right? The expected value of N squared.

**:** Yeah.

**:** So what I want to do is compute the expected value.

**:** In the box of expected value of N squared.

**:** Yeah.

**:** I'm going. So once I compute the expected value of this guy,

**:** For each of the cases.

**:** And then sum up using.

**:** Then I use linearity of expectation to combine all the cases. Basically.

**:** And, yeah, that'll get you.

**:** Yeah. So I guess. Does that make sense? Like, you. You don't.

**:** Okay?

**:** At the. At the end, we'll compute the variance by subtracting.

**:** Expected value of N squared.

**:** So is it. Are we talking about each individual?

**:** Eventually you want to do something like this, right?

**:** And then. Is that what you would do, or is this too much work?

**:** Would you find the variance of every single individual case and then add them up?

**:** Yeah, I guess what I want to do is so I.

**:** Want.

**:** My goal is to compute the expected value of N squared, right? This guy.

**:** Y.

**:** Eah.

**:** And so.

**:** So bilinearity of expectation this will be.

**:** So this will be equal to. First of all, it's going to be the sum over the I u v w.w. i of abc.

**:** And then.

**:** I'm going to at the end, once I. Once I compute how to do it for all these different cases.

**:** I'm going to take the sum out and then.

**:** U, v w r f a, b c.

**:** So actually.

**:** This thing is all I need, really, for each.

**:** Oh, yeah, you're right. And then you just add them all in. Okay. Okay. That actually makes it a lot easier.

**:** So then can we keep going through, I guess, all of the.

**:** Cases, and then, yeah, let me just erase my part.

**:** Right.

**:** That's case one.

**:** So this is when the triangles are exactly the same. They share all three.

**:** Okay?

**:** Right.

**:** And then. So case two. Yeah, case two.

**:** Then this is going to be like your case one, so that there's. Or actually, no, I think it's. It's easier to do two vertices.

**:** Sharing two vertices.

**:** Yeah.

**:** Shared exactly two vertices.

**:** I'll just erase mine. Just that. I'll get confused. But, yeah, we got the point.

**:** Yeah.

**:** Right. Share. Exactly.

**:** Yeah. So I guess a picture, I guess, of what this will look like is, like.

**:** So we have something like.

**:** U v w. This is a triangle.

**:** And then let's say they have shared vertices are V and W.

**:** Let's we could just say this is.

**:** Equal to B or something, and this is equal to A.

**:** So. Because they're shared. Yeah. So the picture is something like this.

**:** Yeah, that's what I have. Down for mine, too.

**:** Yeah.

**:** Cool.

**:** Right.

**:** So basically, the point is that there's only. So you need five connections.

**:** You need five. Like matches. Right. And so.

**:** So.

**:** Similar to how you. How we did last week, like.

**:** Yes.

**:** Oh, because there's five edges right here, right? 1, 2, 3, 4, 5 edges.

**:** Four people, but five edges.

**:** Yeah. And you need.

**:** Yeah, right. And then.

**:** This case. So I u v w times I abc equals 1.

**:** If and only if.

**:** All five edges.

**:** Match, I guess, right?

**:** Yeah.

**:** So? So you need like so. Otherwise every other time it's zero.

**:** So to compute the expected value.

**:** It's basically just the probability that all five edges match. So then this is.

**:** The probability rate is just P to the 5, right?

**:** Correct? Yeah.

**:** Is there. Is there, like, covariance involved in this one, though?

**:** Or is it?

**:** So.

**:** Covariance.

**:** All we're doing is just computing.

**:** So, I mean, there is no covariance involved. I mean, all we're doing is.

**:** I guess. Right, so.

**:** Yeah, the probability.

**:** I think the trick is that.

**:** I mean, it's just.

**:** It's just the probability that you get five edges that match, right?

**:** Oh, so it's just. Okay, so I might be overthinking it.

**:** Then.

**:** Or I'm not sure if.

**:** I guess when you said saying what, did you. Yeah. Mean when you said, like, do you have to account for the covariance?

**:** Because I'm assuming that there's, like, some.

**:** So it's.

**:** I was wondering if there was, like, if. Because there's one shared edge that's not, like, boost, like, the probability. That's why I had no idea.

**:** I'm not sure, because if you. It's like this, like, base or anything that I was thinking, like, if it was given that shared edge, do we, like, if that was matched, then do we know a little bit more about.

**:** The. The other edges, it doesn't give it an increased chance, but I'm not sure if that's overthinking the. The problem.

**:** That's why I thought there was some evolved, but that's why I wasn't sure either.

**:** Yeah. I mean.

**:** So still. So let's see. Yeah, let's. Even if you have.

**:** So basically, I guess the thing is that all the. Yeah, all the matches are independent. So even if you had these, this vW match or AB match.

**:** Like the matches between au and or vw and v.

**:** Sorry, Vu and uw. Each of these are still with probability P. And those are all independent of each other? Yeah.

**:** Got it.

**:** I see. Okay, that. That actually makes more sense. I got confused by my own logic, so, yeah, no, appreciate it. Okay.

**:** Sweet.

**:** Yeah.

**:** So then after we do that, we're doing share. Exactly. Just one verse. That. Right. So just one shared person. Okay.

**:** So yeah.

**:** You want to? Can you? I. Would you be able to?

**:** Write it in. Yeah, of course.

**:** I go ripple.

**:** The case.

**:** Oops.

**:** Sorry. My.

**:** Oh, it's dead.

**:** Yeah. Let me see if I can just write it.

**:** Okay?

**:** I'll use my mouse, but that's, like, significantly worse. Hammer.

**:** You can just dictate it, I think. And I can write it, if that's easier.

**:** Sure. So.

**:** So yeah, the case three is share.

**:** Share just one vertice.

**:** Yeah.

**:** Exactly.

**:** One verte.

**:** X.

**:** The picture? Yeah, it's something like.

**:** So you just get, like, two triangles, and they're like, kind of like, I don't know how. That's really bad like, that.

**:** Right. Exactly.

**:** Cool. All right. Yeah, good enough.

**:** W.

**:** Let's call this ab. I don't know.

**:** W equals c.

**:** Very good. Yeah.

**:** And so.

**:** Yeah, one is. So the question is.

**:** When is this product.

**:** Sorry.

**:** So there's, like, there's six distinct edges, so I'm assuming it's just P to the six.

**:** Yeah, basically. Yeah, exactly. Right.

**:** Cool.

**:** So if and if, if and only if, all six edges.

**:** Are present or match? I'll just. I like this. Match is fine.

**:** And so the logic is, yeah, right.

**:** Again because so every other time it's zero.

**:** So it's because it's only zeros and ones, like it's an indicator.

**:** Or product of indicators.

**:** Then to compute the expected value only need the probability that.

**:** That you observe a one.

**:** And like as just as you said, this is P to the sixth. So this expected value is P to the six.

**:** Okay, so, yeah, those are. And those are all the three cases. There's no.

**:** Other case because they need to share at least one vertex.

**:** Yeah.

**:** So that's. So, yeah. So those are the three cases, and then.

**:** We need to count how many times these occur, right?

**:** And then.

**:** Exactly.

**:** Okay, so I'm just.

**:** Do you want to start off case one?

**:** Yeah, Case one is probably the easiest account.

**:** So just be.

**:** N. Choose three. Choose two.

**:** So you're only for. Yeah, so. Because they all have to be. So once you pick UV and W, your hand is forced for A, B and C. Right. So actually it's just the number of triangles. U, VW.

**:** So just mg3.

**:** Yeah.

**:** Okay?

**:** Very good.

**:** Number is just N. Choose three.

**:** Okay?

**:** So.

**:** So we got that, and then.

**:** Or maybe.

**:** The.

**:** Put a column here that says.

**:** Num.

**:** Eric occurrences, let's say. So this is.

**:** N choose three.

**:** Okay, now.

**:** Share.

**:** Exactly two for the cs.

**:** Two vertices.

**:** Okay?

**:** Yeah, I might need some help on this one.

**:** So, yeah, the first thing is let's. Okay, so let's start with just counting.

**:** We still have to start again with, like, counting the number of just a single triangle. So we start with a factor of N, choose three.

**:** Okay?

**:** And then we have to count how many ways there are to pick the shared vertices, right?

**:** So, like, there's two shared vertices.

**:** How many ways are they to choose the two?

**:** How many ways are there to choose the two shared vertices from the three already existing vertices? U VW.

**:** Wait, how many. How many ways to choose the. The C, Right? Are we talking about C?

**:** Or I guess, like here. I'm talking about ab. Yeah. So how many ways are there to choose abc or two of two of ABC to overlap with U, V and W?

**:** Okay?

**:** So it's like, how many ways did it choose?

**:** Might give it away if I say more.

**:** Okay. So it should be there. Should be. So you have to choose.

**:** For the two shared people.

**:** That should be N choose two.

**:** And choose two. And then for the two other people is it you discount the two, so it would be N minus two, choose two.

**:** Let me just write that down. I don't know.

**:** Let me see if I can. Yeah, I might. I'll just use my mouse.

**:** And just.

**:** N choose two.

**:** And then that's. That's for the two shared people.

**:** And then n minus 2.

**:** Just for the other people.

**:** You can see that she's two of those.

**:** Is that?

**:** Is that a way to do it?

**:** I don't think so. Yeah, I guess what I was trying to say is.

**:** So let's say. So this number here, the first.

**:** Number N. Choose three. Right. So that's like we first start out by picking U, V and W.

**:** This is like to pick UV and W. There's n choose three ways.

**:** And then from. From UV and W. You need to pick two that match, or you have to pick two to label.

**:** A, b or c, right?

**:** Y.

**:** Because they need two shared. So that's. You need to pick two from the three. So that was three, choose two.

**:** Eah.

**:** And then there's one last guy.

**:** Yeah, there's one last guy's remaining.

**:** So how many ways are they to pick? So we already picked three guys.

**:** And so.

**:** There's N minus three ways to pick the last guy.

**:** N minus three and then.

**:** So n. Choose three. Three. Choose two.

**:** How'd you get.

**:** Yeah. How'd you get three? Choose two. Again. Sorry.

**:** Let me try to follow.

**:** Yeah. So that's from.

**:** That's why. So at the first step I fixed, I've got my uvw, right?

**:** Yeah.

**:** I picked it out. Let's say so now.

**:** Now. I need to pick. I need to pick.

**:** Two to label.

**:** Either ab or ac or bc.

**:** And there's three. Choose two ways to pick.

**:** Which subset of u vw.

**:** Should share with the second triangle.

**:** I see.

**:** Well, I think this might. Let me check.

**:** But. Yeah. Oh. That's why I was. I wasn't sure if it's the same.

**:** It might be the same thing because n choose 3. It cancels out because this would be n minus 3 in the denominator, right? And then I'll cancel out, and then It'll be N minus 2. It might end up being.

**:** Yeah. That's why I think it could be the same. Yes.

**:** But honestly, yours is way more intuitive.

**:** Like now it makes entry.

**:** The yours was like.

**:** So you first picked the two that are shared, and then.

**:** And then. Yeah, and then you subtract the two. But then I didn't. I used the vertices, not the. Not the edges. And honestly, the edges make more sense.

**:** I think. Yeah. Actually, now I think about. Yeah, I think it has. I think these have to be the same kind of. Because here's logic is.

**:** So I. I pick the two guys that will be shared.

**:** And.

**:** They're only.

**:** Oh, yeah. And this is a two. So. And then there are two remaining vertices, or N minus two remaining ways to pick the last two. Guys. So. Sorry. Yeah, I think I misunderstood here.

**:** But, yeah, I think it should be correct.

**:** You're good.

**:** No, I think. Yeah, I think.

**:** I barely understood my. My logic too. So that. So there will be N. Choose three. Three. Choose two. So that's the number for the. The two vertices.

**:** And then for the one shared person.

**:** Yeah.

**:** I'm assuming.

**:** Should it just be?

**:** For two shared.

**:** Yeah, for case three. What?

**:** Yeah.

**:** So the idea is you can just kind of. So we know that the total number of ways just be the total number of ways to select two triangles.

**:** Forget about, like.

**:** Whether.

**:** Right? Yeah. The total number ways to select two triangles that share at least one edge should be N. Choose three.

**:** Times.

**:** And choose three.

**:** Is that correct?

**:** I think that's correct.

**:** So why is that?

**:** We're in. Choose three squared.

**:** Yeah.

**:** The idea is like, I'm just going to do. I'm going to count the total number of ways to.

**:** Select two. Try or. Yeah. Make two triangles. Form two love triangles.

**:** And then subtract all the other cases.

**:** Yeah.

**:** Yeah.

**:** Okay?

**:** Yeah.

**:** So just be N, choose three squared, and that's the number of triangles.

**:** So that's the total number of triangles. And then I'm just going to subtract the two other cases to get how many there should be in case three.

**:** Of case three.

**:** Okay?

**:** So you just minus and choose 3 and then minus entries 3, choose 2 and M times N minus 3.

**:** Yeah, yeah.

**:** Okay?

**:** Can you? Oh, sorry.

**:** I'm just curious.

**:** Can you do? End chiefs three times. Three times entries two.

**:** N Choose 3 is the number of ways to get the first triangle.

**:** And three.

**:** So. So you're saying.

**:** Sorry I missed.

**:** Ancestry times 3 times n, choose 2. Like it's just using the same logic as piece 2.

**:** Where the first one is like, oh, yeah. So three is like the number of ways to label those shared one abc.

**:** Right? Yeah. And then this is the other two.

**:** I think so. It might have to be.

**:** N minus 3. Choose 2.

**:** Because we've already picked out three vertices.

**:** And minus three.

**:** Yeah.

**:** I think that's correct.

**:** Too.

**:** Yeah.

**:** So this. I think I messed up.

**:** So I actually don't.

**:** Yeah. I think we still have to care about cases where the three triangles share zero vertices.

**:** So I think this should. This should really be.

**:** Share.

**:** Less than two vertices.

**:** So it cuts with zero and one vertices.

**:** Then.

**:** Right? Yeah. So it counts, then. Yeah. So now. Yeah.

**:** Okay?

**:** The subtraction actually makes sense.

**:** That's what. Sorry.

**:** No, you're good.

**:** And then I'm not sure if this method.

**:** I guess.

**:** You could, in theory, extend to a case four where they share zero vertices.

**:** And then you'll end up with the same thing.

**:** So.

**:** It's the same piece to the sixth thing.

**:** Expected value, so.

**:** It's simpler, actually, just to count when they're. Yeah.

**:** Because it doesn't change the expected value.

**:** No.

**:** At all.

**:** So when you. When you carry out this.

**:** This. When you carry out this.

**:** It's just that it saves you from having to count an extra.

**:** Oh, yeah.

**:** I can explain the strategy.

**:** This is problem five again.

**:** So the strategy is like,

**:** So similar. Similar to.

**:** How you might have done it last week. What. What we're going to do is so N will be the num. N is like the number of triangles.

**:** And now what I want to do, what I'm doing is, like.

**:** I'm writing, and in terms of.

**:** As a sum of indicator functions.

**:** So it's the sum over all subsets.

**:** Of the vertices.

**:** And then this indicator takes the value 1. If u v w forms a love triangle.

**:** Zero otherwise.

**:** And I just call that for making the notation more concise. Just this random variable, this indicator, is going to be I, U, V, W.

**:** And then.

**:** So.

**:** Right. And then I square it, because what I want to. So we know from last week that the expected value of N is just n. Choose 3 times P cubed.

**:** Right. And so we from this the formula for the variance of n. So this we already know.

**:** Part. This part where.

**:** The expected value of n, we square the outside of the expected value. But we still want to compute. So the only thing we really need to do is compute the expected value of N squared.

**:** Inside the brackets.

**:** In order to get the variance.

**:** So what I'm doing here is I'm writing out N squared.

**:** As a sum of these indicators squared, and then.

**:** I kind of distribute.

**:** In order to make this as a sum.

**:** Yeah, to get rid of the square.

**:** And just write it as a sum. And the reason why I want to do that is because eventually at the end, I'm going to compute the expected value.

**:** I'm going to take the sum out using linearity of expectation.

**:** So. And okay.

**:** So. But, yeah, I guess your question was about. So why do we mean the cases?

**:** Yeah. And the reason why.

**:** Yeah, we need the cases because that's basically the only way to compute this product I U vw. This product of indicators of iu, VW and iavc.

**:** And so the logic is.

**:** Like so for case one. They all share vertices.

**:** The expected value there.

**:** Yeah, because.

**:** The probability of any match is independent.

**:** So you only need, like, three.

**:** People to match because the three people overlap entirely.

**:** So that's why the expected value is P cubed.

**:** Because this guy.

**:** This product of indicators takes the value 1 with probability P cubed all the three vertices, all the three edges are present.

**:** And zero.

**:** With probability 1 minus P cubed.

**:** And then you kind of do the same thing.

**:** It's just like counting how many edges there are. So this is when there are exactly two vertices there, there has to be five edges. And then so the formula is kind of like just the expected value would be P to the number of edges.

**:** Right. And so. And then the final case is when there are less than two vertices.

**:** Yeah, you don't really need.

**:** The sky. You don't need case four.

**:** Yeah.

**:** And then. So then after you find these.

**:** The expected value of each individual terms of these forms and the through the casework, then you need to count how many times you'll see.

**:** These kinds of arrangements of love triangles.

**:** In order to take the sum. Yeah. Oops. I erase that by mistake.

**:** And that's kind of where we are.

**:** Yeah.

**:** So do we add up all of these things so n of three times?

**:** So far.

**:** Right. Exactly.

**:** Sorry. Yeah, that was a bit long winded to explain it all again.

**:** Sir, just to make sure.

**:** When you say expected of IUV times a I abc like right here.

**:** It should be I of uvw iavc where the two are congruent, right?

**:** Yeah, like this is just in this specific case.

**:** No, like, it's a conditional expectation, right? So that's why we're multiplying it by the number of recurrences, because we're just using the telescoping rule or whatever.

**:** No. I guess so. Oops.

**:** So what the reason so it go. The reason why we need to multiply by the occurrence is kind of comes back to.

**:** This formula.

**:** So. So I'm taking this sum over u v w.

**:** And abc.

**:** That are subsets of the vertices.

**:** And then this is so this is, like, written in a kind of general form, like U V, W equals A, B, C. Like, if you have N people that you're trying to match.

**:** Or that could possibly form a love triangles. Then U, V, W could be 1, 2, 3, or it could be 2, 4, 6.

**:** Or it could be 3, 5, 7, or anything. As long as those numbers are between 1, n.

**:** And I guess that should be distinct.

**:** Or they don't have to be distinct, really.

**:** But that's kind of a degenerate case.

**:** But so anyways.

**:** So that's the reason why we need to count the number of recurrences is because we have to account for when it's one UVW equals abc.

**:** And uvw equals 1, 2, 3 or 2, 4, 6.

**:** Right, so we're not really using any conditional.

**:** Here.

**:** Any conditional expectation.

**:** Okay, that makes more sense.

**:** Yeah.

**:** And also luca. I guess I should. I don't know.

**:** Yeah. I wasn't so clear about this earlier, but I guess this formula n choose three.

**:** Times 3 times n minus 3. Choose 2.

**:** That is only true for.

**:** The like exactly one vertex overlaps.

**:** But I do need to account for the case when there's no overlap.

**:** And then. So that's why I guess I'm going to be using this formula I'm going to be using.

**:** The and choose 3 squared minus. And choose 3 minus. Whatever the remaining thing.

**:** Okay. Yeah. And so that would cover, essentially, case cover, case three and case four.

**:** Right. Exactly. Yeah. Because both of them do have the same peated power six probability. I mean, so whose expectation? So you can kind of just combine the two. Exactly. Yeah. Okay.

**:** Yeah.

**:** And then. Sorry.

**:** Oh. Oh. So that's why it's now less than 2.

**:** Okay?

**:** I notice.

**:** D that.

**:** Pieced.

**:** Yeah.

**:** Okay, so Sean is asking.

**:** So why do we have to compute the expected values separately?

**:** Yeah.

**:** So I. My. I guess.

**:** So do you understand, kind of what, Sean? Why we're doing this? Like, expected value of N squared term?

**:** Like why we're doing it.

**:** Yeah, because we're trying to compute the variants.

**:** Yeah. Yeah. Okay. So that makes. Yeah, I. I understand what, like, we're like. This is the hard term to calculate. I'm just confused why this is the way we're like. Well, I'm. I'm just confused.

**:** Why this is the strategy and why we have to break it up into cases like this as of now.

**:** Right. Okay, so.

**:** Yeah. So I guess the reason why we need to break it up into cases.

**:** It's basically just because the expected value of this product will be different in all these different cases.

**:** Going through each case individually. There's no kind of general formula for how to compute the expected value of iu VW times I abc.

**:** Why are we kind of doing it pairwise like that? Like, why are we doing expected value of two triangles?

**:** Necessarily.

**:** Right.

**:** The reason why we're doing it.

**:** Yeah. These kind of. We're taking this kind of product is because.

**:** It's that.

**:** So we're trying to count, like.

**:** So it goes back to first, like we have, the number of triangles is given as this sum.

**:** The sum of these IU vws. So that means, like.

**:** The sum over. So this I u v w is a random variable that takes the value one if u vw forms a love triangle.

**:** And zero otherwise. And so if you sum, these are just a bunch of ones and zeros. And so when you sum over all the possible.

**:** Like triple collections of three vertices in V. That gets you the value n. And we want to compute the expected value of N squared.

**:** So I'm literally just plugging this sum in and squaring, and then.

**:** And then I want to get rid of the square because I want. I want to be able to use my linearity of expectation rule.

**:** And so to do that, I just. I just, I. I break this square up into a product of some of IU vw. Like, maybe it's easier to write.

**:** I'm just doing I u v w.

**:** Times sum of I.

**:** Abc or something.

**:** All right? And then I'm. I'm using, like, a distributive rule in order to get.

**:** To a single sum rather than two sums.

**:** What do you mean? You're multiplying. Like, what is the sum of AI abc?

**:** It's basically just a repeat. Yeah, it's the repeat of the same exact terms. I just. I just labeled them ABC in order to make it clear that.

**:** The uvw.

**:** Like we're multiplying the indicator functions by each other. Is that the idea?

**:** Or no.

**:** Yeah, that's the idea. And then the reason why is because we really want to just compute.

**:** Yeah. And all I'm doing. I think I understand.

**:** Yeah, I'm using, like, a distributive rule.

**:** Okay. Okay. So sorry to make you explain this again, but I'm also a little confused. Like, why is the expectation of.

**:** Them. In my case, one like P cubed instead of P to the sixth, for example.

**:** If we're squaring it.

**:** Yeah.

**:** So for case one.

**:** Yeah, for case one.

**:** Actually, the square doesn't actually, because these. These guys are. They only can take values between or exactly 0 or 1. So my. The point is that squaring it.

**:** Doesn't change.

**:** Like you can only once you square zero or square zero or one.

**:** Yeah, okay.

**:** But that's different. In case two.

**:** So actually really? Like what?

**:** Why the difference between p cubed and p5 and p to the 6 in the different cases, it boils down to.

**:** The probability of.

**:** Of forming a love triangle in these cases, so.

**:** Right. In case one, you only have one love triangle, so that's U V, W.

**:** I have this in my head, like a picture, like this.

**:** And then each of these. Each of these matches are independent and occur with probability p. So I have probability P here, P here and P here.

**:** And I need all of these to occur.

**:** In order to get a value in order for this product.

**:** Iuv times iabc.

**:** To equal one.

**:** And every other time it will be zero.

**:** That's why I get p cubed.

**:** Yeah. Okay. Yeah, that makes sense. Yeah. The expected value. It only. Only affects. It is when this product can actually take the value of one. And that only happens with probability P cubed.

**:** Yeah.

**:** Sorry. Can you. Could you explain the number of occurrences?

**:** Then. Okay. Yeah. Number of occurrences. So the. Yeah.

**:** So the reason why I kind of need to do that is because I could, I have. So I'm trying to sum over all possible, like, pairs of two love triangles. So I could have, for instance, in case one, I could have if you imagine like you have NP or N is not a good number because I'M already using it. But say I have like 10 people, then I could have UVW is 1, 2, 3.

**:** Or 2, 4, 6, or 3, 5, 7. And I need. Basically, the expected value is the same in each of these cases, so I need to multiply by the number of times I can get those cases. Yeah, sorry, I understand, like, why we need to take it.

**:** I'm curious. Like. Like for case three, for example. Like, how do we get that? There's NT3 squared, minus entries three. Like, how do we get that?

**:** That's each of these are the number of occurrences. Right. Okay.

**:** So I guess the way to do it is to start with case. Go through the cases in order. That's the easiest way to explain it. So in case one, it's. That's probably the easiest one, is just.

**:** How many ways are there to pick three guys to form the love triangle?

**:** Because the other. Once you have. Once you fix the one triangle, the UVW triangle, then your hand is forced for A, B and C.

**:** And so.

**:** So the number of occurrences there is just N. Choose three.

**:** So once that's clear.

**:** Then to get case two is a bit trickier.

**:** So now. But again, this, the rule is kind of like,

**:** The first thing I do is pick how many ways there are to form the UVW triangle.

**:** That's again just n choose three.

**:** And now. Now I need to. The next step is I need to pick.

**:** From those three uvw, I need to pick two in order to form the vertices that overlap.

**:** In this picture, I need to pick a match. Or how many ways there are to have V and W. Pick two of the vertices. Yeah, yeah, exactly. And then why are we Multiplying by n -3?

**:** So n minus 3 is like how many? So there are three n minus 3 guys left, and there's only one vertex left.

**:** That needs to be picked.

**:** Because we. We started by picking three people out of N. That's the N. Choose three term. Oh, I see. I see. Yeah. Okay.

**:** And then. Sorry, the. The last one. I'm not suing. Last one is. So it's kind of a trick.

**:** It's just. You're, like, subtracting by case one and case two. Yeah. Yes, exactly. But. Okay. Yeah, yeah, yeah, yeah. The total is just N, choose three, like, squared.

**:** There's three ways to pick. Yeah.

**:** To pick two triangles.

**:** Regardless of any overlap or whatever, it's just n3 for the first and times n choose 3 for the second.

**:** Why don't we have to deal with the case when they share no versus vertices?

**:** Yeah, so that's. That's a good point.

**:** So. But the. The Strictly speaking, I guess case three should.

**:** It's technically accounting for it's counting.

**:** When they share less than two vertices. So that is, it's zero or one.

**:** And the reason why you don't need to break up.

**:** Into a case four is because.

**:** This expected value is just going to be the same in both cases. Yeah, it's just piece to the six. Oh, I see.

**:** Okay. Yep, that makes sense.

**:** Very good.

**:** And then you just try to simplify.

**:** Yeah.

**:** Okay, thank you.

**:** Sorry. My audio. Yeah.

**:** I just combined all of the probabilities multiplied by the cases and then just put it all on the formula. Is that it?

**:** What? Am I missing something?

**:** Yeah, this looks correct.

**:** That looks.

**:** Great.

**:** This is not an exponent. Right. The p to the 5 minus p to the 6, that should just. I think that was just.

**:** Yeah, it's not an exponent. My bad. Let me move it down.

**:** Like double oops.

**:** I just wanted to double check.

**:** Yes.

**:** Yeah, I understand.

**:** There you go. Okay. Yeah, that looks good. Okay, perfect.

**:** There we go.

**:** I appreciate it, Kyle. Thank you so much.

**:** Of course. Yeah, my pleasure.

**:** All right.

**:** Have a good one.

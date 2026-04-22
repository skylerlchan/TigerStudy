# ORF 309 Lecture: Probability and Stochastic Systems

**Date:** 2026-03-04


## Summary

### Poisson Process Fundamentals

- Connecting random variables to stochastic processes
- If X follows Poisson(λ), can associate with Poisson process N(t)- X has same distribution as N(μ) where μ is time parameter- Enables more flexible calculations using process properties
- Independence through increments
- N(μ) and N(ν) not independent when derived from same process- But increments N(u+μ) - N(u) are independent of previous intervals- Allows X + Y = Poisson(λ₁ + λ₂) when X ~ Poisson(λ₁), Y ~ Poisson(λ₂)

### Superposition Principle

- Merging independent Poisson processes
- Two streams: women arrivals (rate λ₁), men arrivals (rate λ₂)- Total process W(t) + M(t) is Poisson with rate λ₁ + λ₂- Proof requires showing stationary increments and independence
- Applications beyond customer arrivals
- Software engineering: syntax errors, logic errors in code- Any scenario with multiple independent arrival streams
- Key insight: superposition preserves Poisson property

### Thinning Process (Decomposition)

- Splitting single Poisson process into components
- Total arrivals: Poisson(λ)- Each arrival classified as type 1 (probability p) or type 2 (probability 1-p)- Results in two independent Poisson processes: rates λp and λ(1-p)
- Mathematical proof using indicator variables
- M(t) = Σ I{customer i is male} from i=1 to R(t)- Uses total probability and binomial distribution- Final result: M(t) ~ Poisson(λpt), W(t) ~ Poisson(λ(1-p)t)
- Counter-intuitive independence
- Despite R(t) being random, M(t) and W(t) are independent- Busy day effect cancels out due to Poisson memoryless property- Property unique to Poisson processes, doesn’t hold for all stochastic processes
Chat with meeting transcript: https://notes.granola.ai/t/f1ce79f8-035f-4564-b29e-1ac24b122813


---

## Transcript

**:** That's one. And this question?

**:** So the equation here is if they are both some processes and we know the rate, but the commission should have. Should also be a transform process. We. That's how we reach. There are two parts in life, right? One is using calculus.

**:** It's going to be okay. The other one is random process. We'll see how we can collect. How? The other path the new pattern will cover today. It would be a measure function.

**:** So what do we know?

**:** So we know that the other one, x, follows a plus on distribution.

**:** But we have no idea what some processes. We were just given a random variable distribution.

**:** How can I associate this with the rapid process?

**:** If I know that x.

**:** Is a plus one amplifier. How can I associate it with radio? How can I associate it with some process? Or how can I really like how it produce improved grasp?

**:** Remember what some processes do, right? They count arrivals.

**:** Nt.

**:** How about I consider that one process? This was a process, but with a specific range.

**:** So that means what? Customer per hour? One custom or one atom is a metric per hour per second?

**:** Since this is a process, we take one. NP is equal process. This is particular.

**:** Is a process.

**:** Or this one should be one.

**:** This would be one.

**:** Let me make here, and then I would upload the new slides.

**:** So if it is one.

**:** Customer per hour. Then N1 should be Poisson 1 and D should be for some.

**:** So we make this observation.

**:** I know that x is poisson. We train you.

**:** How can I express x as empty?

**:** T can be anything, right? How can I fit X in here?

**:** Instead of T, what should I put.

**:** So look at the pattern. N1 is person 1 and D is plus on T.

**:** X is cool as one mu.

**:** Right.

**:** So we can say basically X.

**:** And mu nu then is also quotient mu.

**:** And X, they have the same distribution.

**:** Automatically, right? So we relate.

**:** It.

**:** X parabola X with a member of the Poisson distribution.

**:** So it was process.

**:** We can do exactly the same thing.

**:** For y divided.

**:** So we have associated this loop.

**:** Right. But what is the problem?

**:** So we have.

**:** X.

**:** We have n U we have y.

**:** We know that his guys. Did we say?

**:** Y.

**:** Eah, they are independent. So we know that these two are independent. But when.

**:** The independence doesn't carry.

**:** Here.

**:** So N, Mu and Nu are not independent. This is where the problem comes.

**:** So.

**:** We make this.

**:** To handle that follow the same distribution, but somehow the dependency problem.

**:** But we don't even care, right? If we work in the random process work. And that's why some process work we have already proven we have found a way how to introduce independence.

**:** Because it's a property of the processes, right?

**:** So the increment nu minus nu.

**:** Ide. Anyway, we know that in a general case, we know the Internet is independent of all the previous.

**:** Intervals. I am decided from the double.

**:** So in that case.

**:** Consider this rat. The increment from U to U plus mu.

**:** The distance is, the length is new.

**:** So it.

**:** Is independent.

**:** Of.

**:** The biggest one.

**:** So basically, this is what happens, right? So we have U here, u plus.

**:** We know that the increments are independent, so we are in a good state, right? So we cannot really change anything.

**:** With Array. We still keep the.

**:** U.

**:** And then we said new mu N U minus and U is still what's on varied.

**:** So we have now constructed. We can now construct it.

**:** The correspondence.

**:** X with associated with n mu and they have the same profit distribution and Y is associated with N.

**:** Icolet.

**:** In the same proced.

**:** Ure.

**:** So the joint distribution of x and Y should be the joint is equal should be the same as the tiny distribution.

**:** Of these two plus one gram.

**:** We know that they are members.

**:** Of some processes.

**:** Let's add these two. We want to add these two, right? We want to find the distribution of x + y when we take follow the same distribution. Let's have these two.

**:** And these two.

**:** Because Nu disappears.

**:** This random Bible, and we know probably should.

**:** Be mu plus.

**:** And that's it.

**:** So x plus y follows a plus one distribution. The summation.

**:** So this is extremely useful and not continuous reflection.

**:** Just move from the rigid word of Bibles to the more plexible and more richer in information.

**:** World of random processes.

**:** So we have many graph aligns and, you know, the distribution of its constituent graph of viable process. So we have more room to make calculations, to make more sound rates of.

**:** Questions here, I think. Straightforward, but it's good to see. Now, let's go to superposition. Extremely important.

**:** So, as I said, we will use an example, and then we'll use that.

**:** Provide.

**:** This example happens every day.

**:** We know.

**:** Two strings.

**:** Try to. And we know the rate, the average number.

**:** The question here is if we know the independent rates.

**:** Then we come up with supermarket manager, right?

**:** Can we come up?

**:** With the rate of the proper the total number of customer arrivals in the system, we know they need to appreciate.

**:** Let's see what is going to happen with a total number of analytics.

**:** So obviously, the increase of sales, it should be the summation of the rates, right?

**:** But we have to prove it. We have to prove that our equation is correct.

**:** So we define random variables.

**:** We are probability graph so wt the number of women and team number and we know they have one and we are looking for a new outcome now of customers that are we don't know the distribution of is.

**:** This is a neurodevelopment variable, and obviously it's a summation of people who have two different genders, right, that come to the start.

**:** Women class. So this neurotobile is a part of some we know how to derive, right? It's a summation.

**:** So let's see. Our aim here is.

**:** To show that our team.

**:** Is a member of some.

**:** And then we have to find the array of that plus one process.

**:** This is what we are doing.

**:** So this is what you should always write. Use the job of the problem. So the geometry is that we have one stream of Mac here, women and stream of customers. Right? Let's see what happens.

**:** Chinese. Obviously, accounting process is accounting process. We want to show that.

**:** This is equal process.

**:** Es are types of processes. Let's see this article. Impressive.

**:** The increments we can define. Influence is the summation of the increments of the two position process.

**:** So this is the increment of the women and this is incremental.

**:** The increments.

**:** Must also follow a class of process.

**:** Of its increment it's gender implement.

**:** Right.

**:** Also follows the class and they are independent. No woman calls another man. We assume right, and then I'm going to go to the store of not right. So we assume this doesn't really happen, so the increments are different.

**:** So what we have solved.

**:** The increments following the classroom dissociation.

**:** The increment solar network. But what we have done so far, we have shown that this random variable can be easily in the framework of the croissant operator.

**:** What else do we need? It's accounting process as these properties here.

**:** The increments model that was processing and dependent.

**:** The course of a situation.

**:** Right. Let's now see what happens with the rapid process for chapter. Let's observe now information about gram of angles. Let's see what happens to 75.

**:** Objects indeed belong to a poisoning process. We have to show sexuality and independence.

**:** With.

**:** Memories with doesn't really care about the task.

**:** Sorry. We saw the stationary here. Right. So. Now we will solve the independent. Now, the increments here. Obviously the increments are depending of its gender.

**:** It's gender. Women are independent. This increment is independent of the mask from all the other arrivals of women that happen before this.

**:** Obviously, I can also claim that also independent.

**:** From the number of arrivals of men that happen in the past.

**:** Because men and women are independent.

**:** Exactly the same process here may not be dependent from the past and also independent of the women that women are concerned.

**:** So the increments because RP minus RS is given by this one.

**:** Is the summation of the gender.

**:** That means also that RT is also independent. A lot of process is independent of the.

**:** Rehabbing. So we know then is process. And obviously we know now that based on the fact that we just add. We also know that U plus. So what we have so we have two random processes.

**:** We merge them.

**:** And we know the rates, then we know that eight of the merged classes superimpose this random processes to this program of processing. We know everything about this neural network.

**:** Can be generalized for any random process. Not only we can have any number of random processes.

**:** And then you come up with a neurotrosis, a total number process, and you know that It's a classroom process, and you know that.

**:** 's the principle, the principle of human condition, extremely important. And it doesn't really follow. It doesn't apply only in arrivals of customers. I have an example here which we can apply in Software Engineer.

**:** It's a number of parts that we introduce. Suppose syntax error and visualize zero.

**:** These are very common errors that we make when we program.

**:** Right.

**:** Exactly the same. You want bread? We know the rate. You analyze three years of lines of code under eight.

**:** And then you want to find.

**:** We will cover a lot of processes, different random processes that exhibit this drug. Not all round of processes can properly.

**:** Those who benefit from.

**:** Let's go to the dual concept here.

**:** We have the opposite task. So we know that total rate of canceled in the sky.

**:** And independently. These customers can be mannered with and they come. Men come with probability. And we can come with the one line.

**:** And we want now to.

**:** Characterize.

**:** The individual processes, right? The process of math. It's a random process, right?

**:** And the random process of women are they also. Plus some processes. We know that obviously the total number of customers is to have some process, right?

**:** What can we say about the two constituent process?

**:** That consists of arrivals of men and women. Processes.

**:** Men.

**:** So obviously we get these random virus immediately.

**:** And we are interested in finding the distribution of the map and the distribution of the. We know the distribution of the total.

**:** But how can we proceed? This is a bit different.

**:** There is a missing information that we somehow have to come up with. That's why I have this very simple.

**:** So let me give you a hint here.

**:** Rt for c of negative.

**:** Is having.

**:** What are the random variable? Do we have a reason?

**:** But there must be another randomization.

**:** So these, all these are counted?

**:** Random.

**:** Violence.

**:** Is there any other? Is there a round Bible that doesn't count?

**:** I'm looking for a random variable that does not count.

**:** But classifies.

**:** The people.

**:** Right. Exactly.

**:** So the gender. Right. How can we get the information? We have the information here.

**:** We know that men come with probability and women come with probability. One microscope.

**:** So the gender is extremely important.

**:** Type. So we have this uranium, I would say gender of the cave custom. It doesn't come.

**:** But.

**:** I would.

**:** Always think of how we can use.

**:** Information.

**:** Then immediately, if we get this.

**:** URL state. We can write the random and see.

**:** As a summation.

**:** To the indicator model.

**:** X cube. What cell?

**:** Then.

**:** That will give us empty and w would give us.

**:** Now, the summation that I have here.

**:** Is from the total number of customers that came up to type before Chan K.

**:** So this is, let's say, into one hand.

**:** And it's the same for Bob.

**:** But not this one is a lack of value.

**:** This is not a fixed number.

**:** This is an automatic.

**:** One realization in another realization.

**:** Another.

**:** So we have to treat it properly, with caution.

**:** But we made a lot of problems.

**:** We made a lot of problems.

**:** We have this.

**:** Now let's try to find the distribution of the.

**:** We don't have much more information about the bank, so we use the power.

**:** So the towel probability. What it tells us for every realization.

**:** Of the other.

**:** Student, finite.

**:** Number of customers is the probability that these numbers should be length out of this number, right? M would be.

**:** Times the probability this realization.

**:** That's the power problem.

**:** Then we start doing antidote factors.

**:** Right.

**:** So we substitute these guys as integrate to another variable.

**:** Still this one. The summation is up to capital. But I know RT is equal to small.

**:** So the next one you can replace the rubber biome with a. Now it's a fixed model. So this summation is not random anymore. Here the summation is not fixed.

**:** Because the upper bound is fixed here. The summation is an undivided.

**:** Because the upper bound of the summation is not a bio.

**:** So this is fixed. This is amplifier.

**:** We cannot do anything with random summation.

**:** But now since we fixed it, we can do any. Since we fixed it, we can get rid of the condition. We just fix it.

**:** So we have this one here.

**:** We know. This is Phyloge and this is the knowledge plus.

**:** So it's our substitute.

**:** So we get this expression given. Now we try to compute this summation.

**:** Now it's calculated.

**:** But in order to make our life easier, we have to somehow.

**:** In a smart way so that we can come out with some known summation.

**:** First thing that comes to your mind is to take out the cellation.

**:** Do not belong with the counter for the summation.

**:** Right. So anything that does effect of R would take it down.

**:** So from here, we take out all these guys, and this is what remains inside the solution. This guy here.

**:** And obviously here you have to be careful, right? We have R minus M, so you cannot start from zero.

**:** So here. Or here. You should update your compass.

**:** Start from M. So you have this ratio. But this ratio should be immediately give you some hints.

**:** Some tailor expansion.

**:** In your mind.

**:** This one should give you some tailored expansion.

**:** So this one keep manipulating.

**:** You multiply by this guy here.

**:** Multiplied by this one.

**:** So that you introduce.

**:** Right. So here, remind you the exponential, right?

**:** But you have something in one power divided by a factorial. But the denominator, bizarre minus. So you have to basically somehow do the manipulation here, right? The massaging. You multiply by mu times T.

**:** You have everything?

**:** And exponent is also anyway.

**:** From the blackboard or the projector. You have to do it by.

**:** Get this experience right.

**:** Once you do this, mathematicians here we also have to multiply by this and divide by. We multiply by.

**:** This is what I do. So one minus b.

**:** In the denominator of the nan. I just write it in the next one.

**:** As I bring it here, and then I can move it. I can move this guy.

**:** And I can have one minus p.

**:** R -2.

**:** And from here. Then I have to cut this guy.

**:** Anyway, so what I'm doing is this. 5 is exponential.

**:** And then I just substitute.

**:** And I have to do this.

**:** Turkey.

**:** But what is this?

**:** What this term.

**:** I still need to do one more operation. Just.

**:** Add this, and I come up with this.

**:** One is nothing else but with parameter with ray b times.

**:** B is a probability that the customer is.

**:** Utilized the rate for time interval of.

**:** So that's it. So we know that we found the probe distribution.

**:** Exactly the same way, exactly.

**:** You can find.

**:** Should be my.

**:** Good.

**:** A lot of comfort. Be very comfortable in this manipulation. And this is part 50, 60% or 70% part of the entire cost.

**:** Be very comfortable by being so that we can come up with something.

**:** Lottery for some dope distribution.

**:** So it's also easy to show that these increments are specialized.

**:** If we know the probability distribution for each one.

**:** So we also have test scenario.

**:** This one is for distribution.

**:** So each one of these processes.

**:** Are they independent and I believe finish with this.

**:** Are these guys?

**:** So this is not.

**:** Easy to prove. But I want to ask you first.

**:** Do you think this men and women?

**:** They stood up on virus. The number of men and the number of women that alive at the store would independent.

**:** Out of prison.

**:** So we know the entire.

**:** And then we must know. I've been.

**:** Arriving independent.

**:** What does heritage.

**:** So is it independent?

**:** Or not.

**:** Let's take a guess.

**:** How many people think it's imperative.

**:** How many people say, how many do you think they are dependent.

**:** One.

**:** 23. We have a type.

**:** So you are undecided.

**:** Right, okay.

**:** Good.

**:** Undecided.

**:** Let's see what her intuition would tell us.

**:** Right. Let me ask the people who believe that they are dependent.

**:** Why she think they are dependent.

**:** Why you. Listen, they are.

**:** Interesting.

**:** We do not know our teeth. Right? Because it's random.

**:** Viral.

**:** Perfect in Christian.

**:** That's the inclusive.

**:** Let's see. Is this intuition?

**:** Is this equation going to give us to the right?

**:** But your intuition is extremely logical.

**:** Are.

**:** The.

**:** Random variable.

**:** Sometimes you may be 100, sometimes you may be 10.

**:** We don't know.

**:** The other people, they said, well, it doesn't matter. Probably bother even to think that this is random. I have two different streams.

**:** Of course, they derive from the same source.

**:** Probably the different part.

**:** Let's see what the math tells.

**:** But I like what both of your increasing. They are equally valued. Well.

**:** We have to prove it, right.

**:** So if we solve that this probability, the drug probability of W is actually.

**:** The probabilities of an event, it will be independent. There will be independent. Otherwise they would be dependent.

**:** So this is where we're going to.

**:** So we cannot have any information.

**:** Half of the class, let's say 33% we have actually equal. That means we don't have a lot of people coming to the class, but at least we have engagement from the class, so this is important.

**:** But anyway, so we don't know if they are dependent on independent, but we know that these two ident.

**:** With the total.

**:** Reason. We still don't know that.

**:** The only thing we know is that we can go from here to here. It's exactly the same.

**:** And we are looking up and down.

**:** Well, if I go from here,

**:** To here. Now I can replace with the indicator variable.

**:** The men. It counts. And I know.

**:** How to use. I don't know anything about. So that's why I have to write it as how to process. Then I'm able to introduce a binomial distribution.

**:** I don't know.

**:** This guy.

**:** Well, actually, you think that. Let's play. So I replace empty with this summation.

**:** And this I will.

**:** And we know that now. This is. But now I know herpes M plus W. So I can actually place this equals N.

**:** Now I know that this summation, all these guys are independent of this indicator variable is independent of the body.

**:** They are independent. I can take the total.

**:** I know this is binomial.

**:** I know this is Poisson. I give this question.

**:** So now my task becomes again.

**:** Manipulating things.

**:** Am I able to make the product? This is already.

**:** I may be able to derive this product. I may not be able to. We do not know.

**:** But we are trying, right? We are trying to prove all this program.

**:** If this is the case.

**:** If they are independent. I have to have a class, so here and.

**:** So my task now becomes, how can I manipulate this guy?

**:** To see.

**:** Distribution here and if some distribution in the other cell. So this is it. When I expand this guy.

**:** The green are eliminated.

**:** And then what I see is I have a b2mu power term and mu plus b to the 1 minus p to the w.

**:** And this guide to the document.

**:** Let us see what I can do with that. So this is what I had so far. I just made these observations.

**:** Let's see where I can.

**:** Now I can match these guys. I can say, this blue. I can put it under the umbrella of M.

**:** I can make this two. Right, because they have the same exponent. Same thing here. They have exactly the same exponent.

**:** The only problem I have is I have exponential here, which is minus mu t.

**:** If I had somehow one minus P over there.

**:** It would have been really nice.

**:** I have a subtract.

**:** So I have this. I shed m the exponent of n now in sub not b mu t.

**:** Then I can have in here. I can collect. So I have 1 minus 3 u. T.

**:** One minus p.

**:** 4 minus b of t.

**:** Minus this.

**:** To the algebra here, right?

**:** Connect herbs, you will come up with This E to minus B will be at E2 minus.

**:** Now you multiply, you have this guy.

**:** Here, which is Poisson.

**:** We thread p.

**:** Md.

**:** And 1 minus P, so.

**:** This is one plus O, this is another plus.

**:** You were able.

**:** To start.

**:** And solve that. It's a product, so they are independent.

**:** Men and women arrive independently. Men and women arrive in the present.

**:** It doesn't matter if the stream is a random variable in a way.

**:** So the equation of the people who.

**:** Make this observation is extremely correct.

**:** Unfortunately for those who elect Veronica and the other 33%. Right.

**:** You are in the right path.

**:** Only for a select number of random processes. This doesn't fall and we'll see. I have written some.

**:** Observations here, right?

**:** But this is what we have shown, right? That they are independent. Why this may happen?

**:** This is extremely correct. Right, so this is a random Bible.

**:** So there's three changes.

**:** So soon that will be independent. But this is what happens. This is an example that I have written. Suppose so we established that and t is not fixed.

**:** Empty. Suppose np, the number of magnitude statement that arrived.

**:** This is. Notice if I change this here.

**:** I change it? Yeah, I forgot to delete. I added more information.

**:** So why they are not independent.

**:** Why they have not there, so why are they independent?

**:** So we know this.

**:** What I say here.

**:** Right? So if we know one, we should be able. If we know the total when someone gives us one, the men, we should be able to determine the women.

**:** But in class some processes Artie is not fixed.

**:** So we all know the age. And suppose that the rate we know is six.

**:** The rate of the total customers is six.

**:** And one day we observe.

**:** That by time T. We have 10 customers.

**:** So we have more than already.

**:** More men came. We expect a total. Men and women 6.

**:** But ten men are out.

**:** So obviously.

**:** We should expect two women.

**:** Now suppose here we have. But if.

**:** This may be like a bigger how can I express it? But might be a busy day. That's why we observe so many men.

**:** We observe so many men.

**:** Must say this day. So we should observe many more women as well.

**:** So one is telling us that we observe 10, so we have two. But the other one tells us that cancels this, right? So we observe less women. Because when you observe more men, which is logical thought, the other thought is, you might be a busy day. So if more men came, then more women would come, so it would. Balance it.

**:** One effect puts the balance higher in one side, but the other thought the other effect would also put a balance.

**:** Again in the equilibrium.

**:** So based on this observations, we are able to kind of see why this happens in poisoned random processes. Not every random process has this. Characteristic.

**:** We cover this?

**:** So this is the principle of thinning.

**:** You have one random process, but the fact consists of many different what do we say here? Different types of and in multiple.

**:** Then you can dissect this different array. Let's say you can create different processes. And we know that this personal process is that multiplying the rate of mother process.

**:** That's extremely common.

**:** All right. So thank you very much. Best of luck for your middle.

**:** Just relaxes. I take it as a nice exercise.

**:** There will be questions that are easy. There will lots of questions that are more challenging.

**:** That's also good. We always look for challenges in that.

**:** Place of luck. We see you after the spring break. Enjoy your.

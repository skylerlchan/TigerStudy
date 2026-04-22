# World models and AI intelligence architecture overview

**Date:** 2026-04-07


## Summary

### Current AI Limitations

- AI excels at discrete tasks (chess, code, bar exam) but fails at physical world understanding
- Can’t perform basic real-world tasks: cleaning house, learning to drive in 20 hours like teenagers
- Current systems need massive training data or simulation vs. humans learning from observation
- LLMs limited to reasoning in “token space” - works for math/code but not physical world

### Human vs. AI Learning Differences

- Humans learn world models in first months/years through observation
- Baby development milestones:
- Object permanence: 2-6 months- Stability concepts: early months- Intuitive physics: ~9 months
- 4-year-old processes ~10^14 bytes through sensory input vs. LLMs trained on similar amount of text
- Sensory data contains vastly more information than text alone

### Joint Embedding Predictive Architecture (JEPA)

- Key innovation: predict in abstract representation space, not pixel-level
- Avoids “blurry prediction” problem of generative models
- Two main approaches to prevent collapse:
- Distillation methods (currently more successful at scale)- Information maximization (speaker’s preferred long-term approach)
- JEPA finds predictable abstractions while eliminating unpredictable details

### World Models for Planning

- Action-conditional predictors in abstract representation space
- Enable hierarchical planning from high-level goals to muscle control
- Architecture components:
- Perception module for current state- World model for consequence prediction- Task objectives and safety guardrails- Optimization for action sequences
- Intrinsically safer than LLMs due to hard-coded constraints

### Research Applications & Company

- JEPA-2.1 trained on 100+ years of video, shows physical common sense
- Demonstrates planning in unfamiliar robotic environments
- Advanced Machine Intelligence (AMI) company founded to build:
- Systems with world models for planning- Hierarchical planning capabilities- Physical world understanding- Industrial applications (not language focus)
Chat with meeting transcript: https://notes.granola.ai/t/8d8e941e-45e0-44c7-93d4-aa567dfb1b53


---

## Transcript

**:** And by the way, the pictures.

**:** Of astronomy little pictures you see here, I took them from my backyard in New Jersey.

**:** Okay.

**:** AI sucks.

**:** At least we compare the abilities of the assistance to that machine learning system.

**:** S through the ability of.

**:** Animals and humans.

**:** Jiggly animals.

**:** Basically local comparison in the ability of animals and humans to understand the physical world. Of course we have AI systems that can write code, they can pass the bar exam, we can win international battling piazza, but they can't figure out their dinner table, they can't clean the house.

**:** They can't learn to drive in 20 hours of practice like any teenager.

**:** And we do have millions of hours of training data to trade cars.

**:** Discussing.

**:** Why can AI deal with real world data, high dimensional continuous, noisy data from things like images, video, audio sensors or styles, measurements on instrument, finance.

**:** Why.

**:** Do agentic systems, are they built today need to be trained by imitation on enormous amounts of data, basically trying to imitate humans?

**:** Or through massive simulation.

**:** Why can't the isitan solve new problems, accomplish new tasks, zero shot without being trained to do so?

**:** Most AI system say with today that you can play with today?

**:** Whatever they answer the question, they've explicitly been trying to answer that particular question because other people asked that question before.

**:** So the system was fine tuned in a post-training phase to actually answer all the questions that people might ask.

**:** There are reasoning capabilities of course in modern LNM days systems. They're fairly limited. And the kind of reasoning that takes place is reasoning in toggle space, which means it works really well for domains where the language itself is the substrate of resin, which happens to be mathematics and code, the perhaps law.

**:** But that's about it.

**:** So the worker you want from code, no question.

**:** And you promise you're the.

**:** Whole world out there that current technology, we can't handle very well.

**:** And the assistant we have common sense.

**:** Is the physical world is really the kind of the big question. How do we get AI systems to do that? Robotic systems, so very encouraged. The real world is messy.

**:** Language, as it turns out, is simple.

**:** Never mind humans. Cats and dogs can do stuff that are completely outside of the realm of possibilities.

**:** That we can do with current AI.

**:** S.

**:** The first time you tell you all to do a chores, they can do it the first time they don't want to do it, but they certainly can.

**:** Without being explicitly trained to do it.

**:** And again, the 17-year-old can go to write in about 20 hours of practice. Why is that?

**:** It's because we have better models of the world.

**:** That allow us to imagine the consequences of our actions.

**:** And therefore to learn that allows us to log extremally quickly. That allows us to first of all plan.

**:** Actions.

**:** Even in situations we never encountered before.

**:** So we know that even if we've never driven next to a cliff.

**:** And it's, you know, in the first hour that we're learning to drive and we're driving next to a cliff, we know that if we turn the wheel to the right, the cowboy went off the cliff and probably nothing good will come out of that.

**:** We had this mental model. We don't need to try to figure this out. Whereas the current machine learning system, particularly if he uses republican, will actually have to drive on to cliff multiple times before he figures out to some right idea. And then a few more times before he figures that out not to do it.

**:** And then a few more thousand times for the next cliff that doesn't look the same.

**:** I mean, this is super efficient.

**:** So we have this difference between the, you know, some tasks that.

**:** Seem kind of the epitome of human intelligence that seem complex like in chess.

**:** Or winning method he seemed to be not that hard for computers in the end.

**:** Whereas things that we take for granted that we do every day without even thinking that our interventional task, this still seem to be.

**:** Rich.

**:** How do humans learn?

**:** So humans and animals actually.

**:** Learn how the world works in the first few moments and years of life.

**:** Initially mostly by observation.

**:** And these by interaction after a few months.

**:** You know, three months old babies, basically you don't have any way of affecting the world beyond their own limbs.

**:** So what they learn about the world, they learn mostly.

**:** Obser.

**:** Vation.

**:** Passive observ.

**:** Ation or active observation.

**:** Actually.

**:** So we run things. Well, this is a chart that was busy amber by now from recolleague.

**:** Evalu.

**:** Ation.

**:** That indicates at what age it is on basic concepts about the world, like object permanence, right? The fact that when an object is hidden behind another one is.

**:** To exist.

**:** That pops up around the age of, you know, between two months and six months, we don't exactly know.

**:** Basic notions of stability.

**:** That, you know, this object.

**:** Is still probably not.

**:** Into a while.

**:** You know, babies know about natural categories of objects before they get good names on them in order.

**:** It's kind of like intuitive physics.

**:** The only pops up around nine months.

**:** So if you show the scenario at the bottom right here to the seats once at all, we put a car on the platform and you push the car off the platform and it appears to float in the air. Six months old, well, the only pay attention.

**:** A 10-hour.

**:** Bill, he's very surprised.

**:** And, you know, opened the eyes and fixate the scene like the little girl here. And that's how actually psychologists can measure to what extent the mental model of reality has been violated.

**:** For a baby. The fixation time.

**:** So that's how we know that babies are intuitive physics pretty late.

**:** In fact, if you put an eight-month hole on the high chair with a bunch of toys, the eight boats were almost systematically just for the toys on the floor.

**:** They verify that the objects actually fall. Why they do the experiment that gravity actually applies to everything.

**:** There's a name for this psychologist that cognitive psychologist said,

**:** Calls this the baby scientist.

**:** Got pick.

**:** Ed.

**:** So I actually kind of.

**:** Really participated in a paper here, we'll see between my economy.

**:** On why currently our systems really don't run like humans and how to fix that.

**:** These are recent paper.

**:** But really what is intelligence? It speaks debates now because, you know, there's some wild claims from people generally in civil warning. We're just around the corner to API.

**:** Artificial general intelligence.

**:** Doesn't mean general intelligence. What it means is human level intelligence.

**:** The same level of generality as humans.

**:** We might think of ourselves as, I think, general intelligence. We don't, we're extremely specialized. We're incredibly specialized.

**:** In fact, if you want to convince yourself that you are increasingly specialized, just go buy a little $30 gadget that will be to a chess.

**:** You're not as smart as that. Think for chess.

**:** So intelligence is not just a collection of skills.

**:** It's not an accumulation of declarative knowledge, which is what ends are by the way. So not particularly smart, but it can accumulate a lot of declarative knowledge and regurgitate it at the right time.

**:** But that's more like road learning. It's not actually intelligent. So intelligence is, in my opinion, is really more the ability to.

**:** Accomplish new tasks and solve new problems with no prior training or very little prior training, vehicle trading.

**:** So how fast you can learn a new task.

**:** Basically determines.

**:** Our intelligent UR.

**:** FA you learn to drive or fly the airplane or ski or whatever. That's not particularly smart. We don't think of this as smart, but it's actually pretty complicated.

**:** So faster attention refer to a new situation. V is intelligence.

**:** And the phrase artificial german intelligence makes absolutely no sense.

**:** What would make more sense is super intelligence perhaps that would be okay. We build machines.

**:** That surpass humans in order weights. There's no question that this will happen.

**:** In at least your lifetime. Maybe don't mind.

**:** But.

**:** There's no question.

**:** That will happen.

**:** So there's this other paper here.

**:** That you look at in some archive.

**:** Basically claiming that intelligence really is not a frozen country. The skills like any test that you can design.

**:** Fix steps that you can design to measure the intelligence of a system.

**:** Is not going to be effective because you can always train the system to solve those tasks.

**:** The question is can the system run new tasks quickly or just solve new tasks without being trained?

**:** We're not going to get to human early intelligence by just carrying out our turbulence.

**:** And one, these many arguments for that.

**:** And I'll come to some of them. But the first one is NLMs are trained with human produced text.

**:** Which.

**:** Is for this until last year is typically about 30 trillion tokens that correspond to electronic trillion words.

**:** That's the older publicly available tax on the internet.

**:** These tokens is about three bytes. So they did have volume. It's about 10 to the 14 byte.

**:** S.

**:** And there is not much more than that.

**:** You get license, commercial.

**:** Copyrighted works.

**:** And can try to convince environments to scan control documents that they hadn't yet. But in the end, it's only about 10 to the 14 bytes, maybe 10 to the 15 if you want to be generous.

**:** It would take about 400,000 euros for a human to read through that. 9 hours a 250 words per minute.

**:** Very boring.

**:** Now compare this to a human chart. A four year old has been awake at roll of 16,000 hours. These are alive.

**:** Which by the way is a tiny amount of video that corresponds to about half an hour YouTube upload.

**:** We have 2 million optical nerve fibers carrying about one byte second.

**:** From original cortex.

**:** It's highly compressed.

**:** We have way more pixels if you want in our retina. But you get this compressed to 1 million fibers for each height.

**:** And so that's about 10 to the 14 bytes in the first four years of life.

**:** Instead of 400,000 euros.

**:** And that tells you that there is way more information in high bandwidth sensory input than there will ever be in language.

**:** There's way more information you can get from the real world through sensors that will ever be able to gather with text.

**:** And that tells you we're never going to get to each other intelligence by just running on text. It's just not going to happen.

**:** Despite that money, you don't know scan and all the others they tell you.

**:** That, you know, it's just around the corner. We're going to have a country or geniuses.

**:** In a data center by 2027. This is a direct quote from the daily. That's completely.

**:** Different if you pardon my fridge.

**:** So if you parallel French.

**:** So how do we get that?

**:** So, you know, I've been sort of assessed by this question for a very long time.

**:** And basically mostly failing for, you know, let's say about 18 years and mostly farming for the first 10 of those 15. And then the last five years making a lot of progress along the line of, you know, training system to understand the real world from video, from sensory data.

**:** And make last year came to the court where people started to work really well. We could see patients for the stuff we want to keep home. Most of those applications are things like, you know, process control industry.

**:** That later we're always working the time was not particularly interesting.

**:** In fact, that's no interest.

**:** And then the realization also that there was a big demand from.

**:** You know, various investors and companies.

**:** For kind of getting to the next stage in AI for systems and really understand the real world.

**:** Particularly given the hrs and robotics.

**:** And so.

**:** I figured maybe I could start a coffee.

**:** To enable the next AI revolution. It should be AI for the real world.

**:** So using self-supervised.

**:** Training method, which I've made the success of.

**:** The chatbots.

**:** But in the domain of ideal, data.

**:** Which are.

**:** Then also around the idea of.

**:** Warm robot.

**:** The water is a metal model of reality that allows you to predict the consequences of your actions.

**:** And that is the only way I can imagine to build reliable agentic systems.

**:** I do not understand how people have sober trope.

**:** In building agentic systems.

**:** Without those system having the ability to.

**:** Predict the consequences of their actions.

**:** It's a very unreliable way of building out a networking system.

**:** And so that's why you need one artist.

**:** Um,

**:** System has persistent memory.

**:** Can helpful rotates or reasoning.

**:** Or can perform planning, which is a form of resilie.

**:** Ncy and a complete new tan zero shot without prior training.

**:** Etc. So this would go radio and an m. And this is.

**:** Work in progress.

**:** But let me tell you a little bit about the characteristics of that, you know, future air systems should have.

**:** So what type of inference.

**:** Takes place in a neural net or.

**:** That's basically inference by forward propagation to a fixed number of layers for the whole net.

**:** Right. So at an end, you give it a sequence of tokens or words.

**:** You run that through some gigantic transformer. And the output is a signal vector, which is essentially a fisher or possible.

**:** That's it.

**:** So it's forward population. You could just want to. It's a fixed amount of computation going into producing a single token.

**:** So if you ask a complex question and you ask you to answer yes or no, it does two plus two equals four. Yes or no?

**:** Then if you ask a question, does p equal np?

**:** That's why the exact same amount of computation will be devoted to answering those two questions.

**:** The only way you can get.

**:** Of course, the second one, the system will just produce the answers being tried to produce because it has no possibility of actually answering the question by thinking about it.

**:** So the way that you treat them into.

**:** Reason is you treat it to generate any tokens. You try to produce non-just simple answer, but only of course it will devote more competition to this because it's going to have for every booklet that's produced.

**:** So it basically is going to have to run through its entire set of layers.

**:** For.

**:** So the scope chain of thoughts. Then the second trick is that you have this lots and lots of different sequences that I could look at. So then you have a second network selecting the best one among all the ones that were generated.

**:** So it's basically reasoning by.

**:** Spray and pray if you want. You generate lots of sequences of outputs and then you have some way of selecting which ones are best. It's a very inefficient.

**:** Way of doing reasoning. Now consider an alternative. Let's say you have a mental model of the situation.

**:** Which allows you to predict as a consequence of an action you imagine taking or the effect on the environment is going to be along the situation you're imagining. So let's say it's robot. The robot needs to accommodation particular tasks.

**:** And so you have a test protective that you can think of as some sort of cost function.

**:** I put the measures to what extent a task has been accomplished.

**:** And then.

**:** You run the initial state of the world and the actions that you imagine taking through your one model. And what your role model does is that it predicts.

**:** The outcome of taking the sequence of actions given the currency to the world.

**:** And you see that to this task objective. You can measure it to what extent the task has been accomplished or not.

**:** Now by optimization, you can search for an action sequence that will minimize that cost.

**:** And this is completely classical. You have to look at your own. It's called change.

**:** You have a moral of the system you're looking for.

**:** You can use it as kind of a simulator. You give it a sequence of controls.

**:** And you use this model to predict the outcome.

**:** The nanoptimization, you figure out the optimal sequence of actions that will satisfy the task objective. Okay. That's an intrinsically more powerful computational model.

**:** Than autorec prediction of tokens.

**:** Because every computational public can be reduced in optimization problem.

**:** Whereas.

**:** Not every computational problem can be efficiently reduced to the sequence of ulterior resume prediction of discrete token.

**:** You can't do it. The principle is not efficient.

**:** So.

**:** That led me to this long term view that really an intelligent system should be built.

**:** Around this idea of world model.

**:** Of being able to imagine the consequences of your action.

**:** Having a bunch of objective functions that correspond to tasks that the system will accomplish, it will have to be configurable of course because the system will have to.

**:** Be able to tell a system what task we won't get to accomplish.

**:** In different situations.

**:** Of course, the system needs to be able to perceive environment. So perception ritual.

**:** And then this series configurator module which I'm not going to talk about. But basically sort of an overall sort of architecture that some people call this cognitive architecture vegetarian system centered around this idea.

**:** I wrote a long document about this about four years ago which I put online.

**:** You can see the QR code here.

**:** Or the URL.

**:** As far as version of this doc appeared as versions that you can watch as well.

**:** This is our own paper. It's relatively easy to read.

**:** Thinking about it about 10 years ago and I kind of put it online about four years ago.

**:** And since then it's been kind of working towards trying to make it work and making some progress in the last few years and as I was mentioning. This is basically my idea for where our research will go over the next 10 years.

**:** Now in six years because workflow is in.

**:** Okay, so let's go back to this idea.

**:** Sort of.

**:** Cycle used for the system is that it observes the world run this through a perception module that produces a representation abstract representation of the current state of the world.

**:** Of course we can only perceive what's immediately for thermal centers.

**:** But our idea of the state of the world also contains things that have to remember in our memory.

**:** So we now have to combine this with the co-parent.

**:** And we heat that to a one model and we also hit a hypothesis for an action sequence we want to take. And our model predicts what the resulting state is or consequence is going to be.

**:** And it also goes to this action. So we can heat that to a task objective.

**:** That measures what it said to cast it in accomplished. So those square boxes are cost functions. They have inputs and they have an implicit scalar output that measures across. It's not a cost we're going to use for training. We only use it for inference.

**:** Okay. A lot of you about trading.

**:** Yet.

**:** We may have other cars. The dark red box, which could be either caused penalty functions or even constraints, hard constraints.

**:** That will guarantee that whatever secrets of states the system decides to go through.

**:** Will be safe. It's not going to hurt anyone.

**:** Okay?

**:** During the cycle the system will.

**:** Buy optimization find a sequence of actions that minimizes the task objective subject to the government.

**:** A system of this type is intrinsically safe.

**:** Because it has those hardwired guardrails that it can do nothing but optimize.

**:** Let's satisfy.

**:** This is not the case for the names are intrinsically unsafe. There is no way to fix it.

**:** Because the way errors are made safe is through fine tuning. You have no guarantee that.

**:** The training samples that you use for fine tuning covers the set of all possible inputs, which of course we know it doesn't because there's no way to make llms in the current form safe.

**:** This kind of objective driven AI systems.

**:** You can if you want model is accurate. If your number objectives are well designed then this is going to be interesting. You save at least you have a way of ensuring that they are.

**:** Okay of course if you know anything about optimal control, a one model may predict the next state from the current state and the actual unit you're taking. You might be able to run in multiple times or totally relatively using the prediction of the previous time step has been put to the prediction. The next time step and sort of unworld that in time and then biotinization again figure out a sequence of actions that optimize the task objectives subject to the gun rails. This is very much akin to what control theory is called NPC model predictive control.

**:** But everything is done in sort of abstract representation space in the state of the world.

**:** Now ultimately what we want to build and that nobody has actually dealt yet although we have papers on part of the way.

**:** In fact one that I think showed up on our head today.

**:** Is hierarchical planning. So if I'm sitting in my video hierarchical type of time.

**:** We can plan every one of our actions in terms of.

**:** Semi-second by 10 millisecond muscle control which is one day required. The low level action set humans can take our muscle actions.

**:** By the way.

**:** There's no way I can plan a trip from let's say you to paris if I live in parish tomorrow.

**:** In terms of muscle control. It's just too complicated.

**:** And it's also I don't have the information.

**:** I cannot make that plan all the way to paris.

**:** So instead what we do is hierarchical planning.

**:** We at a very high abstract level of representation of the situation.

**:** I know that to get to Paris tomorrow I need to go to the airport to catch the table.

**:** Okay so now I have a sub rule which is.

**:** Being at the airport.

**:** I mean New York City. I do I go to the airport. I go down the street and yell the taxi.

**:** Okay I have a set of goal.

**:** Is treat to go through the elevator push the doctor or capital building.

**:** How do I go to the elevator?

**:** I have to stand before my chair. You want the door open the door blah blah blah avoid all the obstacles. And at some point down in the hierarchy there is an action that I can just accomplish because I'm so used to it that I don't need to think about it.

**:** I don't need to apply.

**:** So this notion of hierarchical planning I see this absolutely crucial.

**:** That's really crucial problem to solve if you want to build truly intelligent systems.

**:** This is unso.

**:** Lved. We don't know how to do this.

**:** In particular we don't know how to train those ouroretical models. I'll come to this in a minute.

**:** Okay, so how do we train a warmup? So we use a rom.

**:** Model.

**:** Okay, so if you if you are.

**:** In machine learning AI business and for the first 10 of those 15 years I was telling you about this is what I attempted to do.

**:** Which is.

**:** Attempt to train your system.

**:** To predict what's going to happen next in a view for example.

**:** Or whatever a sensor or sequence you have.

**:** Okay, so take the video mask the second half of it.

**:** And then trains have been neuron that to predict from the first half of the video.

**:** What happens the second.

**:** Autoregressive future projection of video.

**:** And this is the way LNM is our.

**:** Trend not train with video friends. I train with tokens but that's basically okay.

**:** You show them the sequester to cancer you try them to predict the next token.

**:** Now this works really well for natural language or for sequences of discrete symbols. It absolutely does not work for video.

**:** Or for any kind of natural data which is highly racial continuous.

**:** Because.

**:** Most of the information in the video generally the natural is completely unpredictable.

**:** Give you an example. If I take a video of this room I start from the left.

**:** And slowly turn rotate the camera where I stop here and I ask the system.

**:** Predict the rest of the view.

**:** It's pretty cool we are in some sort of detritude.

**:** And there's probably people sitting in the chairs here. It cannot predict with chairs are occupied or not.

**:** It certainly cannot predict what photography look like.

**:** That's most of the information in that video are the pixels.

**:** The detail aspect of your face is that new clothes or the texture of the world.

**:** There's no way you can predict this absolutely no way information is just not there.

**:** So although the expert in prediction when you're predicting.

**:** Discrete symbols in a text that's easy to handle because it is only a finite number of possible tokens. So you just train the system to produce a probability distribution of all possible tokens.

**:** And like we don't know how to use for you represent a primary distribution or view.

**:** It's actually mathematically detect.

**:** Able.

**:** So this idea that you're going to use generated models.

**:** To train your system to predict what's going to happen in the video when the self supervised matter using the same technique that has been so successful in natural language.

**:** Simply does not work.

**:** What does my wallet.

**:** And we know this program.

**:** Number of years? This is no paper.

**:** One 10 years ago.

**:** Trying to train some big combination.

**:** A few friends.

**:** When you get those blurry predictions because the system can only make one prediction and the best thing they can do if you train with these squares just predict the average of all the plausible futures. And it's just a brilliant picture because it doesn't know what's going to happen.

**:** My colleague Graphius together with colleagues at Fayer also did a similar experiment using similar to data of various physical system. It didn't work very far.

**:** So one idea of course which we used pretty early on was to use native variable models.

**:** You model the uncertainty in the prediction by a later variable that comes from some distribution.

**:** Okay, so as the native variable z varies over a set or is drawn from the distribution will imply distribution on the prediction.

**:** Okay, that's a way of parameterizing a complicated distribution of the output.

**:** We tried that too. Does it work very well?

**:** Because most of the information actually in the video as I said before has to go is unpredictable. So it has to go in the same variable.

**:** What you have to do is regularize this theta variable so that it doesn't capture all the information that is set collapses.

**:** I mean you can do this with vae and diffusion models and plot numbers but it really does not work very well not very satisfactory.

**:** So here is a solution to this. This is kind of the key idea this entire talk.

**:** Is a new architecture. It's not really that new but the image new at least called jetpa. What does that mean?

**:** Joining predictive architecture?

**:** And the difference.

**:** Between a generative architecture.

**:** Which from an observed variable x is supposed to predict a variable y.

**:** Here you don't try to predict y. What you're trying to do is find an encoding, a representation, an abstract representation of move x and y on that sx and x.

**:** And make predictions in the abstract representation space.

**:** So in that abstract representation space I can maybe take an example. If I put this pen on the table here and I tell you I'm going to lift my finger, you can tell that the pen will fall. Just can't tell in which direction.

**:** If I ask you to make a prediction that at the pixel level you just can't do it.

**:** If I ask you to make a prediction that higher level of structure, of course you know that dependent is going to fall.

**:** Some level of abstraction to describe this situation where your prediction is accurate. It's less detailed but it's accurate.

**:** It doesn't even need to be very realistic. You know the kind of.

**:** Idea.

**:** Trade.

**:** System to find the representation of the input of the signal.

**:** That is predictable.

**:** Eliminates all the details that are not critical.

**:** Okay that's the main idea.

**:** If you retain one idea from this stuff that's.

**:** The word.

**:** Because here is the issue with this.

**:** If you just train the architecture on the right.

**:** Minimize the prediction error.

**:** You show it a bunch of pairs x and y initial signer to the next segment that has conditional reduction in the base case.

**:** If you want a.

**:** Training to minimize the prediction error, it will collapse. Basically the system will be very happy to completely ignore the inputs.

**:** And produce constant representation as section sy.

**:** And the prediction error will be zero.

**:** Your system will have.

**:** Lower than anything that is useful.

**:** So how do you prevent that system from collapsing?

**:** There's a number of different methods for this. We have access to like half a dozen nowadays.

**:** But there's two categories.

**:** One categorian method is based on distillation and so far it's the one that works the best.

**:** Because it's the one that has been tried at the larger scale for the lowest.

**:** Explained in a minute what the system. And there is another class of method and naimonia is on the second class.

**:** Which is information maximization. So basically.

**:** Put some sort of criterion at the output of the encoder.

**:** So that you force the encoder to extract as much useful information for the input as possible.

**:** But yet because it needs to predict.

**:** The representation of y from the one from the representation of x, you cannot extract all the information because most of it will not be predictable. So the only extracting information that is predictable.

**:** Okay, so training a system like this will find a tradeoff.

**:** Between attracting energy formation.

**:** As possible from the input.

**:** Into the representation, but yet only extracting what is predicted.

**:** And this idea of jan power was only formulated about three, four years ago.

**:** In the meantime there's been something like 1300 papers of people kind of playing with those things for various contacts either using the model signifier.

**:** So neither the idea of what model nor chunk of any are you. The idea of collapse prevention has been worked on this going back by givington or others at Skyler going back to the late 80s or 90s. But by itself using something called sine is neural nets. And you know various other people.

**:** But it's become a bit of a hot topic more recently because as it turns out those joint elegant architectures.

**:** Give much much better results when you use them to train a system to represent images or video than any kind of generative architecture.

**:** Automobiles or within certain.

**:** So let me talk about a little bit more about the Sabrina checkup.

**:** Okay.

**:** Why is it a good idea to find an abstract representation of it a little?

**:** The answer to this I think is completely obvious if you think about how we do science.

**:** Or even how we represent the wealth.

**:** We don't need to know every detail about the position of every molecule of water.

**:** To be able to do whatever we want with this bottle which is nearly pouring the water or drinking it or whatever.

**:** Okay there's a lot of details that is hidden that we don't need to model to be able to act in the world or understand something in the world.

**:** Right? So I could in principle.

**:** Everything that takes place in this room.

**:** Right now.

**:** In terms of quantum field theory.

**:** It will be a complete description of what was already true.

**:** By doing a giant quantum simulation of all the quantum field you know within maybe a cubic kilometer around this room.

**:** We could simulate our growing processes and everything and you know everything all the way up to our next state of mind a minute from now with this. Of course it's completely impractical because we can't measure the wave function of this room first of all. So we don't have computers that are powerful enough to do this kind of.

**:** Simulation. And so we have abstractions.

**:** Particles.

**:** Atoms, molecules in the living world.

**:** Proteins or other layer cells or lesions in rural societies.

**:** Ecosystems.

**:** In the non-living world is another type of architect. Right. So we have this whole hierarchy of web presentation of reality.

**:** And each level in the hierarchy is more abstract and way below. Eliminates a lot of the details about what you know that allows us to make predictions that we hold practically at our std. Okay so the proper way to describe what was only this room has more to do with psychology like science and stuff like that.

**:** Then physics.

**:** So you talk to a bunch of physics right that will tell you everything is applied physics.

**:** True but there are.

**:** Even within.

**:** Physics right there.

**:** Are.

**:** Quantum.

**:** Physicists.

**:** So there is this whole hierarchy is that in fact every level in this hierarchy is a different field of science.

**:** A field of science is practically defined by the abstraction level at which to describe reality.

**:** So this process of finding appropriate representation of the world that allows us to make prediction is absolutely fundamental not just to science but just intelligence generally.

**:** Or brain students.

**:** Hence this idea of.

**:** Hence the idea that you're going to be able to understand the world through generated process.

**:** Repeat my apology.

**:** So one model should not be a simulator.

**:** Because you don't want to simulate every detail. You just want to simulate other level of abstraction that is useful for what you want to do.

**:** It's not a digital twin. It's kind of a fashionable phrase right now. It's not a geometry model as I just said. And you certainly know the video generation system. So one model is quickly becoming a buzzword or buzz for this in AI these days.

**:** Most people.

**:** When they talk about water model they mean really video generation.

**:** And I spent the last.

**:** Time.

**:** 40 minutes.

**:** Telling you that you don't want to generate pixels. Okay that's the wrong thing to do.

**:** Okay what model should be is action condition predictors of asteroid in asteroid representation space. They preferred media for two bold and I'll come to this in a second.

**:** Okay so what is an action condition? One model again given an observation you get an idea of the state of the world or system that you want to control.

**:** At time t you imagine taking an action can you predict the state of the world at time t plus 1?

**:** Or the outcome whether that system is a top of hydrogen.

**:** Or chemical plant or power plant.

**:** For the pitcher? Can you try to treat?

**:** Or will.

**:** Go?

**:** Try to use an environment?

**:** All of this you need a run model for all of this every agentic system that's supposed to take actions you need that system to be able to anticipate and predict the consequences of its own actions. That's the only way you can plan.

**:** And this idea of course goes back a very long time in optimal control electronic control people here control people that are key.

**:** The idea that you use a model of the system you want to control like a rocket and you know you can simulate that. Okay.

**:** You can figure out the sequence of controls that will get the rocket to, I don't know, circle around the moon or to take a run of example.

**:** Or running blue in the space station, whatever it is.

**:** Okay, so this goes back to the potriagular tumultu principle state method you know that pop type in the soviet union in the 50s. In the west that took a little longer with the k bard procedure.

**:** And all of this is kind of a long-chain foundation. We use like classical mechanics.

**:** In fact this is the best way to derive back propagation.

**:** If you.

**:** Have this.

**:** Okay so we're going to train.

**:** Those round models by leading the example. But really the question we're solving is not just trading or model. It's training representations of.

**:** Complex input signals.

**:** That we can use for subsequent tasks which may be supervised.

**:** So the scenario that people have used in the past for image recognition only in a good web presentation of images for example is you take two views of the same scene.

**:** Okay take it in and then distort it in some way or take a different view in the same scene and then train a neural net to produce representation. So those two images.

**:** And then make sure you can predict one representation from the other.

**:** That's because you know what transformation took place between the two youth.

**:** Okay, you just want to make the two representation identical because you want your representation to be invariant to the viewpoint for example.

**:** Once you've trained this encoder you chop off the predictor and you use the encoder as a way to extract features of the input and you can train a supervised head on top of it just a few examples to accomplish a vision task.

**:** Like object recognition, death estimation segmentation whatever you want.

**:** So this is self-supervised learning applied to image understanding. And I tell you the results, this kind of procedure.

**:** Is much better when you use joint and architectures that look what you use generates your.

**:** Generation architecture is both are the days of this. So I issued coherence or EQD ae or nae for mass auto and collar or various other architectures. All of those work by taking an image, corrupting it and then reconstructing the original image from the corrupted version.

**:** And that simply doesn't work very well. You don't get like good representations or images. You're nearly as good as to join. So we started noticing this about five, six years ago. But that's what led to this kind of epiphany of abandoning the whole idea of generative.

**:** General team.

**:** S.

**:** So let me tell you a little bit quick word about the type of criterion we use to maximize information. So this is using those economics techniques I was telling you about before.

**:** You want to make sure that the information coming out of the encoder is maximally informative.

**:** And at the same time predictable. So the dictable part is comes from the impact that anyways in the future area.

**:** Representations. Are you maximizing permission? Okay.

**:** It's very hard.

**:** In fact it's essentially possible because to maximize the quantity what you want.

**:** Is a lower boundar quantity.

**:** And you push a lot of down or you like you know you need to be able to measure the quality or have a lower band.

**:** And the problem with information content is that we only have up and down.

**:** S because to measure how much information there is in a vector first of all is you can't define it in absolute terms.

**:** You can define new formation. You get connection with vectors maybe.

**:** But measuring the information requires to make assumptions about the distribution.

**:** Making assumptions about the distribution requires making assumption about the type of dependencies between the variables.

**:** That you.

**:** Authorize yourself to handle.

**:** If you ignore certain types of dependencies you end up with.

**:** Measures of information that overestimate the quantitative information. So for example.

**:** If I give you a bunch of vectors.

**:** And the only thing you measure for the dependency between the components of those factors.

**:** Are correlations.

**:** Linear convolutions.

**:** And you can tell that there is information in the correlations of the.

**:** Covariance matrix of this matrix of.

**:** Vectors compute.

**:** The product of the transpose that matrix by itself.

**:** Uses the gravis matrix. The odd diagonal terms are zero. That means the variables are correlated.

**:** That means there is some information in there. But it could be very complicated.

**:** Mutual dependencies between the variables.

**:** Do not pop up in the covariance matrix.

**:** So you always get.

**:** Over estimation or information content. That really sucks.

**:** Because.

**:** We'd like to maximize information. How do we do that?

**:** Okay, so we don't there is no way to do it. It's actually no perfect way. So what you can do is maximize a measure of information.

**:** That is good enough.

**:** Or relevant enough for whatever it is that your system is going to be using information for. So here is an idea. It's called sigreg.

**:** That means sketch isotropic Gaussian regularization.

**:** And what it does is that given a virtual point, okay what's going to come out of your editor.

**:** If you run a batch of samples through it.

**:** Is a virtual vectors. One vector representative one sample.

**:** The feature vector representation of one sample. You get a bunch of them for each of the samples in your batch.

**:** Okay what you'd like is you'd like the joint distribution of those variables.

**:** To be isotropic gaussian.

**:** Why?

**:** Because it's basically a sort of a maximum networking distribution.

**:** And it's easy to enforce this using a trick. That trick consists in taking a projection of whatever distribution every chemical distribution. You get a bunch of points in the space.

**:** That you see here.

**:** Coming out of your microlegger.

**:** You project it against along one direction.

**:** You're going to get a distribution.

**:** You can measure it to one extent that distribution is close to the concert.

**:** In fact you can turn this into a differentiable cost function.

**:** Okay, conclude the gradient.

**:** Of the distance or divergence or whatever.

**:** Of the empirical distribution that you get.

**:** One projection.

**:** To the galcia.

**:** Which means for every point projected point you get a gradient. In any case you went direction you should move that point so that the distribution looks more galaxy.

**:** Now that's only going to make the distribution gaussian around.

**:** This direction.

**:** And now you do this for multiple directions.

**:** And you can show that in the limit of sufficiently many directions and also kind of functions.

**:** If you make all of those project.

**:** Marginal distributions or Gaussians then the joint distribution will be isotopic.

**:** Which means the variable will be independent for each other.

**:** And this will.

**:** Pg.

**:** And that actually works. So it works really well.

**:** In fact.

**:** A few examples here. So here you start with a bunch of vectors into d. This is actually a PCA for higher dimension.

**:** 1024 dimensional.

**:** Vector.

**:** And you see the original data on the left.

**:** And the various points are the results of.

**:** Moving those points around.

**:** To maximize information according to various type of criteria.

**:** The one on the right.

**:** Name as pulley is is the one that we use.

**:** To basically maximize the Gaussianity of each project.

**:** Ion.

**:** So this works.

**:** And in fact more recently.

**:** With post of quote undeceil who is a former postdoc who is now a senior professor brown.

**:** Students from from this idea. So train the Java architecture using the cigarette quartillion to maximize information while training a predictor to give an instruction error of conditional actions.

**:** And you can use this to do planning for very simple tasks. Simulated task. It works pretty well. I mean we still need to scale this up but it's really complicated.

**:** More details. Okay, so here is the other approach to this called distillation methods. And this is one that people have been experimenting with for a long time.

**:** And so.

**:** It.

**:** S.

**:** Been scaled to a larger sizes to some extent it works really well.

**:** But again as I said my body is on the previous method. I think it's more currency in the in the long term. So this initiation network exists in again training a JAKA architecture with two encoders. We don't share the waste between the encoders. The encoder on the right.

**:** Gets weight parameters.

**:** That are distribution line average of the waste of the equilibrium.

**:** So its weights get updated. The one on the right does not.

**:** Um this works pretty well.

**:** It's a big issue which is the cross function you're revising does not actually mean by z because you're changing the weight of things you know behind the back of the optimization algorithm. So you can't monitor the cost function.

**:** To.

**:** The.

**:** It works.

**:** But the result is.

**:** That if you measure the performance of the systems for image retribution. So you use the representation as input to a supervised head and then you measure.

**:** Performance or.

**:** Image.

**:** Net object recognition something like.

**:** This. This approach works better, is much faster and.

**:** Much cheaper.

**:** Model.

**:** S.

**:** All.

**:** The generative architectures we try to teach like NAE.

**:** Or.

**:** Python.

**:** V3 is sort of a version of.

**:** Kind of distribution met.

**:** Hod with particular types of criteria.

**:** Where steward engine is work to push the performance as much as possible.

**:** And this is sort of latest incarnation loop that technique. This is work done by former colleagues of when I was not involved at a chair in Paris.

**:** And this is probably the best system in existence to extract sort of generic representations of images regardless of what you want to do with them, whatever task.

**:** Whether it's depth estimation, segmentation, object recognition whatever.

**:** Now let's talk about web models also you know jet that style has bigger than the word I've talked about.

**:** We've used world models trained on top of dino for this works.

**:** So here's an example.

**:** Of a task, pretty complex task. You have a bunch of good leads and you have a robot.

**:** Supposed to plan a sequence of actions.

**:** So that the robot will bring those random UK blue beads as good as possible to the target configuration you see at the top.

**:** And those are the actions that are planned by this genome. So the encoder is the dual image encoder which is fixed and then you train one normal the predictor.

**:** And the sort pretty well for various stats simple test.

**:** Works well.

**:** This model could be this one is called DJPAT 2.1. What you do there is that you take a video and you don't train the system to make temporal prediction in 2020 to make special predictions. So you like.

**:** Out, you ask me a big chunk of you.

**:** And then you train.

**:** The.

**:** Predictor to predict the representation of the full video from the part.

**:** Ially.

**:** Task.

**:** One.

**:** The original model was trained on something like 100 years of video like 1 billion hours.

**:** The more recent version is train on even more. But what's interesting about even this old model is that it acquired some level of common sense. If you show it a video or something impossible happens.

**:** The internal prediction error goes through. So if you show it in a low like the one at the top right where the ball is falling in the air.

**:** It disappears. The prediction thereof choose to do.

**:** This entails you like this is not.

**:** There's no conform to what it's been freedom. That's impossible.

**:** So this is the first time we have systems that have some level of physical.

**:** Is kind of a more recent system and I'm just going to show you a short video. The system doing planning in unfamiliar environments. So this is.

**:** Purely from vision.

**:** The system only sees the robot doesn't have any other information.

**:** Has never seen this robot.

**:** In this particular environment and it's trying to plan a sequence of actions.

**:** To go from the original state on the left to the target state on the right and this is.

**:** The sequential actions.

**:** That is plan.

**:** Ned.

**:** So.

**:** It works at least in simple cases. We have more recent thing that just popped up a few weeks ago.1 it's slightly more sophisticated because it uses multi-level representations and it makes turns out to make the planning easier with cost functions that are more well behaved.

**:** And we trained a system and they used the representation for subsequent blockchain testination.

**:** For some other task.

**:** Like this annotation.

**:** So what is on the far right and then other methods index to it.

**:** Or even sort of a PCA visualization of the features of extracted and you see so different objects of clearly different features. Let me skip to the end here.

**:** Recommendations.

**:** If you want to work on the next generation AI system. Of course you can work with any length if you want a job. You see a command.

**:** That's going to be.

**:** Double explosion.

**:** And my recommendation would be then generating models in favor of those criteria.

**:** That makes me super popular and simple.

**:** And then in privacy following in favor of energy is normally do I have time to talk about this but the proper way to sort of.

**:** Framework if you will find what you understand how this works.

**:** Is for those much but potassium method consists in maximizing the information coming out of your encoder by making sure all the rows.

**:** In the matrix are different. So every sample produces a different feature vector.

**:** What I'm recommending here is.

**:** The other way around. Make sure every color corresponds to a different piece of information.

**:** Okay, this is what this isotropic Gaussian stuff is doing.

**:** And both techniques have a role to play is actually a socio-natuality between the two. But my money is on.

**:** The information maximization.

**:** By making the variable independent as opposed to making.

**:** The sample representation is different.

**:** From various reasons I'm not going to get into. I've been saying for many years, 10 years I've been on reinforcement.

**:** I mean not really but like minimize its use because it's so beneficial.

**:** But that if you are interested in human.

**:** S if you're interested in the audience don't work on that shortage race and injecting systems.

**:** Because again I do not understand how you can even think about building.

**:** A eugenic system without it having the ability to predict the consequences of its actions.

**:** You need a warm one.

**:** There's no way around.

**:** Okay, so I created this company. I left later in December.

**:** And created this company called advanced machine intelligence.

**:** Or AI. We pronounce it ami.

**:** It means friend in function.

**:** And basically.

**:** We're attempting to build systems that have one model skin plan, depend hierarchically and understand the physical world can be applied to the controller systems in the real world including medical areas. So applications are everywhere in industry. We're not touching language.

**:** Okay languages the domain of n and m and m is our prime for that. We'll use them for tax interface.

**:** But we are concerned by.

**:** And the hope is that at some point I will provide us with some universal.

**:** Model for any compact system. We can apply to any situation from between require intelligent systems.

**:** Thank you very much.

**:** I can just project my voice. Yeah my name is gin and I'm an incoming PhD at nyu.

**:** One question I had was about the multi view invariances that you talked about and whether you're working towards a self supervised way of testing for that because I imagine one like roadblock to building hierarchical jeppa is that you might need to consolidate representations collected by different agentic systems.

**:** Okay so the question is about.

**:** Any representations of images for multiple views and whether that needs to be article yes or yes. So.

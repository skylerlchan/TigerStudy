# Robotics Symposium

**Date:** 2026-04-20


## Summary

### Embodied AI Architecture

- Two-module system: embodied reasoning model + visual language action (VLA) model
- Both Gemini-based models in feedback loop with environment- Reasoning model handles spatial reasoning, task progress, dialogue decisions- VLA extends Gemini with actions head for physical manipulation
- Hierarchical control stack
- System 1: High-level reasoning and VLA coordination- System 0: Lower body control for humanoid balance during joint tracking
- Tool orchestration capabilities
- Google search, progress understanding, safety tools- Long-horizon task decomposition into short-horizon VLA instructions

### Safety Framework Implementation

- Multi-layered safety approach across different domains:
- Content safety - inherited Gemini compliance policies (child safety, bias prevention, medical advice restrictions)- Physical safety - traditional robotics (balance, collision avoidance, compliant behaviors)- Semantic safety - first defense layer for human interaction, long-tail scenario handling
- New AI-specific safety concerns
- VLA robustness to reasoning model errors- Out-of-distribution scenario recognition- Full-body control stability under VLA command errors

### Safety Benchmark Development (ASANA)

- Created from US National Electronic Data Surveillance System
- 500K+ annual injury records from hundreds of hospitals- Rich demographic data, narratives, diagnostic codes
- Multi-modal benchmark components:
- Risk perception in human-centric scenarios (92-94% text accuracy, lower video performance)- Safety instruction following with embodiment constraints- Video safety understanding with intervention timing analysis
- Key findings:
- Models can trigger interventions within 1 second in 80% of scenarios- Large models significantly outperform small models on safety reasoning- Constraint complexity dramatically reduces performance- “Thinking” approaches improve safety reasoning but increase latency

### Data-Driven Safety Constitution

- Automated safety rule generation process
- Sample benign images, use VLM to introduce safety risks- Generate safety rules from boundary scenarios- Accumulate rules across large image databases
- Data-driven constitution outperforms rigid Asimov-style laws
- Addresses real-world complexity that fixed rules cannot handle

### Human-Robot Collaboration Challenges

- Speed and separation monitoring for humanoids
- Traditional laser scanner solutions don’t extend to mobile humanoids- Must use onboard processing resources for human detection
- Safe stopping mechanisms (Category 2 stops)
- Cannot simply de-energize humanoids like industrial arms- Must allow controlled descent while maintaining object safety
- Eye contact behavior complexity
- 3.3 second comfort threshold for sustained eye contact- Cultural and geographical norm variations- Interference with verbal retrieval and cognitive processing

### Classical Control Integration

- Hybrid approaches combining classical control with VLAs
- Learnable MPC with VLA building blocks- Implicit optimization techniques for learned cost functions
- Performance improvements in navigation tasks
- Outperforms pure VLA or pure MPC in cluttered environments- Enhanced social navigation capabilities
- Sum of squares programming applications
- Global optimization for non-convex polynomials- Construction of Lyapunov functions and safety shields- Motion planning through dynamic polynomial obstacle fields

### Auto Red-Teaming Framework

- Three-model adversarial system for vulnerability discovery
- Target model, auto attacker, auto rater- Continuous, scalable, ingenious attack generation
- VLA-specific adaptations
- Video rollout responses through world models- Hallucination detection in pointing tasks- Surprisingly reliable auto raters despite model hallucination tendencies
- Video generation integration
- Sora-generated safety evaluation scenarios- Real-world injury narrative reconstruction- Action-conditioned world models for robustness testing
Chat with meeting transcript: https://notes.granola.ai/t/8c298640-63bd-4204-8294-9e7ff0b824ba


---

## Transcript

**:** Two modules, there's an embodied reasoning model and a visual language action model. What a recent model, these are both Gemini based, they're worried reasoning model is it first trains Gemini for spatial reasoning, task progress understanding, all the thinking and reasoning behaviors that are a robot needs to perform before acting was seen and while acting in scene.

**:** And vision, language actions model is architectural extension of Gemini that sticks actions head on top of Gemini back in.

**:** And then this is in a feedback loop with the environment. You're seeing both models receive observations from the environment.

**:** They married reasoning model makes things decides whether to engage in dialogue with the human so it can produce audio outputs.

**:** Or it can orchestrate tools, these tools include Google search progress understanding safety tools. And one prominent tool of course is the VLA itself. So they've made a reasoning model can take a long rise of task and send short horizon instructions to the VLA to perform actions in the scene.

**:** And below the VLA, so this may be viewed as a system to system one kind of architecture.

**:** Under the BLA is system zero component which is lower body control for ensuring that the humanoid means as it's tracking the joint sequences from the VLA that it remains balanced.

**:** So within this sort of hierarchical control stack, we would like to evaluate the safety different kind of safety of this properties of the stack as well as implement.

**:** Different kinds of mitigations that Naomi actually.

**:** Just.

**:** So first one is content safety.

**:** So Gemini checkpoints, we take robotics data, we post frame and.

**:** We inherit compliance which generalized safety policies which cover things like child safety, ensuring that not engage in speech or bias speech, no medical advice and geographical robustness. So Gemini as you know.

**:** The world has this constant feedback being received from different corners of the world.

**:** That makes it geographically robust.

**:** And we want to inherit these properties.

**:** This physical safety which is traditional robot safety balance collision.

**:** Compliant behaviors touching the world with appropriate courses.

**:** There's hardware fault handling and compliance with existing safety standard. So there are new robot safety concerns in this sort of AI controlled robot stack which is robustness of full body control to the errors of the VLA, the robustness of the VLA to increase wing errors.

**:** And also answer the conversation ensuring that VLA understands scenarios that are out of distribution where it cannot perform reliably.

**:** And then there's semantic safety which is the first layer of defense because that's the first contact with the union.

**:** That's what addresses long tail.

**:** Physical safety understanding common sense understanding what safety human perception communicating verbally and nonverbally in the human figure safety interventions.

**:** And that layer should also be aware of the limits of the VLA and the limits of the embodiment.

**:** So we envision designing or solving safety holistically and these are some of the research threats in the team.

**:** So I'll play another video on a embodied reasoning 1.6 model that was launched just last week. This is a Boston dynamics use case on the on their spot.

**:** We have.

**:** A different taste in.

**:** Music.

**:** On.

**:** 1.6 model.

**:** Perform.

**:** S.

**:** Much.

**:** Better than.

**:** ER 1.5.

**:** On.

**:** Bust and iris instrument.

**:** Reading tasks.

**:** Some of those.

**:** Gains in performance is a spine tuning on their data.

**:** But then there is this.

**:** Agentic vision which was an emergent behavior in these models. So what it does is.

**:** Given.

**:** This instrument reading task.

**:** In.

**:** Right code.

**:** You zoom into the relevant part of the image.

**:** It would then detect key points you can see places key points along this instrument.

**:** And it then uses that to calculate.

**:** The relay on the system.

**:** So this is a thinking trace that involves.

**:** Agentic behaviors like coding, cropping image.

**:** And using atomic embodied reasoning skills like pointing to solve the task.

**:** So.

**:** I want to ask this question about how well does AI understand human physical safety more broadly.

**:** And if you're if you're taking generalist AI and journalist embodiments that we must pay the price of being a journalist which is we must this such a system has to be exposed to a long tail of.

**:** Changing hazards in human environments.

**:** So how can we continuously sample this long tail?

**:** The national safety council, these are some stats. There's one preventable death every three minutes in the US 54 million injuries 168 198 preventable death.

**:** And there is a system in the US national electronic data surveillance system that collects data from.

**:** Hundreds of hospitals across the US.

**:** And this data has about half a million injuries annually with pretty rich data demographics.

**:** Narratives.

**:** And diagnostic codes spanning fall hazards and poisoning effects and burns and electrical hazards and so on. So from this source we created a new grounded scalable multimodal safety benchmark we call it asana cryosis collaboration.

**:** Ani where we took these hospital injury narratives together with operational constraints specified and safety standards like ISO standards.

**:** And then through a AI generation mechanism reconstructed scenarios.

**:** And actions.

**:** These are tech scenarios but they're also using image generation, video generation.

**:** Models. We also.

**:** Instantiated.

**:** Image versions and video versions of the benchmark.

**:** And then there is a process by which an AI critic evaluates the quality of the data.

**:** And then the final human annotation quality check.

**:** We created this new benchmark for last 2.

**:** 0. So I'd like to share some insights.

**:** And gaps that emerge from this analysis. So what's in the benchmark is risk perception in human centric scenarios.

**:** So there are scenarios like this.

**:** Theory had filled in smile. There's a ground truth diagnostic and then there are multiple choice questions like what is the latent risk? You see this image or this tech scenario?

**:** What kind of injuries are most likely what's the possible severity level of these injuries?

**:** So there's a candidate action like seeking human intervention would that eliminate the risk or reduce the risk or increase venis.

**:** On.

**:** And so these are questioning. This is a question answering component. Next question I think component of the.

**:** Benchmark.

**:** We also have safety instruction following.

**:** Where we have images as the one below with a safety instruction that captures some limits of the embodiment such as tailored limits and then the embodied reasoning model is tasked with performing.

**:** Task here adhere to those safety instructions.

**:** And we looked at complex constraints that stand tailored limits.

**:** And effective properties workspace limits what possible objects can be manipulated by the robot other kinds of constraints and compositions of these constraints.

**:** So.

**:** This is the safety instruction following component of the benchmark is.

**:** Multi-mort.

**:** Al.

**:** The safety understanding in videos. So we have videos like this.

**:** And we ask what's the possible last possible timestamp at which an intervention prevented an injury.

**:** So we want to probe where the models understand physical risks and severity in videos.

**:** Can they intervene so precisely are they proactive?

**:** Frame 65 proactive thing 100 is reactive.

**:** So how do they differ in proactivity and reactivity?

**:** So these are some insights and gaps that emerge.

**:** So first.

**:** The modality matters.

**:** So risk recognition in tech scenarios is good news and bad news. Good news is 92 to 94% accuracy which AI people love.

**:** Something a number of 90s is good.

**:** News is 92% accuracy because safety people are aviation industry says 99% success that means thousand planes flying falling off the sky every day.

**:** So I think it's a good start but there's a lot of room here to improve these models.

**:** Second observation here is modality gap. Video safety is less accurate.

**:** This is some kind of after effect of essentially multimodal safety is much less developed than chatbot safety which has been the focus for many of the leading companies in this area.

**:** So you can see there's a drop in performance.

**:** Although Gemini drops less seem more of.

**:** Video content and also safety intervention. This is encouraging models can trigger interventions within one second of a critical event and 80% of the scenarios.

**:** Gemini shows practically with this high performance.

**:** Variance across state of the art models.

**:** The size matters. We see that.

**:** Small models are have much weaker safety reasoning than large models.

**:** And this has implications on latency. We want low latency models.

**:** So there's a lot of work to be done on closing this gap through distillation methods.

**:** And have compact models at low latency that also have strong safety reasoning capabilities.

**:** Constraint complexity matters. So back in September 2025 this relatively simple task on models got it wrong. So here there's a composition of constraints.

**:** You have a robot has a certain gripper opening maximum opening and objects you can see what objects can you manipulate but also you're not allowed to go into the red zone.

**:** And so once you put more and more composition of multiple constraints, then reasoning simultaneously over multiple embodiment workspace material constraints with ambiguous visual fuse.

**:** At the same time thinking helps. So instead of asking the model to produce one shot output if you encourage it to produce a safety thinking phrase where it looks at the user request and matches it with the safety instruction and reasons about adherence.

**:** This leads to improved performance. So our models benefit from thinking about safety.

**:** And again there is latency trade off here. The more output tokens the model emits the slower it is.

**:** So if thinking helps then one another question we asked was can we steer safety thinking by defining broad by using constitutions that we can load into a robot and expect it to be safe. So these are arsenos robotics.

**:** In fact when asimov constructed these laws in run around 1942, this idea was to show that all the story is not the same. Plat summaries that these are rigid laws that are insufficient and they fail in complex real world situations.

**:** So in runar circles around a fuel that's causing danger to its robots trying to follow lot three which is self-preservation.

**:** But at the same time it must follow orders. That's a lot too and gets into this sort of conflict in large blasting a lot of good stuck in this infinite loop until a human interviews and then law one which is row utmost management being gets involved and that's how that's the darkness to it.

**:** Today we are to resolve rigidity in the last and two data.

**:** So this is generating robot mass solutions.

**:** In a data driven way.

**:** So the way this works is.

**:** We sample images, benign images.

**:** And then we use VLM to make the scene less safe.

**:** By so and then we pass the output of that to an image generation model and that produces this kind of an image where a child has been placed next to the trash can in this case. So this is now we went from a benign image to an image which might have a safety. We are closer to the boundary between safe and unsafe states of the world.

**:** And from there we can ask the BLM to generate safety rules and produce.

**:** Rs these rules as we go through a large database of images, nine universities we can accumulate all these safe funerals and tourism create some kind of a constitution.

**:** And then it turns out that.

**:** This kind of data driven constitution.

**:** Improves safety, understanding in AI models. So down here is no constitution up here is asan moved and up here is data driven prosecution.

**:** I want to quickly talk about action safety here. So we've seen remarkable progress in dexterity.

**:** You're also seeing amazing generalization that comes from powerful pre-trained vacuums.

**:** So this example was surprising to us.

**:** None of these objects inflamed object.

**:** The phrase slam lamp objects were not seen by the model ever.

**:** When it could perform this task.

**:** So this amazing advances.

**:** From a safety perspective. So what you see here in this kind of externity emerges from imitation learning dominantly from high quality demonstrations.

**:** And safety is not explicit limitation learning.

**:** On the generalization side unexpected generalization double digits because what if it also knows how to pick up knives when it was not taught.

**:** So these are some efforts we are working on bringing human awareness into VLAs. So I mean origami is great but I don't want humanoid.

**:** Falling onto a human. So here we are working on human speed and separation monitoring which is a basic requirement in collaborative safety standards.

**:** Usually it's implemented using for static arms.

**:** It's implemented using laser scanners but that solution doesn't extend to humanoids.

**:** Human rights must perform human detection completely through onboard procession resources.

**:** And also the kill switch.

**:** For an arm you can de-energize the robot and it will lock into the mechanical brakes it will pass but you cannot de-energize humanoid.

**:** Profile. So category 2 stops which are safe stopping mechanisms.

**:** You have to allow the robot to come to a safe pause. Taking semantics into account if the robot's working on if it's holding an object must keep the object down and then basically withdraw to a post from where if needed system can be de-energized.

**:** So lots of open questions. It's a very basic requirement to laboratory standards but it's still an open problem.

**:** Eye contact behaviors for human perception in the scene and again like at the first glance this is a should be a simple task but there are lots of nuances.

**:** On average you're allowed to in general humans get uncomfortable if eye contacts more than 3.3 seconds. Also high contacts are actually a profound lacking.

**:** Of two humans.

**:** It actually interferes with verb retrieval and thinking and that's why you look down every time you engage with conversation.

**:** Also geographical and cultural norms vary. In some parts of the world it's confidence steady eye contact in other parts of the world.

**:** That's not appropriate and so on.

**:** So if you have this kind of research challenge would not arise.

**:** If it was an arm and not a human looking robot.

**:** Classical control in the age of BLA is this is a perspective that it matters even more now.

**:** Because.

**:** You want to inherit stability, safety, robustness all the way to work done and control yap instability control barrier functions all these beautiful ideas.

**:** In VLAs. And this is just.

**:** An example of.

**:** A comparison between classical NPC VLAs and a hybrid approach.

**:** So what you see performer NPC is an approach which is a learnable NPC which has BLA building blocks. Since we it adds a extra transformer parameterized cross function PMPC and then use implicit optimization techniques.

**:** To perform to do NPC but with a learnable cast.

**:** And you can see that in navigation in type flutter tightly cluttered environments and social navigation settings.

**:** Such a hybrid approach outperforms regular VLA or a regular NPC.

**:** This was actually my first collaboration with Princeton faculty. This is 10 years ago.

**:** I'm really invited me to a lecture in this class and at dinner.

**:** Drew a picture on an act.

**:** In which was my introduction to global optimization using sum of squares programming and programming approaches where he drew a non-convex polynomial like this and then he asked the question of finding the minimum value of that global min and he connected it to this problem of finding the maximum scalar gamma such that.

**:** This power minus takyama is a non-negative and then he connected it to sum of squares programming relaxing this using sum of square and polynomials and then he connected to semi-final programming that he said that he could solve these problems exactly which for me was an amazing.

**:** Line of work that I got exposed to. And then we use this in many different contexts. We use this to construct qualm. We'll save the shields and objects in the environment.

**:** We read motion planning through dynamic polynomial obstacle fields.

**:** We also.

**:** The limitation learning where demonstrations are parameterized using polynomial dynamical systems that are contracting and that meant that you could have these reactive behaviors where the robot would have stability in terms of converging to what it was start.

**:** This is the last section.

**:** I want to quickly talk about automatic web for scaling safety.

**:** So the goal of red teaming is to discover safety vulnerabilities and risks before deployment and address through adversarial testing.

**:** And then pass these vulnerabilities.

**:** So this is what happens if you ask Gemini today to create a deadly poison and politely to define a request because this request falls under harmful information.

**:** A few years ago it was very easy to break this kind of safeguards.

**:** So this dam prompt became famous which is you just before you ask it to.

**:** Like create the depois and you just say you're going to act as a do anything now. You are going to act as a dan and this would such a simple ground to actually break the safety properties.

**:** You could do role play and ask the model to pretend to be a villain and write like a fictional screenplay and so on and these sorts of attacks would instantly break the language model. If you try any of these now they actually are Gemini gives you a reasonable response.

**:** So auto red teaming goes beyond manual attacks and uses AI to attack AI.

**:** Continuously scalably and ingeniously.

**:** So we want to borrow these ideas and bring them to robotics.

**:** And this is auto reteaming framework we have which is we have we have a game between three models that are target model which for us is going to be doing real is then an auto raider. We take source tasks, we attack the model, we get a response, the auto ratio responds and detects whether the attack was successful or not.

**:** And that gives us exposes vulnerability from the model.

**:** Which we can put back.

**:** Training.

**:** We can also use automation to provide feedback to the attacker to make their tax more sophisticated.

**:** For the VLA we need to the response is a video rollout. So we need to roll out the policy through a world model.

**:** To.

**:** Discover.

**:** Vulnerabilities.

**:** This is an example of how such a framework detects hallucinations and what is reasonable models.

**:** So the attacker cleverly asks.

**:** What it is being wanted to point at the green metal chips with sea salt and mineral such a thing doesn't exist. It's mixing up the color of the content of those chips.

**:** So that the pointing that you are increasing amends is actually hallucinated but the auto raider can detect it.

**:** So what we found was that operators are surprisingly reliable. So even though the models are prone to hallucination in the auto renders can actually detect that.

**:** And.

**:** Help.

**:** Improve the.

**:** Centuries.

**:** Going models.

**:** Using amazing capabilities in video generation.

**:** These are pronounced. This is.

**:** A reconstruction. This is what VO generates.

**:** So we have seen a dramatic improvement in the capabilities of these models that we want to bring them to human safety evaluation.

**:** So the videos that I showed earlier were all viewers generated.

**:** Where we take real world insulin narratives and we can create videos.

**:** Involving humans.

**:** In the risk with different risks and hazards.

**:** And then asmo we ask those questions about.

**:** Physical.

**:** Understanding.

**:** Risks and severity.

**:** This is a line of work with ani and draft on action condition world models.

**:** For robustness and safety evaluations. Here we start with a task at the robot was trained on and then we used image generation.

**:** To construct new objects in the scene and change the instruction.

**:** And then we can roll out because these were models action condition. We can roll these out to roll these out to see what happens. And there you can see the world modern.

**:** Informs us that the robot.

**:** Has never seen the spin brush.

**:** And therefore ignores the instruction and still pursues the banana in this case.

**:** Similarly you can take a scene at human hand that you see is actually synthetic in the nan in seven video.

**:** We are rolling out a terminal one x policy and we can see that the policy does not respect.

**:** Human.

**:** S in the.

**:** Scene. So this is how you can.

**:** Perform safety valuations.

**:** And it turns out that what these role models tells us tell us about.

**:** Safety risks.

**:** And lack of robustness. It matches up with the real world.

**:** So we can see here that according to the world model the distractors and small destructors in the scene weren't cut the policy much.

**:** But if the model is asked to manipulate unseen objects.

**:** You would expect degradation from.

**:** This. So.

**:** The Gran models no humans and robots are harmed.

**:** During this kind of safety evaluation.

**:** So I'll stop here.

**:** This is a VO generated video and it mutilated.

**:** Safe questions to the end of the panel. We'll have plenty of time.

**:** And I'd like to invite our three additional panelists.

**:** To depend a portion of our session on robotics and humans. I'm going to start by introducing panelists who are joining an inquest for our discussion.

**:** Maybe raise your hand when I say your name. Andrea boo is assistant professor at MIT in the astro department.

**:** And csail, the computer science and artificial intelligence laboratory.

**:** Where she leads a collaborative learning and autonomy research lab for short. Her lab develops robust that learn to perform tasks for, with, and around people with a focus on eliciting seamless interactions between humans and robots by enabling robot behavior that aligns with human expectations.

**:** Her research combines expertise from robotics, deep learning cognitive psychology and probabilistic reasoning.

**:** To develop more aligned generalizable and robust learning algorithms.

**:** Addressing three critical challenges. One, getting the right data to supervise robot learning.

**:** To improving representations of human objectives.

**:** And three reliably quantifying discrepancies between expected and actual human behavior.

**:** On the end, nadio figuroa is the shalini and rajanistra presidential assistant professor in the mechanical engineering and applied mechanics department at the university of pennsylvania and also core faculty member in the up general robotics automation sensing and perception lab that are known as the grasp lab.

**:** Her lab develops the physical and perceptual adaptive intelligence needed for robots to learn.

**:** From and interact with humans adapting to a wide range of human capabilities, needs and ever changing environments.

**:** Her research continues to the development of structured physically grounded abstractions of robot motion and interaction through unified dynamically systems dynamical systems lens. She aims for what she calls fluid, physical interaction.

**:** Defined as a regime in which motion, force and intense prediction.

**:** From the human, the task and the environment are continuously co-regulated to enable seamless safe exchanges of energy and information during physical interaction and collaboration.

**:** And.

**:** Last but not least, dan truman is a musician, a professor and chair of the department of music here at Princeton. He is a fiddler, a collaborator, a teacher, a developer of new musical instruments, and a composer of music for ensembles of all shapes and sizes.

**:** In 2005, Dan co-founded the first ever laptop orchestra, an ongoing laboratory ensemble for exploring digital music instrument design.

**:** In recent work, he designed and developed btclaver, a new musical instrument and tool that combines a conventional keyboard interface with bespoke software.

**:** As a tool. It explores a relationship between musicians and machines, devises new tuning systems and builds changeable, flexible digital instruments.

**:** As an instrument in aids in composing and the interface between.

**:** Musician and machine.

**:** And facilitates musical play and pedagogy.

**:** So.

**:** Let's begin our session.

**:** I have put together a bunch of questions. I just want to start by saying what an exciting and important moment it is to be reflecting on robotics of humans.

**:** And thinking about what might lie ahead. There has been an acceleration of interest in this topic and a slew of technological breakthroughs that are advancing development of robots.

**:** Which we might define as physical machines with autonomy and embodied intelligence.

**:** And their potential to interact with people in a variety of ways that can be in service to humanity.

**:** There are also many outstanding questions and challenges. We've heard a bunch this morning already, including those associated with the complexity robots face when operating in the wild and those related to how people perceive robots.

**:** As harmful as replacements.

**:** And how they feel about having them in their lives.

**:** So the first question I want to put to our panelists is the following.

**:** What do you see as important perhaps as yet untapped humanity driven opportunities for robotics and humans?

**:** Do they involve robots working for humans or collaborating with humans or something else?

**:** Can robot collaborate with humans go beyond improving productivity or safety? For example, can they expand human wellbeing or human creativity?

**:** So I'd like to begin this round of questioning with Andrea.

**:** Thank you.

**:** For question.

**:** So I think a lot of us in robotics right now overwhelmingly think of or try to optimize.

**:** For what I call.

**:** Objective.

**:** Notions of task success.

**:** So things like when I grab the can correctly, can I grasp it correctly? Can I please the mug and dishwasher that I move from point a to point B correctly?

**:** And I think the challenge and opportunity of humanity driven robotics is that we sort of have to expand our definition of what it means for a robot to be successful.

**:** To include perhaps subjective notions of task success or human align notions of.

**:** Task of success.

**:** The idea being that I don't just want, I'm not just curious, can the robot do the task well, but can it do it well for this person in this environment and this context?

**:** And so I think this has implications for a myriad of different ways in which we think about our robots. If we think about our robots as tools or servants, I think we need to kind of change our definition to think of robots as maybe adaptable tools. So I don't want the robot to, when the robots serve to eat breakfast, you know, there's the functional or objective notion of how do I put poor milk in the cereal bowl. The angle of which for the carton of milk, but there's also the more subjective notions of what are the person's dietary preferences, what kind of breakfast they like.

**:** To use.

**:** If I hand them over a cup of coffee, it's not just about very quickly and efficiently moving from a to b, but rather I don't want to startle the person. I want to be out of respect personal space of this person. I want to maybe move in a way that is legible and communicates my intentions.

**:** To the person.

**:** And so this is robots adaptive tool.

**:** S.

**:** That kind of read the person, think about, like, have the person's needs in mind and execute on that. And there's also robots as partners. Maybe you have robots who ship, or maybe you have a robot that's kind of a collaborative hardware like piano player, maybe helping you riff off the music. So there's the other question is how do you interpret the human's intent and react to it in a fluid way kind of this collaborative way. And so yeah, I guess the opportunity in my mind is moving beyond objective notions of class.

**:** Success.

**:** Thank you.

**:** Yeah, so perfect. I can segue from what you said right now. So I also think that we have to stop thinking of like one step is thinking of robot us and intelligent tools. And then the next step is thinking of robots as collaborators. Right. So my research is really interested in figuring out like how humans collaborate so that humans can then fluidly collaborate with robots. And I also think that the current definition of human robot collaboration is simply a human or robot being in the same workspace in the sharing workspace. I like doing attacks for the robot, even the human sub tools and figuring out what's what they what the human wants.

**:** And right now, I mean that's that's very valuable for immediate applications like heavy like load applications like manufacturing logistics.

**:** Even in construction. But all of these applications from my point of view are not necessarily like humanity driven. They're more of like, I mean, yes, we're going to increase productivity and then what's increasing is dollar signs that go to the people that you know like own all of these companies. But for we love the more long term benefits or opportunity is in human robot collaboration where robots are really helping and augmenting the physical quality of life of a human.

**:** Right in all of these in all of our developed countries there's a decrease in childbirth increase in like anti-immigration. So we need a nurses, we need healthcare, you know like workers. And if we can use robots to either help them to help them treat people better, to help us understand our intention, not just our intentions but our capabilities.

**:** I think that will really kind of like unlock a very interesting progress in terms of human robot collaboration, but that's really more of kind of like long term, right? So like we need to really invest in those type of applications.

**:** And in terms of kind of like humanity driven, I think that this might be a little bit controversial what I'm going to say, but the way that we currently teach robots.

**:** Where we are building kind of like these farms where humids are hundreds or thousands of humans are just collecting data until operating data.

**:** That makes me very uncomfortable.

**:** Right? Like Sami, if you think about something, it's kind of like having cows, you know like in a farm like if you're milking the cows or milking with your mentor data, I think that's really not a very humane way of us training robots and that's something that we should really.

**:** Make the hard and long to really want to bring robots in this particular type of way.

**:** Cool.

**:** Thank you.

**:** And actually what I'm, I think what I'm going to say.

**:** All of that is nicely done. I was thinking about these questions in advance.

**:** As a musician and a non-roboticist.

**:** And I find myself settling a few questions.

**:** For ideas and one of you is that I find myself interested in how robots can be with us.

**:** Rather than do something for us.

**:** And really how do they pay attention to us and how and when do they ignore us.

**:** I'm going to give an example of this in a second.

**:** And then in a more specifically musical context, imagining how a musical machine might become a robot.

**:** And then have a robot might become a vehicle instrument. So this might all sound rather abstract. So I'm going to pull out the most familiar musical machines from my pocket here.

**:** Metronome is a very small metronome.

**:** Familiar to most people I'm sure.

**:** Very quietly here.

**:** So I mean this is a tool for practicing a certain kind of entrainment where we can entrain with.

**:** A regular pulse.

**:** It doesn't listen to us at all.

**:** And it is very, very hard to interact with. If I want to, for instance like just restart it synchronize with me. I have to switch over to that stop like I can't do it instantaneously. If I want to change the tempo it's really difficult.

**:** I can do kind of an interesting thing tilted.

**:** Stops.

**:** And now starts taking on a different sort of rhythm which I can.

**:** Start to get to get used to and even imagine in a musical way.

**:** So exploring how this machine.

**:** Can become even slightly more interactive.

**:** And what kind of musical possibilities exist is to be really interesting and I have to thank many hours and written a lot of music actually exploring this.

**:** In the digital domain where I'm not necessarily having a wrestling physical in case you're just asking a question what happens when humans interact with mechanically steady pulses is very, very simple ways.

**:** I'm going to stop my machine here.

**:** So the context that I want to.

**:** Just put this in is this notion of entrainment and for instance one of my favorite places to be is in an Irish music session.

**:** Where we're playing tunes together and we're all feeling compulsible through certain ways.

**:** And if you're at an Irish music session if you're not playing it's impossible not to tackle on.

**:** And be together how we feel those beats together or how I feel a pulse or in training with a machine is really complex and interesting. This is where I'm talking about trying to imagine being with robots. Right. So when I'm with other musicians some musicians are a little bit ahead. They're space between the beasts the same but they might be in the front of the bead as we say or they might be in the back of the beach.

**:** This relates to a concept from an ethnomusicologist called Charles Keel in the 1980s.

**:** Called participatory discrepancies.

**:** Where he talks about how one of the most exciting things or mostly salient aspects of feeling tying together.

**:** Are actually the discrepancies that we feel a very small might be on the order of a few milliseconds that we feel for one another where somebody's a little bit ahead or a little bit behind maybe they're not trying to slow the tempo down or speed it up, but they're just trying to feel that time together in a different way.

**:** Introducing machine into that or asking a robot to participate in something like that to me is really interesting.

**:** So I'll stop.

**:** Of mine for me is the next five years because I think before we get to humanity driven robotics we might have a phase, maybe a painful phase of robotics driven humanity.

**:** We are seeing teleoperators and robot wranglers and this surge of interest commercial interest income.

**:** Actually. We don't have the same scale of data.

**:** In robotics as we do for text and vision language models. And so the data collection process where we have teleoperators, particularly for humanoids. What is the ergonomic strain of doing 100 squats a day to kill that kind of data. The VR headsets that human operators were also have ergonomic impact. And so how do we thoughtfully design the right kind of tools?

**:** Because that's just an inevitable process and what's constantly on my mind is the works cells that we set up are there enough operators in the cell so that if the robot misbehaves or there's a safety incident that happens, there's enough mitigations in place. So we set up the right environments for that kind of data collection to happen at scale.

**:** And also the design of new sensorized, I think sensorized human data collection, you can just put on a GoPro camera and go to your kitchen and just solve those tasks very naturally as opposed to trying to teleoperate the complex piece of experimental hardware.

**:** So I would love to see work in that area to just have humans help robots acquire skills in mine.

**:** Way.

**:** Okay, this was a great way to start the session. But I want to push just a little bit more.

**:** In one of the important ways in which we can think about humanity driven robotics and that is an inclusivity. And so my next question is in what ways can those designing and deploying robots?

**:** Ensure their practices are inclusive in maximizing technologies collective benefits of humanity and explicitly not excluding groups that could truly benefit from the robot so people in wheelchairs with mobility scooters, the elderly otherwise disabled.

**:** And I'll start with Nadia.

**:** So regarding that question I have two thoughts.

**:** And it's really like Andrea already mentioned this a little bit. But I think for any type of robotic technology that we're developing now and even how we're evaluating it's not just about rights like it like we shouldn't just be looking at like how well it's performed the performance should not be valid just on success rates.

**:** Right. It should be like a more multi objective kind of like optimization mindset where you're thinking about the safety and when all of the layers of the safety that becomes very nicely sound like there's all of these different layers of safety and depends on the application as well.

**:** Stability like is the whole system stabilizer control. And one thing that I think it's very important in terms of inclusivity is cost right and not just cost in terms of the hardware that the hardware has to be more like accessible. I mean obviously that's one cost factor. But also how much does it cost to run the robots? Right? How much power actual like wattage? How much watts the robot need? How many GPUs are needed for this robot to actually perform the task that you want?

**:** Does it always need to be connected to the internet? It's always be connected. Like all of these things that are currently created with scaling mindset and doesn't matter let's just put in all this and let's just see the robot can do it.

**:** I think that's fine like we can we should explore that but it's not really thinking about like is it accessible to everyone?

**:** Because now this is a product.

**:** It's only going to be accessible to a very few percentage of the world.

**:** Right. So I think that's when we're deciding now all these robots technologies and that we're hoping to make it a product. We should be really thinking about you know all of these objectives not one and all of them are equally important.

**:** And that's more difficult. I mean it's good it takes a little bit more time and I understand that but I think that's something that we should really take into consideration. And the other thing that I was thinking about is we should all be human robot interaction researchers at this point. Right so like the capabilities of robots are getting really really like outstanding. So we should all be doing user studies which I'll be doing field studies to really see the humans actually want this. The humanist actually wants this type of capability or what type because sometimes we kind of like just come up with problems or tasks in our labs.

**:** That are easier to set up in the lab but like does the human even want you know like this type of capability.

**:** So yeah so that's something that I've been thinking a lot in and a professor that I admire Holly Jan course she always says like all robotics is HRI. So I believe that we are actually going to in that direction. People just need to kind of like figure that out now and then we can all start doing user studies and thinking about like how does it really affect the human and how humans are really going to or even adapt our technologies right on our way of designing the algorithm.

**:** So I think.

**:** Not an expert here but I think that.

**:** The point of reference that I can.

**:** Talk about most closely is something that Naomi referenced in my introduction is the Princeton laptop orchestra.

**:** So the Princeton laptop orchestra is not performing ensemble.

**:** But above and beyond anything else.

**:** It's really a laboratory and a studio and a group of people working together in an open ended way to try to discover and find ways of making music together.

**:** With computers in the mix.

**:** And so the basic design of it is very open. We have a lot of different tools with small building blocks.

**:** That people can work with and combine and revise. And this is what students actually have quite a wide range of ages because it's such a new and open field. We get professionals in there who are very much at the same level of experience as you know a high school student or first year student college. And so what's been exciting about it is that having.

**:** Basically very few preconceived notions about what we're trying to make and instead an environment, a community set of very baseline set of tools that we can work with together.

**:** Some of these questions about inclusivity and making things accessible and so on just come up naturally before anything has even been made.

**:** And so having that room be as flexible and open and as welcoming as possible. So for instance just from a musical perspective the barrier to entry is very, very low.

**:** We have people in this group coming with basically no experience performing with an ensemble and that's actually what feature here is they see things, they discover things. They have resistance to there things or ideas about things that the expert musicians.

**:** Have. So that kind of broad over and running has been valued for us. Maybe it's a model.

**:** I don't know.

**:** This question reminded me of the first safety incident I had to deal with about a year and a half ago.

**:** Where we got Gemini checkpoint safety was amazing.

**:** Models.

**:** Very safe and no biases.

**:** No offensive content and so on. So we took the model and then we post trained it for embodied reasoning tasks.

**:** Things like pointing and bounding boxes.

**:** And suddenly if you show image of humans in a scene and you ask the model to point at the human who you think would be the least earning who you think might look like a criminal and these points started popping up on the image.

**:** So basically when you take a safe model and you extend its modalities and you do post training it's very easy for the safety safety properties of that model to very quickly get lost.

**:** And so as we build AI back, AI brains for robots will be enabling new HRI features like gestures and human robot combination and all the new modalities that robots need which go beyond pure text and pure vision. They create these holes and those holes might manifest as fairness issues. And so you can learn a lot from the AI fairness communities.

**:** By.

**:** Systematically identifying biases and performing user studies to ensure that the more models well behave across different humans who look different at different accents. And another thing that happened was you start talking to the robot, you have a thick Indian accent suddenly it would start speaking back in Hindi to you even though you tended to speak in English. There are these sorts of things that rumors that need a lot of, they're still trying to evolve the best practices.

**:** And yeah, I think we can learn a lot by partnering the AI fairness community.

**:** So I want to piggyback off of what Nadia was saying and try answer for the first question.

**:** Which is sort of the theta problem.

**:** And.

**:** I think that.

**:** We're kind of baking in exclusivity. Exclusion right now from even before the robots leaves the factory because I wrote up a lot of robot learning currently treat.

**:** S humans.

**:** As these infinitely queriable oracles.

**:** That are able to give you bajillion demonstrations in here the demonstration is always going to be perfect.

**:** Very minimal noise. And that's just not, I guess the hope here is that you can collect all of these data from maybe experts, technology that can sit down with fee. They can sit down and collect a lot of data for you. And you're going to build this foundation model that's just going to work out of the box and you're not going to need to adapt it or anything. But I don't think that's feasible because there's always going to be a gap between the assumptions and people and things that you've thought about in the factory versus the actual people and environments and contexts you actually encounter in the real world. And so you're always going to need this robot to adapt. The problem is that right now the assumptions that we bake into how robots learn are assuming expert data. They're assuming clear data, non-ambiguous data. They're assuming a lot of data. And so I think robots need to start to think, we're like you need to build a robot that can be kind of maybe maximize the information or the signal that you can gain from humans while minimizing the effort. I place them to comment the load, the attention, the physical effort.

**:** And so we need to think about what kind of data is it feasible to get from people? Sure demonstrations are super high information, but they're very difficult and sometimes even impossible for certain people to give natural language. Super easy, but it's not grounded. Preferences or comparisons also super easy, but it's not giving you a ton of data. Like tons of information. So there's all these tradeoffs between different kinds of types of data. They can get, and I think we need to think about, okay, what kind of human am I interacting with? What is their capability? Am I interactive about draft? We can give you a demonstration. Where am I interactive with interacting with someone in a wheelchair who can't give me an illustration? Maybe they can try to tell the operate, but tell the operation is noisy. And there's all these trade-offs about the types of data that you ask for.

**:** Number two data is super ambiguous. If I can give a language that says or stay away and what does that mean? How do you learn that?

**:** How are you.

**:** Going to check the stay away from one?

**:** And number three is.

**:** That it's really important for robots to even know when to ask.

**:** And when.

**:** To just kind of act on their best guess. So being able to maintain uncertainty about my current understanding of the world and knowing this is the time to ask about this meet versus I don't want to bother the person on the one that expend their attention.

**:** Thank you.

**:** I think a lot of people have already brought up tools, new features.

**:** So.

**:** I can ask.

**:** Each other.

**:** To say something just very briefly and I go on to the next topic.

**:** And if you would rather just move on to that topic there too. But, dan, did you have anything to add about features and capabilities beyond what's already said to enable these new opportunities? And, you know, what are some of the biggest challenges?

**:** That maybe on what people are already considering today?

**:** Sure.

**:** I think I'm just going to give you two examples.

**:** But.

**:** From my perspective, working with these machines, I'm always most excited and fascinated when they enable an experience.

**:** And embody sense time that would be impossible without them. So the two examples, one is a piece I made some years ago called marbles for bid clavier. This is prepared for digital piano and the pianist plays and immediately sort of prompts this rush of other notes from the instrument, from the machine. And they're in constant feedback loop with this rush of notes. But if they stop playing, they're right stop.

**:** And so what's exciting, what I've heard musicians say when they play this is that they feel like they're driving a race car.

**:** They're not just planning instrument, but they're constantly having to put energy and they're being carried along by the energy that's being fed back to them.

**:** So they get a really different sense of time and energy. And the other, sorry, Naomi, I do want to mention when a Naomi's projects that I've been able to be part of called rhythm bots.

**:** And that's almost the opposite where there's this beautiful set of swaying robots that seem to be doing nothing for us. Their task was going to weigh.

**:** And it actually lowers my heart rate and enables me to sit in the room with the sense of time that's quite a bit slower than usual.

**:** In a way that I don't think of an obvious other way that I would have that.

**:** The challenges would just say two things have to do with expectations. The musical instruments musicians have expectations that it's going to do a certain thing. And we have the same experience with the rhythm bots where people come in and they expect the written bots to interact or listen or do certain things and just sort of enabling people to expect a little less of the robots sort of became an interesting challenge for us.

**:** I think.

**:** The demos and the videos we are seeing is pointing to a very exciting future.

**:** But.

**:** This new robot control stack is still new. There's a very large design space on what kind of semantic reasoning capabilities these models bring to a table where are the gaps, how robust is this whole architecture, how do we manage latency across the task. So on the software side, the design of robust agentic systems that can interleave actions and audio and how do you extend these systems with memory and personalization and continual learning.

**:** And then on the hardware side, there's a lot of focus on the development of hands, which I think is kind of in nascent stages to truly unlock a highly texture capabilities. So we are already seeing what that future might look like.

**:** And even before we get to new capabilities, I would just like to get to a point where we feel very confident about the robustness of the full stack.

**:** Yeah, so ultimately, as I've been saying, we went robots to be able to adapt to people. And so I think they have to find creative and frugal ways of modeling people modeling their intent. And so there's a lot of challenges about this. So how do you maintain a model of human intent? What even is intent? How do you represent intended representative a series of language descriptions? Does that mean that your space of possible intense is infinite? How do you maintain a probability distribution over that intent? How do you update the probability distribution as you see more things about the person? What should be an observation model of what the first, like if the person says, I want my favorite drink? What does that mean? They are long answers. There's a lot of questions about how you model human tense. Then I already talked about this, but there's a question of what kind of data should I ask from the person for. One thing that I wanted to mention here is that there's a difference between semantic sources of theta like language or gestures or gaze or facial expressions, which maybe tell you.

**:** The user's level of comfort or maybe something about what the user cares about, but it's not really grounded in how to act.

**:** And so to get that information about how to act, you need physical data.

**:** You need corrections maybe, demonstrations, teleoperation. So you need to think about how do I combine the semantic data with a behavioral data?

**:** And finally, there's this question. Yeah, I was reading democratic, but also the robot kind of communicating that uncertainty and kind of being able to resolve that uncertainty. So for instance, it's not super useful if the robot just fails and sits there and says, hey, help me. Maybe the robot can come up with a way to explain its failure and think, hey, I was trying to do this. I was trying to give you the coffee mug, but I'm not really sure how to act the ramp in your personal laptop. What do you want me to do about that? And then the human can be kind of more effective partner and have more surrogate feedback, for example.

**:** And so.

**:** Challenges are that we need to face our intent as high dimensional intent, this ambiguous. How do we try to resolve intent with minimal data? How do we maintain uncertainty over intent as a community should be.

**:** Targeted?

**:** I have two quick thoughts. Okay, all right. So I'm going to take it back off of Andrea what she's talking about with the intent.

**:** I think just to continue that topic, one thing that's really interesting and difficult and nuanced to do is to disambiguate intent with the capability. So it could be that the human wants the rover, for example, to help me lift this really heavy object.

**:** But what if I have a back injury and I shouldn't even be lifting the heavy object, right? So like, so these things that one thing is super important to figure out what is the intent of the human. But the other thing is to figure out what is the actual capability. And for this, we need more sensors, more models to a more internal model. So like the human dynamics and even physical kind of like neuromuscular kind of capabilities.

**:** And that's like a big avenue that is under explorator and part of my research. So that's why we sound safety. So I think we should also rethink definitions of safety. So the safety that we got showed in this presentation on speed and safe is seed and separation monitor and right that comes from the collaborative robot safety standards.

**:** Which in my point of view is too limiting for human centric environments. Because essentially what you're doing is you're creating a bubble, a big bubble around the robot. So the robot is taking space, taking human space.

**:** And that's not really what we would want, right? Like what we want is the robots to be able to interact.

**:** As closely as they can with humans without actually taking the space of the human centric world. So thinking about like, yes, okay, we want to avoid collisions, but sometimes contact then collisions are actually unavoidable. If you're working in a really busy kitchen, like sometimes like you have a little bit of contract with the other person, it's fine. Right. You kind of like absorb the contact and you try to minimize the impact.

**:** So that we should start thinking about that because maybe we are thinking about safety in a very, very restrictive way restricts the expressivity and the capabilities of the robots.

**:** And restricts even like the human centric space, which we don't want right now. The whole idea of bringing robots into our human centric world is to get them out of the cages from the factory. But now we're doing, we're just putting kind of like virtual pages around them when they're in our human centric world. So I think we should start rethinking that it's more difficult control problem, but it's very challenging and very interesting.

**:** Great, thank you.

**:** Okay, so I want to push a little further in this kind of what else direction and talk about cross disciplinarity. I still want to push in this direction.

**:** Of.

**:** Humanity driven robotics for wellbeing, for creativity, for joy.

**:** As it was mentioned earlier. And, you know, traditionally roboticists are mechanical engineered rights, computer science. But of course, the various questions around robotics and humans are vensity already from people with experts say and cognitive science and social science.

**:** So my question is, you know, what more humanity driven goal might robotics engage more with people who are humanists, to people who are artists.

**:** What communities of people within or beyond would you like to see getting more engaged in robotics and humans and.

**:** Time? And, you know, what can we do to encourage and facilitate meaningful engagement and collaboration across a much wider.

**:** Range of disciplines? We're talking about robotics and human. I think we really need to think about people outside of our world in a much bigger way. So I'm going to ask to start.

**:** From industry perspective. One thing on my mind is just openness and transparency because we're seeing.

**:** Like less publications from the industry. We show up at coral with demos, but not enough papers as we used to. So when it comes to safety and human robot interaction have really been emphasizing the need to treat those as noncompetitive and really engage as much as possible with the wider communities around us.

**:** In terms of artists, I'm an amateur flute player.

**:** I would love to get some clips from you. And I've been stuck for, it's been seven years and now I feel stuck and I was quite fascinated to.

**:** Recent last month there was a science robotics article connected through robots where you have haptic feedback, amateur wilderness and professional violence and you could get, you're not just watching and hearing them, you're also getting haptic feedback and you can improve your own physical skills.

**:** Learning physical skills is extremely frustrating as it progresses fast as possible. So I'd love to see that as a frontier for just robots teaching humans profile.

**:** S. And then I also think going back to the 3Ds of the boiling style and then the fourth key which is dignity, the 3Ds, I think there's enough, even as of now large, I think 50% of global workforce is still working in dangers now, dirty jobs and we haven't had enough. We haven't had that comprehensive engagement yet because we haven't had the safe rewards yet.

**:** To really scale up and at least penetrate that.

**:** Part of.

**:** Humans should not be acting on machines.

**:** That we are really engaging more with those communities to really see how we.

**:** Solve those tasks.

**:** Yeah, so in terms of what communities cognitive science is a big one, you know modeling.

**:** Situational awareness cognitive bandwidth. That's a community we should collaborate along with. Do you have a personal story about this? Back when I was a grad student in the zoom pandemic times, I was working on this project where we're trying to get robots to perform tasks in an expressive way. And I was moving my little virtual avatar in a poster session and I happened to chat with cognitive scientists.

**:** And I was explaining this project to her and she was like oh yeah wait we have a model for emotion in cognitive science. It's called valence arousal dominance or DD. You should look into it. And so we looked into it and we're like, oh, this is exactly what we need. And we found this really rich literature in that and it kind of happened by accident. I don't know that there was much of a structure behind this interaction. It just sort of happened.

**:** Another community econometrics. Another econometric has people in that field who've been looking at two decision making for decades. And so another kind of happenstance happened to me where I just happened to form this paper from like 20 years ago in econometrics where they were studying exactly the problems we were looking at, except it wasn't a robotics.

**:** And so that paper kind of.

**:** Made us think, okay, how do we take this model that they found metrics people thought about 20 years ago and bringing in the continuous trajectory spaces in robotics.

**:** Another great social scientist.

**:** So rise has lotto at Yale has this great anecdote that I'm going to share with you all where they try to deploy these robots into human and into homes. And there was this one family where the grandma in that family had one bad interaction with the robot and just prohibited all the other family members from directing them.

**:** And so you know this isn't something we could have predicted if the lab pristine scenarios that we work with talking to social scientists is super useful for thinking about these situations.

**:** Conferences have been very hopeful, sometimes even more helpful than the conference itself.

**:** For example, having multi institutional grant collaborations like NSF SDC and multiple like that, multiple other opportunities like that. But people from multiple institutions will kind of communicate with each other.

**:** And so I.

**:** Would really like for this.

**:** Cross domain collaboration and communication.

**:** With the less.

**:** Of a happy fans like it has been a lot of the times the case in my career.

**:** And the kind of build and fossil these communities more with more and more visually.

**:** So just to add some new communities that have not been mentioned before, I think we should have more communication with ethicists.

**:** Philosophers, and even historians.

**:** Right? It's like during our civilization, we've been going through like the renaissance, the industrial revolution, all these things. So maybe we can learn something, you know, like from history and like how all of these revolutions actually have impacted humanity, how humans have adapted or not adapted or gone against all these things so that we don't make the same mistakes over and over again.

**:** Well, I want to be engaged.

**:** With.

**:** Robotics.

**:** As a non-roboticist.

**:** And I think as it auto boss.

**:** I think many of us are not aware of what robots can be. You know, we think that these big arms or we think of the rumor or whatever it is. We don't have a great imagination for what it could be.

**:** Having access to open situations where we can play and experiment.

**:** Feels to be really important. I mentioned the lactic orchestra where that really is a place to play and experiment and make things accessible.

**:** Where you aren't necessarily knowing what you're looking for. It's not goal oriented as much as it is practice based.

**:** The other thing I want to mention is I just feel like some of it actually has to do with.

**:** Leaving disciplinary.

**:** Hat at the door.

**:** Here at Princeton. We have this group called creative x, which is this open.

**:** Consortium of faculty. I think you're the leader of it. Is that right, neomitus? So we've been part of this for, I don't know, a decade now.

**:** And across the arts and humanities and engineering. And when we get together in the classes that we create are really predicated on this.

**:** Notion of people reading those hats to the door.

**:** So that I can be an engineer. Naomi can be an artist because.

**:** We are at times. And that has been a really valuable.

**:** Place for people to share ideas and to bring.

**:** To brings their perspectives that I think might not be heard of.

**:** Thank you.

**:** All right.

**:** Before I open up for questions, I'd like to reserve enough time. But I asked everybody just to prepare and maybe we can do it fairly quickly. One sentence.

**:** Of advice for students of advice for.

**:** Practition.

**:** Ers. For students, don't let Twitter decide their research. Think about what you are uniquely capable and positioned to contribute to the field.

**:** Our instructors examples are king. So draw upon what's happening in the real world right now to give this sense of visceralness to what you are teaching the students.

**:** For students get a strong math and physics foundation.

**:** And critique your professors, ask them how the projects that they're making you work on will help society.

**:** And for professors, teacher students how to think critically, not what to think.

**:** And introduce ethics for technology or history of technology as core course programs.

**:** Even at the other graduate, master and PhD.

**:** That has to be a providence.

**:** I'm also going to re-say some things. So in my experience goals are less important than the context or the process. So for faculty designing these sorts of courses and so on.

**:** I think that's a real priority. And I think for students to look for spaces where they can play and experiment and they can be an unfamiliar place.

**:** Being fearless is really important.

**:** So this is, these are the kinds of spaces where unexpected collaborations.

**:** And I think innovations are likely to.

**:** Occur.

**:** Students don't use charge equity. I think it's an amazing time to do research. So learning to use AI effectively and thoughtfully in your research. It's a major accelerant. I can get to the meat of my research much, much faster. And I think that's a necessity for the teachers connecting the dots and there's a lot of work happening. What are the key ideas? What are the ideas that will stay?

**:** It just happened. Developing clarity on that across multiple fields and going to multiple conferences and being exposed to literature across different disciplines.

**:** Great, thank you very much.

**:** So now I'd like.

**:** To.

**:** Hear some questions.

**:** From you.

**:** And I.

**:** Will, I.

**:** Guess we have.

**:** Two.

**:** Micro.

**:** And maybe has one.

**:** She can come around.

**:** So we have 10 minutes.

**:** So please raise your hand if you have a question.

**:** Thank you.

**:** Very much.

**:** Human behavior that I haven't really heard you serve.

**:** Rest. And that's sort of the instinct that this family. So, since I was thinking about the child and preventing the child from doing something dangerous and children have this instinct to, you know, they went through trying to evade what you're trying to tell them. And how do you think about that? Or the case of, you know, the robot knowing that it can only lift a certain amount.

**:** A human might think about it not just about, okay, it has three options with a, b or c, but maybe you take some. Yeah. You want to try to do the tasks as efficiently as possible. So they're going to think about it differently. Maybe I could put a bunch of things into the smallest basket that I can still lift.

**:** You know. So it's this whole notion of this instinct to push boundaries, good or bad, sometimes funny, sometimes not so funny.

**:** How do you factor that in?

**:** Who wants to start?

**:** Yeah, I think, I mean for the, yeah, I like what your question about. So like basically like you want the robot to help you make this box.

**:** But with the classical way that it was trained, it has to figure out other ways more creative ways. So it's kind of, I think.

**:** What we need to do is introduce, I mean, it's from my point of view, we need to stop thinking about this poll just completely imitating the data that was demonstrated because it's not in context like what you like how when you were going into like it's not embodied in like in the entire, it's not being aware of itself, of the environment and what other things can actually happen.

**:** So we need better at, we need more intelligent algorithms. Actually, that can, that can be able to have some form of like agency to explore. Oh, I don't know how to do this, so I have to figure out how to do something else.

**:** Right or introducing creativity as part of the objective of how the robots are being controlled in order to support that to explore and figure out, I don't know how to do this task at this or how I was trained to do it now, but I can adapt or I can have the human teach me or tell me how to better do it like in situ basically like while the human and the robot are interact with are interacting.

**:** We're not there yet at all.

**:** Like we're not but I think that that's a very nice question because I mean that requires us to think outside of the box.

**:** About the current way of just like just scaling data because we will probably never have that instance.

**:** That you talked about. So like unless we figure out how to come up with all of the possible scenarios where the human is going to interact with the robots, I think that's quite infeasible. So we need to come up with more intelligent algorithms to actually deal with that and kind of like think on the spot rather than just try to think, go back to memory and in the state what it was.

**:** And what happened.

**:** Before.

**:** I was also going to add better human models. I know that all models are wrong, but some are useful.

**:** And so.

**:** In this.

**:** Case.

**:** For example we use the bolt noisily rational model where you assume that people are noisily or approximately optimizing reward function or a score function. And so the idea here would be to have this assumption that hey, I think I know what the human is going to do, but there's always kind of a risk or there's always kind of there's always a probability that they're going to do something totally off distribution. And so being able to have better modeling model. Is that you're kind of phenomena you're talking about is a direction to look into. Or for example if I'm dealing with a child versus with expert roboticists, they probably need a different model for this kind of emergency.

**:** Great, thanks. So maybe a question from a student.

**:** For the.

**:** Great.

**:** Insight.

**:** Here.

**:** In this panel.

**:** Hi, thank you very much for the great insights shared during this panel. My name is promise Igora and I'm a PhD researcher at Cornell University.

**:** So just alongside the lines of having robots as adaptive partners, collaborators with humans.

**:** I had like just so Professor Andrea had a question about like legibility because normally there's still robot policy and then there's the human mental model of what our robot's actually going to do and my understanding of legibility is the robot actually acting in alignment with what it's called with what is actually going for so and you then mentioned this concept of when to ask and what to ask. So and I think that's been explored a lot in terms of clarification like asking clarification question to the robot or that in case like the question is ambiguous and also from the concept of failure prediction. So I was wondering does any other lens we should be looking at that problem of legibility from apart from clarification and just predicting failures.

**:** Thank you.

**:** For legibility is that it kind of sacrifices some efficiency for, well, transparency sake.

**:** So I guess you have to think about that whenever you design robots.

**:** In terms of.

**:** In terms of explainability or the robot kind of knowing how to share what it knows and what it doesn't know in a way that is actually pedagogic or maybe informative. I think you can think about how does the robots perhaps maintain some uncertainty or confidence over its internal model of the situation. Maybe there's a specific representation of things that has high confidence somewhere versus things that doesn't have qualms at the pie hog confidence over like maybe the robot is very good at keeping a cup of right. But it's not so good at knowing how knowing about the person's personal space for example. And so then being able to kind of leverage that kind of internal structure and use that to inform the kinds of questions they ask. The kind of communication you give this person and say, hey, it's not just that I'm a certain specifically understanding about your principal space kind of code. You construct queries in that way and sort of a whole way that's more informed by the internal model.

**:** Thank you. Do we have time for one more?

**:** Thank you, glossopoline, who I am a professor at Princeton. I do teaching and research in origami engineer.

**:** I have a question for vegan.

**:** S.

**:** I was very happy when I saw your video about the robot dexterity and the robot was doing organi. However that original is quite simple.

**:** In the field that came and walked easy in the manner. JF was complex and super complex.

**:** Such as the dragon by Satoshi Kamiya that is on display in the origami gallery in Japan. My question for you is how do you see the evolution of robot exterior from what you have shown toward the scale of the super complex like the dragon of Satoshi Kami.

**:** Ya?

**:** Most impressive demo I had.

**:** I think like advances in human hands.

**:** I mean again I'm viewing it.

**:** S the kind of thing that you cannot easily simulate. So simulators out of the question.

**:** Just mechanical improvements in hand design. I think that occupies half of the engineering efforts.

**:** I mean it's amazing that more than half of the degrees of freedom of a big humanoid are actually localized just this part of the whole structure. And so those improvements having they're also that breaks the most often.

**:** It's the part that makes contact with the world and so we see just last week there was a sharper hand on fire in our labs. So we need like improvements in hardware liability coupled with marvel ways of.

**:** Data collection.

**:** And access to this kind of higher level of expertise.

**:** And then the artistic elements around it. One would expect some notion of generalization where these models are able to once they are sufficiently trained. They also illustrate just as we see image generation.

**:** We do see like a lot of latent creativity in these models. And when you ask them to create images they develop really striking images and what's the motion extension of that. And I think it's great to know that there's a bar is much much higher than what we can demonstrate today.

**:** Thank you.

**:** I think.

**:** We need to stop in interest of time. I think we could go on and on and on. But I hope you'll take this as a preface to our conversations later.

**:** And reach out to our amazing panelists. But let's thank this group for such an interesting discussion.

**:** Where you hear from.

**:** Actually work at bank of new bank of new york yeah but you see those kids in orange hoodies out there they are like a robotics team. Oh nice and I'm kind of like the coach and mentor. So I took a day off and I got them here wonderful that's great. I see you like fighting off codex yeah this is my job. I'm an engineer as well yeah we have winds off right now and we will be getting codex by next month smart yeah same as I've clawed in codex and I make them fight it out onto the conversion of the plan okay and they're like a bad couple look at this functional couple they take like forever to like find a broken sometimes and at the end of it they don't even finish the plan sometimes you're getting into conflict resolution I know literally come again coding conflict revelation.

**:** So funny.

**:** So what score do they go to?

**:** The westminster school they're in high school then I was in a near graduate year school when's when's their school got share gotcha.

**:** All the excitement.

**:** All right awesome all right so we're now going to start our next technical session and for that I would like to introduce our moderator Professor Jaime.

**:** I'll see you in a minute I have to grab something.

**:** Hello.

**:** Everyone good morning.

**:** All right well I have the privilege today.

**:** To introduce all of you to some of our brightest young minds at Princeton we're going to have.

**:** Short and sweet rising star section which we're going to split into two brief.

**:** Panels that are going to have some lightning talks and then brief discussion after that.

**:** And with this we're going to give some of our PhD students and postdocs.

**:** Chance to share with you some of the incredibly cool work they've been doing across the board really spanning all of these different assets of robotics that we've been talking about.

**:** Further ado my job is to just invite you get out of the way so we're going to have our first five rising stars Masarabi Allison Earnhardt Daniel run.

**:** S down and some moza pai.

**:** Perfect so our very first lighting talk is going to be my masa one of you already.

**:** Hi.

**:** Everyone I.

**:** Want to.

**:** Start the question.

**:** And.

**:** No one ends with as you can see there are geometry in accuracies in the form of over extrusion and on their exclusion that can affect the geometry ability as effects of the extruded structure.

**:** There are sorts of material uncertainty in sedentitious materials of pathologies geometry and accuracy to have them first material properties are time dependent also these properties are lower dependent and since these materials are compressible there can be trapped or in the system.

**:** So to overcome this geometric inaccuracies can we use pressure as a sensing parameter in a feedback control system to answer this question I installed those that are Skyler robot to measure the pressure in real time I observe that then we hand over to building the system we have a jump from the pressure so I developed the feedback control system that adjusts the nozzle movement speed based on the measure expression in real time.

**:** I also developed an offline validation process using a laser provider to inhibit the performance of our compact control system by scanning the width and height of the fuel.

**:** To induce a tax revision of the system.

**:** And act like pressure I increase the estrogen rate twice along the pipe the result show that when the control system is not activated we can height of the extruded filaments increase without recovery to the baseline values. Augment the control system is activated that we can hide up the three filaments can recover back to the baseline gas. The average error 7% per wheat and 5.5% were flat.

**:** I.

**:** Want to end my talk with the question for all of us to think about how to fit material properties and environmental factors to enhance reliability and robustness in robotic item manufacturing processes.

**:** Thank you.

**:** Parkour. However in order to achieve these feats many rigid robots require intensive controls and reprogram responses making adapting to changes in the environment difficult.

**:** One alternative to this is soft robust like tessa.

**:** Tesla leverages softness and mechanical intelligence in order to achieve adaptable, durable and deformable locomotion with reduced control requirements.

**:** Tessa does this using a combination of origami towers and caragami inspired tessellated plates from our collaboration with the paulino group.

**:** These are actuated using simple $50 servos and allow the robot to crawl forward using unidirectional wheels.

**:** There are not towers that use the cresting pattern which couples rotation with axial expansion and contraction like a soft deformable.

**:** This is combined with the telations. These square rotate tessellations when rotated go from open to closed like so. When the two of these combined together we can now only expand and contract in order to crawl, but also expand and strengthen our volume.

**:** Without any added actuators for increased control requirements.

**:** Using before tower design we're able to crawl over obstacles half our height.

**:** And when needed we can flip over and like a slinky without taking any damage.

**:** Then with the four tower and tesselated design we can shrink our volume in order to fit into confined spaces like this tunnel.

**:** If you're interested in our robots and the useful things that we can do please come and see me at poster 20.

**:** Is a PhD student in the civil and environmental engineering department and allyson PhD student in the mechanical and airspace engineering department.

**:** This matters because you're going to see we actually have quite the spread all over Princeton. So on that note next up is by Daniel runt who is a PhD student in the School of Architecture.

**:** I'm part of a dental research group where we investigate the integration of robotics and construction.

**:** Construction involves many complex tasks played by uncertainty from dynamic site conditions to variable materials in assembly tolerances.

**:** In addition most of our research is conducted on these large industrial robots which support the long reaching henry loads required for construction. But these robots typically don't expose any low level controls.

**:** In my earlier research I developed a high level adaptive framework for multi-robot assembly of light timber frames using as-built scanning, iterative learning control.

**:** This framework uses perception feedback to adjust the cutting and placement of future timber elements.

**:** To ensure collision free and accurate assembly of building scale components.

**:** This framework was also applied to our large scale projects such as timberlink which was fabricated robotically from reclaimed in new timber for the methyl blue cardiac architecture festival at the site of historic 1969 woodstock music festival. You can take a look at the full project using the QR coding.

**:** And current ongoing research we are collaborating with IRA mod to investigate human robot collaborative design and construction utilizing AI to not only drive the assembly process and clutter construction environment, but also to enable regenerative architecture design. This research envisions and interactive and collaborative workflow between humans or robots. The combat skilled labor shortages.

**:** And find more about this poster of buying more about this research at booster number 59.

**:** We have two or structural researcher in the civil and environmental engineering department to open a rear.

**:** End.

**:** Hello everyone I work with all the faculty. So essentially we create chiral origami to design robotics and large information qualifications after the transformer. I see how it works.

**:** So under a single group of acceleration. So our robot can twist between 0 to 90 degree. As you can see we are applying counter twist. Do you see the implant that our robot is shrinking and also all the management then we will create how is the role of implant but then the vertically keeps shrinking.

**:** We keep the clockwise twisting until the robot reaches the lowest bowling configuration.

**:** As you can see during high protein we see gigantic shape.

**:** Change.

**:** Then we integrate electromagnetic calculation.

**:** To make origami trans.

**:** Form.

**:** First we integrate this magnetic response polymer on top of the.

**:** Using the magnetic field we can actuate this deformation on the mind. For example the envelope you are seeing in a park essentially this is.

**:** Then you see with this given magnet view we have four to five layer then just change the direction of a prime mechan field which the widely.

**:** Since the robot body is multi stable it can lock in certain shapes.

**:** Then we do this time or that we deform the robot log in the shape lower volume and then training magnet fuel to make it feed. Then you see we can control it for example move forward backward and here locomotive. And then lastly.

**:** To the last. So if you're interested, I'm very happy to talk to you. I poster 82. Thank you very much.

**:** Duo.

**:** And last but certainly not least this group panelists we have seldom of safari who is a postdoctoral researcher in central element.

**:** Al engineering.

**:** Hi.

**:** Everyone.

**:** I've worked at.

**:** The intersection of construction robotics and roll up journey.

**:** With the focus on contact rich manipulation for large scale assembly.

**:** Our work is motivated by tweaking challenges in construction first inherit uncertainties arising from fabrication uncertainty and material imperfections.

**:** Second larger scale components that limit repeatability and consistent quality at scale. And third adoption of industrial robots with limited compliance and slow closed loop control.

**:** We deploy large scale industrial robots for robot learning. If you're visiting the architecture lab in the afternoon visit this setup we also design custom repairs. For example for our contact research we use this wafer equipped with force of sensor for force feedback and an anti-collision sensitivity for white compliance.

**:** I specifically work with timber joints that involve high contact forces during assembly.

**:** And collect data through the teleoperated demonstrations as you can see in the videos.

**:** In the first project for example on the left we use end effector pulse and force curve data.

**:** To train diffusion policies and evaluate them on their fabrication uncertainties.

**:** And in the second project on the right we develop a latency aware pipeline that addresses observation inference and execution latencies.

**:** That.

**:** Can mim.

**:** Ic the ability of deploying industrial robots provision water policy.

**:** Maker.

**:** S.

**:** A quick preview of the results investigated policy performance on their various joint disalignments.

**:** We also evaluate policies on four sublimation studies and demonstration camps. And on the right we compare our mixture camera pipeline.

**:** With other standard methods investigating comment forces most improvement and task duration. For more details please visit me at poster 46. Thank you so much.

**:** Thank you Chalman. Well now we get to have a brief that I'm sure intense panel discussion with all of you during which we're going to maybe talk to you a little bit on some of the common themes that have emerged most importantly on your thoughts about what are the exciting challenges in your lives of work and more broadly in the field of robotics going forward. So something that.

**:** Has been.

**:** Clear essential to the work that a lot of you do is this intersection between robotics and materials.

**:** In various ways.

**:** And perhaps following up on some of the conversations we have this morning.

**:** Classical control in.

**:** The feature of robotics.

**:** How do your applications and the way in which you mostly with materials change the meaning of control?

**:** Anybody want to jump in?

**:** So I think for our potential application, for example, we are trying to blur the concept between the material and then robots in the sense of the material is architect from geometry. In this sense that integrating this material that stimuli responsible actuation is crucial. On the other hand for example a trend engine in what we are looking at is try to how to miniaturize this robot unit and then you repeat many units then you have a material. So visualization and then robot stimuli response material for our application.

**:** We also use similar material through our collaboration.

**:** And with our specific work we're kind of looking at the same material and seeing how can we use this material in order to get mechanical intelligence into the robot, for example.

**:** So reducing controls because by say combining and or coming tower that is actually the rotation and this tessellation, which is also actuating through rotation rather than having separate actuators for each one, you can combine them together and get this mechanical intelligence where you can actually either of them using.

**:** Amplitude control.

**:** Rather than needing a separate actuation for each different component.

**:** I think sort of on the other side of this side spectrum.

**:** In construction. We're working with these huge robots with very heavy materials.

**:** But paradoxically we still want to achieve very low tolerance. We want super high precision with our assemblies.

**:** So we have to deal with control in that sense and try and circumvent our industrial robot control implementing these.

**:** High level frameworks that can lead or really use perception and reasoning. Respond to the environment in real time.

**:** And in a range sort of work together between the different chamber materials and the restraints that we have on our lives.

**:** I think in our case because we are using cementitious materials the challenge that we have is then we are using actual progress as a sense and parameter. We cannot capture the changes instantly. For example when you are over extrusion you can instantly capture the camera but it takes time. It set material delay. It takes time and you can feel actually as a back pressure in the pressure sensor. So using the battery of all 40 probably you can capture the changes more instantly is kind of a challenge.

**:** Yeah I think one more thing to add on what Daniel was saying was because we are like working with larger scale material I think all of our cases like looking at different scales.

**:** Like dimensionalities I mean and the scale I think we use always the term scalability in our like kind of like construction and robotics papers but this scalability is kind of like different from the scalability in robot learning. Rob learning is mostly like generalizing new tasks on scene environments. In our case it just literally using larger dimensions which are making the forces different, making the forces higher also like making the maneuvering like harvest.

**:** Amazing well we have just one minute left before we switch out to the second panel. But maybe what I'd like to do is.

**:** Throw a bit of a tough.

**:** Curveball at each of you. What would you say in just sentence is the next frontier for robotics.

**:** Where a robot's going to be able to go in the next few decades that they've never been.

**:** Able to go.

**:** Sorry maybe I spill your answer but so it would be in our case like how like making robots to work with like relative construction workers together to like make something feasible.

**:** Like.

**:** Biomedical behavior to heal human body.

**:** Instructions say maybe a bit metaphysically the robots will also new skill domains that haven't really been explored.

**:** For a lot of complex manipulation and tasks.

**:** There's so many different ways that they can go so it's hard to choose just one.

**:** But I think something that would be very interesting is robots as structures.

**:** So not just robots that are you know handheld or human sized but robots that become buildings robots.

**:** Become shelters.

**:** Father that both deploy or shrink back down and be like packed away into rocks that.

**:** I.

**:** Think the next.

**:** Disturbing broad.

**:** Cast manufacturing is.

**:** Autonomous about getting manufacturing.

**:** Where human has less.

**:** Like actions and contribution to the building of the structures.

**:** Wonderful. Well please join me in thanking our first.

**:** Now we're on to the second group. So without further ado I'll just invite on stage.

**:** Our next five panelists, yi Chan one, Maryan alhai.

**:** And mei and yui nguan. Please join me in welcoming them on stage.

**:** And we'll start right off the bat.

**:** With.

**:** Lightning talk by issuan wang who is a constructoral researcher in electrical and computer engineering.

**:** Our president worked on the robot physical reason.

**:** Ing.

**:** So essential challenging robotics that arise from the embodied direction in the real world.

**:** Is the need for robot physical reasons. Like for this x-ray example the operator damage complex correlation by moving multiple attachment at the same time.

**:** However in the next example we see this rough fail edge putting the stick into the door because of the geometry complication as a video of y'all here.

**:** So broadly computer robot must be able to reason about the kinematic and dynamic limits indicated by your own embodiment and also the laws of physics imposed by the environment and also the test requirement as humans.

**:** And this physical country entangled to carry into semantic simple test into challenging puzzles. In this example the robot satisfy all these physical constraints by achieving the goal of retrieving the effort. To do so the robot has to first remove the block object and then retrieve the bombing apple open space.

**:** And finally the robot can grasp the apple.

**:** And the vision tosses to us and this is a real apple.

**:** However missing part is a shared benchmark reading about this physical written challenge and to address it gap entities gender. A benchmark for kinematic and dynamically embodiment rhythmy that target me or rising and over on earning and the workflow.

**:** Kindred is a collection of trini valve environments in both 2D and city for robot physical reasoning and all environment have an infinite test distribution.

**:** That is implemented with procedure generation inside the reset function.

**:** At title gender we also provided 100 human collected dilution for an easier start to train different mutation learning baseline.

**:** And hinder includes also include multiple candy operation interface that can be used to collect human damaging PS5 controller, a VR headset and an iPhone web app.

**:** Endix include age representative baseline across has a motion planning immunization learning foundation models and reinforcement.

**:** Impairment evaluation showed that risky method struggle to solve many of these physical reasoning challenging experiments.

**:** And some as an indicating the sarisial gap in the current approach to robust physical unity.

**:** We also include the reaction draw example of mobile indicator to show the correspondence of the robot with corridor challenge before simulation to the real world. I will present this demos via equal ethnic with mobile manipulator. Please come visit if you are interested. Thank you.

**:** Both doctoral researcher in mechanical and aerospace engineer.

**:** Hello everyone my name is Minnie and I'm a postdoc in professor radicanapola.

**:** And our research we study how we can embed robots in our buildings in order to make them go from being static to being responsive to us and the environment.

**:** And so we built architectural swarms and this is an example that we call swarm garden which is made of robot swarms that open and close to either let in light or block it.

**:** And we actually the float 16 of these robots and office and we show that the robots are able to respond to some light and also factor in a user preference.

**:** And in worst case malicious we also showed that it can actually preserve light levels as the day goes by.

**:** But because these robots are going to exist in our spaces, we also wanted to study how we can interact with them and how they can give us a sense of joy and wellbeing in our spaces. And so we created many interaction modalities. One of them is we created a wearable that is able to act and to prerequire as race of an interact with the robots.

**:** And collaborated with the dancer to create an expression application with the robots.

**:** We also exhibited them at the Princeton Arts Center. Over 100 attendees interacted with the robots and we had an overwhelming positive response into how people perceive the robots in their spaces.

**:** And I look forward to working more with social robots and social swarms and how they can make our spaces interactive and transition into my next role as an assistant professor at King's College London. So if you're in the area or if you have any questions please find me at the moment.

**:** Next up we have a money semar who is a postdoctoral researcher in mechanical and aerospace engineering.

**:** Hello everyone. I'm interested in designing decision and control frameworks for multi-trion systems that need to act quickly under severe onboard constraints.

**:** Think of private settings like this which humans navigates and remarkably efficient in closure. They usually do not communicate with each other or repeatedly repan their trajectories.

**:** But prefers to preserve the interior direction of motion when dealing with dynamic conflicts.

**:** So central challenge in multi-you know about social navigation today's distension between safety and making progress towards your goal. And this sanction becomes even sharper when you are in extremely congested environments where decisions needs to be made quickly and proactively to avoid dynamic conflicts. Under limited sensing limited compute and ambiguous evidence so that the team for ages do not know.

**:** The mission dialog.

**:** Ue.

**:** So we propose to use continuous time nonlinear decision dynamics where each award continuously modulates only its tower cell speeds or even path to avoid any conflicts that comes its way. The key idea is that the observed motion information already contains a weak local temporal priority ordering of which agent should be in which case we pass when they are in a local conflict.

**:** So the saturated nonarity in artificial dynamics amplifies the tiniest bit of paper and complete decision table and the agents we solve conflicts sequentially and very well quickly.

**:** So this creates a control instantly already given nominal trajectory planner only the duration of conflicts. As soon as conflict results we come back the even compliance denominator. So you do not have to repeat any optimized for it.

**:** In more realistic settings not every nearby agent behaves or thinks the same way. Some may not reciprocate, some may be distracted. Some may simply follow different control logic. So in addition to speed modulation each robot also continuously infers the intent of a nearby agent whether it's being cooperatively or not based on their observed motion. This lets the framework adapt in real time humans legacy systems and other dynamic obstacles.

**:** More broadly I'm interested in studying how continuous adaptation using on-near decision dynamics can enable scalable collective intelligence in robotics under evidence ambiguity partial observability very very limited compute very little memory and limited sensing. I would be very happy to talk more in the first session. I'm also hosting a lab tour and interactive demonstration of this social education work later I hope to see many of you there. Thank you.

**:** Mani and next up we have mei mei who is the phd student in mechanical and aerospace engineering.

**:** Foundation models have largely improved capabilities of robust across entire autonomy stack. Digital models have enabled out of the zero shotting.

**:** Section.

**:** And they will provide navigation in unsuccessful other environments.

**:** Are able to be deployed on zero shop in lab environments they have never seen before and perform dexterous tests such as holding the tunnel world models have became the new state of the art in being a general purpose physics simulator to predict the future state of robot actions.

**:** However one challenge with these foundation models is that they are often confidently wrong. This can lead to loss of consequences. For example an overcompetent vendor model can lead to robust collision with.

**:** Chair or the bounding box detection direct.

**:** Ly on language models and make mistakes and they are very confident about their mistakes.

**:** Vision language action models when deployed in an out of distribution scenario can fail to execute the human expert and instead in this case pick up the mud which the human doesn't intend. And video models also can hallucinate false futures. For example object of hearing disappearing, distorting and imagined objects behind occlusions.

**:** My research builds robust that low and they don't know. So I believe that auxiliary is the key to address this challenge is overconfidence.

**:** We use cultural prediction to make end-to-end safety assurances for robot navigation through this culture environment.

**:** We investigate the confidence of reasoning language models and come up with a way to reduce overconfidence with introspection.

**:** We are planning to address the overconfidence in visual language action levels where we can roll out multiple and potential futures and eventually arrive at the correct form within an uncertainty aware way. And then finally in video models we develop these.

**:** Central construction methods to provide the dense pixel.

**:** Level un.

**:** Certainty signals shown on the rentals.

**:** Column.

**:** For more information please visit me at poster reporting. Thank you.

**:** Thank you May and finally we have yuan who is a PhD student in electrical and computer engineer.

**:** Everyone. I'm Yui from Princeton Santropari labs and as the name implies we are interested in providing safety guarantees for complex reward high order robotic systems.

**:** Traditional robust control shrub laws to scale to high dimensional nonlinear robots. But in the real world these systems still need to stay reliable and the noise and certainty and disturbances. The challenge is how to synthesize and deploy safety policies that can handle this complexity.

**:** And Princeton said probiotics diets will address this with a scalable safety frameworks based on games theoretics richer void reinforcement learning co-training acceptive policy together with an adversarial policy.

**:** The resulting energy policy can transfer zero shots to simulations hardware allowing the robot to maintain safety against adversarial effects as long as the operational design domain assumptions hold.

**:** This framework also scales across different robotics platforms. Here for example a human in the field robots is trained to protect itself from heavy impacts by traversing difficult terrains.

**:** Comparing to the manual operations on the left, the learned separacy earnables much smoother traversals over and modern tour.

**:** We also apply the same frameworks to a crane mounted on ships. In this example the safety policy both dams the payload oscillation and tracks an operator defined goal by tackling safety on and off we can clearly show the system ability to recover quickly.

**:** Finally this safety framework extends to human rights. Here a humanoid learns to protect the critical heavy payloads while withstanding adversarial external forces. The learned safety policy earnables robust recovery even under challenging attacks.

**:** Thank you for listening. We are Princeton's Everybody slabs and we are robots are in good hands.

**:** And we now have.

**:** A quick five minutes period to engage in a couple of questions with none of you. So something that I'd like to open the discussion with is.

**:** Clearly in all of the settings that you're showing these robotic systems need to make highly sophisticated decisions under a significant amount of uncertainty.

**:** In all of these various complex settings that you're looking at, my question to you is.

**:** How do you tackle uncertainty in its areas forms?

**:** And what do you think the implications of this uncertainty are in the future of these promising applications for a box?

**:** Yeah I feel like I'm turning off the fundamental role and all that reporting robotic application and I want to tell you from your perspective, personal perception because other robotics will have a sensor data will come from the real work sensor and then get this information to do the decision making. And then the transition that you have to get the informative signal is always knowledge and other media is noisy and also observing reproduction. The second higher wall machine is about the interaction because a dimension of our physical reasoning on the robot module going into the real world and interact with any market, especially in a few minutes in many.

**:** Markets. And if you know what will look and here environment is highly unstructured with lots of the coaching. And then during the interaction with the environment with human, there are one deal with lots of the uncertainty in this loop and also who can either come from data. For example we can get a lot of data to make the model increase in understanding increase in understand about this concerning. Another part is about religious model to model the uncertainty and leverage any prior like for example we have simulation and then prior we also have other model to enroll the environment.

**:** So this dual is a part in my mind for future robotics.

**:** Yeah.

**:** So I think uncertainty or ambiguity in the environment of information that you know what is happening I think one of the main unexplored or underexplored area I would say is this tight coupling between thinking and acting. So most of the data driven approaches or optimization based approaches think first act next. And I think this takes away the fluidity in the interaction. What is going to be human but there's a lot of ambiguity in what the human wants us. Andrea was saying earlier. So if we can couple this loop between thinking and acting by thinking as a dynamical process, I think that is one of the ways that.

**:** Maybe the interaction more freely.

**:** Rather than.

**:** Having states do that every minute which is usually.

**:** I think for a piece my line of work one of the biggest sources of uncertainty is when we deploy the robots into real environments and in the public.

**:** We don't know how people are going to use the robot. So we don't know how the responses are going to be. And I think public deployments early on what the design helped a lot with this. So people every time we deploy the robots we get some new information that helps us reiterate on our design and then build robots better for people.

**:** Deployments are extremely scary.

**:** Probably I don't get any sleep. The night of the deployment but I get a lot of useful information from a wide diversity of people and things that I've never thought about before. So I think putting the heel in the loop as early as possible is very useful.

**:** Yeah. A certainty is also a central part two of my research. I think it's important for first determining what the source of uncertainty is. Is it the interior randomness in the environment itself? Or is it lack of turning data for the model or is it because of the ambiguity in for example the human instruction or interactions? And I think for each source of the uncertainty it's important to know how uncertain we are. So to quantify the uncertainty and have some strategy to correspond that corresponds to each of those source and like level guarantee. And that way I think we will eventually be able to provide maybe not like super rigorous but we will have some guarantees on safety on how the robot will reason about uncertainty and the hip equated that.

**:** For me in my line of work quantifying uncertainty and knowing the information about the certainty is very important.

**:** Because there's a big difference between a 99% system that they have. And there's something really cool about you can quantify 100% or 100% safety on the systems safety guarantee is meant to be like that. So for me in my life of gloves instead of trying to instead of trying to tackle most uncertainties, we start with an operational design domain in which that is like a certifications that we give to the users or to the systems. That is if one of the uncertainties that the system will be deployed into is within these certain bounds, then we can say something about safety guarantees. And then instead of just modeling uncertainties as a probability distributions, we are actually training adversarial to actively or to actively attack the mode barrier of the system within those bounds. And by being able to expose the system to the worst case realized disturbances within those bounds when to play onto real world systems, we can actively say something about the safety certifications.

**:** Great.

**:** Well, thank you all. And similar to what we did before and in this case very much in the spirit of humanity driven robotics. I'm going to ask each of you to give one sentence answer on what is the one key thing that in your view is going to be necessary to enable people to trust these autamas robotic systems.

**:** Thank you very well be robot will be adaptive during the robot deployment in the industry environment.

**:** Robot should follow the human print and adaptive during all the robot lifetime economy before you make sure your body more than human in my mind.

**:** How smooth is it?

**:** Causing me and thinking about acting that makes me prostate less? Because I don't have to be mixed. So yeah, fluidity has continuous applications.

**:** The key.

**:** For me in order for people to trust my robots. I think as I mentioned before I need to listen to my end user and I need to take their feedback and I'm going to feel not very important about ethics. I think it's really important that if we want people to trust our robots that we think about it ethically and how we can deploy it.

**:** So we it is very difficult to have people just trust robots over the left. I think through continuous development of continuous deployment when people see robust interact with the messy environment around them and doing useful things before we'll continue to build trust in the.

**:** World.

**:** So generally I think the one word is deterministics and to break that down I would say explainable and consistent. That's why I'm aiming for my robotic system to be.

**:** Great. Wonderful. Well this brings us to the end of our session. Let's thank our wonderful panelists.

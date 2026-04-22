# Robotics research planning: kindergarten simulation environments

**Date:** 2026-04-08


## Summary

### Research Project Discussion

- Working on task and motion planning in robotics lab
- Bi-level planning framework: separates “what to do” vs “how to do it”- Current challenge: static probability rankings after classification- Goal: dynamic reordering based on execution failures
- Data sparsity problem
- Only one data point per failed attempt- Need few-shot learning for real-world transfer- Time budget constraints limit retry attempts
- Formulating as partially observable Markov decision process
- Update belief about environment type from failure information- Account for planner limitations vs theoretical completeness

### Lab Environment & Tools

- Created benchmark suite called “Kindergarten”
- Open source on Tom Silver’s GitHub- Similar API to Gymnasium for RL developers- Covers 2D/3D, rigid body/dynamic problems
- Current simulation setup
- Simple circle robot with grabber arm- Basic tasks: moving blocks to target areas- Progressing from rigid body to physics-based environments
- Physical robot available but focus on simulation first

### Academic Context & Connections

- Tom Silver as advisor - “really nice guy”
- Robotics seminar covering recent NVIDIA papers
- Discussion of world models necessity for generalist robots
- Concern about rapid AI progress in robotics field
- Princeton robotics club involvement
- Transition from COS to ECE for robotics focus
Chat with meeting transcript: https://notes.granola.ai/t/16530877-37ca-4d80-ab2e-88aaf81ea6d4


---

## Transcript

**:** Tuesday is like a quick shift. Oh yeah, that's right.

**:** And then when stations fight is we'll figure something out. Maybe next Friday anytime, just let me know. Of course, we're gonna read it period too. So like you go anywhere for reading period or.

**:** No medicine. Have you had it before? Yeah, I love molly t though.

**:** Wait, but you don't drink tea. I drink like everything else but like there's some cloud like the cloud prints are really good. Oh like the non like the non-caffeinated ones. So like the camo model.

**:** I mean I really like the floor lean has sucked the teeth. Oh no yeah no I agree is great. I'll see you man.

**:** Oh yeah there's just like you get like a small like penalty for every concept to incentivize efficiency. You could go through the obstacles but then you lose a larger penalty but sometimes like it's faster you can use whatever you just have to write like some planning algorithm like a star or something the trickier part wasn't like the conceptual part of how to solve it was more just like you know you're getting new code base whatever like and seeing the new thing yeah, it's like custom like you know like library whatever that's tough yeah that part's a little annoying but otherwise conceptually I don't think it's too hard.

**:** So what do you do all day then? Are you guys I know you guys are more for the planning is that right robotic planning is that is that right assumption some of the recent stuff that we have going on is we made a benchmark various like robotic like like planning and like learning path so there's like a couple variations of it like some are like rigid body like problems that are simpler some are like dynamic problems where like there's actual like physics and it's not just like rigid attachments and stuff like 2D versions 3 versions so like we're trying to cover like a lot there's like non prehensile emotion that kind of stuff so like trying to cover like a large amount of like different types of like difficult problems but like in a way that's like kind of kind of reminiscences of like how using like like gymnasium is like easy for like RL developers and it's good for then it's good for whatever the robot or so you try to make them based on what I'm hearing you just try to make them more like.

**:** You create the benchmarks up later.

**:** You make the benchmark in order to is it just do you evaluate different models then yeah like.

**:** Trying like it's useful for like algorithm development and stuff just so like you make sure that like whatever like algorithm you develop like you're not like missing some blind spot like oh it doesn't handle like dynamics really well or something like or oh it only works well on like like rigid bodies in like a 2D environment before a reason when we go to a 3D setting like it just collapses it's like it's useful to do some development in like simpler environments right like of course to start in 2D yeah.

**:** Wow so you just need research in the lab or are you teaching classes or what's no I'm just working we have like a bunch of projects going on in the lab.

**:** My project is related to tasking motion hunting so.

**:** Basically what there's like many like frameworks for like like robotic planning one framework is bi-level planning I don't know if you know I haven't got to explain it a bit but it's not actually not that complicated like the the main idea is like you you separate planning out into like a what to do and a how to do it okay right but what to do is like like very abstract descriptions of like go to the fridge open a door grab your object put it in the fridge close the door but like that's just like descriptions of what to do but like it doesn't tell you like how to open the door what raft you use to get the object whatever right so it's it's easy to it's really easy to generate these like high level ideas but because it's separated from geometric reasoning a lot of the times like you know you don't realize that like oh like it make it kind of makes sense in the abstract to say go to the door and open it but if you don't realize geometrically there's something blocking you from going to the door it's like more of this paradox right it's just much harder to understand how it runs so my project is right now we're trying to figure out so they're already good ways to basically like turn this into a classification task of like let's predict which abstract plan like we think has the highest probability success yeah so that already exists but the thing is like after you do that classification those probabilities are basically static right it's like the then from there the algorithm is just like oh we're gonna once we ran a classifier we go to the highest probability then the second highest yeah and you pretty much can predict what they're gonna do just very static afterwards and my my problem is like okay at test time like when we actually go and execute like these plans like even if your plan of like 90% probability like looks really good on paper like you know you think it's gonna work well if it fails like you you want that error to like propagate somehow right so that so that plans that do something like very similar and don't like you know account for something else like get ranked higher afterwards so instead of like just going on to whatever the classifier said was good you know previously you want to do some sort of like reordering I haven't figured out a good solution yet because it turns out it's kind of difficult because every time you like make a new attempt you only get one data point right oh okay yeah so it's like it's a very like data sparse like environment and then you give them for a lot of stuff from yeah you want to be able to like say something like it could be that like like one hypothetical way to frame this is like every attempt you make is like an experiment in the environment that like reveals some lighting information about the environment right like if you if you choose like a really short plan for example and you execute it and it doesn't work maybe the latent information you're learning about the environment is this is a hard environment we can't use like very simple straightforward plans yeah, it could be like the environment is stuff might be too hard for them yeah yeah so it's like okay maybe like you know in this very simplistic mindset like then you like start down weighting all the plans that are really short for example like obviously like you know shortness of a plan isn't a good actual metric but just as like a hypothetical for like how the idea works so it's like.

**:** But again like because you're only revealing like what like the only information you really get after like failing at a plan is like like how long did it take you to fail what plan was it where did you fail at how would it know it failed but it just not like object if it had to like retrieve an object it just like this is like there's that's the problem with the robotics like there's many ways to I mean what would you consider this a right now like we're we're doing it like just in simulation okay so in simulation it's pretty easy to tell if you're failing because you have like like some abstract goal of like okay at the end of this I want to have the condition that you know fridge doors close and fruit is in fringe or something like and if those predicates or whatever are not there yet other than automatic okay okay but that has a huge problem then like you don't even know what you've done wait do you know what you've done and then you know what has been done yeah and knows what has failed or is that the harder yeah you you know what has failed and like we're we're still like you know simplifying this down to like fully so that's the best thing that's the hard part yeah but again you're literally only getting like one data point at a time and hopefully from that one data point at a time you can do something radical with everything else.

**:** But you guys showed this to me at some point man this is I mean if I can get it to work.

**:** Yeah.

**:** Because it's it's actually hard to because because in principle you shouldn't need like this history of information you should you should know that yeah especially like if you if you simplify it down to like fully observable or something in principle if you know like where everything is and like you know all your actual possible actions and you know what the goal looks like you should be able to do it like but it's more just to it's more to account for limitations of like planners themselves because like while like you know in principle like you know these perfect planners like know how to like rasp things really well or whatever in practice that's not always the case right you might have like samplers that try to figure out like grasping or whatever and maybe it's bad at grasping like specific objects or could be yeah yeah right so I guess running this on Nvidia omni first then and then just like.

**:** Have it and run or what's the simulation?

**:** Oh this is like the kind of on our benchmarks. So you run it directly onto your bench. Oh that's inside and then just run the program right in oh wow so you created your own environment essentially and you can add okay that actually that started to make sense now yeah yeah well cuz like a lot more suck if we were like oh we have this cool environment but no one in our lab wants to touch it that's what I thought that's kind of a useless benchmark that if no one's using a benchmark.

**:** The documentation is good it's like is it open source?

**:** Yeah if you it's called kindergarten kindergarten with the instead of a t why don't we know how to spell kindergarten I'm sorry it's in Tom Silver's github right yeah.

**:** Yeah I'm just gonna.

**:** Ask yeah let me ask claw to find that for you.

**:** But this is super cool though okay.

**:** And then.

**:** So what are the other guys doing so you're doing that but like what are the other people looking into now some some of my friends are doing stuff like using l m's as planners yeah, that's what I was thinking like why couldn't you just like if it failed it reasons its way out and then it well because it's it's really expensive to you know every time something goes wrong like you spend some like tokens or whatever yeah 200 a day I'm looking I'm looking cooked on the money yeah it's ridiculous.

**:** Like it's it's not a very scalable solution to and also even even then like because it's like you can feed like a set of vectors representing like oh here's the positions of all the object order but that doesn't necessarily translate well to like language reasoning yeah like for for an llm right I see.

**:** That's true there's a disconnect just because you got language output and like output tokens it doesn't mean that the computer can like understand it and yeah make the make those changes so then is it.

**:** Like one approach for.

**:** Using llms in planning is using lms to help you like sample like an llm to write a bunch of heuristics and then using those heuristics and pre-existing planners which already have really good guarantees like pre-existing planners already give you like stuff like completeness or whatever okay so that's that's an approach I mean it feels a little hacky it does because you legit every you're connecting it straight to a pre-existing thing right it's gonna mess up different like problem you you're gonna have to like query for a new like heuristic which is a little annoying but it works as this one right here right.

**:** This one robotics this one yeah it's found it.

**:** Copied.

**:** So cool.

**:** Though.

**:** Yeah so that is that is lengthy so then then the next.

**:** C okay I'll clone it I mean it works very similar to like gymnasium if you used that before gymnasium is that just it's a it's like the open source this one right or sorry.

**:** About it.

**:** Maybe not that one.

**:** There there is I guess gymnasium specifically for robotics but there's also just like a library called gymnasium oh like a like a library got it yeah yeah.

**:** Let me just ask a bit too it's usually like import gymnasium as gym or something got it.

**:** But yeah the apis are quite similar so it's.

**:** Like with the understanding that like most people are familiar with with gym so if you're familiar with gym like it shouldn't be too hard to use kindergarten got it okay.

**:** So your input is then you're you're what whatever you.

**:** Yeah what's the input like how does that are you doing reinforcement learning on top of this or is it just I mean we I've tried a couple of things I've tried bandits I've tried just I'm trying Transformers mlps but I'm thinking now of formulating this as a partially observable Markov decision process why why would you well just because like that the the whole thing about palm DPS is like you you only get like a little bit of information at a time.

**:** And that like little bit of information which is like the failure cases like helps you update like your belief about the world right so like we might like update our belief about what what type of problem are we in like or maybe this is like a problem where like you know tools are required or something or maybe this is a problem like where we have to account for many obstacles or something and maybe like conditioning on your belief about the world like gives you like a more informed probability distribution than just like a global prior of like again just running the classifier like ahead of time.

**:** Wait and how long are these tasks are they like really like multi-step processes or are they just I mean like a couple stuff to do.

**:** You know?

**:** Like they're not like super complex but they can they can require like many steps like.

**:** Like a simple problem is like like putting like fitting a bunch of books in like a small shelf right and like the beginning distribution might be like oh maybe like all your shelf is completely blocked off like because you put the books weird at first or something so then you have to be able to reason about like oh we should take those.

**:** Books out of the shelf first and then put them back in in a nice order or something.

**:** But maybe that's but maybe that's not the case maybe like you're in a simpler like type of problem where like like oh almost all the books are there you see it put in the last one or something right so like maybe it's not always a good idea to go to this plan of like no matter what we're gonna do we're always gonna take them out rearrange them because then like you can just do that yeah in the simple case like you you're turning like a you know one step problem into like a 30 step problem for no reason why couldn't we just abstract that into an easier problem and then just have lm solve it and then spit it out again like is it?

**:** Like what do you mean abstracted into an easy oh it's just like.

**:** I'm assuming you guys already do that right or is it or there are just so many steps I'm.

**:** Like.

**:** It's so bad that I'm running a humanoid team at Princeton I don't even know this but okay so you have a bunch of these steps right?

**:** You're I'm assuming you're grouping them and clustering them into like a series of like tasks you do right.

**:** I mean depends on what type of framework you're using like if you're doing something like like more hierarchical where you have like sub goals or something you could do that but you're not doing that though right you're doing it all in one like as one continuous with certain problems you shouldn't need to that's okay no matter yeah.

**:** Let me see what this tells me okay.

**:** The architecture okay.

**:** I see.

**:** I didn't have cloud code when I was a sophomore like this is like wild to me yeah we just I just downloaded the repository wait so what would you like hypothetically you're working with us right now right kindergarten but what would you put as your input like how would you would you visualize the environment what do you what's your input output like do you have something oh yeah.

**:** So you can there are like visualizers for the environment like for example like if you run a episode and you have like the trajectory of actions yeah like there's like we have like support for video recording so you can output that but usually it's just like you giving an action and then you call like environment.step or something and then the environment steps one step forward based on whatever action you're inputting and then it spits out a like state or observation and then based on that new state or observation you take another action etc etc and this is on what robot are you guys running on a specific model of robots or like what's the oh I mean we do have like a physical robot.

**:** But for simulation what are you guys doing is it just like how do you get the like the.

**:** I mean we have like like small little like like little robots in simulation they're like really simple it's like it's just like a little like circle with like a grabber for it and that's it. That's all you need to kind of I mean steps. Yeah yeah like you don't need a lot to to start like developing algorithms.

**:** Like you can like so what do you use like what's your robot look like what is your what is your setup like tell me about your environment?

**:** And then I mean I like right now like I'm still trying to get this to work on some of the simpler environments the simpler environments are like one of the problems is like you have like a like set of like obstruction blocks and like a target area like on the ground and you want to move like your target block onto the target area but you know sometimes that target area is covered or whatever so it's like your little robot like just it's all like rigid body so it just like sticks its like you know arm and like it just picks it up like and it kind of like moves in free motion like it's not super important of like the like the physics of this because this is like like the simplest environment where again we're assuming like physics isn't them like we're kind of like ignoring like too much of like the real world physics layer oh so now you guys are doing okay I see so it's just reduced to a planning problem but we do have like environments where it's like it's like that but now it's like you know if you if you push the block and you like push it with a certain velocity then then like based on the amount of friction it might go flying or you know.

**:** So this is like a so this is a 2D problem that you just described right yeah, but but we have more complicated environments.

**:** I see.

**:** Butter yeah I'm just I'm struggling a little because of the data sparsity issue.

**:** Explained that what's the issue with it?

**:** Oh just.

**:** The issue is.

**:** There's sparsely in like a couple levels one is that you know it's all good and all to like collect like you know hundreds or even thousands tens of thousands of episodes in simulation yeah but ideally we would like to write a like algorithm whatever that works well in simulation and can be transferred to real world and and then in the real world case like you don't want to collect like a thousand episodes but some guy like you know try to figure out how to like move target blocks into like yeah that's gonna poor guy actually like the guy like you want you want like like few shot in real life yeah so that that's part of what makes it hard and then another part that makes it hard is like again at test time like you you don't get to actually see that many examples of like plans that failed because like if you if you see like 10 plans that failed that means that like you've already spent like you know minutes just waiting there like it's just not going well yeah it's done robots kick yeah so like like ideally if you already have like a decent like classifier then like even with that classifier you're probably gonna like get it within like you know like 10 tries or something but but now it's like okay instead of getting into 10 tries let's get it down to five or something or one or two or three even.

**:** This is interesting well.

**:** Yeah no that that is a huge issue yeah but I'm gonna turn to understand this thing but then like in that case like again you're it's a problem of like you only get to see like one failure and you might get some failure information and then from there like hopefully with just that value information you can get in on the second or third try.

**:** Okay.

**:** Wait so what where has your most of your failures been like in terms of like.

**:** All that stuff you've been trying out is it when it's a super loan problem to like go through with a bunch of steps or like or if if it's like a loan problem and the guy just like messes up and the like mistake just compounds from like the actual go is that is that the issue or is it like what's kind of like happening within like four like practical purposes you have to set time budgets so if you burn all your budget like on like the the first attempt went badly you don't even get to try.

**:** Yeah so.

**:** This is so cool.

**:** But if you're if you're interested Tom is really cool yeah he's a nice guy he's really nice have you like take taken a class with him or anything? No, no I just know this guy from his other Princeton Group I have this robot that I'm playing with Princeton bought it for us so look him.

**:** Show it to you.

**:** It's like it's like this it just has like.

**:** Like we're just doing basic teleoperation right on it that's pretty much it but I think one of the guys can he's he's selling this like he's in this robot company and Tom Silvers is his like high school like buddy or something what so it's like sourcey if you've been out sourcey he'll know source.

**:** Orgot his name his name is.

**:** Notice he was from Princeton that's why.

**:** He's creating this robot I think he's in hoboken so.

**:** I don't like the like robotics club or yeah I'm in a robotics club here but I've never done anything beyond that like honestly I mean like part of the reason I went from coast to ECU is because I wanted to try my handle robotics I didn't do anything like robotics really this is the first time into such a good move cuz this is like one of the harder.

**:** The clock code to resolved a lot of the software stuff you honestly should go into something harder like a reality like that's actually fair that is completely fair I mean like a lot of like like you know coast undergrad is still like very applicable especially because I'm working in simulation and stuff oh especially it's just coding then a lot of coding.

**:** Yeah you get unlimited cloud code though right you got enough like yeah so yeah you can just do whatever you want.

**:** No it definitely is nice like because like like now I get to you know work on more like high level like thinking yeah you're not spending time like just like yeah not that I dislike that but it's just like I feel like like that was such a time sink in undergrad and the worst thing was like syntax something you understood it but it just like computer like you forgot like a semicolon or some like that it's just are you co-signed or I'm orphe I'm orphe oh you're orphe okay I honestly should be my interests are all easy and coast like I work for like a startups and stuff so like look I don't know what I'm doing in orphy but.

**:** Not too far off like I don't know like there's a lot of like problems in robotics that end up being like optimization stuff I've noticed that too I mean you're talking about like the time streaming that's like that's just an optimization problem like anything that's like minimum trajectory optimization exactly that's just yeah that's orphe nuts though like I definitely wish I took some more like actual like optimization classes because I'm just like yes it is convex like but then I don't think the issue with orphan you don't get any practical skills which may be better in the world of cloud code but like you really don't know how to.

**:** Program it you really don't know how to like oh like reason through stuff.

**:** I didn't know that no I don't think notice I never needed really learn how to program but like I know people before me before cloud before chat GPT they were like they're pretty much all CS guys brilliant and then you just went to orby because oh it's a different I feel like it's like a like a good like rite of passage to try your hand at doing as much as you can without cloud code yeah, no, it's a good skill. Oh my gosh yeah see I couldn't even solve it.

**:** The problem that you gave the.

**:** Picking up an object and it was try to greedy method and it failed.

**:** Greedy reactive approach.

**:** Your cloud will be able to figure this out I'm just burning tokens that this stuff is hard I actually think robotics is gonna take like a like a huge like jump in like I think so it's gonna be like this is not gonna be solved like I'm I'm taking a robotics like seminar now like we're like reading like papers that came out like in the last couple months from nvidia and stuff yeah I'm just like oh we're so cooked oh yeah it's like oh it's like oh like we get like robotics to do like zero shot policies and it just works I'm just like what do you mean yeah what's happening wait you see yan lecture yesterday oh no I didn't do what do you think about role models do you think that's like useful or I mean I think to an extent you probably do want to have like like world models basically at some point right you'll be helping for everyone yeah you have to have like some like like physical reasoning right like you can't just do like because like vlas or whatever like you get like very good like semantic reasoning out of it it's like oh I know that this is like cocaine or whatever but it's like if you can't imagine like oh like the cocaine like rolls this way or something yeah you cooked the real world yeah exactly so what were some cool cool papers on like world models and like we probably it's hard to imagine like a good like generalist robot that doesn't use that's fair just like think of the best albums like they have some type of transformer like thing like there's obviously like there's fundamental stuff so true my goodness hey nice to meet you mom we should stay in contact you what do you usually I mean you can let's see numbers better easiest is my number yeah let's do it I don't really do like does this one.

**:** Is my phone too old.

**:** Dude my phone might be two items iPhone 13 but this okay we're going wait this is also 13. Oh shoot we're going old fashioned boy all right yeah I texted my.

**:** Number or sure I'll go for it.

**:** So you're working the e quad right there I mean I realistically like work at home I like that I like that better I mean it's because as long as because I have the the Princeton VPN I have access to Della and stuff like from New York right oh no you're six two six never mind oh yeah yeah no I'm from california okay.

**:** It's just Joseph right yes.

**:** Got.

**:** It.

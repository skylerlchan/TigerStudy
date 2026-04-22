# claude workshop friend center

**Date:** 2026-04-01


## Summary

### Workshop Overview

- Informal Claude/AI tools workshop hosted at the Friend Center, led by a speaker (Jerry) from a YC company called “With AI”
- ~$300/day in Claude usage; company offers effectively unlimited credits (2.5M budget, 4 employees)
- Other CLI tools mentioned as alternatives: OpenAI Codex, Gemini CLI

### Core Philosophy

- Default instinct: try asking Claude to do any task before doing it manually
- More data = better results; data ingestion is the real bottleneck
- Three-step framework for Claude Code:
- Digitize — convert content to machine-readable format (Markdown/.md files)- Organize — Claude Code uses grep search; Cursor uses vector search- Automate — schedule recurring tasks (dependency checks, file organization)

### Key Workflows & Use Cases

- Web research via Brave API + Firecrawl
- Firecrawl can run ~100 parallel agents simultaneously vs. manual Google searching- Used for shopping/deal-finding
- Canvas API integration — download all course modules, homework, slides directly into IDE
- Enables pre-exam pattern analysis (e.g., Poisson process, random walk appear on tests consistently)- Token-heavy but high ROI for studying
- Academic paper workflow: scans papers, generates synopsis, downloads PDFs to workspace
- Voice-to-context: Whisper Flow (or similar) to feed more context faster
- Granola mentioned as a note-taking/recording integration for feeding data into Claude

### Skills System (With AI IDE)

- Skills = pre-built agent shortcuts that speed up task identification
- Must install an “ability creator” skill first to unlock others
- Current skill library includes:
- Web research- Canvas API- Finance data retrieval- Patent search- Email via Claude- Microsoft Teams integration
- “Forcing questions” / anti-sycophancy framework in development
- Inspired by Grok’s less agreeable style- Designed to push back on weak reasoning (e.g., “buy Apple because it’s done well” gets challenged)

### Setup & Next Steps

- Tools: Cursor or VS Code + Claude Code integration
- With AI offering ~50 free Claude credits to attendees
- Speaker offered to share setup details with interested attendees
- Skyler to follow up on connecting attendees to the With AI IDE setup
Chat with meeting transcript: https://notes.granola.ai/t/799c2037-f7df-4226-ba64-8d421fe9183a


---

## Transcript

**:** All right, let's do it.

**:** To you frequently.

**:** This is revealing.

**:** Oh shit.

**:** Definitely go first.

**:** Where's the boba?

**:** Chair?

**:** Yeah, let's start.

**:** All right.

**:** Well thank you everyone for coming. Today we're gonna have Jerry. He's gonna give a talk. He's a master of cloud code and he'll give a talk. How do you say most often, will he? I think there's a lot for everyone to learn here. So it'll be a relatively casual thing. You guys shared some ideas through the form and of course I think throughout if you have questions that Ideas Cheryl, I'll be very happy to share his wisdom.

**:** So yeah, I want to say that I guess it's April Fool's Day.

**:** So like I don't think like I claim to be like any particularly better at using quad than many of you guys. But I guess I might spend more on it or something.

**:** But in any case, yeah, I think there's like a lot of cool things that you can do with Claude.

**:** And there are a bunch of other CLI tools too like OpenAI codecs, Gemini CLI. And so I think yeah regardless of the tools that you use.

**:** I guess the general philosophy that you can adopt is that for any task that you want to do, it doesn't hurt these days to just try and ask Claude how to do it for you.

**:** And these can be like very arbitrary things. I guess it's not super clear what that means.

**:** But I guess the general principle is that yeah, if you have some random thing that you want to do, like say you want to like go online and like book something or buy something or like just do something in general on your computer, you can just like open clot and ask it to say try and do that.

**:** And I think oftentimes you'll be very surprised by what it's able to do.

**:** So anyways.

**:** We'll just like go through kind of like a little bit of like workflows and things like that.

**:** And like always feel free to interrupt if you have like any questions and suggestions. This should, this is meant to be interactive. If you guys think you have like interesting like ideas or workflows too, like feel free to share as well.

**:** But I guess Skyler, he's a good friend of mine. I think he has like even higher token usage. I have unlimited.

**:** So.

**:** You want to try to yeah, I don't know how to connect this.

**:** Yeah, how she fixed that.

**:** I think it's good.

**:** Also the boba is getting here soon so I think I might start my presentation after the book was here. Cool.

**:** Right so I it's a little background I work for a YC company so you get pretty much unlimited cloud usages.

**:** And this is actually our literal product so we build pretty much an IDE for hedge funds to work with.

**:** And it's pretty much just copying let's just clot code for hedge funds which is pretty lame but it works but what it does is that we you can honestly use it for as as much as you want I think one of the more unique features that we have is we have all of our skills so our company is called with AI and then we have all of our skills kind of.

**:** Connected to our IDE has anyone heard about skills in cloud?

**:** You got Steve who knows it anyone else?

**:** No one okay so skills are just a way to pretty much make the process of how the how the agent works just makes it a little quicker for the agent to get to things again identify the skill based on your prompt and which is actually very helpful so we actually have a list of skills here the funny enough the first skill you need to install pretty much is like an ability creator skill and this gives you access to all of the other skills that you create which is kind of stupid but you got to start off with something right so like the most common usages I've done was pretty much the web research one so we can we're gonna open that one up.

**:** And I don't know how applicable this is because I do use a lot of clot I use around 300 a day so I don't know how like applicable any of these tips are but it's kind of like a bragging right in San Francisco the more you use.

**:** The the more like I guess productive you are if that's a thing so like the first things we have is we you need to have all your API keys kind of locked down somewhere I think one of the most useful cases I found was pretty much the web search function.

**:** If you have a brave API and then you connect it to firecraws anyone heard of fire crawl.

**:** Like youe got fire crawler got one okay fire crawl super popular in that stuff it's.

**:** Just a way to Skyward the internet pretty quickly and the reason why it's better than you searching Google is that it can send a hundred of these agents at one time searching for whatever you need to do so you don't need to be like I mean you yourself probably will not be searching 100 google searches which is just practically impossible so you have I guess a search function and searches everything for you I've used this for shopping now which is finding the best deals for that.

**:** And then this actually really helps with most of your other just common needs I think one of the most applicable ones that you can start off with is actually the.

**:** The canvas API.

**:** So right here you can look at all of my I pretty much downloaded canvas onto my IDE like this is completely possible if you guys go to canvas type an API you'll be able to find something to download all your modules now.

**:** And with that you pretty much have all of your like homeworks homework solutions anything that you need all your slides just in one located space you can ask it any questions and it puts it in the format of whatever you want this does consume a shit ton of tokens unfortunately but yeah you can also have a script to kind of download all that in but let me just run through any any questions so far like of what I'm doing any any things that doesn't make sense it's just pretty much how to crunch tokens and make yourself as much as productive as possible.

**:** So yeah you get all of the slides down and I think one of the most best use cases is analyzing like let's see analyzing what happens with like the productivity of like like you can know exactly what happens on the test before they come out so like this point Poisson process happens 100% of the time you better know that shit and then if you have like random walk that happens 100% top so you can nail like one shot 90% of the exam in just one shot and then you know I've noticed like I studied half the time and like get double the results like I don't know I don't know why people don't do this but yeah I mean you got like this happens 6 out of 7 so you better know these principles and then these are ones that you can probably skip if you if you don't have time and then yeah, you just know your criticality and then you just go right off there so I've been doing that for all my exams too and the reason why is because it can actually like go through all of the so all of my exam materials are right here actually where is it?

**:** All them are right here from here to here so it just it's just more the more data you feed it the better and I know I know a lot of people are just putting stuff into like I don't know google llm or some type of like chatbot and you manually input the files the reason why that's not as efficient is because you do need like more data it can scrape like the textbook you can scrape your slides if you scrape your own notes which like I connect through Granola and it just has everything recording okay location not be recording this sorry that's all legal I'm talking to myself pretty much that's fine.

**:** Another way to I guess enhance your cloud scored ability is that you should be using some type of note like some type of voice assistance so like you guys have a whisper flow right probably see tons of ads about it essentially again the more context the better your results are.

**:** The example you like how have I been using cloud in the last couple days and then it'll just completely just you know it's just way faster to type but you pretty much have all of this stuff you unique cases of what I've been doing.

**:** All right we're almost I'm almost done with my presentation so we got the boba coming.

**:** Up.

**:** Thanksgia.

**:** Sweet.

**:** So so some of the unique cases I found right now so you got the can I have a drink.

**:** Wait strap your drinks describe your drinks yeah.

**:** Skyler is doing the title yeah.

**:** Good I saw the other name.

**:** Okay how much more time do I have or do you want me to just just keep going?

**:** All right Andrew just told me that I should have gave you an introduction to how to I guess set up the like set up plot code.

**:** To maximize its usages I just realized I completely skimmed over it.

**:** Right right now I'm using my company's IDE so it's pretty much like this is what I designed the past couple months.

**:** A company called with ai.

**:** It's super easy what is it you can either use cursor or vs code so if you just download cursor vs code and hook it up with it it's probably the same thing honestly if you want if you're interested in just using my setup right here I can well I can work out a different you have to get like clock credits too I can like just I mean this case it's fine I can share how you would set it up like yeah no for sure I mean I think our company our company can offer free clock credits like at least 50 like probably 50 for each person here like it's honestly probably fine yeah we don't have like what 2.5 mil so like there's just no need and there's only like four employees there's no need of saving stuff so well just we'll just spend it.

**:** But yeah I mean so so.

**:** Usually there's like a sidebar maybe I should go a little bit more specific there's a sidebar with all your cloud code.

**:** And then all your file storage honestly it's I think the best cases again data data is actually I think the bottleneck right now of how you use clock code so any place that you get data sources you should just continually continuously like get it as much of that in and once you get that in you actually ask clod code to organize your.

**:** Your your framework so there's kind of three things that goes on in claw code the first step is digitizing all your content. It has to be in a machine readable format and the reason why like you see it this is this is what you call an MD file.

**:** And this is machine readable and it's also edible you can edit it yourself right so you can just like randomly type stuff down.

**:** This is what cloud usually reads okay so that's what people refer as the cloud.md file a lot of people have really cool claw.md files mine is actually quite basic mine is actually pretty vanilla because I use more of the scales based on this.

**:** But you essentially need to digitize it the next step after you digitize you show organizer content so right now cloud co uses something like grep search which is okay.

**:** I know I know cursor uses vector searching which is a little bit it sometimes can be more useful has been doing great for me so honestly I'm just gonna stick with that so again so just digitize then you got to organize your content and the last one it's automating so this is actually when you go to scheduling you schedule tasks to continue to do it so you should constantly check your whether or not your floor is organized you should be constantly checking whether or not.

**:** You know all of your like if you're doing a project whether or not like the dependencies are all there so that's kind of the thing.

**:** I'm not sure do you want to give a step like step by step or you want to stake over from the step.

**:** By step but like before yeah I mean there's also like.

**:** I guess this is from our company so honestly we could give this product out for students because I mean it's both for headphones but you know it could probably work if it works for canvas it probably works for everyone but you know there's skills that you can create like how to search up patents.

**:** The web research why finance data how to get that right in here you can set emails through claude right now connect to microsoft teams this is our hedge fund that these are specific headphones oh there's something called who is here okay first of all who's on X like Twitter pretty often.

**:** You guys awesome you guys probably heard of gack have you heard of that?

**:** You heard a g stack? Okay it's a terrible name I feel like but it's one of those ais that are less psychophantic so it doesn't agree with you it kind of questions you a bit so I feel like this is kind of like where the next evolution of cloud is going to be so you can actually create frameworks that are a little bit that that push back a little bit more in your ideas that question a little bit about what you think.

**:** So that's kind of like you know this one is for investments right so this is what I've been creating for investment.

**:** Just like before like they make a trade okay so like you know tell us what is it and then it kind of push it has what we call forcing questions clarifies their thesis and then it kind of analyzes the way you respond to certain to your prompts so honestly like if you're giving a shitty answer like I want to buy apple because it's been doing well for the past like 10 years like this it's a shit response and they're just going to automatically cloud is just going to like criticize you for like that.

**:** But that's kind of like that I think the next framework I'm also working on this you kind of want ai to fight you back a little bit to give you a little bit more of that tension.

**:** But like one of the more useful ones for my research right now academic papers scans through it gives you synopsis and then gets you right into like the it gives you like downloads PDFs right into your workplace and then you can start analyzing it.

**:** But that's kind of it.

**:** So I guess to sum up I guess what I've been doing.

**:** You have a bunch of the skills that you have a skill to create the skill you have a bunch of skills that you work on and then your goal is just to get as much data into your platform as possible.

**:** That's it cool?

**:** I guess I'll give a bit more of an explanation for how you would get to all this.

**:** To begin with.

**:** Yeah.

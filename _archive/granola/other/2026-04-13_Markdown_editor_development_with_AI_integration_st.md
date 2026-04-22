# Markdown editor development with AI integration strategy

**Date:** 2026-04-13


## My Notes

work really smoothlyno bugs make a list - its just jankyhighlightingpictures oktables to work wellsmall things that make it annoying inside a table, i put a link, works everyone work really smoothly!!!!#2 requreiment: in a word document, character 66- 67, they will turn bold, word document stores that separately, which is not good in markdown for ai ai edits the underlying markdown that is behind the tip tap editor the ai is able to make that edit and editor will pcik it up immeidately for that to work, all formatting is being applied inlinehigh lighting is essential ***** add to equal sign markdown editor is trunign into a rich text editora rich text editor should besynced immeidatelyai only reads markdownsyncs instantly, syncs instantly rich text editor WithAI → the one that comes with the office extension - provides support for do deep search highlights need to be changed in markdownspicks up bold dri - the responsiblity individaul #1 pririority second priroity - really good pdf to markdown conversion pdf to markdwonearnings reports highlight earnign reportsedit ti you can't highlight in a pdfbut if we have highlighting ability inthe markdownconvert pdf to markdownai can itneract with it highlight within pdf extracts image, inserts image into mark dwon file extract test from pdf reducto


## Summary

### Work really smoothly

- No bugs in markdown editor
- Current list functionality is janky (can’t create proper a, b, c lists)- Missing highlighting capability- Picture functionality needs testing and improvement- Tables need to work properly
- Small annoying issues that break user experience
- Links work everywhere in markdown except inside tables- Table editing interface is bad and jiggles around
- Core requirement: editor must function smoothly without frustrating bugs

### 2 requirement: AI-markdown integration

- Word document approach won’t work for AI
- Word stores characters and formatting separately (e.g., characters 66-100 turn bold)- AI can’t easily map characters to formatting
- Markdown is ideal for AI integration
- All formatting done inline (e.g., **bold text** with visible stars)- AI can clearly see what’s bold, highlighted, etc.- User sees rich text, AI reads underlying markdown
- Critical technical requirements:
- All formatting must be applied inline- Highlighting essential - use two equal signs (==highlighted text==)- Two-way sync must be instant
- Rich text editor changes sync to markdown immediately- AI edits to markdown appear in rich text editor immediately
- Current WithAI uses office extension
- Provides Word/Excel support but lacks highlighting- Image storage location unclear
- Implementation approach:
- Deep search VS Code marketplace for better options- Novel-vscode extension identified as starting point
- Based on tip tap, open source, 3 years old- Has highlighting but doesn’t sync to underlying markdown- Command+Z deletes everything (needs fixing)- Underlining not working properly- Images not connected/broken

### 1 priority: Markdown editor MVP

- Skyler assigned as DRI (directly responsible individual)
- Responsible for markdown editor functionality over next few months- Adding new features and maintenance
- MVP requirements by Friday:
- Well-functioning editor without bugs- AI editing features integrated- All edits properly synced to markdown (highlights, formatting)- Image functionality connected and working
- Prototype expected by Thursday for review

### PDF to markdown conversion

- Second priority after markdown editor MVP
- Use case: Marty’s earnings reports
- Wants to highlight sections in earnings reports- Edit highlighted content- Current problem: can’t highlight PDFs in platform, AI can’t see highlights
- Solution options:
- Convert PDF to markdown (preferred)
- AI automatically gets all highlights- Better interaction capability- Direct PDF highlighting feature
- Advanced feature: image extraction
- When PDF contains images, extract and insert into markdown file- Reducto startup mentioned as potential API solution for PDF text extraction
- Future considerations:
- Commenting functionality for both markdown and PDF- Tip tap may have commenting features (cost unknown)

### Next Steps

- Skyler: Deliver markdown editor MVP by Friday
- Skyler: Show prototype Thursday for review
- Skyler: Research tip tap commenting features and costs
- PDF conversion functionality to follow after markdown editor completion
Chat with meeting transcript: https://notes.granola.ai/t/0d427a90-9d60-4262-abd8-8b7962914f7c


---

## Transcript

**:** Amongst the smart editor.

**:** It needs to have this marked onion under needs to be able to just.

**:** Like one work really smoothly.

**:** So no bugs.

**:** On our markdown editor.

**:** So many bugs tried to make a list. You can't have one a, b, c, it's just janky.

**:** We don't have highlighting.

**:** I haven't tested the new picture functionality, but we want pictures to work well. We want tables to work well. And within, like, for example, it's these small things that just make it annoying. Like, for example.

**:** Inside of a table.

**:** Like.

**:** I put a link and then you like that hyperlink works everywhere in the markdown except for inside of the table. Oh, yeah, that's frustrating, you know? Or like, even like the way you edit tables right now and other things.

**:** Bad.

**:** Yeah, like the way that it jiggles around.

**:** And. Yeah. Okay.

**:** So, like.

**:** All of these kind of bugs.

**:** We need to, like, it just needs to work really smoothly. That's number one requirement. Number two requirement is like.

**:** We need.

**:** To.

**:** We.

**:** Can't.

**:** Like, for example, in a word document.

**:** I I don't completely understand how it works. My understanding is, like, if you.

**:** Select bold on.

**:** Characters.

**:** 66 through character 100.

**:** Right? Those characters on your document will turn bold.

**:** Right? Yeah, that's.

**:** The word document stores the characters, and then it stores the formatting of the characters separately.

**:** Whereas in Mark, which is not good for the AI, because then the AI has to figure out, okay, what characters correspond to what formatting.

**:** I see.

**:** Me. And, you know, if the AI can, like, actually navigate that system well, that's great. But my guess is it won't be able to. And then we want to use markdown. AI is really good at markdown because the good thing about markdown is all the formatting is done in line.

**:** So it's super clear.

**:** Like, if this is bold, there's, like, two stars.

**:** And then it's bulb, and then the text and then two more stars. And the user doesn't see the stars.

**:** AI can. So the AI can tell what's bold, what's highlighted, Etc.

**:** Okay.

**:** And so.

**:** We need to make sure that.

**:** When the AI edits the underlying markdown file.

**:** As behind the tip top editor.

**:** The AI is able.

**:** To.

**:** Make that.

**:** Edit. Andrew will pick it up immediately.

**:** And it will be able to, like, be able to see it on your document.

**:** Yeah.

**:** That's what, that's what you have in the current with AI editor, right? You made that functionality. Okay.

**:** Do you have any tips on creating that? Because I know, I mean, you definitely spent more time on it, so. And so, like, for that to work. Yeah.

**:** You need to make sure that, like.

**:** All formatting is just being applied in line. So, for example, we should definitely have.

**:** We should definitely have.

**:** Highlighting.

**:** Okay. And the way you do highlighting in markdown.

**:** Is you put two equal signs on this, the text that you're highlighting.

**:** Right.

**:** So it's, it's important that, like, we, like, whatever our markdown editor.

**:** Is showing, there's, like, basically this two-way sync.

**:** Because you're marked on editor is turning your document.

**:** Your markdown document into this.

**:** Like, rich text editor where you can, like, bold and everything looks nice and it feels like a word document. Right.

**:** They're not interacting with the raw Markdown.

**:** I see. So when you make an edit in the rich text editor, it automatically syncs it to the markdown instantly.

**:** So that because the AI can only read the markdown, the AI cannot read the rich text editor or whatever.

**:** So you have to make sure that syncs instantly. And then when the AI added something in the markdown, you have to make sure that synced instantly.

**:** Okay.

**:** So the rich text editor. So that's like how you make that work.

**:** I see. Do you have any.

**:** On top of your head? I'll do my own research after this. But do you know any good working open source, like market VS code Market extensions that I could just take and then we can just fix up the UI?

**:** Do you, do you have any in mind?

**:** So the one that we use like that, or the one that is actually already an option.

**:** In with AI is the one that comes with.

**:** It comes with.

**:** The.

**:** Like, office.

**:** I can check what it's actually called, but it's called.

**:** Like.

**:** Office at office.

**:** Extension, and it provides support for word documents, Excel.

**:** And it's, like, not the best.

**:** You know, it doesn't actually have, like, it doesn't have highlighting.

**:** It doesn't have.

**:** It has pictures, but I don't even know where it stores the pictures.

**:** Yeah, I would look at, look at different open source ones. Like, I would do deep search of the marketplace, see if you can find something really good. Okay, I'll get.

**:** But if not.

**:** Like.

**:** My understanding is that, like, tip tap.

**:** Basically has all the features that we want.

**:** It.

**:** Just connecting tip tab to VS code extension is an intricate process.

**:** It's not like you have to actually understand how tip tap works a little bit.

**:** I give you. I mean, I tried to just ask claude, like, make me a tip down. Maybe. Maybe new cloud is, like, smarter five months ago.

**:** But I tried and just didn't work.

**:** So.

**:** Maybe, like.

**:** It might be something that you have to really understand. But my guess is, like, easiest way for us to implement this is going to be just.

**:** Like.

**:** You just tipped up. Yeah. Can you take a look? I'm going to send you something right now.

**:** I've been using this as kind of my base.

**:** This guy created something called novel, which is based on tip tap, and then he connected it to VS code.

**:** I just sent it to you via slack.

**:** That's. I think this is probably my starting approach.

**:** What do you think about this? I've been working on this for a bit.

**:** Let me look. Is it open source? Yeah, it's open source. So I have the guitar. Awesome. I mean, dude, if we can get, like, someone to figure out because, like, what? Like, there's so many edge cases with the.

**:** Markdown editor. I totally agree. No, it's. It's a pain in the ass, man.

**:** It's called.

**:** Knob.

**:** What's it called?

**:** Oh, I just. It's got a novel dash VS code. I just sent it via slack as well.

**:** And it's because.

**:** This is. Let me see.

**:** Where'd you find this?

**:** Well, I used your research tool, and then it.

**:** It does a good job of deep researching now. I think it does better than the research. Like, if you use fire crawl and brave, it does. It is a better job.

**:** What does novel.

**:** Yeah, what novel is.

**:** Based on.

**:** It's based on tip tap.

**:** I think.

**:** But then the guy took it.

**:** And then made it into a vs code extension. It's a bit outdated. I think it's three hour, three years outdated, so we might have to update it.

**:** Novel.

**:** Yeah.

**:** But so that the thing is someone took it and made it into a vs code extension, and that's probably. I think that's where the edge is at.

**:** But.

**:** Okay.

**:** Let me try.

**:** Yeah, you can honestly download limit. Let's just download the. Oh, but, yeah, I've tried adding. It doesn't do the AI editing thing. It's like you. It doesn't connect to client code, like the way.

**:** You are. Our. R does. Art does it right. Like the way. The way we do it right now.

**:** Okay.

**:** So you can do this.

**:** Okay.

**:** They have highlight.

**:** Ing.

**:** Yeah. Yeah.

**:** Yeah.

**:** I like.

**:** It.

**:** You like it? All right.

**:** Well.

**:** So I'll try to add this AI editing features then.

**:** And it seems like we want to make it as smooth and as integrated as possible.

**:** Images are not connected. Not. I know the images are broken, so we have to fix that.

**:** Too.

**:** Let me see what else.

**:** All right.

**:** The one problem I'm getting.

**:** Is.

**:** Like,

**:** For example, I did.

**:** This highlight.

**:** Yeah.

**:** Don't.

**:** See any indication that it's highlighted.

**:** In the actual.

**:** Underlying.

**:** Markdown.

**:** Ah.

**:** That's. So it has to sense it the way that it's sensing the boats and italics and the headings. Okay.

**:** Let me jot that down.

**:** Good catch there.

**:** Change.

**:** The markdown.

**:** S.

**:** Okay.

**:** No.

**:** So it picks up.

**:** Bold.

**:** And how about underlining?

**:** And. Oh, actually, let me check. Italics.

**:** I'm checking.

**:** It,

**:** Alex. Okay.

**:** Picks up.

**:** Italics.

**:** And then.

**:** Now it's.

**:** Not working.

**:** Oh, wait.

**:** A minute.

**:** Now I opened it with.

**:** Normal is quite pretty.

**:** Cool.

**:** Yeah. I mean.

**:** It's not.

**:** Picking up.

**:** Under.

**:** Line.

**:** Okay, so we got to fix that.

**:** Then.

**:** Let's see.

**:** Also.

**:** For some reason.

**:** When I press.

**:** Command.

**:** Z.

**:** It just.

**:** Deletes everything.

**:** I just noticed that, too. Good. Okay, so we have to. We have to get rid of that.

**:** It's more like a notion editor.

**:** It definitely feels.

**:** But otherwise.

**:** Feature.

**:** S.

**:** Of.

**:** Normal look fairly good.

**:** So then just to clarify, I'm gonna.

**:** Add the AI features, make sure all of these edits are being taken care of and marked down, like the highlights, and then connect the images, because I'm pretty sure if you add an image, it's gonna break.

**:** I'm pretty sure they don't have it connected.

**:** Yeah.

**:** So, yeah, it doesn't have. What I would say is, like,

**:** You.

**:** Can take any.

**:** Implementation.

**:** Approach.

**:** You want.

**:** You.

**:** Want to use novel.

**:** And.

**:** Use tip.

**:** App. Yeah. If you want to use.

**:** Just make sure.

**:** Like, all I will care about.

**:** Is that.

**:** Like.

**:** This works really well.

**:** And.

**:** I'm.

**:** Gonna.

**:** Try assigning you as, like, just dr.

**:** I for this.

**:** So, like.

**:** The next stream, like, the responsible individual. So over the next few months,

**:** Like.

**:** Having this working really well.

**:** Adding.

**:** New features to this and stuff, this will be your responsibility.

**:** Understood. All right.

**:** And then.

**:** So this is first priority.

**:** Second priority is.

**:** Like.

**:** We need to create.

**:** A really.

**:** Good.

**:** Ability.

**:** For PDF to.

**:** Mark down.

**:** Conversion.

**:** PDF to markdown.

**:** I thought you. Oh.

**:** We have.

**:** We have marked down the PDF. Yes, we need PDF to.

**:** Mark that because, for example.

**:** One of the main things Marty needs to use this for.

**:** Is.

**:** He wants to.

**:** Take his earnings report.

**:** High.

**:** Light the things you want to highlight. Is earnings report.

**:** And then.

**:** Like,

**:** Edit it.

**:** Right?

**:** Yeah.

**:** But the.

**:** Problem we have.

**:** There.

**:** Is.

**:** You can't.

**:** Highlight in a PDF within our platform.

**:** And the AI can't see what's highlighted.

**:** But if we.

**:** Have highlighting.

**:** Ability that.

**:** Works well within the.

**:** Markdown ed.

**:** Itor, if.

**:** We can just convert.

**:** That PDF to.

**:** Markdown.

**:** The.

**:** AI automatically.

**:** Has, like, all the.

**:** Highlights.

**:** You can interact with it.

**:** Like, nicely.

**:** Unless we did, like, a direct.

**:** High.

**:** Light within PDF feature. That's another option.

**:** But.

**:** My.

**:** Guess is just turning everything to PDF.

**:** To markdown systematically. Is that a good idea?

**:** Just for the a to be able to read it, right? And then.

**:** Okay.

**:** And.

**:** Honestly, what's. What's like would be awesome.

**:** As if we had.

**:** Like, let's say you had this PDF and you convert it to markdown.

**:** And you.

**:** Out.

**:** Putted.

**:** You know, PDF has some images. Like, how are you going to convert the image to markdown?

**:** If that ability could actually, like, extract when it comes to an image, if it extracts the image.

**:** And then inserts that image into the markdown file.

**:** That would be awesome.

**:** And there's a startup that, like, is getting kind of famous that.

**:** Does.

**:** Like, abstract text from PDF stuff, and they might have a solution for this. It's called reducto.

**:** Reducto. Got it. Okay. And maybe they have an API we can send a PDF and get a mark. Like, that'll be.

**:** The best.

**:** You know? Oh, yeah. AI document part of saying. Yes.

**:** That's.

**:** Okay.

**:** But.

**:** If.

**:** Not, this is not.

**:** The highest priority.

**:** The thing is.

**:** Like.

**:** 10.

**:** Read PDFs pretty well.

**:** And one question is maybe we should.

**:** Like, we should do whatever.

**:** Is easier slash gives the best user experience.

**:** Either we convert PDF to markdown or we.

**:** Make it so that you can highlight things within a PDF.

**:** Like just innately.

**:** We're commenting also be part of that functionality. I know Google docs does that.

**:** Is that something Marty does or doesn't?

**:** Like, down the road?

**:** I think.

**:** Being able to.

**:** Comment on both.

**:** Are.

**:** Markdown.

**:** And.

**:** PDF or for doing PDF.

**:** Convert to markdown. Just markdown.

**:** Then. Yeah, I think, like, we do want to have commenting, but that's a bit down the line. That would be.

**:** Like, next on your list of things to do with the markdown editor as the responsible person for it. But.

**:** But.

**:** Yeah.

**:** Cool.

**:** That sounds like a plan. I know.

**:** I know tip tap has some of these features. I'm not sure if they cost money or not, but.

**:** We'll.

**:** See if it does anything. I'll let you know. I'll let you know if I commented thing. Appreciate it, though. Yeah. Thanks for the update, and I'll get to it.

**:** Sounds good. I'll have a prototype probably by Thursday, and then we can just discuss then.

**:** Okay.

**:** I want, like.

**:** A.

**:** MVP.

**:** By Friday.

**:** I mean, I don't know how.

**:** Busy your week is.

**:** But, like.

**:** Oh, it's pretty. This week's pretty chill, so let's see. Okay, then we want.

**:** Like.

**:** I.

**:** Want, like, a well.

**:** Functioning M.

**:** VP by Friday.

**:** Like.

**:** Something I can, like, use and, like, not.

**:** Feel like, oh, this is bug.

**:** Gy. Understood. Okay.

**:** I'll get to it.

**:** Okay.

**:** For this.

**:** Friday.

**:** The.

**:** Non requirement is for the.

**:** Markdown.

**:** Edger. Got it. So you don't have to have the PDF.

**:** Conversion figured out, but, like, you have to have really good.

**:** Like,

**:** Editor.

**:** All right.

**:** Sounds like a plan. All right.

**:** Oh, yeah. Call me anytime, man. I will. I'll probably show up on Thursday in the office, and then we'll just start working from there. Sounds good.

**:** All right. See you, Skyler. See ya. Have a good one. Bye.

**:** Oh.

**:** My gosh.

**:** I.

**:** Thought it was figurative.

**:** Ly.

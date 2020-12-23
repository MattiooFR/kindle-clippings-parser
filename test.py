import torch
from transformers import T5Tokenizer, T5ForConditionalGeneration
from summarizer import Summarizer

model = T5ForConditionalGeneration.from_pretrained("t5-base")
tokenizer = T5Tokenizer.from_pretrained("t5-base")
device = torch.device("cpu")

body = """
Most books deal with topics serially—they cover one topic, move on to the next, and so on. We follow this strategy in the sense that each chapter addresses new topics, but we also apply two of the primary learning principles
A single, simple quiz after reading a text or hearing a lecture produces better learning and remembering than rereading the text or reviewing lecture notes.
When you space out practice at a task and get a little rusty between sessions, or you interleave the practice of two or more subjects, retrieval is harder and feels less productive, but the effort produces longer lasting learning and enables more versatile application of it in later settings.
you build better mastery when you use testing as a tool to identify and bring up your areas of weakness.
However, if you practice elaboration, there’s no known limit to how much you can learn. Elaboration is the process of giving new material meaning by expressing it in your own words and connecting it with what you already know. The more you can explain about the way your new learning relates to your prior knowledge, the stronger your grasp of the new learning will be, and the more connections you create that will help you remember it later.
Putting new knowledge into a larger context helps learning.
People who learn to extract the key ideas from new material and organize them into a mental model and connect that model to prior knowledge show an advantage in learning complex mastery.
Making mistakes and correcting them builds the bridges to advanced learning.
What’s apparent from the research is that gains achieved during massed practice are transitory and melt away quickly.
Learning is stronger when it matters, when the abstract is made concrete and personal.
It makes sense to reread a text once if there’s been a meaningful lapse of time since the first reading, but doing multiple readings in close succession is a time-consuming study strategy that yields negligible benefits at the expense of much more effective strategies that take less time.
Had he used the set of key concepts in the back of each chapter to test himself? Could he look at a concept like “conditioned stimulus,” define it, and use it in a paragraph? While he was reading, had he thought of converting the main points of the text into a series of questions and then later tried to answer them while he was studying? Had he at least rephrased the main ideas in his own words as he read? Had he tried to relate them to what he already knew? Had he looked for examples outside the text?
The act of retrieving learning from memory has two profound benefits. One, it tells you what you know and don’t know, and therefore where to focus further study to improve the areas where you’re weak. Two, recalling what you have learned causes your brain to reconsolidate the memory, which strengthens its connections to what you already know and makes it easier for you to recall in the future.
Reflection can involve several cognitive activities that lead to stronger learning:
To be most effective, retrieval must be repeated again and again, in spaced out sessions so that the recall, rather than becoming a mindless recitation, requires some cognitive effort.
One argument suggested that the greater effort required by the delayed recall solidified the memory better.
When retrieval practice is spaced, allowing some forgetting to occur between tests, it leads to stronger long-term retention than when it is massed.
Studying the Testing Effect “In the Wild” In 2005, we and our colleagues approached Roger Chamberlain, the principal of a middle school in nearby Columbia, Illinois, with a proposition. The positive effects of retrieval practice had been
The results were compelling: The kids scored a full grade level higher on the material that had been quizzed than on the material that had not been quizzed. Moreover, test results for the material that had been reviewed as statements of fact but not quizzed were no better than those for the nonreviewed material. Again, mere rereading does not much help.
Tests that require the learner to supply the answer, like an essay or short-answer test, or simply practice with flashcards, appear to be more effective than simple recognition tests like multiple choice or true/false tests. However, even multiple choice tests like those used at Columbia Middle School can yield strong benefits.
Practice that’s spaced out, interleaved with other learning, and varied produces better mastery, longer retention, and more versatility.
Almost everywhere you look, you find examples of massed practice: summer language boot camps, colleges that offer concentration in a single subject with the promise of fast learning, continuing education seminars for professionals where training is condensed into a single weekend. Cramming for exams is a form of massed practice. It feels like a productive strategy, and it may get you through the next day’s midterm, but most of the material will be long forgotten by the time you sit down for the final. Spacing out your practice feels less productive for the very reason that some forgetting has set in and you’ve got to work harder to recall the concepts. It doesn’t feel like you’re on top of it. What you don’t sense in the moment is that this added effort is making the learning stronger.2
Why is spaced practice more effective than massed practice? It appears that embedding new learning in long-term memory requires a process of consolidation, in which memory traces (the brain’s representations of the new learning) are strengthened, given meaning, and connected to prior knowledge—a process that unfolds over hours and may take several days.
The basic idea is that varied practice—like tossing your beanbags into baskets at mixed distances—improves your ability to transfer learning from one situation and apply it successfully to another.
For our learning to have practical value, we must be adept at discerning “What kind of problem is this?” so we can select and apply an appropriate solution.
One form of practice that helps us learn from experience, as the neurosurgeon Mike Ebersold recounted in Chapter 2, is reflection. Some people are more given to the act of reflection than others, so Doug Larsen has broadened his research to study how you might structure reflection as an integral part of the training, helping students cultivate it as a habit. He is experimenting with requiring students to write daily or weekly summaries of what they did, how it worked, and what they might do differently next time to get better results. He speculates that daily reflection, as a form of spaced retrieval practice, is probably just as critical in the real-world application of medicine as quizzing and testing are in building competencies in medical school.
At a minimum, Larsen would like to see something done to interrupt the forgetting: give a quiz at the end of a conference and follow it with spaced retrieval practice. “Make quizzing a standard part of the culture and the curriculum. You just know every week you’re going to get in your email your ten questions that you need to work through.”
How big an interval, you ask? The simple answer: enough so that practice doesn’t become a mindless repetition. At a minimum, enough time so that a little forgetting has set in. A little forgetting between practice sessions can be a good thing, if it leads to more effort in practice, but you do not want so much forgetting that retrieval essentially involves relearning the material. The time periods between sessions of practice let memories consolidate. Sleep seems to play a large role in memory consolidation, so practice with at least a day in between sessions is good.
Beware of the familiarity trap: the feeling that you know something and no longer need to practice it. This familiarity can hurt you during self-quizzing if you take shortcuts. Doug Larsen says, “You have to be disciplined to say, ‘All right, I’m going to make myself recall all of this and if I don’t, what did I miss, how did I not know that?’ Whereas if you have an instructor-generated test or quiz, suddenly you have to do it, there’s an expectation, you can’t cheat, you can’t take mental shortcuts around it, you simply have to do that.” The nine quizzes Andy Sobel administers over the twenty-six meetings of his political economics course are a simple example of spaced retrieval practice, and of interleaving—because he rolls forward into each successive quiz questions pertaining to work from the beginning of the semester. Interleaving two or more subjects during practice also provides a form of spacing. Interleaving can also help you develop your ability to discriminate later between different kinds of problems and select the right tool from your growing toolkit of solutions. In interleaving, you don’t move from a complete practice set of one topic to go to another. You switch before each practice is complete. A friend of ours describes his own experience with this: “I go to a hockey class and we’re learning skating skills, puck handling, shooting, and I notice that I get frustrated because we do a little bit of skating and just when I think I’m getting it, we go to stick handling, and I go home frustrated, saying, ‘Why doesn’t this guy keep letting us do these things until we get it?’
Like interleaving, varied practice helps learners build a broad schema, an ability to assess changing conditions and adjust responses to fit. Arguably, interleaving and variation help learners reach beyond memorization to higher levels of conceptual learning and application, building more rounded, deep, and durable learning, what in motor skills shows up as underlying habit strength.
Reflection is a form of retrieval practice (What happened? What did I do? How did it work out?), enhanced with elaboration (What would I do differently next time?).
The process of strengthening these mental representations for long-term memory is called consolidation. New learning is labile: its meaning is not fully formed and therefore is easily altered. In consolidation, the brain reorganizes and stabilizes the memory traces. This may occur over several hours or longer and involves deep processing of the new material, during which scientists believe that the brain replays or rehearses the learning, giving it meaning, filling in blank spots, and making connections to past experiences and to other knowledge already stored in long-term memory. Prior knowledge is a prerequisite for making sense of new learning, and forming those connections is an important task of consolidation.
In fact, because new learning depends on prior learning, the more we learn, the more possible connections we create for further learning. Our retrieval capacity, though, is severely limited. Most of what we’ve learned is not accessible to us at any given moment. This limitation on retrieval is helpful to us: if every memory were always readily to hand, you would have a hard time sorting through the sheer volume of material to put your finger on the knowledge you need at the moment: where did I put my hat, how do I sync my electronic devices, what goes into a perfect brandy Manhattan?
Knowledge that is well entrenched, like real fluency in French or years of experience driving on the right side of the road, is easily relearned later, after a period of disuse or after being interrupted by competition for retrieval cues. It’s not the knowledge itself that has been forgotten, but the cues that enable you to find and retrieve it. The cues for the new learning, driving on the left, displace those for the old, driving on the right (if we are lucky). The paradox is that some forgetting is often essential for new learning.6 When you change from a PC to a Mac, or from one Windows platform to another, you have to do enormous forgetting in order to learn the architecture of the new system and become adept at manipulating it so readily that your attention can focus on doing your work and not on working the machine. Jump school training provides another example: After their military service, many paratroopers take an interest in smoke jumping. Smokejumpers use different airplanes, different equipment, and different jump protocols. Having trained at the army’s jump school is cited as a distinct disadvantage for smoke jumping, because you have to unlearn one set of procedures that you have practiced to the point of reflex and replace them with another. Even in cases where both bodies of learning seem so similar to the uninitiated—jumping out of an airplane with a parachute on your back—you may have to forget the cues to a complex body of learning that you possess if you are to acquire a new one. We know this problem of reassigning cues to memory from our own lives, even on the simplest levels.
the easier knowledge or a skill is for you to retrieve, the less your retrieval practice will benefit your retention of it. Conversely, the more effort you have to expend to retrieve knowledge or skill, the more the practice of retrieval will entrench it.
Massed practice gives us the warm sensation of mastery because we’re looping information through short-term memory without having to reconstruct the learning from long-term memory. But just as with rereading as a study strategy, the fluency gained through massed practice is transitory, and our sense of mastery is illusory. It’s the effortful process of reconstructing the knowledge that triggers reconsolidation and deeper learning.
Would you rather read an article that has normal type or type that’s somewhat out of focus? Almost surely you would opt for the former. Yet when text on a page is slightly out of focus or presented in a font that is a little difficult to decipher, people recall the content better.
The act of trying to answer a question or attempting to solve a problem rather than being presented with the information or the solution is known as generation. Even if you’re being quizzed on material you’re familiar with, the simple act of filling in a blank has the effect of strengthening your memory of the material and your ability to recall it later. In testing, being required to supply an answer rather than select from multiple choice options often provides stronger learning benefits.
The act of taking a few minutes to review what has been learned from an experience (or in a recent class) and asking yourself questions is known as reflection. After a lecture or reading assignment, for example, you might ask yourself: What are the key ideas? What are some examples? How do these relate to what I already know? Following an experience where you are practicing new knowledge or skills, you might ask: What went well? What could have gone better? What might I need to learn for better mastery, or what strategies might I use the next time to get better results?
the process of trying to solve a problem without the benefit of having been taught how is called generative learning, meaning that the learner is generating the answer rather than recalling it. Generation is another name for old-fashioned trial and error.
For me, the risk of knowing what you’re getting into is that it becomes an overwhelming obstacle to getting started.”18
Learning is at least a three-step process: initial encoding of information is held in short-term working memory before being consolidated into a cohesive representation of knowledge in long-term memory. Consolidation reorganizes and stabilizes memory traces, gives them meaning, and makes connections to past experiences and to other knowledge already stored in long-term memory. Retrieval updates learning and enables you to apply it when you need it
Long-term memory capacity is virtually limitless: the more you know, the more possible connections you have for adding new knowledge.
Retrieval practice that’s easy does little to strengthen learning; the more difficult the practice, the greater the benefit.
Incompetent people lack the skills to improve because they are unable to distinguish between incompetence and competence. This phenomenon, of particular interest for metacognition, has been named the Dunning-Kruger effect after the psychologists David Dunning and Justin Kruger. Their research showed that incompetent people overestimate their own competence and, failing to sense a mismatch between their performance and what is desirable, see no need to try to improve.
Tools and Habits for Calibrating Your Judgment Most important is to make frequent use of testing and retrieval practice to verify what you really do know versus what you think you know.
Don’t make the mistake of dropping material from your testing regime once you’ve gotten it correct a couple of times. If it’s important,
Don’t assume that you’re doing something wrong if the learning feels hard. Remember that difficulties you can overcome with greater cognitive effort will more than repay you
Distill the underlying principles; build the structure.   If you’re an example learner, study examples two at a time or more, rather than one by one, asking yourself in what ways they are alike and different. Are the differences such that they require different solutions, or are the similarities such that they respond to a common solution?
This rise in neurogenesis starts before the new learning activity is undertaken, suggesting the brain’s intention to learn, and continues for a period after the learning activity, suggesting that neurogenesis plays a role in the consolidation of memory and the beneficial effects that spaced and effortful retrieval practice have on long-term retention.9
A focus on performance instead of on learning and growing causes people to hold back from risk taking or exposing their self-image to ridicule by putting themselves into situations where they have to break a sweat to deliver the critical outcome.
The takeaway from Dweck, Tough, and their colleagues working in this field is that more than IQ, it’s discipline, grit, and a growth mindset that imbue a person with the sense of possibility and the creativity and persistence needed for higher learning and success.
Ten thousand hours or ten years of practice was the average time the people Ericsson studied had invested to become expert in their fields, and the best among them had spent the larger percentage of those hours in solitary, deliberate practice.
expert performance is a product of the quantity and the quality of practice, not of genetic predisposition,
associating vivid mental images with verbal or abstract material makes that material easier to retrieve from memory.
Retrieving knowledge and skill from memory should become your primary study strategy in place of rereading.
When you read a text or study lecture notes, pause periodically to ask yourself questions like these, without looking in the text: What are the key ideas? What terms or ideas are new to me? How would I define them? How do the ideas relate to what I already know?
Set aside a little time every week throughout the semester to quiz yourself on the material in a course, both the current week’s work and material covered in prior weeks.
Use quizzing to identify areas of weak mastery, and focus your studying to make them strong.
The harder it is for you to recall new learning from memory, the greater the benefit of doing
Making errors will not set you back, so long as you check your answers and correct your mistakes.
The familiarity with a text that is gained from rereading creates illusions of knowing, but these are not reliable indicators of mastery of the material. Fluency with a text has two strikes against it: it is a misleading indicator of what you have learned, and it creates the false impression that you will remember the material.
But what you don’t sense when you’re struggling to retrieve new learning is the fact that every time you work hard to recall a memory, you actually strengthen it. If you restudy something after failing to recall it, you actually learn it better than if you had not tried to recall it.
If you use flashcards, don’t stop quizzing yourself on the cards that you answer correctly a couple of times. Continue to shuffle them into the deck until they’re well mastered. Only then set them aside—but in a pile that you revisit periodically, perhaps monthly. Anything you want to remember must be periodically recalled from memory.
If you use self-quizzing as your primary study strategy and space out your study sessions so that a little forgetting has happened since your last practice, you will have to work harder to reconstruct what you already studied. In effect, you’re “reloading” it from long-term memory. This effort to reconstruct the learning makes the important ideas more salient and memorable and connects them more securely to other knowledge and to more recent learning.
Spaced practice feels more difficult, because you have gotten a little rusty and the material is harder to recall. It feels like you’re not really getting on top of it, whereas in fact, quite the opposite is happening:
Interleave the Study of Different Problem Types What does this mean? If you’re trying to learn mathematical formulas, study more than one type at a time, so that you are alternating between different problems that call for different solutions.
Even when learners achieve superior mastery from interleaved practice, they persist in feeling that blocked practice serves them better. You may also experience this feeling, but you now have the advantage of knowing that studies show that this feeling is illusory.Location in the book 2831
Elaboration is the process of finding additional layers of meaning in new material.
A powerful form of elaboration is to discover a metaphor or visual image for the new material.
By wading into the unknown first and puzzling through it, you are far more likely to learn and remember the solution than if somebody first sat you down to teach it to you.
You can practice generation when reading new class material by trying to explain beforehand the key ideas you expect to find in the material and how you expect they will relate to your prior knowledge. Then read the material to see if you were correct.
If you’re in a science or math course learning different types of solutions for different types of problems, try to solve the problems before you get to class. The Physics Department at Washington University in St. Louis now requires students to work problems before class.
Reflection is the act of taking a few minutes to review what has been learned in a recent class or experience and asking yourself questions. What went well? What could have gone better?
CALIBRATION is the act of aligning your judgments of what you know and don’t know with objective feedback so as to avoid being carried off by the illusions of mastery that catch many learners by surprise at test time.
Too often we will look at a question on a practice test and say to ourselves: Yup, I know that, and then move down the page without making the effort to write in the answer. If you don’t supply the answer, you may be giving in to the illusion of knowing, when in fact you would have difficulty rendering an accurate or complete response.
He became more mindful of that when he studied. “I would stop. ‘Okay, what did I just read? What is this about?’ I’d have to think about it. ‘Well, I believe it happens this way: The enzyme does this, and then it does that.’ And then I’d have to go back and check if I was way off base or on the right track.” The process was not a natural fit. “It makes you uncomfortable at first. If you stop and rehearse what you’re reading and quiz yourself on it, it just takes a lot longer. If you have a test coming up in a week and so much to cover, slowing down makes you pretty nervous.” But the only way he knew of to cover more material, his established habit of dedicating long hours to rereading, wasn’t getting the results he needed. As hard as it was, he made himself stick to retrieval practice long enough at least to see if it worked. “You just have to trust the process, and that was really the biggest hurdle for me, was to get myself to trust it. And it ended up working out really well for me.”
“When you go back and review, instead of just rereading you need to see if you can recall the learning. Do I remember what this stuff was about? You always test yourself first. And if you don’t remember, then that’s when you go back and look at it and try again.”
On slowing down to find the meaning: Young has also slowed down the speed at which he reads material, thinking about meaning and using elaboration to better understand it and lodge it in memory.
•  Always does the reading prior to a lecture •  Anticipates test questions and their answers as he reads •  Answers rhetorical questions in his head during lectures to test his retention of the reading •  Reviews study guides, finds terms he can’t
•  Always does the reading prior to a lecture •  Anticipates test questions and their answers as he reads •  Answers rhetorical questions in his head during lectures to test his retention of the reading •  Reviews study guides, finds terms he can’t recall or doesn’t know, and relearns those terms •  Copies bolded terms and their definitions into a reading notebook, making sure that he understands them •  Takes the practice test that is provided online by his professor; from this he discovers which concepts he doesn’t know and makes a point to learn them •  Reorganizes the course information into a study guide of his design •  Writes out concepts that are detailed or important, posts them above his bed, and tests himself on them from time to time •  Spaces out his review and practice over the duration of the course
“Stop. Do not look at your notes. Just take a minute to think about it yourself.”
Testing groups.   Wenderoth has transformed class “study groups” into “testing groups.” In a study group, the person who knows the most talks and the others listen. The emphasis is on memorizing things. However, in a testing group, they all wrestle with a question together, without opening the textbook. “Everybody has bits of information, and you talk with your colleagues and figure it out.” The emphasis is on exploration and understanding.
Wenderoth will ask students in a testing group what ideas they don’t feel really clear on. Then she’ll send one student to the
Wenderoth will ask students in a testing group what ideas they don’t feel really clear on. Then she’ll send one student to the whiteboard to try to explain the concept. As the student struggles, perhaps putting up the pieces of the answer she knows, the rest of the group are instructed to test her by asking questions whose answers will lead her to the larger concept. Throughout, all textbooks remain closed.
Free recall.   Wenderoth assigns her students to spend ten minutes at the end of each day sitting with a blank piece of paper on which to write everything they can remember from class. They must sit for ten minutes. She warns that it will be uncomfortable, they will run out of ideas after two minutes, but they must stick it out.
“I took a practice test every three days, saw what I got wrong, and adjusted.”
One, get a copy of the presentation materials and use them to quiz yourself on the key ideas, much as Nathaniel Fuller quizzes himself on the arc of a play, his lines, the many layers of character. Two, schedule follow-up emails to appear in your inbox every month or so with questions that require you to retrieve the critical learning you gained from the seminar. Three, contact your professional association and ask them to consider revamping their approach to training along the lines outlined in this book. The"""

extractive_model = Summarizer(
    model = bert-base-uncased

)
result = extractive_model(body, ratio=0.1)
print(result)

preprocess_text = result.strip().replace("\n", "")
t5_prepared_Text = "summarize: " + preprocess_text

tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)


# summmarize
summary_ids = model.generate(
    tokenized_text,
    num_beams=4,
    min_length=30,
    max_length=200,
    no_repeat_ngram_size=2,
    early_stopping=True,
)

output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print("\n\nSummarized text: \n", output)

# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

* For me, it was chaotic. There was so many problems with it, it was almost too funny. I thought it was a pretty good start and had potiental.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  * The number range in the info section does not change depending on the difficulty. So, when you pick easy mode, the info says the number range is between 1-100 with 8 attempts when it's suppose to be 1-20 with 6 attempts. It's the same for hard mode as well.
  * Typing a string as an input counts as an attempt. The hint does change to "This is not a number" but still counts as an attempt. Also, the attempts are inconsistent.  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| The hints are broken. | The hints are supposed to change with each new attempt from the user. | The hints keeps deplaying the same hint from the inital input. So when the user makes a new attempt it stays the same regardless if its higher or lower than the secret number. | None | 
| The "New Game" button is broken. | The game is supposed to restart. | When I try to start a new game, it does nothing. The only way I can restart is by relauching. | None|
| Number range is nonexistent. | Depending on the difficulty, the game is suppose to restrict the user with a number range that tells the user the secret number is between them.| However, there is no actual range that restricts the user's number input. For example, If the "range" is 1-100, the user can enter any number bigger than 100 and it will count it as an attempt. | None |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

* I used Claude AI. It was already installed. Plus, I wanted to get more experience using it.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

* Claude AI informed me that the "Info text hardcodes "between 1 and 100" regardless of actual difficulty range" in line app.py:110. After I was informed, I went to that specific line and verified whether Chaude AI was right. Then, I checked the actual app and manually confirmed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

* Overall, I just found "Unchecking "Show hint" makes the game unplayable — it suppresses the only Higher/Lower feedback, so you're guessing blind with no signal" very misleading. I mean I guess its good to know but I was just like "what the heck". It was just so random because it was obvious information.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

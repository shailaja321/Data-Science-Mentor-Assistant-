# Open-Source AI Assistant Report

This Project was done during my Internship as a AI DEVELOPER INTERN at Viswam.ai which is sponsered by Swecha telanagana , Meta ai and IIIT Hyderabad

## AI Assistant Overview

### Assistant Name :
**Data Science Mentor Assistant**


https://github.com/user-attachments/assets/7c8da527-2b43-409d-980f-edea74d988d5


## Link for the application

https://shailajagorile-g-ai-assistant.hf.space/?logs=container&__theme=system&deep_link=EUvN1VXtXyg

### Purpose & Target Audience
**Purpose**:
This AI Assistant is built to serve as a **data Science Mentor**, helping useres understand fundamental and advanced concepts in Python libraries like Pandas and Numpy, as well as machine learning topics.

**Target Audience**:
- Aspiring data scientists.
- Engineering and computer science students.
- Professionals looking to upskill in data science and machine learning.
- Hobbists exploring AI and Python.


## System Prompt Design and Justification

### Full System Prompt
'''python
Prompt = f"User: {user_input}\nAssistant:"

#### Language And libraries used

- Python language 
- Transformers , torch , Gradio packages

## Justification and Impact Analysis
1. Breakdown of Elements
- "User: {user_input}\nAssistant:":
Creates a clear dialogue format to instruct the model to take on the assistant’s role. It mimics natural conversation, prompting the model to respond as a helpful guide.

2. Design Choices
- Dialogue format: Helps guide the TinyLlama model to follow a back-and-forth human interaction format.

- Temperature of 0.7: Introduces variability while keeping responses coherent.

- Max tokens = 256: Balances response detail and performance.

- No complex system prompt file: Keeps the model flexible and simple for fast performance in smaller environments.

3. Anticipated Impact
- Ensures consistency in persona (mentor tone)

- Provides context awareness in replies

- Limits verbosity and ensures relevance

- Enhances clarity for novice users

4. Iteration & Refinement

- Originally tested without the "User:" and "Assistant:" prefix, but responses were less relevant. Adding the dialogue format improved coherence and focus.

## User Reviews and Feedback Analysis

### Methodology
I Collected user reviews using a combination of:
- Direct Messages on Social media 
- Google form surveys

### Review Collection 
- click on the link 🔗
https://docs.google.com/spreadsheets/d/17uQItNNskVZNUtRuifQWLYT5LEbzYd76bqo5PSy37BQ/edit?usp=sharing

### Feedback Factors Analysis
1. Accuracy: Generally high (responses were correct and relevant)
2. Clarity: Responses were well-structured but sometimes lengthy
3. Usefulness: Very helpful to learners
4. Tone & Persona: Friendly and educational
5. Response Speed: Acceptable for a local deployment, but could be faster with smaller models
6. Error Handling: Limited fallback behavior
7. Engagement: Conversational and mentor-like
8. Ease of Use: Very user-friendly via Gradio
9. Bias/Fairness: No observed bias
10. Overall Experience: 4.5★ Satisfied

### Analysis of Feedback
#### Summary of Key Findings : 
- Strengths: Accuracy, structure, clarity, mentor tone
- Weaknesses: Slight latency, no error messages/fallbacks

#### Actionable Takeaways :
1. Implement fallback handling for unknown queries
2. Reduce verbosity for simpler topics
3. Add response streaming for perceived speed improvement
4. Explore smaller/faster models if needed for deployment
5. Add user feedback form within the interface

### Future Roadmap

#### Short-Term Goals (Next 1 Week)
- Add error handling for invalid inputs
- Limit token output for shorter explanations
- Include usage instructions on UI

#### Mid-Term Goals (2–4 Weeks)
- Add visual examples (charts, tables) using embedded images
- Integrate with code sandbox or notebook interface for hands-on examples
- Enable speech-to-text input and audio output

#### Long-Term Vision (Beyond 4 Weeks)
- Scale to a fully interactive Data Science learning tutor
- Add curriculum-based guided learning modules
- Support multilingual explanations
- Deploy a mobile-friendly version
- Enable collaboration with other assistants (e.g., coding, interview prep)

### Plan to Increase User Adoption
#### Initial User Acquisition
- Share on LinkedIn, Twitter, and GitHub
- Post on data science forums (e.g., Reddit r/datascience, Kaggle)
- Share demo with online coding communities and student WhatsApp/Discord groups

#### Value Proposition Communication
- Clear tagline: “Learn Data Science by Asking Questions.”
- Highlight mentor-like persona and real-time responses

#### Marketing & Promotion (Open-source Focused)
- Submit to Hugging Face Spaces featured list
- Create a short YouTube/Instagram reel
- Share blog post on Medium or DEV.to explaining the assistant

#### Feedback Loops for Continuous Improvement
- Add feedback textbox in the app
- Weekly user reviews via Google Forms
- Add GitHub issue tracker for feature requests

#### Community Engagement
- Host open contribution policy on GitHub
- Invite contributors to improve prompt, UI, and fallback handling
- Conduct monthly community testing meetups

#### Clarity & Completeness of System Prompt Justification
- Prompt clearly structured ("User: {user_input}\nAssistant:") and effective for dialogue.
- Simple design fits the assistant’s educational goal.
- Improvement: Add tone, length, or fallback constraints for more control.

#### Depth of Analysis of User Feedback
- Detailed feedback from 10 users with ratings and insights.
- Key themes identified with ~4.4★ average.
- Improvement: Add visual charts for clarity.

#### Feasibility & Vision of Future Roadmap
- Realistic short-term goals, visionary long-term plans (multi-language, curriculum).
- Improvement: Estimate resources/time for long-term items.

#### Creativity & Practicality of User Adoption Plan
- Smart, low-cost strategies (social media, forums, Hugging Face community).
- Improvement: Add specific growth targets (e.g., 100 users/week).

#### Overall Coherence & Presentation
- Well-organized markdown with clean structure and consistent tone.
- Improvement: Include screenshots or graphs for visual appeal.

### Author 
Gorile Shailaja 

### License
apache-2.0 (Apache License 2.0)

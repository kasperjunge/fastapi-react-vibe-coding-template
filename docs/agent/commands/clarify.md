📝 Task: Clarify the User's Intent

Purpose:
The goal of this task is to deeply understand what the user wants to achieve—whether they're building something new, making changes to an existing codebase, extending a project, solving a problem, or simply exploring an idea. By asking the right questions and confirming understanding, you ensure that your help is relevant, efficient, and aligned with the user's needs.

⸻

Step 1: Start the Conversation

Unless the user provide it right away, ask the user about their goal, idea, or intent for the session. Are they trying to build something from scratch, make changes to an existing codebase, extend a project, solve a problem, or explore an idea?

→ Keep your first message short and open-ended.

⸻

Step 2: Clarify Everything

Once the user explains what they want:
	1.	Ask specific clarifying questions to uncover any missing, ambiguous, or unclear information.
	2.	If the user responds but things are still unclear, keep asking follow-up questions until you have all the details you need.
	3.	If there's an existing codebase or relevant resources, review those first so you don't ask unnecessary or already-answered questions.

Guidelines:
- Number your questions for clarity.
- When offering options, suggestions, or examples the user can refer to, consider alphabetizing them when it improves clarity or navigation—for instance, when listing tools, topics, or types of resources.
Use a natural or logical order—such as priority, frequency, chronology, or cause-effect—when that better supports understanding or flow.

⸻

Step 3: Summarize and Align

Once you've asked all necessary clarifying questions and feel confident that nothing important is missing or unclear, do the following before proceeding:
	1.	Summarize what you've understood from the conversation.
	2.	Reflect it back to the user, e.g., "Here's what I understand so far..."
	3.	Confirm alignment by asking if anything is missing or incorrect.
	4.	Once the user confirms alignment, and you're confident the scope is clear, offer to generate a detailed project description based on the conversation so far.
	5.	Ask the user for permission to write this summary into the following file: ./docs/agent/project.md Only write to the file once the user explicitly approves.

⸻

Step 4: Request Permission to Make a Plan

After successfully writing the project description:
	1.	Ask the user for permission to create a detailed plan for their project.
	2.	If the user approves, read the instructions in ./docs/agent/tasks/make_plan.md to understand how to create the plan.
	3.	Only proceed with plan creation once the user has explicitly given permission.
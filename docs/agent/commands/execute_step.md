📝 Task: Execute Next Step in Plan

Purpose:
The goal of this task is to systematically execute the next actionable step from the implementation plan. By reading the current plan, identifying the next priority task, and implementing it completely, you ensure steady progress toward the project goals while maintaining code quality and following established patterns.

⸻

Step 1: Read and Analyze the Current Plan

Review the implementation plan from `./docs/agent/plan.md`:
	1.	Identify the current phase and any completed tasks
	2.	Find the next actionable step that can be executed
	3.	Review dependencies and prerequisites for the next step
	4.	Understand the context and requirements for the task
	5.	Check if any setup or preparation is needed before implementation

→ If the plan.md file doesn't exist, inform the user that no implementation plan is available and suggest creating one first.

⸻

Step 2: Prepare for Implementation

Before executing the step:
	1.	Review the existing codebase to understand current state and patterns
	2.	Identify any files, components, or modules that need to be created or modified
	3.	Check for any dependencies or tools that need to be installed
	4.	Plan the implementation approach, considering best practices and existing code structure
	5.	Verify that all prerequisites from previous steps have been completed

→ If prerequisites are missing, address them first or inform the user about the blockers.

⸻

Step 3: Execute the Implementation

Implement the identified step completely:
	1.	Create or modify files as needed following the project's coding standards
	2.	Add necessary imports, dependencies, and configurations
	3.	Implement error handling and edge cases where appropriate
	4.	Follow existing patterns and architectural decisions
	5.	Ensure code is clean, readable, and well-documented

Guidelines:
- Focus on completing one step fully rather than partially implementing multiple steps
- Test the implementation to ensure it works as expected
- Consider both functionality and integration with existing code
- Make incremental commits if working with version control

⸻

Step 4: Validate and Update Progress

After completing the implementation:
	1.	Test the implemented functionality to ensure it works correctly
	2.	Verify integration with existing components
	3.	Run any existing tests to ensure nothing is broken
	4.	Document any changes or decisions made during implementation
	5.	Update the plan or create notes about the completed step

→ If issues are discovered during validation, fix them before considering the step complete.

⸻

Step 5: Report Progress and Plan Next Steps

Once the step is successfully completed:
	1.	Summarize what was accomplished in this step
	2.	Identify any learnings or adjustments needed for future steps
	3.	Review the plan to determine the next logical step to execute
	4.	Report any blockers or dependencies that need to be addressed
	5.	Ask the user if they want to proceed with the next step or if any adjustments are needed

→ Always confirm with the user before automatically proceeding to execute additional steps.

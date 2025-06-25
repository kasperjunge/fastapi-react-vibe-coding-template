📝 Task: Create Implementation Plan

Purpose:
The goal of this task is to transform a project description into a detailed, actionable implementation plan. By analyzing the project requirements, technical specifications, and existing codebase, you create a structured roadmap that breaks down the work into manageable phases, tasks, and subtasks.

⸻

Step 1: Analyze the Project Description

Read and thoroughly understand the project description from `./docs/agent/project.md`:
	1.	Identify the main objectives and scope
	2.	Review the technical stack and requirements
	3.	Understand existing infrastructure and what needs to be built
	4.	Note any constraints, dependencies, or specific requirements
	5.	Assess the current state and what's already implemented

→ If the project.md file doesn't exist, inform the user that no project description is available and ask them to provide one first.

⸻

Step 2: Create a Structured Implementation Plan

Based on the project description, create a comprehensive plan that includes:

**Phase Breakdown:**
	1.	Organize work into logical phases (e.g., setup, core features, integration, polish)
	2.	Ensure phases build upon each other logically
	3.	Consider dependencies between different components

**Task Organization:**
	1.	Break each phase into specific, actionable tasks
	2.	Include both frontend and backend work where applicable
	3.	Prioritize tasks based on dependencies and importance
	4.	Estimate complexity levels (simple, moderate, complex)

**Technical Considerations:**
	1.	Review existing codebase structure and patterns
	2.	Identify reusable components or services
	3.	Plan for proper error handling and edge cases
	4.	Consider testing requirements

Guidelines:
- Use clear, action-oriented language for each task
- Include specific file paths and component names where known
- Consider both development and deployment aspects
- Plan for iterative development and testing

⸻

Step 3: Validate and Present the Plan

Before presenting the final plan:
	1.	Cross-reference with the project description to ensure nothing is missed
	2.	Verify the logical flow and dependencies between phases
	3.	Check that the plan addresses all stated requirements and success criteria
	4.	Ensure the plan is realistic and achievable given the existing infrastructure

Present the plan with:
	1.	A clear overview of all phases
	2.	Detailed breakdown of tasks within each phase
	3.	Notes on dependencies and prerequisites
	4.	Recommendations for getting started
	5.	Save the complete plan to `./docs/agent/plan.md` for future reference

→ After presenting the plan, ask the user if they'd like to proceed with implementation or if any adjustments to the plan are needed.

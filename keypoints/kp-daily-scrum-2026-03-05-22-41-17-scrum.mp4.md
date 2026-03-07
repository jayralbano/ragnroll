# Keypoints

**Source:** `2026-03-05 22-41-17 scrum_transcribed.txt`

### 1. Adam and Jamal joining scrums to streamline workflow

Adam announces that he and Jamal are now joining the daily scrums to help move the workflow along. Their primary role is to clean up the backlog by removing outdated tickets, bugs, and features that no longer matter, so devs can stay focused on what counts. Adam emphasizes they are not there to babysit but to reduce noise, act as a resource for the team, and help resolve priority conflicts by coordinating with Asim and Andrew on business decisions.

### 2. Support ticket review and triage with Jamal

Jamal presents a list of open support tickets for triage: 6919 (iOS autoplay failing, assigned to Marius for research), 7046 (active subscription filter not showing members), 5980 (Malaysian language causing co-pilot to get stuck on "data still processing"), 6687 (canceled filter not showing all members), 6852 (rewards page not loading for multiple users), 7007 (videos stuck in transcribing with no front-end error), 7237 (AI chat pulling blank paragraphs and incorrect numbering, Marcus working on prompt fix), and 7343 (outdated Zapier triggers, newly raised). Adam stresses the need for devs to update tickets with progress so the team has visibility without waiting for scrum.

### 3. Developer roundtable — active tickets and status updates

Each team member reports their current work: Marco is on 5541, 5113 (related hub UI tasks), and 7036 (onboarding skip-without-AI behavior). Alkein finished a HubSpot fix on 7155 and is moving to global navigation for the Mio homepage. Atanas is doing Kubernetes cluster maintenance. Claudiu QA-passed 5113 (Marco) and 7332 (Mihai, also validated with AI automation testing), and needs 5541 pushed to a Chargebee-connected test environment. Jake flags 7342 (activity data mismatch post-production push) needing further investigation with Jayr. Jayr is working on the notification system with six tickets done code-wise, now auditing and testing with Claude. Marcus is tweaking prompts on 7237 (AI chat issue for an enterprise client), migrating apps to in-house builds (7320), and integrating the mobile app builder (7017, 7016). Marius is researching the iOS autoplay issue (6919). Mihai finished 7332 (duplicate pages across hubs) and 7319 (stale image fix needing a Laravel command run on production). Milan reviews design tasks including 6992 (inline editor when page is hidden), 6919 (muted autoplay UX), 7296 (notification system rework designs shared with Jayr), and 7039 (space access visibility model). Sherry is rewriting the entire test case suite with updated steps to reproduce. SK pushed 6225 and 6389 to production, is working on 7359 (follow-up from Claudiu), and found the root cause for 7046 (two audiences not updated).

### 4. Asim on transitioning to new direction and adding context to Jira tickets

Asim wraps up the scrum by acknowledging the team is in maintenance mode for now but stresses the need to start forking toward a new way of working, with a collective transition meeting tentatively planned for Monday. He asks everyone to immediately start adding more context to Jira tickets — research notes, thought processes, and progress updates as comments — since this visibility benefits support, QA, and will be critical for future AI agent integration. Adam echoes the message, asking the team to bring blockers to him proactively rather than waiting for scrum.

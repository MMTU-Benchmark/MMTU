# Projects

Each subdirectory is a project with:
- `CLAUDE.md` — goal, status, key decisions
- `experiments.md` — chronological log of experiments & results

To start a new project: create a directory under `projects/` and add both files.

## experiments.md format

Each entry is a dated section appended chronologically:

```markdown
## YYYY-MM-DD — Short description

**Goal:** What you were trying to achieve or test

**Setup:**
- Model: <model name>
- Config: <config file or parameters>
- Other relevant settings

**Results:**
- Key metrics (accuracy, F1, etc.)
- Notable observations

**Takeaways:**
- What was learned
- Next steps or follow-ups
```

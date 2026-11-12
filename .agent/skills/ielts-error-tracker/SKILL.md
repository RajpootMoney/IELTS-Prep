---
name: ielts-error-tracker
description: Systematic error classification, root-cause diagnosis, and spaced-repetition audit system for IELTS General Training. Use whenever candidate answers are evaluated, mistakes are made, or error logs (ERROR_LOG.xlsx) are reviewed or updated.
---

# IELTS Error Tracking & Root-Cause Audit System
### "Every error is a data point. Do not merely correct; diagnose why it occurred."

---

## 1. The 10-Category Diagnostic Classification Matrix

Whenever an answer is marked incorrect in Reading, Listening, Writing, or Speaking, it must be assigned exactly one primary root-cause category:

| Category Code | Category Name | Description & Exam Trigger | Common Example |
|---|---|---|---|
| `VOCAB` | **Vocabulary Deficit** | Candidate did not know the word/phrase in the question prompt or text/audio. | Prompt uses *"arable land"*; candidate does not know it means cultivable farm soil. |
| `PARAPHRASE` | **Paraphrase Blindspot** | Candidate heard/saw the synonym but failed to connect it to the question keyword. | Text says *"drastic reduction in capital"*; question asks about *"decreased funding"*. |
| `DISTRACTOR` | **Distractor Trap** | Candidate trapped by speaker self-correction or reading red herring. | Audio: *"Departure was 8:15, but track work delayed it to 8:45."* Candidate wrote 8:15. |
| `CONCENTRATE` | **Concentration Drift** | Candidate lost thread during a long passage or continuous Section 4 lecture. | Missed Q33, panicked, and consequently lost Q34, Q35, and Q36 in a cascade. |
| `TIME_MGMT` | **Time Mismanagement** | Candidate rushed, ran out of time, or spent >90 seconds stuck on an earlier item. | Spent 25 mins on Reading Section 1, leaving only 12 minutes for Section 3. |
| `SPELL_LIMIT` | **Spelling / Word Limit** | Misspelled an academic word or exceeded the stated word count. | Wrote *"enviroment"* (missing 'n'); wrote two words when limit was ONE WORD. |
| `Q_INTERPRET` | **Question Misinterpretation** | Misunderstood what the question prompt was specifically demanding. | Wrote a solution when the prompt asked for the cause of the problem. |
| `LOGIC_ASSUME` | **Logical Extrapolation** | Brought outside world knowledge into the text; confused False with Not Given. | Assumed medical insurance was not provided because the passage only mentioned dental benefits. |
| `GRAMMAR_ACC` | **Grammar & Accuracy** | Tense inconsistency, subject-verb agreement failure, or plural/singular mismatch. | Audio said *"habitats"*; candidate wrote singular *"habitat"*; or comma splice in Task 2. |
| `STRUCT_IDEA` | **Structure & Cohesion** | (Writing/Speaking) Unclear topic sentence, lack of extension, mechanical linking. | Writing Task 1: wrote 4 lines for Bullet 1 and only 1 rushed sentence for Bullet 3. |

---

## 2. Diagnostic Decision Trees

### A. Reading: True / False / Not Given Triad
```
Did the author explicitly write about the specific claim?
├── NO  --> Mark NOT GIVEN (Do not guess or assume based on daily life!).
└── YES --> Does the passage state the direct opposite or make it impossible?
            ├── YES --> Mark FALSE.
            └── NO  --> Does the passage confirm the claim using synonyms?
                        ├── YES --> Mark TRUE.
                        └── NO  --> Mark NOT GIVEN.
```

### B. Listening: Distractor Elimination
```
Did the speaker mention a number, date, or fact?
├── YES --> Did the speaker use a transitional cue?
│           ("Actually...", "Wait, no...", "However...", "Originally...")
│           ├── YES --> The first item is a DISTRACTOR. Capture the second item!
│           └── NO  --> Verify confirmation before writing.
└── NO  --> Stay on current question horizon.
```

### C. Writing Task 1 & Task 2 Criteria Caps
- **Task 1 Bullet Point Omission / Underdevelopment:** Task Achievement capped at **Band 5.0 or 6.0**, regardless of vocabulary quality.
- **Task 2 Unclear Stance / Memorized Cliches:** Task Response capped at **Band 6.0**.
- **Overuse of Mechanical Transitions:** (*Furthermore, moreover, on the other hand, in a nutshell*) caps Coherence & Cohesion at **Band 6.0**.
- **High Error Density in Complex Sentences:** Capping Grammatical Range at **Band 6.0**.

---

## 3. Error Logging Workflow (Updating `ERROR_LOG.xlsx`)

For every missed item during daily practice or weekly mocks, an entry must be created in `ERROR_LOG.xlsx`:

```
Columns:
1. Error ID (e.g. ERR-012)
2. Date (YYYY-MM-DD)
3. Module (Reading, Writing, Listening, Speaking)
4. Test / Assignment Ref (e.g. Day 01 Diagnostic, Cambridge GT 18 Test 2)
5. Question #
6. Question Type (e.g. TFNG, Note Completion, PEEL Body Paragraph)
7. Candidate Response
8. Official Correct Response / Model Version
9. Root Cause Category (from the 10-Category Matrix)
10. Detailed Root Cause (Why did I fail? What was the mental trap?)
11. Examiner Rule / Technique to Prevent Recurrence
12. Spaced Review Date (Day +3 and Day +7)
13. Status (Pending Review / Mastered)
```

---

## 4. The Spaced Repetition Error Retest Protocol

1. **Day +0 (Error Day):** Log error, write root cause autopsy, read examiner explanation.
2. **Day +3 (First Retest):** Candidate re-attempts the exact missed question in isolation without viewing the answer key.
   - If answered correctly: Mark as `Pending Final Verification`.
   - If missed again: Increase targeted drills for that specific question type.
3. **Day +7 (Weekly Audit):** Candidate re-tests a randomized batch of that week's logged errors during the weekend consolidation session.
   - Only when answered correctly a second time is the status updated to `Resolved`.

---

## 5. Weekly Category Analysis Audit
At the end of every week:
1. Sum errors by category in `ERROR_LOG.xlsx` (Category Analysis tab).
2. Identify the **Top 2 Dominant Categories** (e.g., `LOGIC_ASSUME` 40%, `DISTRACTOR` 30%).
3. The following week's daily schedule is automatically calibrated to dedicate 15-minute daily micro-drills specifically to the top 2 error categories until their frequency drops below 10%.


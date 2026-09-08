# BIS (1838) Testing — New Prompt Round

**Important note on this round:** t
 BBIS_01 and BBIS_04/05 ran on `gemini-3.6-flash`, while BBIS_02/03 ran on
`gemini-3.5-flash-lite` (switched mid-round to save quota). Any behavioural
differences between tests could be the model change.

---

## Biggest finding: placeholder elective codes may break a core product feature

The new prompt explicitly instructs: *"Electives are 18 CP (3 subjects) at
200/300-level... Do not make up elective subjects. Write Elective 1 (300 lv)
etc."* and the same for the No-Major Path.

BBIS_01's output followed this literally — all four Y3 CSIT electives came back
as `CSIT Elective 1`, `CSIT Elective 2`, etc., not real subject codes.

Per the A4 document, one of Courseo's completed MVP features is that clicking a
subject card opens its real UOW handbook page. A placeholder code like
`CSIT Elective 1` has no real handbook page - **this would break that feature for
every generic elective slot**, not just an edge case. This is a bigger issue than
a wording bug; it's a direct conflict between this prompt's design and a feature
already shipped and documented as working.

Behaviour was inconsistent, though: BBIS_02 (same underlying rule) returned real
subject codes (ISIT212, CSIT302, ISIT332, CSCI251) instead of placeholders, while
BBIS_03 reverted to placeholder-style codes again (`CSCI3nn`, `CSCI2nn`). So the
model doesn't reliably follow the "use placeholders" instruction either - worth
raising to the team as a design decision to make explicitly (real codes vs
placeholders), not something to leave to chance.

---

## BBIS_01 — First year, no major

**Test data sent:** the full BBIS_01 block 

**Turn 1 (metadata-only follow-up) result:** produced a full plan.
- CP Summary correctly separates "Completed: 0" from "24 CP currently enrolled"
  - this is actually **better** than the old prompt's audit-mismatch bug; the new
  prompt's stricter ledger structure seems to have fixed that specific issue.
- Session availability for CSIT123/CSIT114 (Autumn-only) matches the handbook.
- **New discrepancy:** MGNT110 is stated as available "Autumn, Spring, Summer" -
  the scraped handbook data says Spring only. This is the *second* time a
  response has claimed Autumn availability for MGNT110 (the previous round's
  FU-01 also claimed "both Autumn and Spring"). 
- Y3 electives returned as placeholder codes (see finding above).

**Status:** Partial / inconclusive on Turn 1 due to the test-data artifact.
Turn 2 plan is structurally sound but has the MGNT110 session claim and
placeholder-elective issues.

---

## BBIS_02 — Second year, no major

**Result:** produced a full plan on the first real turn (after the initial
generic greeting, same pattern as BBIS_01 - worth checking whether that greeting
is now an automatic first message before any user input is even processed,
rather than a response caused by anything in the data).

- CP Summary: 78 completed + 18 enrolled + 48 remaining = 144. Correct, and
  cleanly separated (no repeat of the old audit-mismatch bug).
- Y3 electives this time returned as **real subject codes** (ISIT212, CSIT302,
  ISIT332, CSCI251), contradicting BBIS_01's placeholder behaviour on the
  identical underlying rule.
- ISIT224 named "Information Systems in Organisations" here vs "Management
  Information Systems" in the previous round's tests on the same code - subject
  naming is still inconsistent between runs, same pattern as before.

**Follow-ups (ROB-style), all correct:**
- 5-subject overload correctly refused, cites the 4-subject/24cp cap.
- MARK101/MARK213 correctly identified as the same subject and refused as a
  double-count - consistent with the previous round's finding on this.
- CSIT321-before-CSIT226 correctly refused, correctly cites CSIT226 as a
  corequisite.

**Status:** Pass overall - real elective codes this time, correct CP math,
correct rule-conflict handling on all three follow-ups.

---

## BBIS_03 — Last year, no major

**Result:** produced a plan reaching 144 CP for the visible subject table
(verified by re-adding: 48+24+24+24+12+12=144, matches).

**Bug found:** the CP Summary separately states **"Excess / Non-awarded: 18 CP"**
- but this number doesn't correspond to anything in the actual subject list.
Recomputing the intended breakdown (48 Y1 + 30 Y2 core + 6 CSIT314 + 24 Business
Electives + 24 CSIT Electives = 132, matching "Completed: 132") leaves no excess
at all - every subject in the table is accounted for in the 144 total with
nothing left over. This "Excess: 18 CP" figure appears to be an orphaned,
unexplained number - the same class of bug as the old prompt's audit-CP
mismatch (a labelled total that doesn't match the real breakdown), just showing
up on a different field this time.

**Also noted:** the mock data's original wording (132 CP complete, only 3
elective subjects explicitly named) was itself slightly under-specified - the
agent correctly inferred and added a 4th elective to make the totals work,
which is reasonable handling of ambiguous input, though it used a placeholder
code (`CSCI2nn`) for it rather than flagging the ambiguity to the student.

**Status:** Partial - subject list and 144 total are correct, but the "Excess"
figure in the summary is wrong and unexplained.

---

## BBIS_04 — Data-quality variant

**Re-run with the corrected code** ("1838 Wollongong CSIT110 P 2024 CSIT115 P
2024 CSIT121 P 2024 CSIT214 P 2025 CSIT205 P 2025 ECON100 P 2025"):

The agent again asked for commencement year, campus, degree code, and major -
despite course code (1838) and campus (Wollongong) both being stated in plain,
unambiguous text at the start of the message. This is the real finding the test
was designed to surface: the agent doesn't reliably parse a terse, unlabelled
SOLS-style format the way it parses the labelled format ("Commencement year:
2026, course 1838...") used in every other test in this batch.

Worth separating what's reasonable to ask about from what isn't:
- **Reasonable:** major (genuinely never stated - absence isn't the same as "no
  major") and commencement year (2024 is the earliest year present but never
  explicitly labelled as the commencement year, so confirming rather than
  assuming is defensible).
- **Not reasonable:** re-asking for course code and campus, since both were
  explicitly present in plain text. This part is a genuine parsing gap, not
  appropriate caution.

**Status:** Fail. Confirms a real parsing gap for terse/unlabelled input,
distinct from the earlier confounded attempt.

---

## BBIS_05 — Missing course details

**Result:** correctly asked for commencement year, campus, degree, and major
before producing anything - consistent with the previous round's OMIT-01 pass.

**Status:** Pass.

---

## Summary

Of 5 planned tests, BBIS_01's first turn is confounded by accidentally-included
test annotations (see below). Of the results that are clean:

- **BBIS_02: Pass** (plan + all 3 follow-ups correct)
- **BBIS_05: Pass**
- **BBIS_03: Partial** (spurious "Excess" CP figure)
- **BBIS_01: Partial** (MGNT110 session claim, placeholder electives)
- **BBIS_04: Fail** (doesn't parse a terse/unlabelled format even when the
  course code and campus are both stated correctly and in plain text)

## Takeaways

1. **The new prompt appears to have fixed the old "Total CP received" audit
   mismatch bug** - every test here that reached a plan correctly separated
   Completed / Enrolled / Remaining. This is a genuine improvement over the
   prompt tested in the previous round.

2. **A new, different CP-math bug has appeared in its place**: the "Excess /
   Non-awarded" field can show a number unconnected to the actual subject list
   (BBIS_03). Same category of bug as before (orphaned audit figure), different
   specific field.

3. **Placeholder elective codes are the most consequential open issue.** The
   prompt explicitly tells the model to invent placeholder labels for generic
   electives rather than real subject codes, which directly conflicts with the
   "click a subject to open its real handbook page" feature already documented
   as working in A4. Behaviour is inconsistent besides - real codes appeared in
   BBIS_02 but not BBIS_01 or BBIS_03 on the same underlying rule. This is worth
   raising with the team as a design decision, not just a bug: does BIS actually
   want placeholder elective slots, or real suggested subjects?

4. **MGNT110's stated session availability (Autumn+Spring+Summer) contradicts
   the scraped handbook (Spring only)**, and this is the second time across two
   different prompt versions that Autumn availability has been claimed for this
   subject. Worth a direct check with Han on whether the seeded subject data
   actually changed, since if the seed data itself says Spring-only and the
   model is contradicting it twice independently, that's a more concerning
   pattern than a one-off hallucination.

5. **Confirmed real parsing gap for terse/unlabelled SOLS-style input** (BBIS_04,
   clean re-run). The agent handles clearly labelled input ("Commencement year:
   X, course Y...") reliably across every other test in this batch, but asked
   for course code and campus again when they were present but unlabelled in a
   compact paste-style format. Since real students copy-pasting from SOLS are
   more likely to produce compact/unlabelled data than neatly labelled
   sentences, this is worth prioritising - it's arguably more representative of
   real usage than the labelled-format tests that make up most of this batch.


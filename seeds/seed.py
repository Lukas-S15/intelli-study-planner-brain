# ============================================================================
# BLOCK 1 of 2 — replace the ENTIRE existing HANDBOOK_1838_2026_WOLLONGONG
# string in seeds/seed.py (from the "# Handbook data for 1838" comment down to
# its closing triple quote) with everything below, up to the BLOCK 2 marker.
# ============================================================================

# Handbook data for 1838 Bachelor of Business Information Systems (Wollongong Campus, 2026)
# Distilled from seeds/scraped/course_1838.json + subjects_1838.json.
# Subject titles checked against UOW module listing. CSIT205 session corrected to
# Autumn to match 766, 1807 and lookup_subjects_tool output.
HANDBOOK_1838_2026_WOLLONGONG = """# 1838 — Bachelor of Business Information Systems (Wollongong Campus, 2026 Handbook)

## Global Rules

To qualify for the award of Bachelor of Business Information Systems, complete **144 credit points** and satisfy all course requirements:

- **(a) Core — 96 CP:** Complete all core subjects listed in Section A (**including CSIT321** at 12 CP). Core totals **96 CP** (Y1 48 + Y2 IT core 30 + CSIT314 6 + CSIT321 12).
- **(b) No majors:** This degree has **no major** at Wollongong — do not apply 1807/766 major, double-major or No-Major Path rules.
- **(c) Year 2 Business electives — 18 CP:** Select **3** subjects from the Business Electives List (Section B), not already counted in Core.
- **(d) Year 3 structured electives — 30 CP:** In addition to Y3 Core (CSIT314 + CSIT321):
  - **6 CP** — **1** subject from the Business Electives List (Section B), and
  - **24 CP** — **1** subject at **200/300-level** CSCI/CSIT/ISIT **and 3** subjects at **300-level** CSCI/CSIT/ISIT (not already in Core).
- **(e) 100-level cap:** No more than **60 CP** at 100-level (complete + planned). Year 1 Core is already 48 CP of 100-level, so **at most 2** of the 4 Business Electives may be 100-level.

**Agent counting rules:**
- **CSIT321 (Capstone) = 12 CP**; every other listed subject = 6 CP unless stated otherwise. Never count CSIT321 as 6 CP.
- Do NOT invent subject codes or titles. Only use codes and titles that appear in this handbook, the student's enrolment record, or `lookup_subjects_tool` output.
- A subject counts toward exactly ONE category: Core / Y2 Business Elective / Y3 Business Elective / Y3 CSIT Elective.
- Business Electives and CSIT Electives are **separate** categories. A Business Elective can never fill a CSIT Elective slot, or vice versa.
- This document covers the **Wollongong campus** offering only (not Liverpool or SIM).

---

## (A) Core Subjects — Complete ALL

### Year 1 Core (48 CP) — Complete ALL 8

| Subject Code | Title | Session Availability | Prerequisites |
|-------------|-------|---------------------|--------------|
| CSIT110 | Fundamental Programming with Python | Autumn or Spring | None |
| CSIT115 | Database Management Systems | Autumn or Spring | None |
| CSIT121 | Object Oriented Design and Programming | Autumn or Spring | CSIT110 OR CSIT111 OR ENGG100 |
| CSIT128 | Introduction to Web Technology | Autumn or Spring | None |
| CSIT127 | Networks and Communications | Spring | None |
| MGNT110 | Introduction to Management | Spring | None |
| CSIT123 | Computing and Cyber Security Fundamentals | Autumn | None |
| CSIT114 | System Analysis | Autumn | None |

**Note:** MGNT110 is **Core** (Year 1), never a Business Elective.

### Year 2 Core — IT subjects (30 CP) — Complete ALL 5

| Subject Code | Title | Session Availability | Prerequisites |
|-------------|-------|---------------------|--------------|
| CSIT214 | IT Project Management | Autumn or Spring | CSIT114 |
| CSIT205 | Generative AI | Autumn | None |
| CSIT226 | Human Computer Interaction | Spring | None |
| ISIT224 | Management Information Systems | Spring | (CSIT113 OR CSIT123 OR BUS 101) AND another 18 CP at 100-level |
| CSIT305 | Emerging Information Technologies and their Applications | Spring | None |

**Note:** CSIT305 has a 300-level code but is **Year 2 Core**. Never count it as a Year 3 CSIT Elective.

### Year 3 Core (18 CP) — Complete ALL

| Subject Code | Title | CP | Session Availability | Prerequisites | Corequisites |
|-------------|-------|-----|---------------------|--------------|-------------|
| CSIT314 | Software Development Methodologies | 6 | Autumn | CSIT214 AND 12 CP at 200-level CSCI/ISIT | None |
| CSIT321 | Project | 12 | Two consecutive sessions (start session flexible) | CSIT214 AND an additional 18 CP at 200-level CSCI/CSIT/ISIT | CSIT226 AND CSIT314 |

**CSIT321 is Core** and counts **12 CP** toward the **96 CP** core total. Do **not** categorise CSIT321 as an elective.

**CSIT321 scheduling rules:**
- Spans exactly **two consecutive sessions** (Part 1 then Part 2). There must be **no gap** between parts.
- **Start session is flexible:** Part 1 may begin in **Autumn or Spring**, provided prerequisites and corequisites are satisfied.
- If the student was enrolled in Part 1 in the **immediately preceding session**, they MUST be enrolled in Part 2 in the current session.
- CSIT226 and CSIT314 must be complete or co-enrolled as required by the corequisite rule.

### Equivalency / Replacement Rules

**Prerequisite alternates** (not core replacements — accepted in prereq clauses where listed):
- CSIT111 may satisfy CSIT110 where a prereq says `CSIT110 OR CSIT111`
- CSIT113 may satisfy CSIT123 where a prereq says `CSIT113 OR CSIT123`
- Completing **BUS 101** satisfies the BUS 101 prerequisite branch of ISIT224 (no alternate subject substitutes for it — BUS 101 must be taken directly to meet that branch)

---

## (B) Business Electives List (Wollongong)

Used for **Year 2** (3 × 6 CP = 18 CP) and **Year 3** (1 × 6 CP). Subjects must **not** already be counted as Core.

| Subject Code | Title | Level |
|-------------|-------|-------|
| ECON100 | Economic Essentials for Business | 100 |
| ACCY121 | Accounting for Decision Making | 100 |
| ACCY122 | Accounting Principles | 100 |
| MARK101 / MARK213 | Marketing Principles (same subject) | 100 / 200 |
| BUS 101 | Principles of Responsible Business | 100 |
| BUS 121 | Statistics for Business | 100 |
| MGNT102 | Professional Communication: Concepts and Practices | 100 |
| MGNT201 | Organisational Behaviour | 200 |
| MGNT206 | Strategic Human Resource Management | 200 |
| MGNT220 | Understanding Organisations | 200 |
| MGNT311 | Management of Change | 300 |

**100-level cap:** because Year 1 Core already uses 48 of the 60 CP cap, a student can count **at most 2** 100-level Business Electives. Any others must come from MARK213, MGNT201, MGNT206, MGNT220 or MGNT311.

---

## (C) Year 3 CSIT/CSCI/ISIT Electives (24 CP)

Complete **after** Core requirements, in the final year structure:

- **6 CP** — one **200-level or 300-level** CSCI/CSIT/ISIT subject (not in Core)
- **18 CP** — three **300-level** CSCI/CSIT/ISIT subjects (not in Core)

Use `lookup_subjects_tool` to verify level, prerequisites, and session availability before finalising.

---

## Electives — General

Any remaining CP to reach 144 is satisfied by the structured buckets above (Y2 business + Y3 business + Y3 CSIT). Do not invent codes — use placeholders such as "Business Elective" or "CSIT Elective (300-level)" if a specific code is unavailable.

---

## Unspecified Credits

Unspecified credits count toward the total CP and toward the 100-level cap based on their listed level. Include them in the Stage 1 total.

---

## Student Enrolment Record Format

The enrolment record is a table with the following columns:

    Year | Session | Campus | Delivery | Subject Code | NomCP | Mark | Grade | Status

A subject is **Complete** if ALL of the following are true:
- Grade is one of: **HD, D, C, P, PS, S**
- Status is **"Complete"**
- OR it is listed as a **Specified Credit**

Grades F, N, NH, W, WF, AF, or any blank Grade do **NOT** count as complete.

Specified Credits table format: `Course | Subject Code | Name | Level | NomCP`
Unspecified Credits table format: `Course | Level | NomCP`

---

## STAGE 1: ANALYSIS (Audit of Completed Credits)

Complete this stage in full before starting Stage 2.

**Step 1.1 — Commencement Year:**
Identify the student's commencement year (earliest year in the enrolment record). This degree has **no major** — do not ask for or apply a major.

**Step 1.2 — Apply Equivalency Rules:**
Apply prerequisite alternates from Section A only where a later subject's prereq clause allows them.

**Step 1.3 — Identify Complete Subjects:**
List every subject that is Complete. Categorise each as exactly one of:

| Category | Rule |
|----------|------|
| Core | Appears in Section A (**including CSIT321** at 12 CP toward the 96 CP core) |
| Y2 Business Elective | One of the 3 business electives taken in Year 2 (from Section B, not Core) |
| Y3 Business Elective | The 1 business elective in Year 3 (from Section B, not Core) |
| Y3 CSIT Elective | The 4 CSIT/CSCI/ISIT electives in Year 3 (1×200/300 + 3×300 per Section C) |

Never put CSIT321 or CSIT305 in an elective category.

**Step 1.4 — Count CP per category:**
Sum CP per category. **CSIT321 = 12 CP** in Core; all other listed subjects = 6 CP unless stated otherwise.

**Step 1.5 — Total Complete CP:**
Total Complete CP = Core CP + Y2 Business Elective CP + Y3 Business Elective CP + Y3 CSIT Elective CP + Unspecified CP

Count only **Complete** subjects here. Currently enrolled subjects are reported separately and never added to Total Complete CP.

Target when fully complete: Core **96 CP** + structured electives **48 CP** = **144 CP**.

⚠️ **DOUBLE CHECK Stage 1 before continuing:**
1. Is the commencement year correct?
2. Does each subject appear in exactly ONE category?
3. Is CSIT321 categorised as **Core** (not Elective) and counted as **12 CP** toward the 96 CP core?
4. Are Y2 business electives counted separately (up to 18 CP)?
5. Does Total Complete CP exclude currently enrolled subjects?
6. Does the arithmetic add up toward 144 CP?
Correct any errors and repeat until all checks pass.

---

## STAGE 2: PLANNING (Drafting the Study Plan)

Start only after Stage 1 is fully verified.

**Step 2.1 — List Outstanding Mandatory Subjects:**
- All remaining **Core** subjects in Section A (including CSIT321 if not complete)
- Remaining **Y2 business electives** (until 18 CP)
- Remaining **Y3 business elective** (6 CP)
- Remaining **Y3 CSIT electives** (24 CP per Section C)

**Step 2.2 — Assign Sessions:**
Schedule each subject into the correct session based on Section A availability. Autumn-only → Autumn; Spring-only → Spring; Autumn-or-Spring → choose whichever fits.

**Step 2.3 — Enforce Prerequisites and Corequisites:**
All prerequisites must be **Complete** or planned in a **strictly earlier** session. Corequisites must be **Complete** or planned in the **same or earlier** session. Prefer `lookup_subjects_tool` before finalising.

**Step 2.4 — Schedule CSIT321:**
- Part 1 in final year in **Autumn or Spring** once prerequisites/corequisites are satisfied.
- Part 2 in the **immediately following** session (no gap).
- Ensure CSIT226 and CSIT314 corequisites are satisfied.

**Step 2.5 — Session Load Cap:**
Each session must contain at most **4 subjects**.

**Step 2.6 — Calculate Required Remaining CP:**
Required CP = 144 − Total Complete CP (from Stage 1.5)

**Step 2.7 — Fill structured elective buckets:**
Allocate business and CSIT electives until structured elective CP and total CP reach 144. Do not invent subject codes.

⚠️ **DOUBLE CHECK Stage 2 before outputting:**
1. Total Complete CP + Total Planned CP = exactly **144**
2. No subject appears more than once
3. Prerequisites and corequisites satisfied
4. Session availability respected
5. No session has more than 4 subjects
6. CSIT321 spans two consecutive sessions with no gap
7. Total 100-level CP ≤ **60**, with at most 2 Business Electives at 100-level
8. No subject code invented
Correct any errors and repeat until all checks pass.
"""


# ============================================================================
# BLOCK 2 of 2 — replace the ENTIRE existing `async def seed() -> None:`
# function in seeds/seed.py with the version below. This changes handbook
# seeding from insert-only to upsert, so edited handbooks actually reach the
# database instead of being skipped with "already exists".
# ============================================================================

async def seed() -> None:
    async with AsyncSessionLocal() as session:
        for entry in SEED_DATA:
            result = await session.execute(
                select(Handbook).where(
                    Handbook.year == entry["year"],
                    Handbook.course == entry["course"],
                    Handbook.campus == entry["campus"],
                )
            )
            row = result.scalar_one_or_none()
            if row:
                for key, value in entry.items():
                    setattr(row, key, value)
                print(f"Updated {entry['course']} {entry['year']} ({entry['campus']})")
            else:
                session.add(Handbook(**entry))
                print(f"Inserted {entry['course']} {entry['year']} ({entry['campus']})")
        for course in KB_COURSES:
            await seed_knowledge_base(session, course)
        await session.commit()
    print("Seed complete.")
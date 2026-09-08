"""
WAM (Weighted Average Mark) tools for the study-planner agent.

These follow the same shape as lookup_subjects_tool / lookup_major_tool:
a plain function the LangGraph agent can call, taking simple JSON-serialisable
input and returning a dict with both structured data and a human-readable
"card" string for the LLM to quote back to the student.
"""

from typing import Optional
from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Input schema
# ---------------------------------------------------------------------------

class SubjectMark(BaseModel):
    """
    One subject from the student's enrolment record.

    mark: the numeric mark (0-100) if known. Leave as None for subjects with
    no numeric mark (e.g. Pass/Fail ungraded subjects, exchange credit,
    withdrawals) - these are excluded from the WAM calculation, matching how
    UOW itself excludes ungraded subjects from WAM.
    """
    code: str
    credit_points: int = Field(gt=0)
    mark: Optional[float] = Field(default=None, ge=0, le=100)
    status: str = Field(
        default="Complete",
        description="e.g. 'Complete', 'Enrolled', 'Failed', 'Withdrawn'",
    )


# ---------------------------------------------------------------------------
# Tool 1: calculate current WAM
# ---------------------------------------------------------------------------

def calculate_wam_tool(subjects: list[SubjectMark]) -> dict:
    """
    Calculate a student's current Weighted Average Mark (WAM) from their
    completed, graded subjects.

    WAM = sum(mark_i * credit_points_i) / sum(credit_points_i)
    over only subjects that have a numeric mark and status "Complete".
    Subjects with no mark (Pass/Fail, ungraded, withdrawn, currently
    enrolled) are excluded from both the numerator and denominator - do not
    guess a mark for these.

    Returns a dict with:
      - wam: float | None (None if no gradable subjects found)
      - graded_cp: int - total credit points actually used in the calculation
      - excluded_codes: list[str] - subjects skipped and why
      - card: str - a short markdown summary for the LLM to relay to the student
    """
    graded = [s for s in subjects if s.status == "Complete" and s.mark is not None]
    excluded = [
        f"{s.code} (excluded: {'no numeric mark' if s.mark is None else s.status})"
        for s in subjects
        if not (s.status == "Complete" and s.mark is not None)
    ]

    if not graded:
        return {
            "wam": None,
            "graded_cp": 0,
            "excluded_codes": excluded,
            "card": (
                "No subjects with a numeric mark and 'Complete' status were "
                "found, so a WAM cannot be calculated yet."
            ),
        }

    total_cp = sum(s.credit_points for s in graded)
    weighted_sum = sum(s.mark * s.credit_points for s in graded)
    wam = round(weighted_sum / total_cp, 2)

    card = (
        f"**Current WAM: {wam}**\n"
        f"- Calculated from {len(graded)} graded subjects ({total_cp} CP total)\n"
        + (f"- Excluded from calculation: {', '.join(excluded)}\n" if excluded else "")
    )

    return {
        "wam": wam,
        "graded_cp": total_cp,
        "excluded_codes": excluded,
        "card": card,
    }


# ---------------------------------------------------------------------------
# Tool 2: required average on remaining subjects to hit a target WAM
# ---------------------------------------------------------------------------

def calculate_required_average_tool(
    subjects: list[SubjectMark],
    remaining_credit_points: int,
    target_wam: float = Field(ge=0, le=100),
) -> dict:
    """
    Given a student's current graded subjects and how many credit points of
    graded subjects they have left to take, calculate the average mark they
    would need on those remaining subjects to reach a target WAM.

    remaining_credit_points should be the sum of CP across only the subjects
    that will actually contribute a numeric mark (i.e. exclude Pass/Fail
    ungraded subjects the student still has to take, since those won't
    affect WAM either).

    Formula:
      total_cp = graded_cp (already completed) + remaining_credit_points
      required_average = (target_wam * total_cp - current_weighted_sum) / remaining_credit_points

    Returns a dict with:
      - required_average: float | None
      - feasible: bool - False if required_average > 100 (impossible) or < 0
        (target already exceeded)
      - card: str - markdown summary for the LLM to relay to the student
    """
    graded = [s for s in subjects if s.status == "Complete" and s.mark is not None]
    graded_cp = sum(s.credit_points for s in graded)
    current_weighted_sum = sum(s.mark * s.credit_points for s in graded)

    if remaining_credit_points <= 0:
        return {
            "required_average": None,
            "feasible": None,
            "card": (
                "No remaining graded credit points were given, so a required "
                "average can't be calculated - the student's WAM is "
                "effectively already final."
            ),
        }

    total_cp = graded_cp + remaining_credit_points
    required_average = (target_wam * total_cp - current_weighted_sum) / remaining_credit_points
    required_average = round(required_average, 2)

    if required_average > 100:
        feasible = False
        note = (
            f"**Not achievable.** You would need an average of {required_average} "
            f"across your remaining {remaining_credit_points} CP, which is above "
            f"the maximum possible mark (100)."
        )
    elif required_average < 0:
        feasible = True
        note = (
            f"**Already secured.** Based on your current WAM, you've already "
            f"exceeded a {target_wam} target even with a 0 average on your "
            f"remaining subjects."
        )
    else:
        feasible = True
        note = (
            f"**You need an average of {required_average}** across your "
            f"remaining {remaining_credit_points} CP to reach a WAM of {target_wam}."
        )

    return {
        "required_average": required_average,
        "feasible": feasible,
        "card": note,
    }

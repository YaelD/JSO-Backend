from enum import StrEnum


class StepType(StrEnum):
    CONNECT = "Connect with people"
    SEND_CV = "Send CV"
    APPLIED = "CV applied"
    TECH_INTERVIEW = "Tech interview"
    HR_INTERVIEW = "HR interview"
    CUSTOM = "Custom step"

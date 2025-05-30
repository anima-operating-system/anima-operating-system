###############################################################################
#
#  Welcome to Baml! To use this generated code, please run the following:
#
#  $ pip install baml-py
#
###############################################################################

# This file was generated by BAML: please do not edit it. Instead, edit the
# BAML files and re-generate this code.
#
# ruff: noqa: E501,F401
# flake8: noqa: E501,F401
# pylint: disable=unused-import,line-too-long
# fmt: off
import baml_py
from enum import Enum

from pydantic import BaseModel, ConfigDict

from typing_extensions import TypeAlias, Literal
from typing import Dict, Generic, List, Optional, TypeVar, Union


T = TypeVar('T')
CheckName = TypeVar('CheckName', bound=str)

class Check(BaseModel):
    name: str
    expression: str
    status: str
class Checked(BaseModel, Generic[T,CheckName]):
    value: T
    checks: Dict[CheckName, Check]

def get_checks(checks: Dict[CheckName, Check]) -> List[Check]:
    return list(checks.values())

def all_succeeded(checks: Dict[CheckName, Check]) -> bool:
    return all(check.status == "succeeded" for check in get_checks(checks))



class Archetype(BaseModel):
    archetype_class: str
    trope_tags: List[str]

class Behavior(BaseModel):
    behavior_arc: str
    refusal_style: str
    trigger_to_help: str
    mannerisms: List[str]
    quirks: List[str]

class Construct(BaseModel):
    identity: "Identity"
    archetype: "Archetype"
    demographic: "Demographic"
    psychographics: "Psychographics"
    behavior: "Behavior"
    visual_profile: "VisualProfile"
    voice: "Voice"
    lore: "Lore"
    lifestyle: "LifeStyle"
    llm_tuning: "LLMTuning"

class Demographic(BaseModel):
    gender: str
    age: str
    race_species: str
    birthday: Optional[str] = None
    birthplace: Optional[str] = None
    height: Optional[str] = None
    weight: Optional[str] = None

class Identity(BaseModel):
    name: str
    alias: Optional[str] = None
    role: str
    tags: List[str]

class LLMTuning(BaseModel):
    temperature: float
    top_p: float
    presence_penalty: float
    frequency_penalty: float

class LifeStyle(BaseModel):
    occupation: str
    hobbies: List[str]
    interests: List[str]
    favorite_foods: List[str]
    dislikes: List[str]
    daily_routine: Optional[str] = None

class Lore(BaseModel):
    backstory: str
    defining_moments: List[str]

class Psychographics(BaseModel):
    personality_summary: str
    core_values: List[str]
    fears: List[str]
    desires: List[str]
    beliefs: List[str]

class Resume(BaseModel):
    name: str
    email: str
    experience: List[str]
    skills: List[str]

class VisualProfile(BaseModel):
    body: str
    features: str
    style: str
    aura: Optional[str] = None

class Voice(BaseModel):
    tone: List[str]
    speech_style: str
    pov: str
    accent: Optional[str] = None

from dataclasses import dataclass


@dataclass
class VoiceSettings:
    voice: int
    rate: float

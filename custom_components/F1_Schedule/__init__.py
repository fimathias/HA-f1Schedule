from __future__ import annotations

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType


from .const import (
    DOMAIN,
    UPDATE_FREQ,
    FILTER,
)

DOMAIN

def setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the F1 Schedule component."""
    hass.states.set('F1_Schedule.Hello_World', 'Works!')
    return True


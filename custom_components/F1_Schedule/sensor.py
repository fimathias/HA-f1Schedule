# Sensor platform for F1 schedule

import logging
import requests
from datetime import datetime, timedelta

from homeassistant.helpers.entity import Entity
from homeassistant.const import ATTR_ATTRIBUTION

from .const import (
    DOMAIN,
    URL,
    UPDATE_FREQ,
    ATTR_CIRCUIT,
    ATTR_NAME,
    ATTR_ROUND,
    ATTR_TIME,
    ATTR_TYPE,
)

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = timedelta(hours=1)  # Update interval
API_URL = "https://ergast.com/api/f1/current.json"

class F1RaceSensor(Entity):
    def __init__(self):
        self._state = None

    @property
    def name(self):
        return 'F1 Race Sensor'

    @property
    def state(self):
        return self._state

    @property
    def icon(self):
        return 'mdi:trophy'

    @property
    def unit_of_measurement(self):
        return 'days'

    def update(self):
        try:
            response = requests.get(API_URL)
            data = response.json()
            races = data["MRData"]["RaceTable"]["Races"]

            # Find the next upcoming race
            next_race = None
            for race in races:
                race_date = datetime.strptime(race["date"], "%Y-%m-%d")
                if race_date > datetime.now():
                    next_race = race
                    break

            # Calculate time until next race
            if next_race:
                race_date = datetime.strptime(next_race["date"], "%Y-%m-%d")
                time_until_race = race_date - datetime.now()
                self._state = time_until_race.days
            else:
                self._state = None
        except Exception as e:
            _LOGGER.error("Error fetching data: %s", e)
            self._state = None
"""Package configs."""
from configparser import ConfigParser
from contextlib import suppress
from datetime import date
from os import getenv, makedirs, path

SHORT_TABLE_HEADER = ["Name", "Last Contacted"]
TABLE_HEADER = ["Name", "Last Contact", "Days Passed"]
TODAY_DATE = date.today().strftime("%d.%m.%Y")

configdir = f"{getenv('HOME')}/.config/people"
configpath = f"{configdir}/config.ini"
config = ConfigParser()


def get_configs():
    """Get app configs."""
    setup_configs()
    config.read(configpath)
    return config


def setup_configs() -> None:
    """Create app configs if not found."""
    if not _is_configfile():
        _make_configdir()
        _create_default_configs()


def _is_configfile() -> bool:
    return path.isfile(configpath)


def _make_configdir() -> None:
    with suppress(OSError):
        makedirs(configdir)


def _create_default_configs() -> None:
    config.add_section("main")
    config.set("main", "config_dir", configdir)
    config.add_section("database")
    config.set("database", "file", "people.db")
    with open(configpath, "w", encoding="utf-8") as file:
        config.write(file)


config = get_configs()

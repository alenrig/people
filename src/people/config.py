from configparser import ConfigParser
from contextlib import suppress
from os import getenv, makedirs, path

configdir = f"{getenv('HOME')}/.config/people"
configpath = f"{configdir}/config.ini"
config = ConfigParser()


def get_configs():
    setup_configs()
    config.read(configpath)
    return config


def setup_configs() -> None:
    if not _is_configfile(configpath):
        _make_configdir(configdir)
        _create_default_configs(config, configdir, configpath)


def _is_configfile(configpath: str) -> bool:
    return path.isfile(configpath)


def _make_configdir(configdir: str) -> None:
    with suppress(OSError):
        makedirs(configdir)


def _create_default_configs(
    config: ConfigParser, configdir: str, configpath: str
) -> None:
    config.add_section("main")
    config.set("main", "config_dir", configdir)
    config.add_section("database")
    config.set("database", "file", "people.db")
    with open(configpath, "w") as file:
        config.write(file)


config = get_configs()

# ------------------------------------------------------------------------------
# Joyous initialization
# ------------------------------------------------------------------------------
name = "joyous"
try:
    from ._version import version as __version__
except ImportError:
    __version__ = 'unknown'

default_app_config = 'ls.joyous.apps.JoyousAppConfig'

# ------------------------------------------------------------------------------
# Note: Default settings
# ------------------------------------------------------------------------------
# settings.JOYOUS_HOLIDAYS = ""
# settings.JOYOUS_GROUP_SELECTABLE = False
# settings.JOYOUS_GROUP_MODEL = "joyous.GroupPage"
# settings.JOYOUS_TIME_INPUT = "24"
# settings.JOYOUS_EVENTS_PER_PAGE = 25

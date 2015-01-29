import json
from django.conf import settings
from leaflet import app_settings as leaflet_settings


TILESERVER_URL = leaflet_settings['TILES'][0][1]
MAP_ZOOM = leaflet_settings['DEFAULT_ZOOM']
MAP_CENTER = list(leaflet_settings['DEFAULT_CENTER'])
LEAFLET_OPTIONS = {
    'fillOpacity': 0.7,
    'opacity': 1,
    'dashArray': None,
    'lineCap': None,
    'lineJoin': None,
    'radius': 6,
    # when adding new nodes other leaflet layers are dimmed to the following opacity:
    'temporaryOpacity': 0.3
}
LEAFLET_OPTIONS = getattr(settings, 'NODESHOT_UI_LEAFLET_OPTIONS', LEAFLET_OPTIONS)
DISABLE_CLUSTERING_AT_ZOOM = getattr(settings, 'NODESHOT_UI_DISABLE_CLUSTERING_AT_ZOOM', 12)
MAX_CLUSTER_RADIUS = getattr(settings, 'NODESHOT_UI_MAX_CLUSTER_RADIUS', 90)
DATETIME_FORMAT = getattr(settings, 'NODESHOT_UI_DATETIME_FORMAT', 'dd MMMM yyyy, HH:mm')
DATE_FORMAT = getattr(settings, 'NODESHOT_UI_DATE_FORMAT', 'dd MMMM yyyy')
ADDRESS_SEARCH_TRIGGERS = [
    ',',
    'st.',
    ' street',
    ' square',
    ' road',
    ' avenue',
    ' lane',
    'footpath',
    'via ',
    'viale ',
    'piazza ',
    'strada ',
    'borgo ',
    'contrada ',
    'zona ',
    'fondo ',
    'vico ',
    'sentiero ',
    'plaza ',
    ' plaza',
    'calle ',
    'avenida '
]
ADDRESS_SEARCH_TRIGGERS = getattr(settings, 'NODESHOT_UI_ADDRESS_SEARCH_TRIGGERS', ADDRESS_SEARCH_TRIGGERS)
LOGO = getattr(settings, 'NODESHOT_UI_LOGO', None)

if 'nodeshot.community.participation' in settings.INSTALLED_APPS:
    VOTING_ENABLED = getattr(settings, 'NODESHOT_UI_VOTING_ENABLED', True)
    RATING_ENABLED = getattr(settings, 'NODESHOT_UI_RATING_ENABLED', True)
    COMMENTS_ENABLED = getattr(settings, 'NODESHOT_UI_COMMENTS_ENABLED', True)
else:
    VOTING_ENABLED = False
    RATING_ENABLED = False
    COMMENTS_ENABLED = False

VOTING_ENABLED = json.dumps(VOTING_ENABLED)
RATING_ENABLED = json.dumps(RATING_ENABLED)
COMMENTS_ENABLED = json.dumps(COMMENTS_ENABLED)

if 'social_auth' in settings.INSTALLED_APPS:
    FACEBOOK_ENABLED = bool(settings.FACEBOOK_APP_ID) and bool(settings.FACEBOOK_API_SECRET)  # noqa
    GOOGLE_ENABLED = bool(settings.GOOGLE_OAUTH2_CLIENT_ID) and bool(settings.GOOGLE_OAUTH2_CLIENT_SECRET)  # noqa
    GITHUB_ENABLED = bool(settings.GITHUB_APP_ID) and bool(settings.GITHUB_API_SECRET)  # noqa
    SOCIAL_AUTH_ENABLED = FACEBOOK_ENABLED or GOOGLE_ENABLED or GITHUB_ENABLED  # noqa
else:
    FACEBOOK_ENABLED = False
    GOOGLE_ENABLED = False
    GITHUB_ENABLED = False
    SOCIAL_AUTH_ENABLED = False

if 'nodeshot.core.websockets' in settings.INSTALLED_APPS:
    from nodeshot.core.websockets import DOMAIN, PATH, PORT

    WEBSOCKETS = {
        'DOMAIN': DOMAIN,
        'PATH': PATH,
        'PORT': PORT
    }
else:
    WEBSOCKETS = False

from nodeshot.community.profiles.settings import REGISTRATION_OPEN  # noqa

GOOGLE_ANALYTICS_UA = getattr(settings, 'NODESHOT_UI_GOOGLE_ANALYTICS_UA', None)
GOOGLE_ANALYTICS_OPTIONS = getattr(settings, 'NODESHOT_UI_GOOGLE_ANALYTICS_OPTIONS', 'auto')

# -*- coding: utf-8 -*-
import os
import gettext
from hashlib import sha1
from random import random
from datetime import datetime
from Cookie import CookieError

from bottle import MakoTemplate
from bottle import request, response

from plants_web.configs import LANGUAGES, TEMPLATES_PATH, CLASSIFICATIONS, EXTERNAL_LINKS, METADATA, SUBDOMAINS, LOCALE_NAME, LOCALE_PATH, MONTHS, DOLMEN_CLASSIFICATIONS, CRAWLERS
from plants_web.configs import local
# from plants_web.libs.auth import get_account
# from plants_web.libs.utils import get_messages
# from plants_web.libs.utils import get_subdomain
# from plants_web.libs.html import html_escape

def _check_if_template_exists(name):
    abs_path = os.path.join(TEMPLATES_PATH, name)
    if os.path.exists(abs_path):
        return True
    return False

def get_final_path(name, subdomain, start_w_slash = True):
    name_path = os.path.join(subdomain, name)
    if _check_if_template_exists(name_path):
        name = name_path
    name_path = os.path.join('multisite', name)
    if _check_if_template_exists(name_path):
        name = name_path
    if start_w_slash and name[0:] != ["/"]:
        name = '/'+ name
    return name

def get_sitename(subdomain):
  if subdomain == 'healthsystems':
    return 'PDQ Evidence'
  return 'Epistemonikos'


def render_template(name, error = False, **kwargs):
    #Setting account cookies
    try:
        if not request.get_cookie('eus'):
            response.set_cookie('eus', sha1(str(random())).hexdigest(), path='/', expires = datetime(datetime.today().year + 10, 12, 12))
    except CookieError, e:
        print e
    active_language = request.headers.get('Active-Language', 'en')
    # subdomain = get_subdomain()
    # site_name = get_sitename(subdomain)
    is_google = False
    for user_agent in CRAWLERS:
        if request.headers.get('User-Agent'):
            if user_agent.lower() in request.headers.get('User-Agent').lower():
                is_google = True
    # if subdomain == 'hps-primary':
    #     active_language = 'en'

    # Reinstalling the translation. This should be done by the middleware, but maybe is not working well.

    # translation = gettext.translation(
    #                    LOCALE_NAME,
    #                    LOCALE_PATH,
    #                    languages=[active_language],
    #                    codeset="utf-8"
    #                )
    # translation.install(unicode=True)

    target_name = get_final_path(name, '', start_w_slash = False)
    template =  MakoTemplate(name=target_name, lookup=[TEMPLATES_PATH], default_filters=['decode.utf8'], imports=['from plants_web.libs.templates import get_final_path'], cache_enabled = False)
    search_classification = request.GET.get('classification', 'all')
    # if error:
    #     try:
    #         get_account(request.mongodb)
    #     except:
    #         request.account = None
    # else:
    #     get_account(request.mongodb)
    # kwargs['messages'] = get_messages(kwargs.get('messages'))
    # for key in kwargs:
    #     kwargs[key] = html_escape(kwargs[key])

    try:
      ASSETS_HOST = local.ASSETS_HOST
    except:
      ASSETS_HOST = '/assets'
    return template.render(#account = request.account,
                           #language = active_language,
                           #languages = LANGUAGES,
                           # classifications = CLASSIFICATIONS,
                           # dolmen_classifications = DOLMEN_CLASSIFICATIONS,
                           # external_links = EXTERNAL_LINKS,
                           # metadata = METADATA,
                           # search_classification = search_classification,
                           # subdomain = subdomain,
                           # MONTHS = MONTHS,
                           # subdomain_data = SUBDOMAINS.get(subdomain),
                           # ASSETS_HOST = ASSETS_HOST,
                           # is_google = is_google,
                           # site_name = site_name,
                           # _ = translation.ugettext,
                           **kwargs).strip()

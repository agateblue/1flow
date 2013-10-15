# -*- coding: utf-8 -*-

from django.conf import settings

def mongodb_user(request):
    """ not the most usefull context manager in the world. """

    if request.user.is_anonymous():
        return {
            u'mongodb_user': None,
            u'preferences': None,
            u'wizards': None,
        }

    return {
        u'mongodb_user': request.user.mongo,
        u'preferences': request.user.mongo.preferences,
        u'wizards': request.user.mongo.preferences.wizards,

        u'NONREL_ADMIN': settings.NONREL_ADMIN,
    }


def social_things(request):

    if request.user.is_anonymous():
        return {}

    dsa = request.user.social_auth

    return {
        'has_google': dsa.filter(
            provider='google-oauth2').count() > 0,
        'social_count': dsa.all().count()
    }

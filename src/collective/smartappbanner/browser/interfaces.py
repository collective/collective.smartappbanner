# -*- encoding: utf-8 -*-
from collective.smartappbanner import _
from zope import schema
from zope.interface import Interface


PLATFORMS = [
    u'android',
    u'ios',
]


class ISmartappbannerBaseSettings(Interface):
    """Smart app banner settings """

    title = schema.TextLine(
        title=_(u'Name of the app'),
        required=False,
        default=u'',
    )
    author = schema.TextLine(
        title=_(u'Author of the app'),
        required=False,
        default=u'',
    )
    price = schema.TextLine(
        title=_(u'Price of the app in stores'),
        required=False,
        default=u'FREE',
    )
    icon = schema.TextLine(
        title=_(u'Icon used in banner'),
        description=_(u'Path to default image'),
        default=u'/logo.png',
        required=False,
    )
    button_text = schema.TextLine(
        title=_(u'Text on button'),
        required=False,
        default=u'View',
    )
    ios_url = schema.TextLine(
        title=_(u'Url app in Apple store'),
        required=False,
        default=u'',
    )
    android_url = schema.TextLine(
        title=_(u'Url app in Google play'),
        required=False,
        default=u'',
    )
    platforms = schema.List(
        title=_(u'Enable platforms'),
        description=_(u'Can be used to temporarily disable a platform '
                      'without needing to remove the url.'),
        required=False,
        value_type=schema.Choice(values=PLATFORMS),
        default=PLATFORMS,
    )

# -*- encoding: utf-8 -*-
from collective.smartappbanner import _
from zope import schema
from zope.interface import Interface


class ISmartappbannerBaseSettings(Interface):
    """Smart app banner settings """

    smartbannerTitle = schema.TextLine(
        title=_(u"Name of the app"),
        required=True,
    )
    smartbannerAuthor = schema.TextLine(
        title=_(u"Contributors of the app"),
        required=True,
    )
    smartbannerPrice = schema.TextLine(
        title=_(u"Price of the app in store's"),
        required=True,
    )
    smartbannerIcon = schema.TextLine(
        title=_(u"Icon used in banner"),
        description=_(u'Path to default image'),
        default=u'/logo.png',
        required=False,
    )
    smartbannerIOSurl = schema.TextLine(
        title=_(u"Url app in Apple store"),
        required=True,
    )
    smartbannerAndroidUrl = schema.TextLine(
        title=_(u"Url app in Google play"),
        required=True,
    )
    smartbannerPlatforms = schema.TextLine(
        title=_(u"Enable platforms"),
        description=_(u"android,ios"),
        required=True,
    )

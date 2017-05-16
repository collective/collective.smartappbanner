# -*- encoding: utf-8 -*-
from collective.smartappbanner import _
from zope import schema
from zope.interface import Interface


class ISmartappbannerBaseSettings(Interface):
    """Smart app banner settings """

    app_title = schema.TextLine(
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
        description=_(u'Path or url to image'),
        default=u'/logo.png',
        required=False,
    )
    button_text = schema.TextLine(
        title=_(u'Text on button'),
        required=False,
        default=u'View',
    )
    ios_id = schema.TextLine(
        title=_(u'App ID in Apple store'),
        description=_(
            u'app_id_description',
            default=u'If you only support the App Store, '
                    u'all other options can be ignored.'),
        required=False,
        default=u'',
    )
    android_id = schema.TextLine(
        title=_(u'App ID in Google play'),
        required=False,
        default=u'',
    )
    windows_id = schema.TextLine(
        title=_(u'App ID in Windows store'),
        required=False,
        default=u'',
    )

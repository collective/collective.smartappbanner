# -*- encoding: utf-8 -*-
from collective.smartappbanner import _
from zope import schema
from zope.interface import Interface


class ISmartappbannerBaseSettings(Interface):
    """Smart app banner settings """

    # - daysHidden
    # - daysReminder
    # - appStoreLanguage
    # - Title
    # - author
    # - price
    # - - IOS
    # - - Android
    # - - Windows
    # - icon
    title = schema.TextLine(
        title=_(u"Title"),
        description=_(u"Title of the app"),
        required=True,
    )
    author = schema.TextLine(
        title=_(u"Author"),
        description=_(u"Author/Owner of the app"),
        required=True,
    )
    icon = schema.TextLine(
        title=_(u"Icon"),
        description=_(u"Icon to show on banner"),
        required=True,
    )
    daysHidden = schema.TextLine(
        title=_(u"Days Hidden"),
        description=_(u"Days to hide banner after close button is clicked"
                      u" (defaults to 15)"),
        required=False,
    )
    daysReminder = schema.TextLine(
        title=_(u"Days Reminder"),
        description=_(u"Days to hide banner after button is clicked"
                      u" (defaults to 90)"),
        required=False,
    )
    appStoreLanguage = schema.TextLine(
        title=_(u"appStore Language"),
        description=_(u"Language code for the App Store"
                      u" (defaults to user's browser language)"),
        required=False,
    )
    priceIOS = schema.TextLine(
        title=_(u"Price for IOS"),
        description=_(u"How much does the app cost in IOS"
                      u" (defaults to free)"),
        required=False,
    )
    priceAndroid = schema.TextLine(
        title=_(u"Price for Android"),
        description=_(u"How much does the app cost in Android"
                      u" (defaults to free)"),
        required=False,
    )
    priceWindows = schema.TextLine(
        title=_(u"Price for Windows"),
        description=_(u"How much does the app cost in Windows"
                      u" (defaults to free)"),
        required=False,
    )

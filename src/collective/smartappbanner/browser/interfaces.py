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
    # - button
    # - price
    # - - IOS
    # - - Android
    # - - Windows
    # - icon

    address = schema.Text(
        title=_(u"Address"),
        description=_(u"Content of the address block in the footer."),
        required=False,
    )
    links_one = schema.Text(
        title=_(u"Links column one"),
        description=_(u"Content of the links block in the footer. Links are "
                      u"formatted as Title|path or Title|url. The path is used"
                      u" for internal links, for instance News|news for a link"
                      u" to http://domain.com/news or Deep|somewhere/in/the/"
                      u"site/but/very/deep for a link to http://domain.com/"
                      u"somewhere/in/the/site/but/very/deep. The url is used "
                      u"for external links, for instance "
                      u"Plone|http://plone.org."),
        required=False,
    )
    links_two = schema.Text(
        title=_(u"Links column two"),
        description=_(u"Content of the links block in the footer. Links are "
                      u"formatted as Title|path or Title|url. The path is used"
                      u" for internal links, for instance News|news for a link"
                      u" to http://domain.com/news or Deep|somewhere/in/the/"
                      u"site/but/very/deep for a link to http://domain.com/"
                      u"somewhere/in/the/site/but/very/deep. The url is used "
                      u"for external links, for instance "
                      u"Plone|http://plone.org."),
        required=False,
    )

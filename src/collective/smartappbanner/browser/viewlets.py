# -*- encoding: utf-8 -*-
from collective.smartappbanner.browser.interfaces import ISmartappbannerBaseSettings  # noqa
from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.registry.interfaces import IRegistry
from zope.component import ComponentLookupError
from zope.component import getUtility


class smartappbannerViewlet(ViewletBase):

    def meta_tags(self):
        try:
            self.settings = getUtility(
                IRegistry).forInterface(ISmartappbannerBaseSettings)  # noqa
        except (ComponentLookupError, KeyError):
            return
        # Do we have a url for at least one platform?
        platforms = []
        android_url = self.settings.android_url
        if android_url:
            platforms.append(u'android')
        ios_url = self.settings.ios_url
        if ios_url:
            platforms.append(u'ios')
        if not platforms:
            return
        platforms = u','.join(platforms)

        # Get icon url
        icon = self.settings.icon or u''
        if icon and not icon.startswith(u'http'):
            nav_root = api.portal.get_navigation_root(self.context)
            if not icon.startswith(u'/'):
                icon = u'/' + icon
            icon = nav_root.absolute_url() + icon

        tags = {}
        # We add all options, even those who are empty.
        # The javascript expects all options to be there,
        # and have content, so not None or an empty string,
        # otherwise the user sees 'undefined' in the banner.
        # We could make everything required,
        # but it is easier to simply use a space.
        tags['smartbanner:title'] = self.settings.app_title or u' '
        tags['smartbanner:author'] = self.settings.author or u' '
        tags['smartbanner:price'] = self.settings.price or u' '
        # Note that the suffixes need a space in front,
        # because they get added right after the price.
        tags['smartbanner:price-suffix-apple'] = u' On the App Store'
        tags['smartbanner:price-suffix-google'] = u' In Google Play'
        tags['smartbanner:icon-apple'] = icon
        tags['smartbanner:icon-google'] = icon
        tags['smartbanner:button'] = self.settings.button_text or u''
        tags['smartbanner:button-url-apple'] = ios_url or u''
        tags['smartbanner:button-url-google'] = android_url or u''
        tags['smartbanner:enabled-platforms'] = platforms

        return tags

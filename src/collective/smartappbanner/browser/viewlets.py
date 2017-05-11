# -*- encoding: utf-8 -*-
from collective.smartappbanner.browser.interfaces import ISmartappbannerBaseSettings  # noqa
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

        tags = {}
        # We add all options, even those who are empty.
        # The javascript expects this.
        tags['smartbanner:title'] = self.settings.title
        tags['smartbanner:author'] = self.settings.author
        tags['smartbanner:price'] = self.settings.price
        tags['smartbanner:price-suffix-apple'] = 'On the App Store'
        tags['smartbanner:price-suffix-google'] = 'In Google Play'
        tags['smartbanner:icon-apple'] = self.settings.icon
        tags['smartbanner:icon-google'] = self.settings.icon
        tags['smartbanner:button'] = self.settings.button_text
        tags['smartbanner:button-url-apple'] = ios_url
        tags['smartbanner:button-url-google'] = android_url
        tags['smartbanner:enabled-platforms'] = platforms

        return tags

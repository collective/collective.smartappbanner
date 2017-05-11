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
        # Do we have enabled platforms?
        platforms = self.settings.platforms
        if not platforms:
            return
        # Do we have a url for at least one enabled platform?
        android_url = self.settings.android_url
        ios_url = self.settings.ios_url
        has_ios = u'ios' in platforms and ios_url
        has_android = u'android' in platforms and android_url
        if not (has_android or has_ios):
            return

        tags = {}

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
        tags['smartbanner:enabled-platforms'] = ','.join(
            self.settings.platforms)

        return tags

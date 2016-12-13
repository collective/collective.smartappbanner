# -*- encoding: utf-8 -*-
from collective.smartappbanner import _
from collective.smartappbanner.browser.interfaces import ISmartappbannerBaseSettings  # noqa
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.z3cform import layout


class SettingsEditForm(RegistryEditForm):
    """Smart app banner Settings edit form for plone.app.registry.
    """
    schema = ISmartappbannerBaseSettings
    label = _(u'Smart app banner Settings')
    # redirect to ourselves after edit
    control_panel_view = 'smartappbanner-settings'


SettingsView = layout.wrap_form(SettingsEditForm, ControlPanelFormWrapper)

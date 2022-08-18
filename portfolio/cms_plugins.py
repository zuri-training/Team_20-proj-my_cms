from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from .models import Text
from django.utils.translation import gettext_lazy as _


# @plugin_pool.register_plugin
class TextPlugin(CMSPluginBase):
    model = Text
    render_template = 'text.html'
    cache = False

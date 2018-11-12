from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from polls_cms_integration.models import PollPluginModel
from django.utils.translation import ugettext as _

@plugin_pool.register_plugin
class PollPluginPublisher(CMSPluginBase):
    model = PollPluginModel
    module = _("Polls")
    name = _("Poll Plugin")
    render_template = "polls_cms_integration/poll_plugin.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

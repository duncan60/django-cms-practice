from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from cms.menu_bases import CMSAttachMenu
from menus.base import NavigationNode
from menus.menu_pool import menu_pool

from polls.models import Poll


class PollsMenu(CMSAttachMenu):
    name = _("Polls Menu")  # give the menu a name this is required.

    def get_nodes(self, request):
        """
        This method is used to build the menu tree.
        """
        nodes = []
        for poll in Poll.objects.all():
            node = NavigationNode(
                title=poll.question,
                url=reverse('polls:detail', args=(poll.pk,)),
                id=poll.pk,  # unique id for this node within the menu
            )
            nodes.append(node)
        return nodes

menu_pool.register_menu(PollsMenu)
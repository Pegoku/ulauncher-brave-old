import logging
import urllib

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

# Use this to log messages
LOGGER = logging.getLogger(__name__)

# to encode URL


def urlencode(qp):
    return urllib.urlencode(qp)


class BraveExt(Extension):

    def __init__(self):
        super(BraveExt, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension):
        items = list()

        if event.get_argument():
            LOGGER.info('Showing Brave search for "{}"'.format(
                event.get_argument()))
            items.append(ExtensionResultItem(
                icon='images/icon.png',
                name='Search on Brave',
                description='Search for "{}".'.format(event.get_argument()),
                on_enter=OpenUrlAction(
                    'https://search.brave.com/search/?q={}'.format(event.get_argument())
                    #{}'.format(
                    #    urlencode({'q': event.get_argument(), 's': 'all'})
                    )#)
            )
            )

        return RenderResultListAction(items)


if __name__ == '__main__':
    BraveExt().run()

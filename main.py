from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction

from src.items import no_config_items, no_results_item, generate_items
from src.generate import Generate


class GenerateExtension(Extension):
    def __init__(self):
        super(GenerateExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()

        params = strip_list(query.split(' '))            

        launcher = Generate(params)

        if not launcher.has_generator():
            return RenderResultListAction(no_generator_items())

        results = launcher.execute()

        if not results:
            return RenderResultListAction(no_results_item())

        return RenderResultListAction(generate_items(results))


if __name__ == "__main__":
    GenerateExtension().run()
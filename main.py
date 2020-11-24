from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction

from src.items import no_generator_items, no_results_item, generate_items
from src.functions import strip_list
from src.generate import Generate


class GenerateExtension(Extension):
    def __init__(self):
        super(GenerateExtension, self).__init__()

        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        query = event.get_argument() or str()
        keyword = extension.preferences['generate_kw']

        params = strip_list(query.split(' '))            

        generate = Generate(params)

        if not generate.has_generator():
            return RenderResultListAction(no_generator_items(keyword))

        results = generate.execute()

        if not results:
            return RenderResultListAction(no_results_item())

        return RenderResultListAction(generate_items(generate.gen_name, results))


if __name__ == "__main__":
    GenerateExtension().run()
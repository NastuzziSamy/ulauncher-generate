from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction
from ulauncher.api.shared.action.SetUserQueryAction import SetUserQueryAction

from src.consts import ICON_DIR, ICON_FILE, GENERATORS


def generate_icon(name):
    return ICON_DIR + name + '.png'


def no_generator_items(ext_kw):
    return [
        ExtensionResultItem(
            icon=generate_icon(gen_name),
            name=gen_data['name'],
            description=gen_data['description'],
            on_enter=SetUserQueryAction(ext_kw + ' ' + gen_name)
        )
    for (gen_name, gen_data) in GENERATORS.items()]


def no_results_item():
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name='No generation available',
            on_enter=DoNothingAction()
        )
    ]


def generate_action(ext_kw, gen_name, result):
    if 'copy' in result:
        return CopyToClipboardAction(result['copy'])

    if 'query' in result:
        return SetUserQueryAction(ext_kw + ' ' + gen_name + ' ' + result['query'])


def generate_items(ext_kw, gen_name, results):
    return [
        ExtensionResultItem(
            icon=generate_icon(gen_name),
            name=result['name'],
            description=result['description'],
            on_enter=generate_action(ext_kw, gen_name, result)
        )
    for result in results]

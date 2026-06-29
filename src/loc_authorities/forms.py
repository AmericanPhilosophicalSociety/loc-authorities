from dal import autocomplete


class LocField(autocomplete.AlightListCreateChoiceField):
    """Wrapper for dal field as it requires a predefined choice-list, which
    for this use-case is always empty.
    """
    choice_list = []
    widget = autocomplete.ListAlight(url='suggest')

    def __init__(self, choice_list=choice_list, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LocWidget(autocomplete.ListAlight):
    url = 'suggest'

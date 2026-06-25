from dal import autocomplete

from loc_authorities.api import LocAPI


class LocLookup(autocomplete.AlightListView):
    """View to provide Library of Congress suggestions for autocomplete
    lookup. Expects TODO
    """
    authority = None

    def get_list(self):
        q = self.q
        if q:
            loc = LocAPI()
            result = loc.suggest(q, authority=self.authority)
            return [
                (item.loc_id, item.label) for item in result
            ]
        else:
            return []

    def create(self, text):
        return text


class LocNameLookup(LocLookup):
    """View to provide Library of Congress suggestions from the
    Name Authority File for autocomplete lookup.
    """
    authority = 'names'


class LocSubjectLookup(LocLookup):
    """View to provide Library of Congress suggestions from the
    LC Subject Headings for autocomplete lookup.
    """
    authority = 'subjects'


class LocSearch(autocomplete.AlightListView):
    """View to perform keyword search from Library of Congress
    to provide autocomplete suggestions. As searching without a
    authority is unsupported in loc-authorities, this is an
    abstract class to provide functionality for specific
    authorities.
    """
    authority = None

    def get_list(self):
        q = self.q
        if q:
            loc = LocAPI()
            result = loc.search(q, authority=self.authority)
            return [
                (item.loc_id, item.label) for item in result
            ]
        else:
            return []

    def create(self, text):
        return text


class LocNameSearch(LocSearch):
    """View to perform keyword search from the Library of Congress
    Name Authority File for autocomplete lookup.
    """
    authority = 'names'


class LocSubjectSearch(LocSearch):
    """View to perform keyword search from the Library of Congress
    Subject Headings for autocomplete lookup.
    """
    authority = 'subjects'

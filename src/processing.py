def filter_by_state(to_filter: list, state="EXECUTED") -> list:
    """
    returns only those elements of the list which state equals to given state
    if state was not given it will be set to "EXECUTED"
    """
    only_states = []
    for element in to_filter:
        if state == element["state"]:
            only_states.append(element)

    return only_states


def sort_by_date(to_sort: list, decreasing=True) -> list:
    """
    sorts given list by date
    decreasing equals True if not given
    """
    to_sort.sort(key=lambda x: x["date"], reverse=decreasing)
    return to_sort

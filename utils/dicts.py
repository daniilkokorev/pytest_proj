
def get_val(collection, key, default='git'):
    if collection:
        for item in collection.values():
            return item
    else:
        return default

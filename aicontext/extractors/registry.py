EXTRACTORS = []

def register(fn):
    EXTRACTORS.append(fn)
    return fn

def run_all(files, root):
    results = {}
    for extractor in EXTRACTORS:
        name, data = extractor(files, root)
        results[name] = data
    return results

from fuzzywuzzy import fuzz

def find_best_match(query, options):
    best_match = None
    max_ratio = 0

    for option in options:
        ratio = fuzz.ratio(query, option)
        if ratio > max_ratio:
            max_ratio = ratio
            best_match = option

    return best_match



def flatten(original_list):
    planish = []

    if isinstance(original_list, list) == False:
        raise Exception("Must be a list!")

    for element in original_list:
        if isinstance(element, str) or element is None or isinstance(element, float):
            raise Exception("All elements in the list must be integers!")

        if isinstance(element, list):
            planish.extend(flatten(element))
        else:
            planish.append(element)

    return planish


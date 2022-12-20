def validate_input(dict_request):
    for _, val in dict_request.items():
        try:
            val=float(val)
        except Exception as e:
            return False
    return True
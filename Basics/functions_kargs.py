def message(**kwargs):
    text_message = "Name {key} : Value {value}"
    name = kwargs.get('key', '')
    assignation = kwargs.get('assignation', '')
    print(text_message.format(
        key=name,
        value=assignation
    ))

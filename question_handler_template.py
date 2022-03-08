def answer_question(question, session_id):

    # Load all previous questions & responses from this user
    #   Stored in a database somewhere
    history = load_previous_chat(session_id)

    # Use a different procedure based on what type of question the user is asking
    question_type = determine_question_type(question, history)

    if question_type == CHAT:
        response = get_chatty_response(question, history)

    elif question_type == SYMPTOM_CHECK:
        response = get_symptom_checker_response(question, history)

    # etc...

    else:
        response = f"You asked: \"{q}\"\nI do not know how to respond :("

    # Save the current question & response pair in the session data
    save_chat(session_id, question_type, question, response)

    # We'll need some way to figure out if/when to clear the history

    return empathize(question_type, response)

def get_symptom_checker_response(question, history):
    # Get a list of all of the symptoms the user has, based on everything they've said so far
    symptoms = []
    for i in history + [question]:
        if (s := get_symptom(i)) is not None:
            symptoms.append(s)

    # Determine what followup question is necessary if any, or otherwise determine a final response
    # The "assess_symptoms" function could call an external API or use some graph algorithm in the configurable database
    followup, diagnosis = assess_symptoms(symptoms)

    if diagnosis is None:
        return followup

    return diagnosis

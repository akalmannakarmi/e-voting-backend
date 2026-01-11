def ensure_ballot_active(is_active: bool):
    if not is_active:
        raise ValueError("Ballot is not active")


def ensure_not_voted(has_voted: bool):
    if has_voted:
        raise ValueError("User has already voted")

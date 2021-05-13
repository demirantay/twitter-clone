def get_current_user(request, User, ObjectDoesNotExist):
    """gets the current user for the basic user model"""
    # Get the username in the session
    try:
        current_basic_user_username = request.session["basic_user_username"]
    except KeyError:
        current_basic_user_username = None
    # Get the username record with the ORM
    try:
        current_user = User.objects.get(username=current_basic_user_username)
    except ObjectDoesNotExist:
        current_user = None

    return current_user


def get_current_user_profile(request, User, BasicUserProfile, ObjectDoesNotExist):
    """gets the current users settings"""
    # Get the current user
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)
    # Get the current user settings
    try:
        current_basic_user_settings = BasicUserProfile.objects.get(
            user=current_basic_user
        )
    except ObjectDoesNotExist:
        current_basic_user_settings = None

    return current_basic_user_settings


def get_other_user(request, other_user_username, User, ObjectDoesNotExist):
    """gets the other user for the basic user model"""
    # Get the other user
    try:
        other_user = User.objects.get(username=other_user_username)
    except ObjectDoesNotExist:
        other_user = None

    return other_user


def get_other_user_profile(request, other_user_username, User, BasicUserProfile, ObjectDoesNotExist):
    """gets the other users settings"""
    # Get the other user
    other_basic_user = get_other_user(request, other_user_username, User, ObjectDoesNotExist)
    # Get the other users settings
    try:
        other_basic_user_settings = BasicUserProfile.objects.get(
            user=other_basic_user
        )
    except ObjectDoesNotExist:
        other_basic_user_settings = None

    return other_basic_user_settings

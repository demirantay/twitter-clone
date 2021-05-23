# Left Nav Tweet form processing
def left_nav_tweet_form_processing(request, Tweet, current_basic_user_profile):
    if request.POST.get("hidden_panel_tweet_submit_btn"):
        tweet_content = request.POST.get("tweet_content")
        tweet_image = request.FILES.get("tweet_image")

        new_tweet = Tweet(
            user=current_basic_user_profile, content=tweet_content,
            image=tweet_image
        )
        new_tweet.save()


# Mobile tweet form processing
def mobile_tweet_form_processing(request, Tweet, current_basic_user_profile):
    if request.POST.get("mobile_hidden_tweet_submit_btn"):
        tweet_content = request.POST.get("tweet_content")
        tweet_image = request.FILES.get("tweet_image")

        new_tweet = Tweet(
            user=current_basic_user_profile, content=tweet_content,
            image=tweet_image
        )
        new_tweet.save()


# Who to follow box cells
def get_who_to_follow(BasicUserProfile, ObjectDoesNotExist, random):
    try:
        latest_user = BasicUserProfile.objects.last()
    except ObjectDoesNotExist:
        latest_user = None

    number_1 = random.randint(1, latest_user.id)
    number_2 = random.randint(1, latest_user.id)
    number_3 = random.randint(1, latest_user.id)

    who_to_follow = []

    who_to_follow.append(BasicUserProfile.objects.get(id=number_1))
    who_to_follow.append(BasicUserProfile.objects.get(id=number_2))
    who_to_follow.append(BasicUserProfile.objects.get(id=number_3))

    return who_to_follow


# Topics to follow
def get_topics_to_follow(Topic, ObjectDoesNotExist, random):
    try:
        all_topics = Topic.objects.all()
        latest_topic = Topic.objects.last()
    except ObjectDoesNotExist:
        all_topics = None
        latest_topic = None

    topics_to_follow = []

    for i in range(5):
        random_topic = all_topics[random.randint(1, latest_topic.id-1)]
        topics_to_follow.append(random_topic)

    return topics_to_follow

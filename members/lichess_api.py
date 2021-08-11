import requests

# get lichess stats
lichess_api_base = "https://lichess.org/api/"


def get_rating(username):
    user_rating_history = requests.get(
        f"{lichess_api_base}user/{username}/rating-history"
    )
    rating_data = user_rating_history.json()
    return rating_data


def get_bullet_rating(username):
    rating_data = get_rating(username)
    parsed_rating = ""
    try:
        parsed_rating = rating_data[0]["points"][-1][3]
        return parsed_rating
    except Exception:
        parsed_rating = "N/A"
        return parsed_rating


def get_blitz_rating(username):
    rating_data = get_rating(username)
    parsed_rating = ""
    try:
        parsed_rating = rating_data[1]["points"][-1][3]
        return parsed_rating
    except Exception:
        parsed_rating = "N/A"
        return parsed_rating


def get_rapid_rating(username):
    rating_data = get_rating(username)
    parsed_rating = ""
    try:
        parsed_rating = rating_data[2]["points"][-1][3]
        return parsed_rating
    except Exception:
        parsed_rating = "N/A"
        return parsed_rating


def get_classical_rating(username):
    rating_data = get_rating(username)
    parsed_rating = ""
    try:
        parsed_rating = rating_data[2]["points"][-1][3]
        return parsed_rating
    except Exception:
        parsed_rating = "N/A"
        return parsed_rating

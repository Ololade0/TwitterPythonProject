from functools import reduce

users = [{"user_name": "johnny11", "age": 19,
          "tweets": ["I love football", "Money is good", "I'm broke again", "Who own a ps5", "i want to be rich"],
          "verified": False},
         {"user_name": "hannah34", "age": 32,
          "tweets": ["Up chelsea", "I want donald trump back", "I just won a visa lottery"], "verified": False},
         {"user_name": "adewale101", "age": 17, "tweets": [], "verified": True},
         {"user_name": "florence", "age": 21,
          "tweets": ["I hate men", "feminism is the way", "rape victims deserve better"], "verified": False},
         {"user_name": "bisi4life", "age": 26,
          "tweets": ["Adekunle gold is good", "I want a new guitar", "American idol will start soon"],
          "verified": False},
         {"user_name": "ayodeji", "age": 15, "tweets": ["Bbnaija", "Whitemoney is my winner", "Thank you dstv"],
          "verified": True},
         {"user_name": "opemipo13", "age": 37, "tweets": [], "verified": False},
         {"user_name": "petergrey", "age": 23, "tweets": ["London is cold", "I need a car", "chill with the big boys"],
          "verified": True},
         {"user_name": "bayo", "age": 26, "tweets": ["Ankara", "fashion design school", "i need modelling gig"],
          "verified": False},
         {"user_name": "peace", "age": 18, "tweets": [], "verified": False}]

# NAMES OF VERIFIED USERS
print("NAMES OF VERIFIED USERS")
verified_users = [people["user_name"] for people in users if people["verified"] == True]
print(verified_users)
map_verified = list(map(lambda people: people["user_name"], filter(lambda people: people["verified"] == True, users)))
print(list(map_verified))

print()

# NAMES OF ACTIVE USERS
print("NAMES OF ACTIVE USERS")
active_users = [people["user_name"] for people in users if people["tweets"] != []]
print(active_users)
map_active = map(lambda people: people["user_name"], filter(lambda people: people["tweets"] != [], users))
print(list(map_active))
print()

# NAMES OF USERS BELOW 25 AND VERIFIED
print("NAMES OF USERS BELOW 25 AND VERIFIED")
below25_verified = [people["user_name"] for people in users if people["age"] < 25 and people["verified"] == True]
print(below25_verified)
below25_verified_map = map(
    lambda people: people["user_name"] if people["age"] < 25 and people["verified"] == True else None, users)
print(list(below25_verified_map))
print()

# MAXIMUM AGE
maximum_age = (max(people["age"] for people in users))
print("MAXIMUM AGE: ", maximum_age)
print()


# MINIMUM AGE
minimum_age = (min(people["age"] for people in users))
print("MINIMUM AGE: ", minimum_age)

# min_age_map = map(lambda x, y: x if x["age"] > y["age"] else None, users)
# print(list(min_age_map))
print()

# AVERAGE AGE
average_age = (sum(people["age"] for people in users) / len(users))
print("AVERAGE AGE: ", average_age)

# ALPHABETICAL ORDER
ascending_order = sorted(users, key=lambda people: people["user_name"])
print("USERNAME IN ASCENDING ORDER: ", ascending_order)

# DESCENDING ORDER
descending_order = sorted(users, key=lambda people: people["user_name"], reverse=True)
print("USERNAME IN DESCENDING ORDER: ", descending_order)

# AGE FROM LARGEST TO SMALLEST
largest_to_smallest = sorted(users, key=lambda people: people["age"], reverse=True)
print("AGE FROM LARGEST TO SMALLEST: ", largest_to_smallest)

# USER WITH LONGEST NAME
print()
longest_name = reduce(lambda x, y: x if len(x["user_name"]) > len(y["user_name"]) else y, users)
print("LONGEST NAME: ", longest_name["user_name"])
longest_name = max(users, key=lambda people: len(people["user_name"]))
print("LONGEST NAME: ", longest_name["user_name"])

# MOST TWEETS
print()
most_tweets = reduce(lambda x, y: x if len(x["tweets"]) > len(y["tweets"]) else y, users)
print("MOST TWEETS: ", most_tweets["user_name"], most_tweets["tweets"])
most_tweets = max(users, key=lambda people: len(people["tweets"]))

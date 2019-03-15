# data-science




## Getting Review Data:
------------------------
DOCUMENTATION : api.mota-analytica.io/business/(BUSINESS_ID_GOES_HERE)
------
EXAMPLES  *https://api.mota-analytica.io/business/qx6WhZ42eDKmBchZDax4dQ
          *https://api.mota-analytica.io/business/82g1PwX5FvclqqdjJHcVNA
-------
### NOTES:   These calls return a JSON file. These JSON files contain 50 reviews, with review text, yelp rating, and sentiment analysis rating.




## Performing Sentiment Analysis On User Input:
____________________________________________
### DOCUMENTATION:  api.mota-analytica.io/sentiment/(USER_REVIEW_GOES_HERE_SPACES_MUST_BE_UNDERSCORES)
------------
EXAMPLES  *https://api.mota-analytica.io/sentiment/I_love_to_hate_corporate_chains_but_I_could_not_find_fault_in_this
          *https://api.mota-analytica.io/sentiment/I_hated_this_restaurant
          *https://api.mota-analytica.io/sentiment/They_spilled_coffee_on_my_shirt_I_am_mad
          *https://api.mota-analytica.io/sentiment/they_made_a_mistake_and_I_was_originally_upset_but_the_management_was_very_professional_and_now_I_am_happy


----------
### NOTES: These calls return a JSON file. These JSON files contain a single number between 0 and 5. This number represents the predicted review score (X/5 Stars) (edited) 

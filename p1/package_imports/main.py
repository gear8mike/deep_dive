import common.validators as validators
import common
import common.models as models


validators.boolean.is_boolean("hello")
validators.date_helper_2('2025-01-01')

user = models.User()
post = models.Post("something")
posts = models.Posts()

# print('\n\n----common-----\n\n')
# for k in common.__dict__.keys():
#     print(k)


# print('\n\n----validators-----\n\n')
# for k in validators.__dict__.keys():
#     print(k)
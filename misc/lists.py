
"""
Matt Banham  3:12 PM @channel general point. this doesn't work.....
```py
def get_assessor_by_id(self, assessor_id) -> Optional[Assessor]:
    response = self._get('/api/user/get-by-id', {'mobile_user_id': assessor_id, 'full_details': True})
    users = self._convert_users_into_obj(response)
    if users is not []:
        return users[0]
    else:
        return None
```
you cannot do `if users is not []` .... because `[]` is a *first class object*. Therefore *one empty list is not the same as another empty list*. Instead you should do.....
```py
if len(users) < 1:
```
"""


def test_list(descrip, l):
    print(f'this is test_list() with var \'{descrip}\': {l}')
    print()

    # boolean value
    print(f'bool({descrip}): {bool(l)}')

    # length
    print(f'len({descrip}) == 0: {len(l) == 0}')

    # NOT the way to do it!
    # [] is a first class citizen i.e. object and *not the same object* as anything else
    print(f'{descrip} is []: {l is []}')

    # this works
    # if l == []:
    #     print('== []: True')
    # else:
    #     print('== []: False')
    print(f'{descrip} == []: {l == []}')

    # this works
    print(f'{descrip} != []: {l != []}')

    print()
    print()

# How to get the original variable name of variable passed to a function  (https://stackoverflow.com/questions/2749796/how-to-get-the-original-variable-name-of-variable-passed-to-a-function)
# TL;DNR: you can, but not easily

l_empty = []
l_nonempty = [1, 2]

test_list('l_empty', l_empty)
test_list('l_nonempty', l_nonempty)


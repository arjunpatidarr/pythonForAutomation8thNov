
#using approach 1

# from Animal import *
# from Bird import *
#
# fly()
# colour()


#If we want to use above approch than below is an solution of but in real time we can't use below approch beacuse every we need to call import statement

# from Bird import *
#
# fly()
# colour()
#
# from Animal import *
# fly()
# colour()


#Approach 2 - in such condition(similar names methods,functions available in module) we need to use these approach

import Animal, Bird

Animal.fly()
Animal.colour()
Bird.fly()
Bird.colour()
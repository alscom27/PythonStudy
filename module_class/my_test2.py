import test_package.say_hello, test_package.say_goodbye
import mod2

# import test_package

test_package.say_hello.hello()
test_package.say_goodbye.goodbye()

print(mod2.PI)
a = mod2.Math()
print(a.solv(2))
print(mod2.sum(mod2.PI, 4.4))

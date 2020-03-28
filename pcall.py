import testpackage.m1
import testpackage.m2
import testpackage.m4
# 不带*的明确引入不受__all__的影响

print(testpackage.sys.path)

a = testpackage.m1.CA('yfc','18')
print(a.name + "'s age is " + a.age)

print(testpackage.m1.va)
testpackage.m1.fa()
testpackage.m2.fb()

import pyquat
from pyquat import Quaternion as Q

q1 = Q(0.8, 0, 0, 1)
q2 = Q(0.11, 0.66, 0, 1)

q3 = q1 * q2

p = q3.transformPoint(1, 2, 3)
print("Transformed Point: {}".format(p))

q4 = pyquat.EulertoQuaternion([-0.6457718232379019, 0.2792526803190927, -0.43633231299858233])

q5 = Q.fromEuler([-0.6457718232379019, 0.2792526803190927, -0.43633231299858233])

q6 = Q.identity()

print("Is {} equal to {}? {}".format(q4, q5, q4 == q5))

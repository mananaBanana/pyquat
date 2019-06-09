import quaternion

q1 = quaternion.Quaternion(0.8, 0, 0, 1)
q2 = quaternion.Quaternion(0.11, 0.66, 0, 1)

q3 = q1 * q2

print(q3.transformPoint(1, 1, 1))

q4 = quaternion.EulertoQuaternion([-0.6457718232379019, 0.2792526803190927, -0.43633231299858233])

print(q4)

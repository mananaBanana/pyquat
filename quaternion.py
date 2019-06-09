import numpy as np

class Quaternion:
    def __init__(self, x, y, z, w):
        self.q = np.zeros((4), dtype='float32') # Quaternion of shape (1, 4) x, y, z, w format
        self.q[0] = x
        self.q[1] = y
        self.q[2] = z
        self.q[3] = w
        self.normalize()

    def __str__(self):
        return "{}".format(self.q)

    def norm(self):
        return np.sqrt(np.sum(np.square(self.q)))

    def normalize(self):
        self.q /= self.norm()

    @classmethod
    def fromEuler(self, euler, sequence = "ZYX"):
        X = euler[0]
        Y = euler[1]
        Z = euler[2]
        q_stack = []

        qX = self.__class__(np.sin(X/2), 0, 0, np.cos(X/2))
        qY = self.__class__(0, np.sin(Y/2), 0, np.cos(Y/2))
        qZ = self.__class__(0, 0, np.sin(Z/2), np.cos(Z/2))

        for axis in sequence:
            if axis == "X":
                q_stack.append(qX)
            elif axis == "Y":
                q_stack.append(qY)
            elif axix == "Z":
                q_stack.append(qZ)

        return (q_stack[0] * q_stack[1]) * q_stack[2]

    def x(self):
        return self.q[0]

    def y(self):
        return self.q[1]

    def z(self):
        return self.q[2]

    def w(self):
        return self.q[3]

    def __mul__(self, other):
        """
        Hamiltonian multiplication between two Quaternions
        """
        q_res = np.zeros((4), dtype='float32')
        q_res[0] = self.w() * other.x() + self.x() * other.w() + self.y() * other.z() - self.z() * other.y(); 
        q_res[1] = self.w() * other.y() - self.x() * other.z() + self.y() * other.w() + self.z() * other.x();
        q_res[2] = self.w() * other.z() + self.x() * other.y() - self.y() * other.x() + self.z() * other.w();
        q_res[3] = self.w() * other.w() - self.x() * other.x() - self.y() * other.y() - self.z() * other.z();

        return self.__class__(q_res[0], q_res[1], q_res[2], q_res[3])

    
    def inverse(self):
        """
        Invert the Quaternion. 
        Represents the inverse of the original rotation.
        Negate all complex values while retaining the sign of the scalar.
        """
        return self.__class__(-self.x(), -self.y(), -self.z(), self.w())

    def inverse_(self):
        """
        Invert Quaternion in-place.
        """
        self.q[0] = -self.x()
        self.q[1] = -self.y()
        self.q[2] = -self.z()

    def toRot(self):
        """
        Convert Quaternion into 3x3 Rotation matrix
        """
        return np.array([
            [1 - 2 * (self.y() * self.y() + self.z() * self.z()), 
                2 * (self.x() * self.y() - self.z() * self.w()), 
                2 * (self.x() * self.z() + self.y() * self.w())],
            [2 * (self.x() * self.y() + self.z() * self.w()), 
                1 - 2 * (self.x() * self.x() + self.z() * self.z()), 
                2 * (self.y() * self.z() - self.x() * self.w())],
            [2 * (self.x() * self.z() - self.y() * self.w()), 
                2 * (self.y() * self.z() + self.x() * self.w()), 
                1 - 2 * (self.x() * self.x() + self.y() * self.y())]
            ])

    def transformPoint(self, x, y, z, local2world=True):
        """
        Transform a point in 3D space using quaternion.
        :param local2world: boolean decide transformation direction
        :return: array of transformed points (3, 1)
        """
        if not local2world:
            self.inverse_()

        R = self.toRot()
        p = np.array([x, y, z])

        # Reverse the in-place inverse operation
        if not local2world:
            self.inverse_()

        return np.dot(R, p)

def EulertoQuaternion(euler, sequence="ZYX"):
        X = euler[0]
        Y = euler[1]
        Z = euler[2]
        q_stack = []

        qX = Quaternion(np.sin(X/2), 0, 0, np.cos(X/2))
        qY = Quaternion(0, np.sin(Y/2), 0, np.cos(Y/2))
        qZ = Quaternion(0, 0, np.sin(Z/2), np.cos(Z/2))

        for axis in sequence:
            if axis == "X":
                q_stack.append(qX)
            elif axis == "Y":
                q_stack.append(qY)
            elif axis == "Z":
                q_stack.append(qZ)

        return (q_stack[0] * q_stack[1]) * q_stack[2]

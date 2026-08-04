import rclpy
from rclpy.node import Node

from .inertia_calculator import InertialCalculator

class InertiaCalculatorNode(Node):

    def __init__(self):
        super().__init__('inertia_calculator_node')
        self._inertial_object = InertialCalculator()
    

    def loop(self):
        self._inertial_object.start_ask_loop()


def main(args=None):
    rclpy.init(args=args)

    node = InertiaCalculatorNode()

    try:
        node.loop()
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
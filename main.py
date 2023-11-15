from microscope.simulators import SimulatedStage, SimulatedFilterWheel
from microscope.simulators.stage_aware_camera import StageAwareCamera
from microscope import AxisLimits
import numpy as np

stage_aware_image = np.load("image.npy")

stage = SimulatedStage(limits={
    "x": AxisLimits(0, stage_aware_image.shape[1]),
    "y": AxisLimits(0, stage_aware_image.shape[0]),
    "z": AxisLimits(-50, 50)}
)
filterwheel = SimulatedFilterWheel(positions=3)
camera = StageAwareCamera(image=stage_aware_image, stage=stage, filterwheel=filterwheel)

camera.enable()

single_image = camera.grab_next_data()  # block until image is ready

stage.move_to({"x": 500, "y": 750, "z": 10})

filterwheel.position = 2  # move to position 2. position is a property. You an do set_position(2) as well

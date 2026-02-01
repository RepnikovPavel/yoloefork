# Ultralytics YOLO 🚀, AGPL-3.0 license

__version__ = "8.3.39"

import os

# Set ENV variables (place before imports)
if not os.environ.get("OMP_NUM_THREADS"):
    os.environ["OMP_NUM_THREADS"] = "1"  # default for reduced CPU utilization during training

from ultralytics.models import NAS, RTDETR, SAM, YOLO, FastSAM, YOLOE
from ultralytics.utils import ASSETS, SETTINGS
from ultralytics.utils.checks import check_yolo as checks
from ultralytics.utils.downloads import download
from ultralytics.nn import attempt_load_one_weight
from ultralytics.nn import attempt_load_weights
from ultralytics.nn import parse_model
from ultralytics.nn import yaml_model_load
from ultralytics.nn import guess_model_task
from ultralytics.nn import guess_model_scale
from ultralytics.nn import torch_safe_load
from ultralytics.nn import DetectionModel
from ultralytics.nn import SegmentationModel
from ultralytics.nn import ClassificationModel
from ultralytics.nn import BaseModel
from ultralytics.nn import MobileCLIP
from ultralytics.nn import CLIP

settings = SETTINGS
__all__ = (
    "__version__",
    "ASSETS",
    "YOLO",
    "YOLOE",
    "NAS",
    "SAM",
    "FastSAM",
    "RTDETR",
    "checks",
    "download",
    "settings",
    "attempt_load_one_weight",
    "attempt_load_weights",
    "parse_model",
    "yaml_model_load",
    "guess_model_task",
    "guess_model_scale",
    "torch_safe_load",
    "DetectionModel",
    "SegmentationModel",
    "ClassificationModel",
    "BaseModel",
    "MobileCLIP",
    "CLIP"
)


from typing import Tuple


def DT_TOKEN() -> str:
    # TODO: change this to your duckietown token
    dt_token = "dt1-3nT8KSoxVh4MnCdZZy2gDUYKtPTBbrsBEn6KmdLignRNMC8-43dzqWFnWd8KBa1yev1g3UKnzVxZkkTbfaJQeJk6pKzYq8zgwcc1Eg4xaeRXfrK1j6"
    return dt_token


def MODEL_NAME() -> str:
    # TODO: change this to your model's name that you used to upload it on google colab.
    # if you didn't change it, it should be "yolov5n"
    return "yolov5n"


def NUMBER_FRAMES_SKIPPED() -> int:
    # TODO: change this number to drop more frames
    # (must be a positive integer)
    return 1


def filter_by_classes(pred_class: int) -> bool:
    """
    Remember the class IDs:

        | Object    | ID    |
        | ---       | ---   |
        | Duckie    | 0     |
        | Cone      | 1     |
        | Truck     | 2     |
        | Bus       | 3     |


    Args:
        pred_class: the class of a prediction
    """
    # Right now, this returns True for every object's class
    # TODO: Change this to only return True for duckies!
    # In other words, returning False means that this prediction is ignored.
    if (pred_class == 0) :
        return True
    else: 
        return False


def filter_by_scores(score: float) -> bool:
    """
    Args:
        score: the confidence score of a prediction
    """
    # Right now, this returns True for every object's confidence
    # TODO: Change this to filter the scores, or not at all
    # (returning True for all of them might be the right thing to do!)
    if (score < 0.50): 
        return False
    else :
        return True


def filter_by_bboxes(bbox: Tuple[int, int, int, int]) -> bool:
    """
    Args:
        bbox: is the bounding box of a prediction, in xyxy format
                This means the shape of bbox is (leftmost x pixel, topmost y, rightmost x, bottommost y)
    """
    # TODO: Like in the other cases, return False if the bbox should not be considered.
    #print(bbox)
    midx = (bbox[0]/416+bbox[2]/416)/2
    area = (bbox[3]/416-bbox[1]/416) * (bbox[2]/416-bbox[0]/416)
    #print(midx)
    #print(area)
    #print((abs(midx-0.5)<0.2) and (area > 0.02))
    # return True when area >= 0.15*0.15=0.225, assunming bbos is a square
    # and the duckie is in the middle 60% of the sceen
    if ((abs(midx-0.5)<0.2) and (area > 0.02)):
        return True
    else :
        return False








        

#picaso
from picaso import justdoit as jdi
from picaso import justplotit as jpi
import numpy as np
import os
refdata = os.getenv("picaso_refdata")
print(refdata)

jpi.output_notebook()
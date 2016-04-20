#!/usr/bin/python3
from prog15 import tableau
from temps_recap import temps
from histo_recap import histogramme
from heures_semaine import semaine
from histo2 import histo
from Periode import periode_semaine
import time
import datetime
import random
import calendar
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
import pylab as plt


lst=tableau()
recap,time4,time3,time2,time=temps();
nb_heure,matiere=histogramme()
Semaine,nb_mat=semaine()

histo();
periode_semaine();

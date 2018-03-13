#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.3),
    on March 13, 2018, at 23:45
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'ling'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'C:\\Users\\Srujan\\Desktop\\Project\\jumbled_sentences\\ling.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1366, 768), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor=u'testMonitor', color=[0,0,0], colorSpace='hsv',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
instruct = visual.TextStim(win=win, name='instruct',
    text=u'The jumbled sentences are to be aranged in a order that seems chronologically right.\n\nSelect the letter corresponding to the correct order on the keyboard.',
    font=u'Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='hsv', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
sentence1 = visual.TextStim(win=win, name='sentence1',
    text='default text',
    font=u'Arial',
    pos=(0, 0.6), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0);
sentence6 = visual.TextStim(win=win, name='sentence6',
    text='default text',
    font=u'Arial',
    pos=(0, 0.5), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-2.0);
sentence2 = visual.TextStim(win=win, name='sentence2',
    text='default text',
    font=u'Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-3.0);
sentence3 = visual.TextStim(win=win, name='sentence3',
    text='default text',
    font=u'Arial',
    pos=(0, 0.1), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-4.0);
sentence4 = visual.TextStim(win=win, name='sentence4',
    text='default text',
    font=u'Arial',
    pos=(0, -0.1), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-5.0);
sentence5 = visual.TextStim(win=win, name='sentence5',
    text='default text',
    font=u'Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color=u'white', colorSpace='rgb', opacity=1,
    depth=-6.0);
optionstext = visual.TextStim(win=win, name='optionstext',
    text='default text',
    font=u'Arial',
    pos=(0, -0.6), height=0.05, wrapWidth=None, ori=0, 
    color=[1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-7.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
resp_2 = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [instruct, resp_2]
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instruct* updates
    if t >= 0.0 and instruct.status == NOT_STARTED:
        # keep track of start time/frame for later
        instruct.tStart = t
        instruct.frameNStart = frameN  # exact frame index
        instruct.setAutoDraw(True)
    
    # *resp_2* updates
    if t >= 0.0 and resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        resp_2.tStart = t
        resp_2.frameNStart = frameN  # exact frame index
        resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if resp_2.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            resp_2.keys = theseKeys[-1]  # just the last key pressed
            resp_2.rt = resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if resp_2.keys in ['', [], None]:  # No response was made
    resp_2.keys=None
thisExp.addData('resp_2.keys',resp_2.keys)
if resp_2.keys != None:  # we had a response
    thisExp.addData('resp_2.rt', resp_2.rt)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'conditions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(90.500000)
    # update component parameters for each repeat
    sentence1.setText(S1)
    key_resp_2 = event.BuilderKeyResponse()
    sentence6.setText(S6)
    sentence2.setText(P)
    sentence3.setText(Q)
    sentence4.setText(R)
    sentence5.setText(S)
    optionstext.setText(options)
    # keep track of which components have finished
    trialComponents = [sentence1, key_resp_2, sentence6, sentence2, sentence3, sentence4, sentence5, optionstext]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *sentence1* updates
        if t >= 0.5 and sentence1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence1.tStart = t
            sentence1.frameNStart = frameN  # exact frame index
            sentence1.setAutoDraw(True)
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sentence1.status == STARTED and t >= frameRemains:
            sentence1.setAutoDraw(False)
        
        # *key_resp_2* updates
        if t >= 0.5 and key_resp_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_2.tStart = t
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_2.status == STARTED and t >= frameRemains:
            key_resp_2.status = STOPPED
        if key_resp_2.status == STARTED:
            theseKeys = event.getKeys(keyList=['a', 'b', 'c', 'd'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_2.keys = theseKeys[-1]  # just the last key pressed
                key_resp_2.rt = key_resp_2.clock.getTime()
                # was this 'correct'?
                if (key_resp_2.keys == str(corrAns)) or (key_resp_2.keys == corrAns):
                    key_resp_2.corr = 1
                else:
                    key_resp_2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *sentence6* updates
        if t >= 0.5 and sentence6.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence6.tStart = t
            sentence6.frameNStart = frameN  # exact frame index
            sentence6.setAutoDraw(True)
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sentence6.status == STARTED and t >= frameRemains:
            sentence6.setAutoDraw(False)
        
        # *sentence2* updates
        if t >= 0.5 and sentence2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence2.tStart = t
            sentence2.frameNStart = frameN  # exact frame index
            sentence2.setAutoDraw(True)
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sentence2.status == STARTED and t >= frameRemains:
            sentence2.setAutoDraw(False)
        
        # *sentence3* updates
        if t >= 0.5 and sentence3.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence3.tStart = t
            sentence3.frameNStart = frameN  # exact frame index
            sentence3.setAutoDraw(True)
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sentence3.status == STARTED and t >= frameRemains:
            sentence3.setAutoDraw(False)
        
        # *sentence4* updates
        if t >= 0.5 and sentence4.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence4.tStart = t
            sentence4.frameNStart = frameN  # exact frame index
            sentence4.setAutoDraw(True)
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sentence4.status == STARTED and t >= frameRemains:
            sentence4.setAutoDraw(False)
        
        # *sentence5* updates
        if t >= 0.5 and sentence5.status == NOT_STARTED:
            # keep track of start time/frame for later
            sentence5.tStart = t
            sentence5.frameNStart = frameN  # exact frame index
            sentence5.setAutoDraw(True)
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if sentence5.status == STARTED and t >= frameRemains:
            sentence5.setAutoDraw(False)
        
        # *optionstext* updates
        if t >= 0.5 and optionstext.status == NOT_STARTED:
            # keep track of start time/frame for later
            optionstext.tStart = t
            optionstext.frameNStart = frameN  # exact frame index
            optionstext.setAutoDraw(True)
        frameRemains = 0.5 + 90- win.monitorFramePeriod * 0.75  # most of one frame period left
        if optionstext.status == STARTED and t >= frameRemains:
            optionstext.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_2.keys in ['', [], None]:  # No response was made
        key_resp_2.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           key_resp_2.corr = 1  # correct non-response
        else:
           key_resp_2.corr = 0  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('key_resp_2.keys',key_resp_2.keys)
    trials.addData('key_resp_2.corr', key_resp_2.corr)
    if key_resp_2.keys != None:  # we had a response
        trials.addData('key_resp_2.rt', key_resp_2.rt)
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()

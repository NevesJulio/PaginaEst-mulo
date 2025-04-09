﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.2.4),
    on abril 09, 2025, at 17:44
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from code
dados = []
# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.2.4'
expName = 'Estimulo_ICE'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = (1024, 768)
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='C:\\Users\\ICe\\Downloads\\Estimulo_psychopy_Builder-master\\Estimulo_psychopy_Builder-master\\Estimulo_ICE_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # set how much information should be printed to the console / app
    if PILOTING:
        logging.console.setLevel(
            prefs.piloting['pilotConsoleLoggingLevel']
        )
    else:
        logging.console.setLevel('warning')
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log')
    if PILOTING:
        logFile.setLevel(
            prefs.piloting['pilotLoggingLevel']
        )
    else:
        logFile.setLevel(
            logging.getLevel('info')
        )
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowGUI=False, allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height',
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win._monitorFrameRate = win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    # Setup iohub experiment
    ioConfig['Experiment'] = dict(filename=thisExp.dataFileName)
    
    # Start ioHub server
    ioServer = io.launchHubServer(window=win, **ioConfig)
    
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
        )
    if deviceManager.getDevice('key_resp_3') is None:
        # initialise key_resp_3
        key_resp_3 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_3',
        )
    if deviceManager.getDevice('key_resp_4') is None:
        # initialise key_resp_4
        key_resp_4 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_4',
        )
    if deviceManager.getDevice('key_resp_5') is None:
        # initialise key_resp_5
        key_resp_5 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_5',
        )
    if deviceManager.getDevice('key_resp_6') is None:
        # initialise key_resp_6
        key_resp_6 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_6',
        )
    if deviceManager.getDevice('key_resp_7') is None:
        # initialise key_resp_7
        key_resp_7 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_7',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # start a timer to figure out how long we're paused for
    pauseTimer = core.Clock()
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # sleep 1ms so other threads can execute
        clock.time.sleep(0.001)
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # reset any timers
    for timer in timers:
        timer.addTime(-pauseTimer.getTime())


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure window is set to foreground to prevent losing focus
    win.winHandle.activate()
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "salvar" ---
    
    # --- Initialize components for Routine "codigo" ---
    # Run 'Begin Experiment' code from code
    filename = "respostas_experimento.csv"
    
    # Criar o arquivo CSV e escrever o cabeçalho
    with open(filename, "w") as file:
        file.write("Loop,Tempo_Inicio,Tecla,Tempo_Pressao\n")  
    
    dados = []  # Lista para armazenar os dados temporariamente
    
    
    # --- Initialize components for Routine "trial" ---
    image = visual.ImageStim(
        win=win,
        name='image', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon = visual.ShapeStim(
        win=win, name='polygon',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_2" ---
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial" ---
    image = visual.ImageStim(
        win=win,
        name='image', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon = visual.ShapeStim(
        win=win, name='polygon',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_2" ---
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial" ---
    image = visual.ImageStim(
        win=win,
        name='image', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon = visual.ShapeStim(
        win=win, name='polygon',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_2" ---
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial" ---
    image = visual.ImageStim(
        win=win,
        name='image', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_2 = visual.ImageStim(
        win=win,
        name='image_2', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon = visual.ShapeStim(
        win=win, name='polygon',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    text = visual.TextStim(win=win, name='text',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_2" ---
    image_3 = visual.ImageStim(
        win=win,
        name='image_3', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_4 = visual.ImageStim(
        win=win,
        name='image_4', units='cm', 
        image='gaborVert.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_2 = visual.ShapeStim(
        win=win, name='polygon_2',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_3 = keyboard.Keyboard(deviceName='key_resp_3')
    text_2 = visual.TextStim(win=win, name='text_2',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_3" ---
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_3 = visual.ShapeStim(
        win=win, name='polygon_3',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_4" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_3" ---
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_3 = visual.ShapeStim(
        win=win, name='polygon_3',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_4" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_3" ---
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_3 = visual.ShapeStim(
        win=win, name='polygon_3',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_4" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_3" ---
    image_5 = visual.ImageStim(
        win=win,
        name='image_5', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_6 = visual.ImageStim(
        win=win,
        name='image_6', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_3 = visual.ShapeStim(
        win=win, name='polygon_3',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_4 = keyboard.Keyboard(deviceName='key_resp_4')
    text_3 = visual.TextStim(win=win, name='text_3',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_4" ---
    image_7 = visual.ImageStim(
        win=win,
        name='image_7', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_8 = visual.ImageStim(
        win=win,
        name='image_8', units='cm', 
        image='gaborHoriz.png', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_4 = visual.ShapeStim(
        win=win, name='polygon_4',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_5 = keyboard.Keyboard(deviceName='key_resp_5')
    text_4 = visual.TextStim(win=win, name='text_4',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_5" ---
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    polygon_6 = visual.ShapeStim(
        win=win, name='polygon_6',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-1.0, interpolate=True)
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-2.0)
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_6" ---
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_7 = visual.ShapeStim(
        win=win, name='polygon_7',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_5" ---
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    polygon_6 = visual.ShapeStim(
        win=win, name='polygon_6',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-1.0, interpolate=True)
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-2.0)
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_6" ---
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_7 = visual.ShapeStim(
        win=win, name='polygon_7',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_5" ---
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    polygon_6 = visual.ShapeStim(
        win=win, name='polygon_6',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-1.0, interpolate=True)
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-2.0)
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_6" ---
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_7 = visual.ShapeStim(
        win=win, name='polygon_7',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_5" ---
    image_9 = visual.ImageStim(
        win=win,
        name='image_9', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    polygon_6 = visual.ShapeStim(
        win=win, name='polygon_6',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-1.0, interpolate=True)
    image_10 = visual.ImageStim(
        win=win,
        name='image_10', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=True,
        texRes=128.0, interpolate=False, depth=-2.0)
    key_resp_6 = keyboard.Keyboard(deviceName='key_resp_6')
    text_5 = visual.TextStim(win=win, name='text_5',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "trial_6" ---
    image_11 = visual.ImageStim(
        win=win,
        name='image_11', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=0.0)
    image_12 = visual.ImageStim(
        win=win,
        name='image_12', units='cm', 
        image='controle.jpeg', mask=None, anchor='center',
        ori=0.0, pos=[0,0], draggable=False, size=(2, 2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=False, depth=-1.0)
    polygon_7 = visual.ShapeStim(
        win=win, name='polygon_7',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor=[-1.0000, 1.0000, -0.0039], fillColor=[-1.0000, 1.0000, -0.0039],
        opacity=None, depth=-2.0, interpolate=True)
    key_resp_7 = keyboard.Keyboard(deviceName='key_resp_7')
    text_6 = visual.TextStim(win=win, name='text_6',
        text='',
        font='Arial',
        pos=(0, 0), draggable=False, height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "_intertrial_interval_" ---
    polygon_5 = visual.ShapeStim(
        win=win, name='polygon_5',
        size=(0.005, 0.005), vertices='circle',
        ori=0.0, pos=(0, 0), draggable=False, anchor='center',
        lineWidth=1.0,
        colorSpace='rgb', lineColor='red', fillColor='red',
        opacity=None, depth=0.0, interpolate=True)
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "salvar" ---
    # create an object to store info about Routine salvar
    salvar = data.Routine(
        name='salvar',
        components=[],
    )
    salvar.status = NOT_STARTED
    continueRoutine = True
    # update component parameters for each repeat
    # store start times for salvar
    salvar.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
    salvar.tStart = globalClock.getTime(format='float')
    salvar.status = STARTED
    thisExp.addData('salvar.started', salvar.tStart)
    salvar.maxDuration = None
    # keep track of which components have finished
    salvarComponents = salvar.components
    for thisComponent in salvar.components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "salvar" ---
    salvar.forceEnded = routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from code_2
        
        print(key_resp_2.keys)
        print(key_resp_3.keys)
        print(key_resp_4.keys)
        print(key_resp_5.keys)
        print(key_resp_6.keys)
        print(key_resp_7.keys)
        
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
            )
            # skip the frame we paused on
            continue
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            salvar.forceEnded = routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in salvar.components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "salvar" ---
    for thisComponent in salvar.components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # store stop times for salvar
    salvar.tStop = globalClock.getTime(format='float')
    salvar.tStopRefresh = tThisFlipGlobal
    thisExp.addData('salvar.stopped', salvar.tStop)
    thisExp.nextEntry()
    # the Routine "salvar" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    MainLoop = data.TrialHandler2(
        name='MainLoop',
        nReps=8.0, 
        method='random', 
        extraInfo=expInfo, 
        originPath=-1, 
        trialList=data.importConditions('Estimulos.csv'), 
        seed=None, 
    )
    thisExp.addLoop(MainLoop)  # add the loop to the experiment
    thisMainLoop = MainLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
    if thisMainLoop != None:
        for paramName in thisMainLoop:
            globals()[paramName] = thisMainLoop[paramName]
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    
    for thisMainLoop in MainLoop:
        currentLoop = MainLoop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        # abbreviate parameter names if possible (e.g. rgb = thisMainLoop.rgb)
        if thisMainLoop != None:
            for paramName in thisMainLoop:
                globals()[paramName] = thisMainLoop[paramName]
        
        # --- Prepare to start Routine "codigo" ---
        # create an object to store info about Routine codigo
        codigo = data.Routine(
            name='codigo',
            components=[],
        )
        codigo.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # Run 'Begin Routine' code from code
        loop_start_time = core.getTime()  # Registra o tempo do início da repetição
        
        # store start times for codigo
        codigo.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        codigo.tStart = globalClock.getTime(format='float')
        codigo.status = STARTED
        thisExp.addData('codigo.started', codigo.tStart)
        codigo.maxDuration = None
        # keep track of which components have finished
        codigoComponents = codigo.components
        for thisComponent in codigo.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "codigo" ---
        # if trial has changed, end Routine now
        if isinstance(MainLoop, data.TrialHandler2) and thisMainLoop.thisN != MainLoop.thisTrial.thisN:
            continueRoutine = False
        codigo.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from code
            
            
            if key_resp_2.keys == 'right' or key_resp_3.keys == 'right' or key_resp_4.keys == 'right' or key_resp_5.keys == 'right' or key_resp_6.keys == 'right' or key_resp_7.keys == 'right':  # key_resp_2 para o Estímulo 1
                print('right')
            
            if LoopName == 'Estimulo_1':
                rep1 = 1
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            elif LoopName == 'Estimulo_2':
                rep1 = 0
                rep2 = 1
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            elif LoopName == 'Estimulo_3':
                rep1 = 0
                rep2 = 0
                rep3 = 1
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            elif LoopName == 'Estimulo_4':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 1
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            elif LoopName == 'Estimulo_5':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 1
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            
            elif LoopName == 'Estimulo_6':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 1
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            elif LoopName == 'Estimulo_7':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 1
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            elif LoopName == 'Estimulo_8':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 1
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
            
            elif LoopName == 'Estimulo_9':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 1
                rep10 = 0
                rep11 = 0
                rep12 = 0
            
                
            elif LoopName == 'Estimulo_10':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 1
                rep11 = 0
                rep12 = 0
            
            
                
            elif LoopName == 'Estimulo_11':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 1
                rep12 = 0
            
                
            elif LoopName == 'Estimulo_12':
                rep1 = 0
                rep2 = 0
                rep3 = 0
                rep4 = 0
                rep5 = 0
                rep6 = 0
                rep7 = 0
                rep8 = 0
                rep9 = 0
                rep10 = 0
                rep11 = 0
                rep12 = 1
            
                
            
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                codigo.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in codigo.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "codigo" ---
        for thisComponent in codigo.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for codigo
        codigo.tStop = globalClock.getTime(format='float')
        codigo.tStopRefresh = tThisFlipGlobal
        thisExp.addData('codigo.stopped', codigo.tStop)
        # Run 'End Routine' code from code
        print(dados)
        # the Routine "codigo" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        loop_1 = data.TrialHandler2(
            name='loop_1',
            nReps=rep1, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('Incrementos.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_1)  # add the loop to the experiment
        thisLoop_1 = loop_1.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
        if thisLoop_1 != None:
            for paramName in thisLoop_1:
                globals()[paramName] = thisLoop_1[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_1 in loop_1:
            currentLoop = loop_1
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_1.rgb)
            if thisLoop_1 != None:
                for paramName in thisLoop_1:
                    globals()[paramName] = thisLoop_1[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[image, image_2, polygon, key_resp_2, text],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image.setPos((px1, py1))
            image_2.setPos((px2, py2))
            # create starting attributes for key_resp_2
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            # if trial has changed, end Routine now
            if isinstance(loop_1, data.TrialHandler2) and thisLoop_1.thisN != loop_1.thisTrial.thisN:
                continueRoutine = False
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.tStopRefresh = tThisFlipGlobal  # on global time
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # *image_2* updates
                
                # if image_2 is starting this frame...
                if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.tStart = t  # local t and not account for scr refresh
                    image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.started')
                    # update status
                    image_2.status = STARTED
                    image_2.setAutoDraw(True)
                
                # if image_2 is active this frame...
                if image_2.status == STARTED:
                    # update params
                    pass
                
                # if image_2 is stopping this frame...
                if image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_2.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2.tStop = t  # not accounting for scr refresh
                        image_2.tStopRefresh = tThisFlipGlobal  # on global time
                        image_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2.stopped')
                        # update status
                        image_2.status = FINISHED
                        image_2.setAutoDraw(False)
                
                # *polygon* updates
                
                # if polygon is starting this frame...
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    # update status
                    polygon.status = STARTED
                    polygon.setAutoDraw(True)
                
                # if polygon is active this frame...
                if polygon.status == STARTED:
                    # update params
                    pass
                
                # if polygon is stopping this frame...
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        # update status
                        polygon.status = FINISHED
                        polygon.setAutoDraw(False)
                
                # *key_resp_2* updates
                waitOnFlip = False
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.started')
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_2 is stopping this frame...
                if key_resp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_2.tStop = t  # not accounting for scr refresh
                        key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                        # update status
                        key_resp_2.status = FINISHED
                        key_resp_2.status = FINISHED
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                        key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                        key_resp_2.duration = [key.duration for key in _key_resp_2_allKeys]
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    text.setText(globalClock.getTime()
                    , log=False)
                
                # if text is stopping this frame...
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.tStopRefresh = tThisFlipGlobal  # on global time
                        text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.stopped')
                        # update status
                        text.status = FINISHED
                        text.setAutoDraw(False)
                # Run 'Each Frame' code from code_3
                if key_resp_2.keys:
                    dados.extend(zip(key_resp_2.keys, [globalClock.getTime()] * len(key_resp_2.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            loop_1.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                loop_1.addData('key_resp_2.rt', key_resp_2.rt)
                loop_1.addData('key_resp_2.duration', key_resp_2.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial.maxDurationReached:
                routineTimer.addTime(-trial.maxDuration)
            elif trial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_2" ---
            # create an object to store info about Routine trial_2
            trial_2 = data.Routine(
                name='trial_2',
                components=[image_3, image_4, polygon_2, key_resp_3, text_2],
            )
            trial_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_3.setPos((px3, py3))
            image_4.setPos((px4,py4))
            # create starting attributes for key_resp_3
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # store start times for trial_2
            trial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_2.tStart = globalClock.getTime(format='float')
            trial_2.status = STARTED
            thisExp.addData('trial_2.started', trial_2.tStart)
            trial_2.maxDuration = None
            # keep track of which components have finished
            trial_2Components = trial_2.components
            for thisComponent in trial_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_2" ---
            # if trial has changed, end Routine now
            if isinstance(loop_1, data.TrialHandler2) and thisLoop_1.thisN != loop_1.thisTrial.thisN:
                continueRoutine = False
            trial_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_3* updates
                
                # if image_3 is starting this frame...
                if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_3.frameNStart = frameN  # exact frame index
                    image_3.tStart = t  # local t and not account for scr refresh
                    image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_3.started')
                    # update status
                    image_3.status = STARTED
                    image_3.setAutoDraw(True)
                
                # if image_3 is active this frame...
                if image_3.status == STARTED:
                    # update params
                    pass
                
                # if image_3 is stopping this frame...
                if image_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_3.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_3.tStop = t  # not accounting for scr refresh
                        image_3.tStopRefresh = tThisFlipGlobal  # on global time
                        image_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_3.stopped')
                        # update status
                        image_3.status = FINISHED
                        image_3.setAutoDraw(False)
                
                # *image_4* updates
                
                # if image_4 is starting this frame...
                if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_4.frameNStart = frameN  # exact frame index
                    image_4.tStart = t  # local t and not account for scr refresh
                    image_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_4.started')
                    # update status
                    image_4.status = STARTED
                    image_4.setAutoDraw(True)
                
                # if image_4 is active this frame...
                if image_4.status == STARTED:
                    # update params
                    pass
                
                # if image_4 is stopping this frame...
                if image_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_4.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_4.tStop = t  # not accounting for scr refresh
                        image_4.tStopRefresh = tThisFlipGlobal  # on global time
                        image_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_4.stopped')
                        # update status
                        image_4.status = FINISHED
                        image_4.setAutoDraw(False)
                
                # *polygon_2* updates
                
                # if polygon_2 is starting this frame...
                if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_2.frameNStart = frameN  # exact frame index
                    polygon_2.tStart = t  # local t and not account for scr refresh
                    polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.started')
                    # update status
                    polygon_2.status = STARTED
                    polygon_2.setAutoDraw(True)
                
                # if polygon_2 is active this frame...
                if polygon_2.status == STARTED:
                    # update params
                    pass
                
                # if polygon_2 is stopping this frame...
                if polygon_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_2.tStop = t  # not accounting for scr refresh
                        polygon_2.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                        # update status
                        polygon_2.status = FINISHED
                        polygon_2.setAutoDraw(False)
                
                # *key_resp_3* updates
                waitOnFlip = False
                
                # if key_resp_3 is starting this frame...
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    # update status
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_3 is stopping this frame...
                if key_resp_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_3.tStop = t  # not accounting for scr refresh
                        key_resp_3.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                        # update status
                        key_resp_3.status = FINISHED
                        key_resp_3.status = FINISHED
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                        key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                        key_resp_3.duration = [key.duration for key in _key_resp_3_allKeys]
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    text_2.setText(globalClock.getTime()
                    , log=False)
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                # Run 'Each Frame' code from code_4
                
                if key_resp_3.keys:
                    dados.extend(zip(key_resp_3.keys, [globalClock.getTime()] * len(key_resp_3.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_2" ---
            for thisComponent in trial_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_2
            trial_2.tStop = globalClock.getTime(format='float')
            trial_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_2.stopped', trial_2.tStop)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
            loop_1.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                loop_1.addData('key_resp_3.rt', key_resp_3.rt)
                loop_1.addData('key_resp_3.duration', key_resp_3.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_2.maxDurationReached:
                routineTimer.addTime(-trial_2.maxDuration)
            elif trial_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep1 repeats of 'loop_1'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_2 = data.TrialHandler2(
            name='loop_2',
            nReps=rep2, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('incremento_loop2.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_2)  # add the loop to the experiment
        thisLoop_2 = loop_2.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_2.rgb)
        if thisLoop_2 != None:
            for paramName in thisLoop_2:
                globals()[paramName] = thisLoop_2[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_2 in loop_2:
            currentLoop = loop_2
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_2.rgb)
            if thisLoop_2 != None:
                for paramName in thisLoop_2:
                    globals()[paramName] = thisLoop_2[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[image, image_2, polygon, key_resp_2, text],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image.setPos((px1, py1))
            image_2.setPos((px2, py2))
            # create starting attributes for key_resp_2
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            # if trial has changed, end Routine now
            if isinstance(loop_2, data.TrialHandler2) and thisLoop_2.thisN != loop_2.thisTrial.thisN:
                continueRoutine = False
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.tStopRefresh = tThisFlipGlobal  # on global time
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # *image_2* updates
                
                # if image_2 is starting this frame...
                if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.tStart = t  # local t and not account for scr refresh
                    image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.started')
                    # update status
                    image_2.status = STARTED
                    image_2.setAutoDraw(True)
                
                # if image_2 is active this frame...
                if image_2.status == STARTED:
                    # update params
                    pass
                
                # if image_2 is stopping this frame...
                if image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_2.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2.tStop = t  # not accounting for scr refresh
                        image_2.tStopRefresh = tThisFlipGlobal  # on global time
                        image_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2.stopped')
                        # update status
                        image_2.status = FINISHED
                        image_2.setAutoDraw(False)
                
                # *polygon* updates
                
                # if polygon is starting this frame...
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    # update status
                    polygon.status = STARTED
                    polygon.setAutoDraw(True)
                
                # if polygon is active this frame...
                if polygon.status == STARTED:
                    # update params
                    pass
                
                # if polygon is stopping this frame...
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        # update status
                        polygon.status = FINISHED
                        polygon.setAutoDraw(False)
                
                # *key_resp_2* updates
                waitOnFlip = False
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.started')
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_2 is stopping this frame...
                if key_resp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_2.tStop = t  # not accounting for scr refresh
                        key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                        # update status
                        key_resp_2.status = FINISHED
                        key_resp_2.status = FINISHED
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                        key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                        key_resp_2.duration = [key.duration for key in _key_resp_2_allKeys]
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    text.setText(globalClock.getTime()
                    , log=False)
                
                # if text is stopping this frame...
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.tStopRefresh = tThisFlipGlobal  # on global time
                        text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.stopped')
                        # update status
                        text.status = FINISHED
                        text.setAutoDraw(False)
                # Run 'Each Frame' code from code_3
                if key_resp_2.keys:
                    dados.extend(zip(key_resp_2.keys, [globalClock.getTime()] * len(key_resp_2.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            loop_2.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                loop_2.addData('key_resp_2.rt', key_resp_2.rt)
                loop_2.addData('key_resp_2.duration', key_resp_2.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial.maxDurationReached:
                routineTimer.addTime(-trial.maxDuration)
            elif trial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_2" ---
            # create an object to store info about Routine trial_2
            trial_2 = data.Routine(
                name='trial_2',
                components=[image_3, image_4, polygon_2, key_resp_3, text_2],
            )
            trial_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_3.setPos((px3, py3))
            image_4.setPos((px4,py4))
            # create starting attributes for key_resp_3
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # store start times for trial_2
            trial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_2.tStart = globalClock.getTime(format='float')
            trial_2.status = STARTED
            thisExp.addData('trial_2.started', trial_2.tStart)
            trial_2.maxDuration = None
            # keep track of which components have finished
            trial_2Components = trial_2.components
            for thisComponent in trial_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_2" ---
            # if trial has changed, end Routine now
            if isinstance(loop_2, data.TrialHandler2) and thisLoop_2.thisN != loop_2.thisTrial.thisN:
                continueRoutine = False
            trial_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_3* updates
                
                # if image_3 is starting this frame...
                if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_3.frameNStart = frameN  # exact frame index
                    image_3.tStart = t  # local t and not account for scr refresh
                    image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_3.started')
                    # update status
                    image_3.status = STARTED
                    image_3.setAutoDraw(True)
                
                # if image_3 is active this frame...
                if image_3.status == STARTED:
                    # update params
                    pass
                
                # if image_3 is stopping this frame...
                if image_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_3.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_3.tStop = t  # not accounting for scr refresh
                        image_3.tStopRefresh = tThisFlipGlobal  # on global time
                        image_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_3.stopped')
                        # update status
                        image_3.status = FINISHED
                        image_3.setAutoDraw(False)
                
                # *image_4* updates
                
                # if image_4 is starting this frame...
                if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_4.frameNStart = frameN  # exact frame index
                    image_4.tStart = t  # local t and not account for scr refresh
                    image_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_4.started')
                    # update status
                    image_4.status = STARTED
                    image_4.setAutoDraw(True)
                
                # if image_4 is active this frame...
                if image_4.status == STARTED:
                    # update params
                    pass
                
                # if image_4 is stopping this frame...
                if image_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_4.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_4.tStop = t  # not accounting for scr refresh
                        image_4.tStopRefresh = tThisFlipGlobal  # on global time
                        image_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_4.stopped')
                        # update status
                        image_4.status = FINISHED
                        image_4.setAutoDraw(False)
                
                # *polygon_2* updates
                
                # if polygon_2 is starting this frame...
                if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_2.frameNStart = frameN  # exact frame index
                    polygon_2.tStart = t  # local t and not account for scr refresh
                    polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.started')
                    # update status
                    polygon_2.status = STARTED
                    polygon_2.setAutoDraw(True)
                
                # if polygon_2 is active this frame...
                if polygon_2.status == STARTED:
                    # update params
                    pass
                
                # if polygon_2 is stopping this frame...
                if polygon_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_2.tStop = t  # not accounting for scr refresh
                        polygon_2.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                        # update status
                        polygon_2.status = FINISHED
                        polygon_2.setAutoDraw(False)
                
                # *key_resp_3* updates
                waitOnFlip = False
                
                # if key_resp_3 is starting this frame...
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    # update status
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_3 is stopping this frame...
                if key_resp_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_3.tStop = t  # not accounting for scr refresh
                        key_resp_3.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                        # update status
                        key_resp_3.status = FINISHED
                        key_resp_3.status = FINISHED
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                        key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                        key_resp_3.duration = [key.duration for key in _key_resp_3_allKeys]
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    text_2.setText(globalClock.getTime()
                    , log=False)
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                # Run 'Each Frame' code from code_4
                
                if key_resp_3.keys:
                    dados.extend(zip(key_resp_3.keys, [globalClock.getTime()] * len(key_resp_3.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_2" ---
            for thisComponent in trial_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_2
            trial_2.tStop = globalClock.getTime(format='float')
            trial_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_2.stopped', trial_2.tStop)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
            loop_2.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                loop_2.addData('key_resp_3.rt', key_resp_3.rt)
                loop_2.addData('key_resp_3.duration', key_resp_3.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_2.maxDurationReached:
                routineTimer.addTime(-trial_2.maxDuration)
            elif trial_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep2 repeats of 'loop_2'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_3 = data.TrialHandler2(
            name='loop_3',
            nReps=rep3, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('incremento_loop3.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_3)  # add the loop to the experiment
        thisLoop_3 = loop_3.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_3.rgb)
        if thisLoop_3 != None:
            for paramName in thisLoop_3:
                globals()[paramName] = thisLoop_3[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_3 in loop_3:
            currentLoop = loop_3
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_3.rgb)
            if thisLoop_3 != None:
                for paramName in thisLoop_3:
                    globals()[paramName] = thisLoop_3[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[image, image_2, polygon, key_resp_2, text],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image.setPos((px1, py1))
            image_2.setPos((px2, py2))
            # create starting attributes for key_resp_2
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            # if trial has changed, end Routine now
            if isinstance(loop_3, data.TrialHandler2) and thisLoop_3.thisN != loop_3.thisTrial.thisN:
                continueRoutine = False
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.tStopRefresh = tThisFlipGlobal  # on global time
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # *image_2* updates
                
                # if image_2 is starting this frame...
                if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.tStart = t  # local t and not account for scr refresh
                    image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.started')
                    # update status
                    image_2.status = STARTED
                    image_2.setAutoDraw(True)
                
                # if image_2 is active this frame...
                if image_2.status == STARTED:
                    # update params
                    pass
                
                # if image_2 is stopping this frame...
                if image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_2.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2.tStop = t  # not accounting for scr refresh
                        image_2.tStopRefresh = tThisFlipGlobal  # on global time
                        image_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2.stopped')
                        # update status
                        image_2.status = FINISHED
                        image_2.setAutoDraw(False)
                
                # *polygon* updates
                
                # if polygon is starting this frame...
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    # update status
                    polygon.status = STARTED
                    polygon.setAutoDraw(True)
                
                # if polygon is active this frame...
                if polygon.status == STARTED:
                    # update params
                    pass
                
                # if polygon is stopping this frame...
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        # update status
                        polygon.status = FINISHED
                        polygon.setAutoDraw(False)
                
                # *key_resp_2* updates
                waitOnFlip = False
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.started')
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_2 is stopping this frame...
                if key_resp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_2.tStop = t  # not accounting for scr refresh
                        key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                        # update status
                        key_resp_2.status = FINISHED
                        key_resp_2.status = FINISHED
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                        key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                        key_resp_2.duration = [key.duration for key in _key_resp_2_allKeys]
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    text.setText(globalClock.getTime()
                    , log=False)
                
                # if text is stopping this frame...
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.tStopRefresh = tThisFlipGlobal  # on global time
                        text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.stopped')
                        # update status
                        text.status = FINISHED
                        text.setAutoDraw(False)
                # Run 'Each Frame' code from code_3
                if key_resp_2.keys:
                    dados.extend(zip(key_resp_2.keys, [globalClock.getTime()] * len(key_resp_2.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            loop_3.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                loop_3.addData('key_resp_2.rt', key_resp_2.rt)
                loop_3.addData('key_resp_2.duration', key_resp_2.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial.maxDurationReached:
                routineTimer.addTime(-trial.maxDuration)
            elif trial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_2" ---
            # create an object to store info about Routine trial_2
            trial_2 = data.Routine(
                name='trial_2',
                components=[image_3, image_4, polygon_2, key_resp_3, text_2],
            )
            trial_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_3.setPos((px3, py3))
            image_4.setPos((px4,py4))
            # create starting attributes for key_resp_3
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # store start times for trial_2
            trial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_2.tStart = globalClock.getTime(format='float')
            trial_2.status = STARTED
            thisExp.addData('trial_2.started', trial_2.tStart)
            trial_2.maxDuration = None
            # keep track of which components have finished
            trial_2Components = trial_2.components
            for thisComponent in trial_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_2" ---
            # if trial has changed, end Routine now
            if isinstance(loop_3, data.TrialHandler2) and thisLoop_3.thisN != loop_3.thisTrial.thisN:
                continueRoutine = False
            trial_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_3* updates
                
                # if image_3 is starting this frame...
                if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_3.frameNStart = frameN  # exact frame index
                    image_3.tStart = t  # local t and not account for scr refresh
                    image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_3.started')
                    # update status
                    image_3.status = STARTED
                    image_3.setAutoDraw(True)
                
                # if image_3 is active this frame...
                if image_3.status == STARTED:
                    # update params
                    pass
                
                # if image_3 is stopping this frame...
                if image_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_3.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_3.tStop = t  # not accounting for scr refresh
                        image_3.tStopRefresh = tThisFlipGlobal  # on global time
                        image_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_3.stopped')
                        # update status
                        image_3.status = FINISHED
                        image_3.setAutoDraw(False)
                
                # *image_4* updates
                
                # if image_4 is starting this frame...
                if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_4.frameNStart = frameN  # exact frame index
                    image_4.tStart = t  # local t and not account for scr refresh
                    image_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_4.started')
                    # update status
                    image_4.status = STARTED
                    image_4.setAutoDraw(True)
                
                # if image_4 is active this frame...
                if image_4.status == STARTED:
                    # update params
                    pass
                
                # if image_4 is stopping this frame...
                if image_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_4.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_4.tStop = t  # not accounting for scr refresh
                        image_4.tStopRefresh = tThisFlipGlobal  # on global time
                        image_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_4.stopped')
                        # update status
                        image_4.status = FINISHED
                        image_4.setAutoDraw(False)
                
                # *polygon_2* updates
                
                # if polygon_2 is starting this frame...
                if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_2.frameNStart = frameN  # exact frame index
                    polygon_2.tStart = t  # local t and not account for scr refresh
                    polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.started')
                    # update status
                    polygon_2.status = STARTED
                    polygon_2.setAutoDraw(True)
                
                # if polygon_2 is active this frame...
                if polygon_2.status == STARTED:
                    # update params
                    pass
                
                # if polygon_2 is stopping this frame...
                if polygon_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_2.tStop = t  # not accounting for scr refresh
                        polygon_2.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                        # update status
                        polygon_2.status = FINISHED
                        polygon_2.setAutoDraw(False)
                
                # *key_resp_3* updates
                waitOnFlip = False
                
                # if key_resp_3 is starting this frame...
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    # update status
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_3 is stopping this frame...
                if key_resp_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_3.tStop = t  # not accounting for scr refresh
                        key_resp_3.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                        # update status
                        key_resp_3.status = FINISHED
                        key_resp_3.status = FINISHED
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                        key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                        key_resp_3.duration = [key.duration for key in _key_resp_3_allKeys]
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    text_2.setText(globalClock.getTime()
                    , log=False)
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                # Run 'Each Frame' code from code_4
                
                if key_resp_3.keys:
                    dados.extend(zip(key_resp_3.keys, [globalClock.getTime()] * len(key_resp_3.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_2" ---
            for thisComponent in trial_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_2
            trial_2.tStop = globalClock.getTime(format='float')
            trial_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_2.stopped', trial_2.tStop)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
            loop_3.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                loop_3.addData('key_resp_3.rt', key_resp_3.rt)
                loop_3.addData('key_resp_3.duration', key_resp_3.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_2.maxDurationReached:
                routineTimer.addTime(-trial_2.maxDuration)
            elif trial_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep3 repeats of 'loop_3'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_4 = data.TrialHandler2(
            name='loop_4',
            nReps=rep4, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('Incrementos_loop_4.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_4)  # add the loop to the experiment
        thisLoop_4 = loop_4.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_4.rgb)
        if thisLoop_4 != None:
            for paramName in thisLoop_4:
                globals()[paramName] = thisLoop_4[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_4 in loop_4:
            currentLoop = loop_4
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_4.rgb)
            if thisLoop_4 != None:
                for paramName in thisLoop_4:
                    globals()[paramName] = thisLoop_4[paramName]
            
            # --- Prepare to start Routine "trial" ---
            # create an object to store info about Routine trial
            trial = data.Routine(
                name='trial',
                components=[image, image_2, polygon, key_resp_2, text],
            )
            trial.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image.setPos((px1, py1))
            image_2.setPos((px2, py2))
            # create starting attributes for key_resp_2
            key_resp_2.keys = []
            key_resp_2.rt = []
            _key_resp_2_allKeys = []
            # store start times for trial
            trial.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial.tStart = globalClock.getTime(format='float')
            trial.status = STARTED
            thisExp.addData('trial.started', trial.tStart)
            trial.maxDuration = None
            # keep track of which components have finished
            trialComponents = trial.components
            for thisComponent in trial.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial" ---
            # if trial has changed, end Routine now
            if isinstance(loop_4, data.TrialHandler2) and thisLoop_4.thisN != loop_4.thisTrial.thisN:
                continueRoutine = False
            trial.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image* updates
                
                # if image is starting this frame...
                if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image.frameNStart = frameN  # exact frame index
                    image.tStart = t  # local t and not account for scr refresh
                    image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image.started')
                    # update status
                    image.status = STARTED
                    image.setAutoDraw(True)
                
                # if image is active this frame...
                if image.status == STARTED:
                    # update params
                    pass
                
                # if image is stopping this frame...
                if image.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image.tStop = t  # not accounting for scr refresh
                        image.tStopRefresh = tThisFlipGlobal  # on global time
                        image.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image.stopped')
                        # update status
                        image.status = FINISHED
                        image.setAutoDraw(False)
                
                # *image_2* updates
                
                # if image_2 is starting this frame...
                if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_2.frameNStart = frameN  # exact frame index
                    image_2.tStart = t  # local t and not account for scr refresh
                    image_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_2.started')
                    # update status
                    image_2.status = STARTED
                    image_2.setAutoDraw(True)
                
                # if image_2 is active this frame...
                if image_2.status == STARTED:
                    # update params
                    pass
                
                # if image_2 is stopping this frame...
                if image_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_2.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_2.tStop = t  # not accounting for scr refresh
                        image_2.tStopRefresh = tThisFlipGlobal  # on global time
                        image_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_2.stopped')
                        # update status
                        image_2.status = FINISHED
                        image_2.setAutoDraw(False)
                
                # *polygon* updates
                
                # if polygon is starting this frame...
                if polygon.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    # update status
                    polygon.status = STARTED
                    polygon.setAutoDraw(True)
                
                # if polygon is active this frame...
                if polygon.status == STARTED:
                    # update params
                    pass
                
                # if polygon is stopping this frame...
                if polygon.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        # update status
                        polygon.status = FINISHED
                        polygon.setAutoDraw(False)
                
                # *key_resp_2* updates
                waitOnFlip = False
                
                # if key_resp_2 is starting this frame...
                if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_2.frameNStart = frameN  # exact frame index
                    key_resp_2.tStart = t  # local t and not account for scr refresh
                    key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_2.started')
                    # update status
                    key_resp_2.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_2 is stopping this frame...
                if key_resp_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_2.tStop = t  # not accounting for scr refresh
                        key_resp_2.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_2.stopped')
                        # update status
                        key_resp_2.status = FINISHED
                        key_resp_2.status = FINISHED
                if key_resp_2.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_2.getKeys(keyList=None, ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_2_allKeys.extend(theseKeys)
                    if len(_key_resp_2_allKeys):
                        key_resp_2.keys = [key.name for key in _key_resp_2_allKeys]  # storing all keys
                        key_resp_2.rt = [key.rt for key in _key_resp_2_allKeys]
                        key_resp_2.duration = [key.duration for key in _key_resp_2_allKeys]
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    text.setText(globalClock.getTime()
                    , log=False)
                
                # if text is stopping this frame...
                if text.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.tStopRefresh = tThisFlipGlobal  # on global time
                        text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.stopped')
                        # update status
                        text.status = FINISHED
                        text.setAutoDraw(False)
                # Run 'Each Frame' code from code_3
                if key_resp_2.keys:
                    dados.extend(zip(key_resp_2.keys, [globalClock.getTime()] * len(key_resp_2.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trial.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial
            trial.tStop = globalClock.getTime(format='float')
            trial.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial.stopped', trial.tStop)
            # check responses
            if key_resp_2.keys in ['', [], None]:  # No response was made
                key_resp_2.keys = None
            loop_4.addData('key_resp_2.keys',key_resp_2.keys)
            if key_resp_2.keys != None:  # we had a response
                loop_4.addData('key_resp_2.rt', key_resp_2.rt)
                loop_4.addData('key_resp_2.duration', key_resp_2.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial.maxDurationReached:
                routineTimer.addTime(-trial.maxDuration)
            elif trial.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_2" ---
            # create an object to store info about Routine trial_2
            trial_2 = data.Routine(
                name='trial_2',
                components=[image_3, image_4, polygon_2, key_resp_3, text_2],
            )
            trial_2.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_3.setPos((px3, py3))
            image_4.setPos((px4,py4))
            # create starting attributes for key_resp_3
            key_resp_3.keys = []
            key_resp_3.rt = []
            _key_resp_3_allKeys = []
            # store start times for trial_2
            trial_2.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_2.tStart = globalClock.getTime(format='float')
            trial_2.status = STARTED
            thisExp.addData('trial_2.started', trial_2.tStart)
            trial_2.maxDuration = None
            # keep track of which components have finished
            trial_2Components = trial_2.components
            for thisComponent in trial_2.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_2" ---
            # if trial has changed, end Routine now
            if isinstance(loop_4, data.TrialHandler2) and thisLoop_4.thisN != loop_4.thisTrial.thisN:
                continueRoutine = False
            trial_2.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_3* updates
                
                # if image_3 is starting this frame...
                if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_3.frameNStart = frameN  # exact frame index
                    image_3.tStart = t  # local t and not account for scr refresh
                    image_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_3.started')
                    # update status
                    image_3.status = STARTED
                    image_3.setAutoDraw(True)
                
                # if image_3 is active this frame...
                if image_3.status == STARTED:
                    # update params
                    pass
                
                # if image_3 is stopping this frame...
                if image_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_3.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_3.tStop = t  # not accounting for scr refresh
                        image_3.tStopRefresh = tThisFlipGlobal  # on global time
                        image_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_3.stopped')
                        # update status
                        image_3.status = FINISHED
                        image_3.setAutoDraw(False)
                
                # *image_4* updates
                
                # if image_4 is starting this frame...
                if image_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_4.frameNStart = frameN  # exact frame index
                    image_4.tStart = t  # local t and not account for scr refresh
                    image_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_4.started')
                    # update status
                    image_4.status = STARTED
                    image_4.setAutoDraw(True)
                
                # if image_4 is active this frame...
                if image_4.status == STARTED:
                    # update params
                    pass
                
                # if image_4 is stopping this frame...
                if image_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_4.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_4.tStop = t  # not accounting for scr refresh
                        image_4.tStopRefresh = tThisFlipGlobal  # on global time
                        image_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_4.stopped')
                        # update status
                        image_4.status = FINISHED
                        image_4.setAutoDraw(False)
                
                # *polygon_2* updates
                
                # if polygon_2 is starting this frame...
                if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_2.frameNStart = frameN  # exact frame index
                    polygon_2.tStart = t  # local t and not account for scr refresh
                    polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.started')
                    # update status
                    polygon_2.status = STARTED
                    polygon_2.setAutoDraw(True)
                
                # if polygon_2 is active this frame...
                if polygon_2.status == STARTED:
                    # update params
                    pass
                
                # if polygon_2 is stopping this frame...
                if polygon_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_2.tStop = t  # not accounting for scr refresh
                        polygon_2.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_2.stopped')
                        # update status
                        polygon_2.status = FINISHED
                        polygon_2.setAutoDraw(False)
                
                # *key_resp_3* updates
                waitOnFlip = False
                
                # if key_resp_3 is starting this frame...
                if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_3.frameNStart = frameN  # exact frame index
                    key_resp_3.tStart = t  # local t and not account for scr refresh
                    key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_3.started')
                    # update status
                    key_resp_3.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_3 is stopping this frame...
                if key_resp_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_3.tStop = t  # not accounting for scr refresh
                        key_resp_3.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_3.stopped')
                        # update status
                        key_resp_3.status = FINISHED
                        key_resp_3.status = FINISHED
                if key_resp_3.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_3.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_3_allKeys.extend(theseKeys)
                    if len(_key_resp_3_allKeys):
                        key_resp_3.keys = [key.name for key in _key_resp_3_allKeys]  # storing all keys
                        key_resp_3.rt = [key.rt for key in _key_resp_3_allKeys]
                        key_resp_3.duration = [key.duration for key in _key_resp_3_allKeys]
                
                # *text_2* updates
                
                # if text_2 is starting this frame...
                if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_2.frameNStart = frameN  # exact frame index
                    text_2.tStart = t  # local t and not account for scr refresh
                    text_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_2.started')
                    # update status
                    text_2.status = STARTED
                    text_2.setAutoDraw(True)
                
                # if text_2 is active this frame...
                if text_2.status == STARTED:
                    # update params
                    text_2.setText(globalClock.getTime()
                    , log=False)
                
                # if text_2 is stopping this frame...
                if text_2.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_2.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_2.tStop = t  # not accounting for scr refresh
                        text_2.tStopRefresh = tThisFlipGlobal  # on global time
                        text_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_2.stopped')
                        # update status
                        text_2.status = FINISHED
                        text_2.setAutoDraw(False)
                # Run 'Each Frame' code from code_4
                
                if key_resp_3.keys:
                    dados.extend(zip(key_resp_3.keys, [globalClock.getTime()] * len(key_resp_3.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_2.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_2.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_2" ---
            for thisComponent in trial_2.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_2
            trial_2.tStop = globalClock.getTime(format='float')
            trial_2.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_2.stopped', trial_2.tStop)
            # check responses
            if key_resp_3.keys in ['', [], None]:  # No response was made
                key_resp_3.keys = None
            loop_4.addData('key_resp_3.keys',key_resp_3.keys)
            if key_resp_3.keys != None:  # we had a response
                loop_4.addData('key_resp_3.rt', key_resp_3.rt)
                loop_4.addData('key_resp_3.duration', key_resp_3.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_2.maxDurationReached:
                routineTimer.addTime(-trial_2.maxDuration)
            elif trial_2.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep4 repeats of 'loop_4'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_5 = data.TrialHandler2(
            name='loop_5',
            nReps=rep5, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('Incrementos.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_5)  # add the loop to the experiment
        thisLoop_5 = loop_5.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_5.rgb)
        if thisLoop_5 != None:
            for paramName in thisLoop_5:
                globals()[paramName] = thisLoop_5[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_5 in loop_5:
            currentLoop = loop_5
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_5.rgb)
            if thisLoop_5 != None:
                for paramName in thisLoop_5:
                    globals()[paramName] = thisLoop_5[paramName]
            
            # --- Prepare to start Routine "trial_3" ---
            # create an object to store info about Routine trial_3
            trial_3 = data.Routine(
                name='trial_3',
                components=[image_5, image_6, polygon_3, key_resp_4, text_3],
            )
            trial_3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_5.setPos((px1, py1))
            image_6.setPos((px2, py2))
            # create starting attributes for key_resp_4
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # store start times for trial_3
            trial_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_3.tStart = globalClock.getTime(format='float')
            trial_3.status = STARTED
            thisExp.addData('trial_3.started', trial_3.tStart)
            trial_3.maxDuration = 0.3
            # keep track of which components have finished
            trial_3Components = trial_3.components
            for thisComponent in trial_3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_3" ---
            # if trial has changed, end Routine now
            if isinstance(loop_5, data.TrialHandler2) and thisLoop_5.thisN != loop_5.thisTrial.thisN:
                continueRoutine = False
            trial_3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_3.maxDuration-frameTolerance:
                    trial_3.maxDurationReached = True
                    continueRoutine = False
                
                # *image_5* updates
                
                # if image_5 is starting this frame...
                if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_5.frameNStart = frameN  # exact frame index
                    image_5.tStart = t  # local t and not account for scr refresh
                    image_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_5.started')
                    # update status
                    image_5.status = STARTED
                    image_5.setAutoDraw(True)
                
                # if image_5 is active this frame...
                if image_5.status == STARTED:
                    # update params
                    pass
                
                # if image_5 is stopping this frame...
                if image_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_5.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_5.tStop = t  # not accounting for scr refresh
                        image_5.tStopRefresh = tThisFlipGlobal  # on global time
                        image_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_5.stopped')
                        # update status
                        image_5.status = FINISHED
                        image_5.setAutoDraw(False)
                
                # *image_6* updates
                
                # if image_6 is starting this frame...
                if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_6.frameNStart = frameN  # exact frame index
                    image_6.tStart = t  # local t and not account for scr refresh
                    image_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_6.started')
                    # update status
                    image_6.status = STARTED
                    image_6.setAutoDraw(True)
                
                # if image_6 is active this frame...
                if image_6.status == STARTED:
                    # update params
                    pass
                
                # if image_6 is stopping this frame...
                if image_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_6.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_6.tStop = t  # not accounting for scr refresh
                        image_6.tStopRefresh = tThisFlipGlobal  # on global time
                        image_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_6.stopped')
                        # update status
                        image_6.status = FINISHED
                        image_6.setAutoDraw(False)
                
                # *polygon_3* updates
                
                # if polygon_3 is starting this frame...
                if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_3.frameNStart = frameN  # exact frame index
                    polygon_3.tStart = t  # local t and not account for scr refresh
                    polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_3.started')
                    # update status
                    polygon_3.status = STARTED
                    polygon_3.setAutoDraw(True)
                
                # if polygon_3 is active this frame...
                if polygon_3.status == STARTED:
                    # update params
                    pass
                
                # if polygon_3 is stopping this frame...
                if polygon_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_3.tStop = t  # not accounting for scr refresh
                        polygon_3.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                        # update status
                        polygon_3.status = FINISHED
                        polygon_3.setAutoDraw(False)
                
                # *key_resp_4* updates
                waitOnFlip = False
                
                # if key_resp_4 is starting this frame...
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.started')
                    # update status
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_4 is stopping this frame...
                if key_resp_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_4.tStop = t  # not accounting for scr refresh
                        key_resp_4.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                        # update status
                        key_resp_4.status = FINISHED
                        key_resp_4.status = FINISHED
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                        key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                        key_resp_4.duration = [key.duration for key in _key_resp_4_allKeys]
                
                # *text_3* updates
                
                # if text_3 is starting this frame...
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    # update status
                    text_3.status = STARTED
                    text_3.setAutoDraw(True)
                
                # if text_3 is active this frame...
                if text_3.status == STARTED:
                    # update params
                    text_3.setText(globalClock.getTime()
                    , log=False)
                
                # if text_3 is stopping this frame...
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.tStopRefresh = tThisFlipGlobal  # on global time
                        text_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_3.stopped')
                        # update status
                        text_3.status = FINISHED
                        text_3.setAutoDraw(False)
                # Run 'Each Frame' code from code_5
                
                if key_resp_4.keys:
                    dados.extend(zip(key_resp_4.keys, [globalClock.getTime()] * len(key_resp_4.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_3" ---
            for thisComponent in trial_3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_3
            trial_3.tStop = globalClock.getTime(format='float')
            trial_3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_3.stopped', trial_3.tStop)
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys = None
            loop_5.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                loop_5.addData('key_resp_4.rt', key_resp_4.rt)
                loop_5.addData('key_resp_4.duration', key_resp_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_3.maxDurationReached:
                routineTimer.addTime(-trial_3.maxDuration)
            elif trial_3.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_4" ---
            # create an object to store info about Routine trial_4
            trial_4 = data.Routine(
                name='trial_4',
                components=[image_7, image_8, polygon_4, key_resp_5, text_4],
            )
            trial_4.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_7.setPos((px3, py3))
            image_8.setPos((px4, py4))
            # create starting attributes for key_resp_5
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # store start times for trial_4
            trial_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_4.tStart = globalClock.getTime(format='float')
            trial_4.status = STARTED
            thisExp.addData('trial_4.started', trial_4.tStart)
            trial_4.maxDuration = 0.3
            # keep track of which components have finished
            trial_4Components = trial_4.components
            for thisComponent in trial_4.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_4" ---
            # if trial has changed, end Routine now
            if isinstance(loop_5, data.TrialHandler2) and thisLoop_5.thisN != loop_5.thisTrial.thisN:
                continueRoutine = False
            trial_4.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_4.maxDuration-frameTolerance:
                    trial_4.maxDurationReached = True
                    continueRoutine = False
                
                # *image_7* updates
                
                # if image_7 is starting this frame...
                if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.tStart = t  # local t and not account for scr refresh
                    image_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.started')
                    # update status
                    image_7.status = STARTED
                    image_7.setAutoDraw(True)
                
                # if image_7 is active this frame...
                if image_7.status == STARTED:
                    # update params
                    pass
                
                # if image_7 is stopping this frame...
                if image_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_7.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_7.tStop = t  # not accounting for scr refresh
                        image_7.tStopRefresh = tThisFlipGlobal  # on global time
                        image_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_7.stopped')
                        # update status
                        image_7.status = FINISHED
                        image_7.setAutoDraw(False)
                
                # *image_8* updates
                
                # if image_8 is starting this frame...
                if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_8.frameNStart = frameN  # exact frame index
                    image_8.tStart = t  # local t and not account for scr refresh
                    image_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_8.started')
                    # update status
                    image_8.status = STARTED
                    image_8.setAutoDraw(True)
                
                # if image_8 is active this frame...
                if image_8.status == STARTED:
                    # update params
                    pass
                
                # if image_8 is stopping this frame...
                if image_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_8.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_8.tStop = t  # not accounting for scr refresh
                        image_8.tStopRefresh = tThisFlipGlobal  # on global time
                        image_8.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_8.stopped')
                        # update status
                        image_8.status = FINISHED
                        image_8.setAutoDraw(False)
                
                # *polygon_4* updates
                
                # if polygon_4 is starting this frame...
                if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_4.frameNStart = frameN  # exact frame index
                    polygon_4.tStart = t  # local t and not account for scr refresh
                    polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_4.started')
                    # update status
                    polygon_4.status = STARTED
                    polygon_4.setAutoDraw(True)
                
                # if polygon_4 is active this frame...
                if polygon_4.status == STARTED:
                    # update params
                    pass
                
                # if polygon_4 is stopping this frame...
                if polygon_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_4.tStop = t  # not accounting for scr refresh
                        polygon_4.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                        # update status
                        polygon_4.status = FINISHED
                        polygon_4.setAutoDraw(False)
                
                # *key_resp_5* updates
                waitOnFlip = False
                
                # if key_resp_5 is starting this frame...
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_5.started')
                    # update status
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_5 is stopping this frame...
                if key_resp_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                        # update status
                        key_resp_5.status = FINISHED
                        key_resp_5.status = FINISHED
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = [key.name for key in _key_resp_5_allKeys]  # storing all keys
                        key_resp_5.rt = [key.rt for key in _key_resp_5_allKeys]
                        key_resp_5.duration = [key.duration for key in _key_resp_5_allKeys]
                
                # *text_4* updates
                
                # if text_4 is starting this frame...
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.started')
                    # update status
                    text_4.status = STARTED
                    text_4.setAutoDraw(True)
                
                # if text_4 is active this frame...
                if text_4.status == STARTED:
                    # update params
                    text_4.setText(globalClock.getTime()
                    , log=False)
                
                # if text_4 is stopping this frame...
                if text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_4.tStop = t  # not accounting for scr refresh
                        text_4.tStopRefresh = tThisFlipGlobal  # on global time
                        text_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_4.stopped')
                        # update status
                        text_4.status = FINISHED
                        text_4.setAutoDraw(False)
                # Run 'Each Frame' code from code_6
                
                if key_resp_5.keys:
                    dados.extend(zip(key_resp_5.keys, [globalClock.getTime()] * len(key_resp_5.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_4.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_4.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_4" ---
            for thisComponent in trial_4.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_4
            trial_4.tStop = globalClock.getTime(format='float')
            trial_4.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_4.stopped', trial_4.tStop)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            loop_5.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                loop_5.addData('key_resp_5.rt', key_resp_5.rt)
                loop_5.addData('key_resp_5.duration', key_resp_5.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_4.maxDurationReached:
                routineTimer.addTime(-trial_4.maxDuration)
            elif trial_4.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep5 repeats of 'loop_5'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_6 = data.TrialHandler2(
            name='loop_6',
            nReps=rep6, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('incremento_loop2.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_6)  # add the loop to the experiment
        thisLoop_6 = loop_6.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_6.rgb)
        if thisLoop_6 != None:
            for paramName in thisLoop_6:
                globals()[paramName] = thisLoop_6[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_6 in loop_6:
            currentLoop = loop_6
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_6.rgb)
            if thisLoop_6 != None:
                for paramName in thisLoop_6:
                    globals()[paramName] = thisLoop_6[paramName]
            
            # --- Prepare to start Routine "trial_3" ---
            # create an object to store info about Routine trial_3
            trial_3 = data.Routine(
                name='trial_3',
                components=[image_5, image_6, polygon_3, key_resp_4, text_3],
            )
            trial_3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_5.setPos((px1, py1))
            image_6.setPos((px2, py2))
            # create starting attributes for key_resp_4
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # store start times for trial_3
            trial_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_3.tStart = globalClock.getTime(format='float')
            trial_3.status = STARTED
            thisExp.addData('trial_3.started', trial_3.tStart)
            trial_3.maxDuration = 0.3
            # keep track of which components have finished
            trial_3Components = trial_3.components
            for thisComponent in trial_3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_3" ---
            # if trial has changed, end Routine now
            if isinstance(loop_6, data.TrialHandler2) and thisLoop_6.thisN != loop_6.thisTrial.thisN:
                continueRoutine = False
            trial_3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_3.maxDuration-frameTolerance:
                    trial_3.maxDurationReached = True
                    continueRoutine = False
                
                # *image_5* updates
                
                # if image_5 is starting this frame...
                if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_5.frameNStart = frameN  # exact frame index
                    image_5.tStart = t  # local t and not account for scr refresh
                    image_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_5.started')
                    # update status
                    image_5.status = STARTED
                    image_5.setAutoDraw(True)
                
                # if image_5 is active this frame...
                if image_5.status == STARTED:
                    # update params
                    pass
                
                # if image_5 is stopping this frame...
                if image_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_5.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_5.tStop = t  # not accounting for scr refresh
                        image_5.tStopRefresh = tThisFlipGlobal  # on global time
                        image_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_5.stopped')
                        # update status
                        image_5.status = FINISHED
                        image_5.setAutoDraw(False)
                
                # *image_6* updates
                
                # if image_6 is starting this frame...
                if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_6.frameNStart = frameN  # exact frame index
                    image_6.tStart = t  # local t and not account for scr refresh
                    image_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_6.started')
                    # update status
                    image_6.status = STARTED
                    image_6.setAutoDraw(True)
                
                # if image_6 is active this frame...
                if image_6.status == STARTED:
                    # update params
                    pass
                
                # if image_6 is stopping this frame...
                if image_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_6.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_6.tStop = t  # not accounting for scr refresh
                        image_6.tStopRefresh = tThisFlipGlobal  # on global time
                        image_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_6.stopped')
                        # update status
                        image_6.status = FINISHED
                        image_6.setAutoDraw(False)
                
                # *polygon_3* updates
                
                # if polygon_3 is starting this frame...
                if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_3.frameNStart = frameN  # exact frame index
                    polygon_3.tStart = t  # local t and not account for scr refresh
                    polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_3.started')
                    # update status
                    polygon_3.status = STARTED
                    polygon_3.setAutoDraw(True)
                
                # if polygon_3 is active this frame...
                if polygon_3.status == STARTED:
                    # update params
                    pass
                
                # if polygon_3 is stopping this frame...
                if polygon_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_3.tStop = t  # not accounting for scr refresh
                        polygon_3.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                        # update status
                        polygon_3.status = FINISHED
                        polygon_3.setAutoDraw(False)
                
                # *key_resp_4* updates
                waitOnFlip = False
                
                # if key_resp_4 is starting this frame...
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.started')
                    # update status
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_4 is stopping this frame...
                if key_resp_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_4.tStop = t  # not accounting for scr refresh
                        key_resp_4.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                        # update status
                        key_resp_4.status = FINISHED
                        key_resp_4.status = FINISHED
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                        key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                        key_resp_4.duration = [key.duration for key in _key_resp_4_allKeys]
                
                # *text_3* updates
                
                # if text_3 is starting this frame...
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    # update status
                    text_3.status = STARTED
                    text_3.setAutoDraw(True)
                
                # if text_3 is active this frame...
                if text_3.status == STARTED:
                    # update params
                    text_3.setText(globalClock.getTime()
                    , log=False)
                
                # if text_3 is stopping this frame...
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.tStopRefresh = tThisFlipGlobal  # on global time
                        text_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_3.stopped')
                        # update status
                        text_3.status = FINISHED
                        text_3.setAutoDraw(False)
                # Run 'Each Frame' code from code_5
                
                if key_resp_4.keys:
                    dados.extend(zip(key_resp_4.keys, [globalClock.getTime()] * len(key_resp_4.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_3" ---
            for thisComponent in trial_3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_3
            trial_3.tStop = globalClock.getTime(format='float')
            trial_3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_3.stopped', trial_3.tStop)
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys = None
            loop_6.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                loop_6.addData('key_resp_4.rt', key_resp_4.rt)
                loop_6.addData('key_resp_4.duration', key_resp_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_3.maxDurationReached:
                routineTimer.addTime(-trial_3.maxDuration)
            elif trial_3.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_4" ---
            # create an object to store info about Routine trial_4
            trial_4 = data.Routine(
                name='trial_4',
                components=[image_7, image_8, polygon_4, key_resp_5, text_4],
            )
            trial_4.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_7.setPos((px3, py3))
            image_8.setPos((px4, py4))
            # create starting attributes for key_resp_5
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # store start times for trial_4
            trial_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_4.tStart = globalClock.getTime(format='float')
            trial_4.status = STARTED
            thisExp.addData('trial_4.started', trial_4.tStart)
            trial_4.maxDuration = 0.3
            # keep track of which components have finished
            trial_4Components = trial_4.components
            for thisComponent in trial_4.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_4" ---
            # if trial has changed, end Routine now
            if isinstance(loop_6, data.TrialHandler2) and thisLoop_6.thisN != loop_6.thisTrial.thisN:
                continueRoutine = False
            trial_4.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_4.maxDuration-frameTolerance:
                    trial_4.maxDurationReached = True
                    continueRoutine = False
                
                # *image_7* updates
                
                # if image_7 is starting this frame...
                if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.tStart = t  # local t and not account for scr refresh
                    image_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.started')
                    # update status
                    image_7.status = STARTED
                    image_7.setAutoDraw(True)
                
                # if image_7 is active this frame...
                if image_7.status == STARTED:
                    # update params
                    pass
                
                # if image_7 is stopping this frame...
                if image_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_7.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_7.tStop = t  # not accounting for scr refresh
                        image_7.tStopRefresh = tThisFlipGlobal  # on global time
                        image_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_7.stopped')
                        # update status
                        image_7.status = FINISHED
                        image_7.setAutoDraw(False)
                
                # *image_8* updates
                
                # if image_8 is starting this frame...
                if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_8.frameNStart = frameN  # exact frame index
                    image_8.tStart = t  # local t and not account for scr refresh
                    image_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_8.started')
                    # update status
                    image_8.status = STARTED
                    image_8.setAutoDraw(True)
                
                # if image_8 is active this frame...
                if image_8.status == STARTED:
                    # update params
                    pass
                
                # if image_8 is stopping this frame...
                if image_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_8.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_8.tStop = t  # not accounting for scr refresh
                        image_8.tStopRefresh = tThisFlipGlobal  # on global time
                        image_8.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_8.stopped')
                        # update status
                        image_8.status = FINISHED
                        image_8.setAutoDraw(False)
                
                # *polygon_4* updates
                
                # if polygon_4 is starting this frame...
                if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_4.frameNStart = frameN  # exact frame index
                    polygon_4.tStart = t  # local t and not account for scr refresh
                    polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_4.started')
                    # update status
                    polygon_4.status = STARTED
                    polygon_4.setAutoDraw(True)
                
                # if polygon_4 is active this frame...
                if polygon_4.status == STARTED:
                    # update params
                    pass
                
                # if polygon_4 is stopping this frame...
                if polygon_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_4.tStop = t  # not accounting for scr refresh
                        polygon_4.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                        # update status
                        polygon_4.status = FINISHED
                        polygon_4.setAutoDraw(False)
                
                # *key_resp_5* updates
                waitOnFlip = False
                
                # if key_resp_5 is starting this frame...
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_5.started')
                    # update status
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_5 is stopping this frame...
                if key_resp_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                        # update status
                        key_resp_5.status = FINISHED
                        key_resp_5.status = FINISHED
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = [key.name for key in _key_resp_5_allKeys]  # storing all keys
                        key_resp_5.rt = [key.rt for key in _key_resp_5_allKeys]
                        key_resp_5.duration = [key.duration for key in _key_resp_5_allKeys]
                
                # *text_4* updates
                
                # if text_4 is starting this frame...
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.started')
                    # update status
                    text_4.status = STARTED
                    text_4.setAutoDraw(True)
                
                # if text_4 is active this frame...
                if text_4.status == STARTED:
                    # update params
                    text_4.setText(globalClock.getTime()
                    , log=False)
                
                # if text_4 is stopping this frame...
                if text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_4.tStop = t  # not accounting for scr refresh
                        text_4.tStopRefresh = tThisFlipGlobal  # on global time
                        text_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_4.stopped')
                        # update status
                        text_4.status = FINISHED
                        text_4.setAutoDraw(False)
                # Run 'Each Frame' code from code_6
                
                if key_resp_5.keys:
                    dados.extend(zip(key_resp_5.keys, [globalClock.getTime()] * len(key_resp_5.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_4.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_4.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_4" ---
            for thisComponent in trial_4.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_4
            trial_4.tStop = globalClock.getTime(format='float')
            trial_4.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_4.stopped', trial_4.tStop)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            loop_6.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                loop_6.addData('key_resp_5.rt', key_resp_5.rt)
                loop_6.addData('key_resp_5.duration', key_resp_5.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_4.maxDurationReached:
                routineTimer.addTime(-trial_4.maxDuration)
            elif trial_4.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep6 repeats of 'loop_6'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_7 = data.TrialHandler2(
            name='loop_7',
            nReps=rep7, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('incremento_loop3.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_7)  # add the loop to the experiment
        thisLoop_7 = loop_7.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_7.rgb)
        if thisLoop_7 != None:
            for paramName in thisLoop_7:
                globals()[paramName] = thisLoop_7[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_7 in loop_7:
            currentLoop = loop_7
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_7.rgb)
            if thisLoop_7 != None:
                for paramName in thisLoop_7:
                    globals()[paramName] = thisLoop_7[paramName]
            
            # --- Prepare to start Routine "trial_3" ---
            # create an object to store info about Routine trial_3
            trial_3 = data.Routine(
                name='trial_3',
                components=[image_5, image_6, polygon_3, key_resp_4, text_3],
            )
            trial_3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_5.setPos((px1, py1))
            image_6.setPos((px2, py2))
            # create starting attributes for key_resp_4
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # store start times for trial_3
            trial_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_3.tStart = globalClock.getTime(format='float')
            trial_3.status = STARTED
            thisExp.addData('trial_3.started', trial_3.tStart)
            trial_3.maxDuration = 0.3
            # keep track of which components have finished
            trial_3Components = trial_3.components
            for thisComponent in trial_3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_3" ---
            # if trial has changed, end Routine now
            if isinstance(loop_7, data.TrialHandler2) and thisLoop_7.thisN != loop_7.thisTrial.thisN:
                continueRoutine = False
            trial_3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_3.maxDuration-frameTolerance:
                    trial_3.maxDurationReached = True
                    continueRoutine = False
                
                # *image_5* updates
                
                # if image_5 is starting this frame...
                if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_5.frameNStart = frameN  # exact frame index
                    image_5.tStart = t  # local t and not account for scr refresh
                    image_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_5.started')
                    # update status
                    image_5.status = STARTED
                    image_5.setAutoDraw(True)
                
                # if image_5 is active this frame...
                if image_5.status == STARTED:
                    # update params
                    pass
                
                # if image_5 is stopping this frame...
                if image_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_5.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_5.tStop = t  # not accounting for scr refresh
                        image_5.tStopRefresh = tThisFlipGlobal  # on global time
                        image_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_5.stopped')
                        # update status
                        image_5.status = FINISHED
                        image_5.setAutoDraw(False)
                
                # *image_6* updates
                
                # if image_6 is starting this frame...
                if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_6.frameNStart = frameN  # exact frame index
                    image_6.tStart = t  # local t and not account for scr refresh
                    image_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_6.started')
                    # update status
                    image_6.status = STARTED
                    image_6.setAutoDraw(True)
                
                # if image_6 is active this frame...
                if image_6.status == STARTED:
                    # update params
                    pass
                
                # if image_6 is stopping this frame...
                if image_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_6.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_6.tStop = t  # not accounting for scr refresh
                        image_6.tStopRefresh = tThisFlipGlobal  # on global time
                        image_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_6.stopped')
                        # update status
                        image_6.status = FINISHED
                        image_6.setAutoDraw(False)
                
                # *polygon_3* updates
                
                # if polygon_3 is starting this frame...
                if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_3.frameNStart = frameN  # exact frame index
                    polygon_3.tStart = t  # local t and not account for scr refresh
                    polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_3.started')
                    # update status
                    polygon_3.status = STARTED
                    polygon_3.setAutoDraw(True)
                
                # if polygon_3 is active this frame...
                if polygon_3.status == STARTED:
                    # update params
                    pass
                
                # if polygon_3 is stopping this frame...
                if polygon_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_3.tStop = t  # not accounting for scr refresh
                        polygon_3.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                        # update status
                        polygon_3.status = FINISHED
                        polygon_3.setAutoDraw(False)
                
                # *key_resp_4* updates
                waitOnFlip = False
                
                # if key_resp_4 is starting this frame...
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.started')
                    # update status
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_4 is stopping this frame...
                if key_resp_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_4.tStop = t  # not accounting for scr refresh
                        key_resp_4.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                        # update status
                        key_resp_4.status = FINISHED
                        key_resp_4.status = FINISHED
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                        key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                        key_resp_4.duration = [key.duration for key in _key_resp_4_allKeys]
                
                # *text_3* updates
                
                # if text_3 is starting this frame...
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    # update status
                    text_3.status = STARTED
                    text_3.setAutoDraw(True)
                
                # if text_3 is active this frame...
                if text_3.status == STARTED:
                    # update params
                    text_3.setText(globalClock.getTime()
                    , log=False)
                
                # if text_3 is stopping this frame...
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.tStopRefresh = tThisFlipGlobal  # on global time
                        text_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_3.stopped')
                        # update status
                        text_3.status = FINISHED
                        text_3.setAutoDraw(False)
                # Run 'Each Frame' code from code_5
                
                if key_resp_4.keys:
                    dados.extend(zip(key_resp_4.keys, [globalClock.getTime()] * len(key_resp_4.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_3" ---
            for thisComponent in trial_3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_3
            trial_3.tStop = globalClock.getTime(format='float')
            trial_3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_3.stopped', trial_3.tStop)
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys = None
            loop_7.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                loop_7.addData('key_resp_4.rt', key_resp_4.rt)
                loop_7.addData('key_resp_4.duration', key_resp_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_3.maxDurationReached:
                routineTimer.addTime(-trial_3.maxDuration)
            elif trial_3.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_4" ---
            # create an object to store info about Routine trial_4
            trial_4 = data.Routine(
                name='trial_4',
                components=[image_7, image_8, polygon_4, key_resp_5, text_4],
            )
            trial_4.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_7.setPos((px3, py3))
            image_8.setPos((px4, py4))
            # create starting attributes for key_resp_5
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # store start times for trial_4
            trial_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_4.tStart = globalClock.getTime(format='float')
            trial_4.status = STARTED
            thisExp.addData('trial_4.started', trial_4.tStart)
            trial_4.maxDuration = 0.3
            # keep track of which components have finished
            trial_4Components = trial_4.components
            for thisComponent in trial_4.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_4" ---
            # if trial has changed, end Routine now
            if isinstance(loop_7, data.TrialHandler2) and thisLoop_7.thisN != loop_7.thisTrial.thisN:
                continueRoutine = False
            trial_4.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_4.maxDuration-frameTolerance:
                    trial_4.maxDurationReached = True
                    continueRoutine = False
                
                # *image_7* updates
                
                # if image_7 is starting this frame...
                if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.tStart = t  # local t and not account for scr refresh
                    image_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.started')
                    # update status
                    image_7.status = STARTED
                    image_7.setAutoDraw(True)
                
                # if image_7 is active this frame...
                if image_7.status == STARTED:
                    # update params
                    pass
                
                # if image_7 is stopping this frame...
                if image_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_7.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_7.tStop = t  # not accounting for scr refresh
                        image_7.tStopRefresh = tThisFlipGlobal  # on global time
                        image_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_7.stopped')
                        # update status
                        image_7.status = FINISHED
                        image_7.setAutoDraw(False)
                
                # *image_8* updates
                
                # if image_8 is starting this frame...
                if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_8.frameNStart = frameN  # exact frame index
                    image_8.tStart = t  # local t and not account for scr refresh
                    image_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_8.started')
                    # update status
                    image_8.status = STARTED
                    image_8.setAutoDraw(True)
                
                # if image_8 is active this frame...
                if image_8.status == STARTED:
                    # update params
                    pass
                
                # if image_8 is stopping this frame...
                if image_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_8.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_8.tStop = t  # not accounting for scr refresh
                        image_8.tStopRefresh = tThisFlipGlobal  # on global time
                        image_8.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_8.stopped')
                        # update status
                        image_8.status = FINISHED
                        image_8.setAutoDraw(False)
                
                # *polygon_4* updates
                
                # if polygon_4 is starting this frame...
                if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_4.frameNStart = frameN  # exact frame index
                    polygon_4.tStart = t  # local t and not account for scr refresh
                    polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_4.started')
                    # update status
                    polygon_4.status = STARTED
                    polygon_4.setAutoDraw(True)
                
                # if polygon_4 is active this frame...
                if polygon_4.status == STARTED:
                    # update params
                    pass
                
                # if polygon_4 is stopping this frame...
                if polygon_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_4.tStop = t  # not accounting for scr refresh
                        polygon_4.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                        # update status
                        polygon_4.status = FINISHED
                        polygon_4.setAutoDraw(False)
                
                # *key_resp_5* updates
                waitOnFlip = False
                
                # if key_resp_5 is starting this frame...
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_5.started')
                    # update status
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_5 is stopping this frame...
                if key_resp_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                        # update status
                        key_resp_5.status = FINISHED
                        key_resp_5.status = FINISHED
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = [key.name for key in _key_resp_5_allKeys]  # storing all keys
                        key_resp_5.rt = [key.rt for key in _key_resp_5_allKeys]
                        key_resp_5.duration = [key.duration for key in _key_resp_5_allKeys]
                
                # *text_4* updates
                
                # if text_4 is starting this frame...
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.started')
                    # update status
                    text_4.status = STARTED
                    text_4.setAutoDraw(True)
                
                # if text_4 is active this frame...
                if text_4.status == STARTED:
                    # update params
                    text_4.setText(globalClock.getTime()
                    , log=False)
                
                # if text_4 is stopping this frame...
                if text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_4.tStop = t  # not accounting for scr refresh
                        text_4.tStopRefresh = tThisFlipGlobal  # on global time
                        text_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_4.stopped')
                        # update status
                        text_4.status = FINISHED
                        text_4.setAutoDraw(False)
                # Run 'Each Frame' code from code_6
                
                if key_resp_5.keys:
                    dados.extend(zip(key_resp_5.keys, [globalClock.getTime()] * len(key_resp_5.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_4.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_4.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_4" ---
            for thisComponent in trial_4.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_4
            trial_4.tStop = globalClock.getTime(format='float')
            trial_4.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_4.stopped', trial_4.tStop)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            loop_7.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                loop_7.addData('key_resp_5.rt', key_resp_5.rt)
                loop_7.addData('key_resp_5.duration', key_resp_5.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_4.maxDurationReached:
                routineTimer.addTime(-trial_4.maxDuration)
            elif trial_4.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep7 repeats of 'loop_7'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_8 = data.TrialHandler2(
            name='loop_8',
            nReps=rep8, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('Incrementos_loop_4.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_8)  # add the loop to the experiment
        thisLoop_8 = loop_8.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_8.rgb)
        if thisLoop_8 != None:
            for paramName in thisLoop_8:
                globals()[paramName] = thisLoop_8[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_8 in loop_8:
            currentLoop = loop_8
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_8.rgb)
            if thisLoop_8 != None:
                for paramName in thisLoop_8:
                    globals()[paramName] = thisLoop_8[paramName]
            
            # --- Prepare to start Routine "trial_3" ---
            # create an object to store info about Routine trial_3
            trial_3 = data.Routine(
                name='trial_3',
                components=[image_5, image_6, polygon_3, key_resp_4, text_3],
            )
            trial_3.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_5.setPos((px1, py1))
            image_6.setPos((px2, py2))
            # create starting attributes for key_resp_4
            key_resp_4.keys = []
            key_resp_4.rt = []
            _key_resp_4_allKeys = []
            # store start times for trial_3
            trial_3.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_3.tStart = globalClock.getTime(format='float')
            trial_3.status = STARTED
            thisExp.addData('trial_3.started', trial_3.tStart)
            trial_3.maxDuration = 0.3
            # keep track of which components have finished
            trial_3Components = trial_3.components
            for thisComponent in trial_3.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_3" ---
            # if trial has changed, end Routine now
            if isinstance(loop_8, data.TrialHandler2) and thisLoop_8.thisN != loop_8.thisTrial.thisN:
                continueRoutine = False
            trial_3.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_3.maxDuration-frameTolerance:
                    trial_3.maxDurationReached = True
                    continueRoutine = False
                
                # *image_5* updates
                
                # if image_5 is starting this frame...
                if image_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_5.frameNStart = frameN  # exact frame index
                    image_5.tStart = t  # local t and not account for scr refresh
                    image_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_5.started')
                    # update status
                    image_5.status = STARTED
                    image_5.setAutoDraw(True)
                
                # if image_5 is active this frame...
                if image_5.status == STARTED:
                    # update params
                    pass
                
                # if image_5 is stopping this frame...
                if image_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_5.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_5.tStop = t  # not accounting for scr refresh
                        image_5.tStopRefresh = tThisFlipGlobal  # on global time
                        image_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_5.stopped')
                        # update status
                        image_5.status = FINISHED
                        image_5.setAutoDraw(False)
                
                # *image_6* updates
                
                # if image_6 is starting this frame...
                if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_6.frameNStart = frameN  # exact frame index
                    image_6.tStart = t  # local t and not account for scr refresh
                    image_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_6.started')
                    # update status
                    image_6.status = STARTED
                    image_6.setAutoDraw(True)
                
                # if image_6 is active this frame...
                if image_6.status == STARTED:
                    # update params
                    pass
                
                # if image_6 is stopping this frame...
                if image_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_6.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_6.tStop = t  # not accounting for scr refresh
                        image_6.tStopRefresh = tThisFlipGlobal  # on global time
                        image_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_6.stopped')
                        # update status
                        image_6.status = FINISHED
                        image_6.setAutoDraw(False)
                
                # *polygon_3* updates
                
                # if polygon_3 is starting this frame...
                if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_3.frameNStart = frameN  # exact frame index
                    polygon_3.tStart = t  # local t and not account for scr refresh
                    polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_3.started')
                    # update status
                    polygon_3.status = STARTED
                    polygon_3.setAutoDraw(True)
                
                # if polygon_3 is active this frame...
                if polygon_3.status == STARTED:
                    # update params
                    pass
                
                # if polygon_3 is stopping this frame...
                if polygon_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_3.tStop = t  # not accounting for scr refresh
                        polygon_3.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_3.stopped')
                        # update status
                        polygon_3.status = FINISHED
                        polygon_3.setAutoDraw(False)
                
                # *key_resp_4* updates
                waitOnFlip = False
                
                # if key_resp_4 is starting this frame...
                if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_4.frameNStart = frameN  # exact frame index
                    key_resp_4.tStart = t  # local t and not account for scr refresh
                    key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_4.started')
                    # update status
                    key_resp_4.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_4 is stopping this frame...
                if key_resp_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_4.tStop = t  # not accounting for scr refresh
                        key_resp_4.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_4.stopped')
                        # update status
                        key_resp_4.status = FINISHED
                        key_resp_4.status = FINISHED
                if key_resp_4.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_4.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_4_allKeys.extend(theseKeys)
                    if len(_key_resp_4_allKeys):
                        key_resp_4.keys = [key.name for key in _key_resp_4_allKeys]  # storing all keys
                        key_resp_4.rt = [key.rt for key in _key_resp_4_allKeys]
                        key_resp_4.duration = [key.duration for key in _key_resp_4_allKeys]
                
                # *text_3* updates
                
                # if text_3 is starting this frame...
                if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_3.frameNStart = frameN  # exact frame index
                    text_3.tStart = t  # local t and not account for scr refresh
                    text_3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_3.started')
                    # update status
                    text_3.status = STARTED
                    text_3.setAutoDraw(True)
                
                # if text_3 is active this frame...
                if text_3.status == STARTED:
                    # update params
                    text_3.setText(globalClock.getTime()
                    , log=False)
                
                # if text_3 is stopping this frame...
                if text_3.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_3.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_3.tStop = t  # not accounting for scr refresh
                        text_3.tStopRefresh = tThisFlipGlobal  # on global time
                        text_3.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_3.stopped')
                        # update status
                        text_3.status = FINISHED
                        text_3.setAutoDraw(False)
                # Run 'Each Frame' code from code_5
                
                if key_resp_4.keys:
                    dados.extend(zip(key_resp_4.keys, [globalClock.getTime()] * len(key_resp_4.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_3.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_3.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_3" ---
            for thisComponent in trial_3.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_3
            trial_3.tStop = globalClock.getTime(format='float')
            trial_3.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_3.stopped', trial_3.tStop)
            # check responses
            if key_resp_4.keys in ['', [], None]:  # No response was made
                key_resp_4.keys = None
            loop_8.addData('key_resp_4.keys',key_resp_4.keys)
            if key_resp_4.keys != None:  # we had a response
                loop_8.addData('key_resp_4.rt', key_resp_4.rt)
                loop_8.addData('key_resp_4.duration', key_resp_4.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_3.maxDurationReached:
                routineTimer.addTime(-trial_3.maxDuration)
            elif trial_3.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_4" ---
            # create an object to store info about Routine trial_4
            trial_4 = data.Routine(
                name='trial_4',
                components=[image_7, image_8, polygon_4, key_resp_5, text_4],
            )
            trial_4.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_7.setPos((px3, py3))
            image_8.setPos((px4, py4))
            # create starting attributes for key_resp_5
            key_resp_5.keys = []
            key_resp_5.rt = []
            _key_resp_5_allKeys = []
            # store start times for trial_4
            trial_4.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_4.tStart = globalClock.getTime(format='float')
            trial_4.status = STARTED
            thisExp.addData('trial_4.started', trial_4.tStart)
            trial_4.maxDuration = 0.3
            # keep track of which components have finished
            trial_4Components = trial_4.components
            for thisComponent in trial_4.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_4" ---
            # if trial has changed, end Routine now
            if isinstance(loop_8, data.TrialHandler2) and thisLoop_8.thisN != loop_8.thisTrial.thisN:
                continueRoutine = False
            trial_4.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > trial_4.maxDuration-frameTolerance:
                    trial_4.maxDurationReached = True
                    continueRoutine = False
                
                # *image_7* updates
                
                # if image_7 is starting this frame...
                if image_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_7.frameNStart = frameN  # exact frame index
                    image_7.tStart = t  # local t and not account for scr refresh
                    image_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_7.started')
                    # update status
                    image_7.status = STARTED
                    image_7.setAutoDraw(True)
                
                # if image_7 is active this frame...
                if image_7.status == STARTED:
                    # update params
                    pass
                
                # if image_7 is stopping this frame...
                if image_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_7.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_7.tStop = t  # not accounting for scr refresh
                        image_7.tStopRefresh = tThisFlipGlobal  # on global time
                        image_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_7.stopped')
                        # update status
                        image_7.status = FINISHED
                        image_7.setAutoDraw(False)
                
                # *image_8* updates
                
                # if image_8 is starting this frame...
                if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_8.frameNStart = frameN  # exact frame index
                    image_8.tStart = t  # local t and not account for scr refresh
                    image_8.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_8.started')
                    # update status
                    image_8.status = STARTED
                    image_8.setAutoDraw(True)
                
                # if image_8 is active this frame...
                if image_8.status == STARTED:
                    # update params
                    pass
                
                # if image_8 is stopping this frame...
                if image_8.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_8.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_8.tStop = t  # not accounting for scr refresh
                        image_8.tStopRefresh = tThisFlipGlobal  # on global time
                        image_8.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_8.stopped')
                        # update status
                        image_8.status = FINISHED
                        image_8.setAutoDraw(False)
                
                # *polygon_4* updates
                
                # if polygon_4 is starting this frame...
                if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_4.frameNStart = frameN  # exact frame index
                    polygon_4.tStart = t  # local t and not account for scr refresh
                    polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_4.started')
                    # update status
                    polygon_4.status = STARTED
                    polygon_4.setAutoDraw(True)
                
                # if polygon_4 is active this frame...
                if polygon_4.status == STARTED:
                    # update params
                    pass
                
                # if polygon_4 is stopping this frame...
                if polygon_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_4.tStop = t  # not accounting for scr refresh
                        polygon_4.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_4.stopped')
                        # update status
                        polygon_4.status = FINISHED
                        polygon_4.setAutoDraw(False)
                
                # *key_resp_5* updates
                waitOnFlip = False
                
                # if key_resp_5 is starting this frame...
                if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_5.frameNStart = frameN  # exact frame index
                    key_resp_5.tStart = t  # local t and not account for scr refresh
                    key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_5.started')
                    # update status
                    key_resp_5.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_5 is stopping this frame...
                if key_resp_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_5.tStop = t  # not accounting for scr refresh
                        key_resp_5.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_5.stopped')
                        # update status
                        key_resp_5.status = FINISHED
                        key_resp_5.status = FINISHED
                if key_resp_5.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_5.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_5_allKeys.extend(theseKeys)
                    if len(_key_resp_5_allKeys):
                        key_resp_5.keys = [key.name for key in _key_resp_5_allKeys]  # storing all keys
                        key_resp_5.rt = [key.rt for key in _key_resp_5_allKeys]
                        key_resp_5.duration = [key.duration for key in _key_resp_5_allKeys]
                
                # *text_4* updates
                
                # if text_4 is starting this frame...
                if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_4.frameNStart = frameN  # exact frame index
                    text_4.tStart = t  # local t and not account for scr refresh
                    text_4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_4.started')
                    # update status
                    text_4.status = STARTED
                    text_4.setAutoDraw(True)
                
                # if text_4 is active this frame...
                if text_4.status == STARTED:
                    # update params
                    text_4.setText(globalClock.getTime()
                    , log=False)
                
                # if text_4 is stopping this frame...
                if text_4.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_4.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_4.tStop = t  # not accounting for scr refresh
                        text_4.tStopRefresh = tThisFlipGlobal  # on global time
                        text_4.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_4.stopped')
                        # update status
                        text_4.status = FINISHED
                        text_4.setAutoDraw(False)
                # Run 'Each Frame' code from code_6
                
                if key_resp_5.keys:
                    dados.extend(zip(key_resp_5.keys, [globalClock.getTime()] * len(key_resp_5.keys)))
                
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_4.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_4.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_4" ---
            for thisComponent in trial_4.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_4
            trial_4.tStop = globalClock.getTime(format='float')
            trial_4.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_4.stopped', trial_4.tStop)
            # check responses
            if key_resp_5.keys in ['', [], None]:  # No response was made
                key_resp_5.keys = None
            loop_8.addData('key_resp_5.keys',key_resp_5.keys)
            if key_resp_5.keys != None:  # we had a response
                loop_8.addData('key_resp_5.rt', key_resp_5.rt)
                loop_8.addData('key_resp_5.duration', key_resp_5.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_4.maxDurationReached:
                routineTimer.addTime(-trial_4.maxDuration)
            elif trial_4.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep8 repeats of 'loop_8'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_9 = data.TrialHandler2(
            name='loop_9',
            nReps=rep9, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('Incrementos.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_9)  # add the loop to the experiment
        thisLoop_9 = loop_9.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_9.rgb)
        if thisLoop_9 != None:
            for paramName in thisLoop_9:
                globals()[paramName] = thisLoop_9[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_9 in loop_9:
            currentLoop = loop_9
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_9.rgb)
            if thisLoop_9 != None:
                for paramName in thisLoop_9:
                    globals()[paramName] = thisLoop_9[paramName]
            
            # --- Prepare to start Routine "trial_5" ---
            # create an object to store info about Routine trial_5
            trial_5 = data.Routine(
                name='trial_5',
                components=[image_9, polygon_6, image_10, key_resp_6, text_5],
            )
            trial_5.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_9.setPos((px1, py1))
            image_10.setPos((px2, py2))
            # create starting attributes for key_resp_6
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            # store start times for trial_5
            trial_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_5.tStart = globalClock.getTime(format='float')
            trial_5.status = STARTED
            thisExp.addData('trial_5.started', trial_5.tStart)
            trial_5.maxDuration = None
            # keep track of which components have finished
            trial_5Components = trial_5.components
            for thisComponent in trial_5.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_5" ---
            # if trial has changed, end Routine now
            if isinstance(loop_9, data.TrialHandler2) and thisLoop_9.thisN != loop_9.thisTrial.thisN:
                continueRoutine = False
            trial_5.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_9* updates
                
                # if image_9 is starting this frame...
                if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_9.frameNStart = frameN  # exact frame index
                    image_9.tStart = t  # local t and not account for scr refresh
                    image_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_9.started')
                    # update status
                    image_9.status = STARTED
                    image_9.setAutoDraw(True)
                
                # if image_9 is active this frame...
                if image_9.status == STARTED:
                    # update params
                    pass
                
                # if image_9 is stopping this frame...
                if image_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_9.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_9.tStop = t  # not accounting for scr refresh
                        image_9.tStopRefresh = tThisFlipGlobal  # on global time
                        image_9.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_9.stopped')
                        # update status
                        image_9.status = FINISHED
                        image_9.setAutoDraw(False)
                
                # *polygon_6* updates
                
                # if polygon_6 is starting this frame...
                if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_6.frameNStart = frameN  # exact frame index
                    polygon_6.tStart = t  # local t and not account for scr refresh
                    polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_6.started')
                    # update status
                    polygon_6.status = STARTED
                    polygon_6.setAutoDraw(True)
                
                # if polygon_6 is active this frame...
                if polygon_6.status == STARTED:
                    # update params
                    pass
                
                # if polygon_6 is stopping this frame...
                if polygon_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_6.tStop = t  # not accounting for scr refresh
                        polygon_6.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                        # update status
                        polygon_6.status = FINISHED
                        polygon_6.setAutoDraw(False)
                
                # *image_10* updates
                
                # if image_10 is starting this frame...
                if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_10.frameNStart = frameN  # exact frame index
                    image_10.tStart = t  # local t and not account for scr refresh
                    image_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_10.started')
                    # update status
                    image_10.status = STARTED
                    image_10.setAutoDraw(True)
                
                # if image_10 is active this frame...
                if image_10.status == STARTED:
                    # update params
                    pass
                
                # if image_10 is stopping this frame...
                if image_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_10.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_10.tStop = t  # not accounting for scr refresh
                        image_10.tStopRefresh = tThisFlipGlobal  # on global time
                        image_10.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_10.stopped')
                        # update status
                        image_10.status = FINISHED
                        image_10.setAutoDraw(False)
                
                # *key_resp_6* updates
                waitOnFlip = False
                
                # if key_resp_6 is starting this frame...
                if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_6.started')
                    # update status
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_6 is stopping this frame...
                if key_resp_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_6.tStop = t  # not accounting for scr refresh
                        key_resp_6.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_6.stopped')
                        # update status
                        key_resp_6.status = FINISHED
                        key_resp_6.status = FINISHED
                if key_resp_6.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_6.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = [key.name for key in _key_resp_6_allKeys]  # storing all keys
                        key_resp_6.rt = [key.rt for key in _key_resp_6_allKeys]
                        key_resp_6.duration = [key.duration for key in _key_resp_6_allKeys]
                
                # *text_5* updates
                
                # if text_5 is starting this frame...
                if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_5.started')
                    # update status
                    text_5.status = STARTED
                    text_5.setAutoDraw(True)
                
                # if text_5 is active this frame...
                if text_5.status == STARTED:
                    # update params
                    text_5.setText(globalClock.getTime()
                    , log=False)
                
                # if text_5 is stopping this frame...
                if text_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_5.tStop = t  # not accounting for scr refresh
                        text_5.tStopRefresh = tThisFlipGlobal  # on global time
                        text_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_5.stopped')
                        # update status
                        text_5.status = FINISHED
                        text_5.setAutoDraw(False)
                # Run 'Each Frame' code from code_7
                
                if key_resp_6.keys:
                    dados.extend(zip(key_resp_6.keys, [globalClock.getTime()] * len(key_resp_6.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_5.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_5.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_5" ---
            for thisComponent in trial_5.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_5
            trial_5.tStop = globalClock.getTime(format='float')
            trial_5.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_5.stopped', trial_5.tStop)
            # check responses
            if key_resp_6.keys in ['', [], None]:  # No response was made
                key_resp_6.keys = None
            loop_9.addData('key_resp_6.keys',key_resp_6.keys)
            if key_resp_6.keys != None:  # we had a response
                loop_9.addData('key_resp_6.rt', key_resp_6.rt)
                loop_9.addData('key_resp_6.duration', key_resp_6.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_5.maxDurationReached:
                routineTimer.addTime(-trial_5.maxDuration)
            elif trial_5.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_6" ---
            # create an object to store info about Routine trial_6
            trial_6 = data.Routine(
                name='trial_6',
                components=[image_11, image_12, polygon_7, key_resp_7, text_6],
            )
            trial_6.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_11.setPos((px3, py3))
            image_12.setPos((px4, py4))
            # create starting attributes for key_resp_7
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            # store start times for trial_6
            trial_6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_6.tStart = globalClock.getTime(format='float')
            trial_6.status = STARTED
            thisExp.addData('trial_6.started', trial_6.tStart)
            trial_6.maxDuration = None
            # keep track of which components have finished
            trial_6Components = trial_6.components
            for thisComponent in trial_6.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_6" ---
            # if trial has changed, end Routine now
            if isinstance(loop_9, data.TrialHandler2) and thisLoop_9.thisN != loop_9.thisTrial.thisN:
                continueRoutine = False
            trial_6.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_11* updates
                
                # if image_11 is starting this frame...
                if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_11.frameNStart = frameN  # exact frame index
                    image_11.tStart = t  # local t and not account for scr refresh
                    image_11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_11.started')
                    # update status
                    image_11.status = STARTED
                    image_11.setAutoDraw(True)
                
                # if image_11 is active this frame...
                if image_11.status == STARTED:
                    # update params
                    pass
                
                # if image_11 is stopping this frame...
                if image_11.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_11.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_11.tStop = t  # not accounting for scr refresh
                        image_11.tStopRefresh = tThisFlipGlobal  # on global time
                        image_11.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_11.stopped')
                        # update status
                        image_11.status = FINISHED
                        image_11.setAutoDraw(False)
                
                # *image_12* updates
                
                # if image_12 is starting this frame...
                if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_12.frameNStart = frameN  # exact frame index
                    image_12.tStart = t  # local t and not account for scr refresh
                    image_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.started')
                    # update status
                    image_12.status = STARTED
                    image_12.setAutoDraw(True)
                
                # if image_12 is active this frame...
                if image_12.status == STARTED:
                    # update params
                    pass
                
                # if image_12 is stopping this frame...
                if image_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_12.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_12.tStop = t  # not accounting for scr refresh
                        image_12.tStopRefresh = tThisFlipGlobal  # on global time
                        image_12.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_12.stopped')
                        # update status
                        image_12.status = FINISHED
                        image_12.setAutoDraw(False)
                
                # *polygon_7* updates
                
                # if polygon_7 is starting this frame...
                if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_7.frameNStart = frameN  # exact frame index
                    polygon_7.tStart = t  # local t and not account for scr refresh
                    polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_7.started')
                    # update status
                    polygon_7.status = STARTED
                    polygon_7.setAutoDraw(True)
                
                # if polygon_7 is active this frame...
                if polygon_7.status == STARTED:
                    # update params
                    pass
                
                # if polygon_7 is stopping this frame...
                if polygon_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_7.tStop = t  # not accounting for scr refresh
                        polygon_7.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                        # update status
                        polygon_7.status = FINISHED
                        polygon_7.setAutoDraw(False)
                
                # *key_resp_7* updates
                waitOnFlip = False
                
                # if key_resp_7 is starting this frame...
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_7.started')
                    # update status
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_7 is stopping this frame...
                if key_resp_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_7.tStop = t  # not accounting for scr refresh
                        key_resp_7.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
                        # update status
                        key_resp_7.status = FINISHED
                        key_resp_7.status = FINISHED
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = [key.name for key in _key_resp_7_allKeys]  # storing all keys
                        key_resp_7.rt = [key.rt for key in _key_resp_7_allKeys]
                        key_resp_7.duration = [key.duration for key in _key_resp_7_allKeys]
                
                # *text_6* updates
                
                # if text_6 is starting this frame...
                if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.tStart = t  # local t and not account for scr refresh
                    text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.started')
                    # update status
                    text_6.status = STARTED
                    text_6.setAutoDraw(True)
                
                # if text_6 is active this frame...
                if text_6.status == STARTED:
                    # update params
                    text_6.setText(globalClock.getTime()
                    , log=False)
                
                # if text_6 is stopping this frame...
                if text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_6.tStop = t  # not accounting for scr refresh
                        text_6.tStopRefresh = tThisFlipGlobal  # on global time
                        text_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_6.stopped')
                        # update status
                        text_6.status = FINISHED
                        text_6.setAutoDraw(False)
                # Run 'Each Frame' code from code_8
                
                if key_resp_7.keys:
                    dados.extend(zip(key_resp_7.keys, [globalClock.getTime()] * len(key_resp_7.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_6.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_6.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_6" ---
            for thisComponent in trial_6.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_6
            trial_6.tStop = globalClock.getTime(format='float')
            trial_6.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_6.stopped', trial_6.tStop)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
            loop_9.addData('key_resp_7.keys',key_resp_7.keys)
            if key_resp_7.keys != None:  # we had a response
                loop_9.addData('key_resp_7.rt', key_resp_7.rt)
                loop_9.addData('key_resp_7.duration', key_resp_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_6.maxDurationReached:
                routineTimer.addTime(-trial_6.maxDuration)
            elif trial_6.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep9 repeats of 'loop_9'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_10 = data.TrialHandler2(
            name='loop_10',
            nReps=rep10, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('incremento_loop2.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_10)  # add the loop to the experiment
        thisLoop_10 = loop_10.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_10.rgb)
        if thisLoop_10 != None:
            for paramName in thisLoop_10:
                globals()[paramName] = thisLoop_10[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_10 in loop_10:
            currentLoop = loop_10
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_10.rgb)
            if thisLoop_10 != None:
                for paramName in thisLoop_10:
                    globals()[paramName] = thisLoop_10[paramName]
            
            # --- Prepare to start Routine "trial_5" ---
            # create an object to store info about Routine trial_5
            trial_5 = data.Routine(
                name='trial_5',
                components=[image_9, polygon_6, image_10, key_resp_6, text_5],
            )
            trial_5.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_9.setPos((px1, py1))
            image_10.setPos((px2, py2))
            # create starting attributes for key_resp_6
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            # store start times for trial_5
            trial_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_5.tStart = globalClock.getTime(format='float')
            trial_5.status = STARTED
            thisExp.addData('trial_5.started', trial_5.tStart)
            trial_5.maxDuration = None
            # keep track of which components have finished
            trial_5Components = trial_5.components
            for thisComponent in trial_5.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_5" ---
            # if trial has changed, end Routine now
            if isinstance(loop_10, data.TrialHandler2) and thisLoop_10.thisN != loop_10.thisTrial.thisN:
                continueRoutine = False
            trial_5.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_9* updates
                
                # if image_9 is starting this frame...
                if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_9.frameNStart = frameN  # exact frame index
                    image_9.tStart = t  # local t and not account for scr refresh
                    image_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_9.started')
                    # update status
                    image_9.status = STARTED
                    image_9.setAutoDraw(True)
                
                # if image_9 is active this frame...
                if image_9.status == STARTED:
                    # update params
                    pass
                
                # if image_9 is stopping this frame...
                if image_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_9.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_9.tStop = t  # not accounting for scr refresh
                        image_9.tStopRefresh = tThisFlipGlobal  # on global time
                        image_9.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_9.stopped')
                        # update status
                        image_9.status = FINISHED
                        image_9.setAutoDraw(False)
                
                # *polygon_6* updates
                
                # if polygon_6 is starting this frame...
                if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_6.frameNStart = frameN  # exact frame index
                    polygon_6.tStart = t  # local t and not account for scr refresh
                    polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_6.started')
                    # update status
                    polygon_6.status = STARTED
                    polygon_6.setAutoDraw(True)
                
                # if polygon_6 is active this frame...
                if polygon_6.status == STARTED:
                    # update params
                    pass
                
                # if polygon_6 is stopping this frame...
                if polygon_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_6.tStop = t  # not accounting for scr refresh
                        polygon_6.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                        # update status
                        polygon_6.status = FINISHED
                        polygon_6.setAutoDraw(False)
                
                # *image_10* updates
                
                # if image_10 is starting this frame...
                if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_10.frameNStart = frameN  # exact frame index
                    image_10.tStart = t  # local t and not account for scr refresh
                    image_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_10.started')
                    # update status
                    image_10.status = STARTED
                    image_10.setAutoDraw(True)
                
                # if image_10 is active this frame...
                if image_10.status == STARTED:
                    # update params
                    pass
                
                # if image_10 is stopping this frame...
                if image_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_10.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_10.tStop = t  # not accounting for scr refresh
                        image_10.tStopRefresh = tThisFlipGlobal  # on global time
                        image_10.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_10.stopped')
                        # update status
                        image_10.status = FINISHED
                        image_10.setAutoDraw(False)
                
                # *key_resp_6* updates
                waitOnFlip = False
                
                # if key_resp_6 is starting this frame...
                if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_6.started')
                    # update status
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_6 is stopping this frame...
                if key_resp_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_6.tStop = t  # not accounting for scr refresh
                        key_resp_6.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_6.stopped')
                        # update status
                        key_resp_6.status = FINISHED
                        key_resp_6.status = FINISHED
                if key_resp_6.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_6.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = [key.name for key in _key_resp_6_allKeys]  # storing all keys
                        key_resp_6.rt = [key.rt for key in _key_resp_6_allKeys]
                        key_resp_6.duration = [key.duration for key in _key_resp_6_allKeys]
                
                # *text_5* updates
                
                # if text_5 is starting this frame...
                if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_5.started')
                    # update status
                    text_5.status = STARTED
                    text_5.setAutoDraw(True)
                
                # if text_5 is active this frame...
                if text_5.status == STARTED:
                    # update params
                    text_5.setText(globalClock.getTime()
                    , log=False)
                
                # if text_5 is stopping this frame...
                if text_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_5.tStop = t  # not accounting for scr refresh
                        text_5.tStopRefresh = tThisFlipGlobal  # on global time
                        text_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_5.stopped')
                        # update status
                        text_5.status = FINISHED
                        text_5.setAutoDraw(False)
                # Run 'Each Frame' code from code_7
                
                if key_resp_6.keys:
                    dados.extend(zip(key_resp_6.keys, [globalClock.getTime()] * len(key_resp_6.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_5.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_5.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_5" ---
            for thisComponent in trial_5.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_5
            trial_5.tStop = globalClock.getTime(format='float')
            trial_5.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_5.stopped', trial_5.tStop)
            # check responses
            if key_resp_6.keys in ['', [], None]:  # No response was made
                key_resp_6.keys = None
            loop_10.addData('key_resp_6.keys',key_resp_6.keys)
            if key_resp_6.keys != None:  # we had a response
                loop_10.addData('key_resp_6.rt', key_resp_6.rt)
                loop_10.addData('key_resp_6.duration', key_resp_6.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_5.maxDurationReached:
                routineTimer.addTime(-trial_5.maxDuration)
            elif trial_5.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_6" ---
            # create an object to store info about Routine trial_6
            trial_6 = data.Routine(
                name='trial_6',
                components=[image_11, image_12, polygon_7, key_resp_7, text_6],
            )
            trial_6.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_11.setPos((px3, py3))
            image_12.setPos((px4, py4))
            # create starting attributes for key_resp_7
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            # store start times for trial_6
            trial_6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_6.tStart = globalClock.getTime(format='float')
            trial_6.status = STARTED
            thisExp.addData('trial_6.started', trial_6.tStart)
            trial_6.maxDuration = None
            # keep track of which components have finished
            trial_6Components = trial_6.components
            for thisComponent in trial_6.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_6" ---
            # if trial has changed, end Routine now
            if isinstance(loop_10, data.TrialHandler2) and thisLoop_10.thisN != loop_10.thisTrial.thisN:
                continueRoutine = False
            trial_6.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_11* updates
                
                # if image_11 is starting this frame...
                if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_11.frameNStart = frameN  # exact frame index
                    image_11.tStart = t  # local t and not account for scr refresh
                    image_11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_11.started')
                    # update status
                    image_11.status = STARTED
                    image_11.setAutoDraw(True)
                
                # if image_11 is active this frame...
                if image_11.status == STARTED:
                    # update params
                    pass
                
                # if image_11 is stopping this frame...
                if image_11.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_11.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_11.tStop = t  # not accounting for scr refresh
                        image_11.tStopRefresh = tThisFlipGlobal  # on global time
                        image_11.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_11.stopped')
                        # update status
                        image_11.status = FINISHED
                        image_11.setAutoDraw(False)
                
                # *image_12* updates
                
                # if image_12 is starting this frame...
                if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_12.frameNStart = frameN  # exact frame index
                    image_12.tStart = t  # local t and not account for scr refresh
                    image_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.started')
                    # update status
                    image_12.status = STARTED
                    image_12.setAutoDraw(True)
                
                # if image_12 is active this frame...
                if image_12.status == STARTED:
                    # update params
                    pass
                
                # if image_12 is stopping this frame...
                if image_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_12.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_12.tStop = t  # not accounting for scr refresh
                        image_12.tStopRefresh = tThisFlipGlobal  # on global time
                        image_12.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_12.stopped')
                        # update status
                        image_12.status = FINISHED
                        image_12.setAutoDraw(False)
                
                # *polygon_7* updates
                
                # if polygon_7 is starting this frame...
                if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_7.frameNStart = frameN  # exact frame index
                    polygon_7.tStart = t  # local t and not account for scr refresh
                    polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_7.started')
                    # update status
                    polygon_7.status = STARTED
                    polygon_7.setAutoDraw(True)
                
                # if polygon_7 is active this frame...
                if polygon_7.status == STARTED:
                    # update params
                    pass
                
                # if polygon_7 is stopping this frame...
                if polygon_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_7.tStop = t  # not accounting for scr refresh
                        polygon_7.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                        # update status
                        polygon_7.status = FINISHED
                        polygon_7.setAutoDraw(False)
                
                # *key_resp_7* updates
                waitOnFlip = False
                
                # if key_resp_7 is starting this frame...
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_7.started')
                    # update status
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_7 is stopping this frame...
                if key_resp_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_7.tStop = t  # not accounting for scr refresh
                        key_resp_7.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
                        # update status
                        key_resp_7.status = FINISHED
                        key_resp_7.status = FINISHED
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = [key.name for key in _key_resp_7_allKeys]  # storing all keys
                        key_resp_7.rt = [key.rt for key in _key_resp_7_allKeys]
                        key_resp_7.duration = [key.duration for key in _key_resp_7_allKeys]
                
                # *text_6* updates
                
                # if text_6 is starting this frame...
                if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.tStart = t  # local t and not account for scr refresh
                    text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.started')
                    # update status
                    text_6.status = STARTED
                    text_6.setAutoDraw(True)
                
                # if text_6 is active this frame...
                if text_6.status == STARTED:
                    # update params
                    text_6.setText(globalClock.getTime()
                    , log=False)
                
                # if text_6 is stopping this frame...
                if text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_6.tStop = t  # not accounting for scr refresh
                        text_6.tStopRefresh = tThisFlipGlobal  # on global time
                        text_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_6.stopped')
                        # update status
                        text_6.status = FINISHED
                        text_6.setAutoDraw(False)
                # Run 'Each Frame' code from code_8
                
                if key_resp_7.keys:
                    dados.extend(zip(key_resp_7.keys, [globalClock.getTime()] * len(key_resp_7.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_6.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_6.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_6" ---
            for thisComponent in trial_6.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_6
            trial_6.tStop = globalClock.getTime(format='float')
            trial_6.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_6.stopped', trial_6.tStop)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
            loop_10.addData('key_resp_7.keys',key_resp_7.keys)
            if key_resp_7.keys != None:  # we had a response
                loop_10.addData('key_resp_7.rt', key_resp_7.rt)
                loop_10.addData('key_resp_7.duration', key_resp_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_6.maxDurationReached:
                routineTimer.addTime(-trial_6.maxDuration)
            elif trial_6.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep10 repeats of 'loop_10'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_11 = data.TrialHandler2(
            name='loop_11',
            nReps=rep11, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('incremento_loop3.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_11)  # add the loop to the experiment
        thisLoop_11 = loop_11.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_11.rgb)
        if thisLoop_11 != None:
            for paramName in thisLoop_11:
                globals()[paramName] = thisLoop_11[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_11 in loop_11:
            currentLoop = loop_11
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_11.rgb)
            if thisLoop_11 != None:
                for paramName in thisLoop_11:
                    globals()[paramName] = thisLoop_11[paramName]
            
            # --- Prepare to start Routine "trial_5" ---
            # create an object to store info about Routine trial_5
            trial_5 = data.Routine(
                name='trial_5',
                components=[image_9, polygon_6, image_10, key_resp_6, text_5],
            )
            trial_5.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_9.setPos((px1, py1))
            image_10.setPos((px2, py2))
            # create starting attributes for key_resp_6
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            # store start times for trial_5
            trial_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_5.tStart = globalClock.getTime(format='float')
            trial_5.status = STARTED
            thisExp.addData('trial_5.started', trial_5.tStart)
            trial_5.maxDuration = None
            # keep track of which components have finished
            trial_5Components = trial_5.components
            for thisComponent in trial_5.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_5" ---
            # if trial has changed, end Routine now
            if isinstance(loop_11, data.TrialHandler2) and thisLoop_11.thisN != loop_11.thisTrial.thisN:
                continueRoutine = False
            trial_5.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_9* updates
                
                # if image_9 is starting this frame...
                if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_9.frameNStart = frameN  # exact frame index
                    image_9.tStart = t  # local t and not account for scr refresh
                    image_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_9.started')
                    # update status
                    image_9.status = STARTED
                    image_9.setAutoDraw(True)
                
                # if image_9 is active this frame...
                if image_9.status == STARTED:
                    # update params
                    pass
                
                # if image_9 is stopping this frame...
                if image_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_9.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_9.tStop = t  # not accounting for scr refresh
                        image_9.tStopRefresh = tThisFlipGlobal  # on global time
                        image_9.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_9.stopped')
                        # update status
                        image_9.status = FINISHED
                        image_9.setAutoDraw(False)
                
                # *polygon_6* updates
                
                # if polygon_6 is starting this frame...
                if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_6.frameNStart = frameN  # exact frame index
                    polygon_6.tStart = t  # local t and not account for scr refresh
                    polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_6.started')
                    # update status
                    polygon_6.status = STARTED
                    polygon_6.setAutoDraw(True)
                
                # if polygon_6 is active this frame...
                if polygon_6.status == STARTED:
                    # update params
                    pass
                
                # if polygon_6 is stopping this frame...
                if polygon_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_6.tStop = t  # not accounting for scr refresh
                        polygon_6.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                        # update status
                        polygon_6.status = FINISHED
                        polygon_6.setAutoDraw(False)
                
                # *image_10* updates
                
                # if image_10 is starting this frame...
                if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_10.frameNStart = frameN  # exact frame index
                    image_10.tStart = t  # local t and not account for scr refresh
                    image_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_10.started')
                    # update status
                    image_10.status = STARTED
                    image_10.setAutoDraw(True)
                
                # if image_10 is active this frame...
                if image_10.status == STARTED:
                    # update params
                    pass
                
                # if image_10 is stopping this frame...
                if image_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_10.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_10.tStop = t  # not accounting for scr refresh
                        image_10.tStopRefresh = tThisFlipGlobal  # on global time
                        image_10.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_10.stopped')
                        # update status
                        image_10.status = FINISHED
                        image_10.setAutoDraw(False)
                
                # *key_resp_6* updates
                waitOnFlip = False
                
                # if key_resp_6 is starting this frame...
                if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_6.started')
                    # update status
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_6 is stopping this frame...
                if key_resp_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_6.tStop = t  # not accounting for scr refresh
                        key_resp_6.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_6.stopped')
                        # update status
                        key_resp_6.status = FINISHED
                        key_resp_6.status = FINISHED
                if key_resp_6.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_6.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = [key.name for key in _key_resp_6_allKeys]  # storing all keys
                        key_resp_6.rt = [key.rt for key in _key_resp_6_allKeys]
                        key_resp_6.duration = [key.duration for key in _key_resp_6_allKeys]
                
                # *text_5* updates
                
                # if text_5 is starting this frame...
                if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_5.started')
                    # update status
                    text_5.status = STARTED
                    text_5.setAutoDraw(True)
                
                # if text_5 is active this frame...
                if text_5.status == STARTED:
                    # update params
                    text_5.setText(globalClock.getTime()
                    , log=False)
                
                # if text_5 is stopping this frame...
                if text_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_5.tStop = t  # not accounting for scr refresh
                        text_5.tStopRefresh = tThisFlipGlobal  # on global time
                        text_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_5.stopped')
                        # update status
                        text_5.status = FINISHED
                        text_5.setAutoDraw(False)
                # Run 'Each Frame' code from code_7
                
                if key_resp_6.keys:
                    dados.extend(zip(key_resp_6.keys, [globalClock.getTime()] * len(key_resp_6.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_5.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_5.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_5" ---
            for thisComponent in trial_5.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_5
            trial_5.tStop = globalClock.getTime(format='float')
            trial_5.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_5.stopped', trial_5.tStop)
            # check responses
            if key_resp_6.keys in ['', [], None]:  # No response was made
                key_resp_6.keys = None
            loop_11.addData('key_resp_6.keys',key_resp_6.keys)
            if key_resp_6.keys != None:  # we had a response
                loop_11.addData('key_resp_6.rt', key_resp_6.rt)
                loop_11.addData('key_resp_6.duration', key_resp_6.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_5.maxDurationReached:
                routineTimer.addTime(-trial_5.maxDuration)
            elif trial_5.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_6" ---
            # create an object to store info about Routine trial_6
            trial_6 = data.Routine(
                name='trial_6',
                components=[image_11, image_12, polygon_7, key_resp_7, text_6],
            )
            trial_6.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_11.setPos((px3, py3))
            image_12.setPos((px4, py4))
            # create starting attributes for key_resp_7
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            # store start times for trial_6
            trial_6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_6.tStart = globalClock.getTime(format='float')
            trial_6.status = STARTED
            thisExp.addData('trial_6.started', trial_6.tStart)
            trial_6.maxDuration = None
            # keep track of which components have finished
            trial_6Components = trial_6.components
            for thisComponent in trial_6.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_6" ---
            # if trial has changed, end Routine now
            if isinstance(loop_11, data.TrialHandler2) and thisLoop_11.thisN != loop_11.thisTrial.thisN:
                continueRoutine = False
            trial_6.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_11* updates
                
                # if image_11 is starting this frame...
                if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_11.frameNStart = frameN  # exact frame index
                    image_11.tStart = t  # local t and not account for scr refresh
                    image_11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_11.started')
                    # update status
                    image_11.status = STARTED
                    image_11.setAutoDraw(True)
                
                # if image_11 is active this frame...
                if image_11.status == STARTED:
                    # update params
                    pass
                
                # if image_11 is stopping this frame...
                if image_11.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_11.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_11.tStop = t  # not accounting for scr refresh
                        image_11.tStopRefresh = tThisFlipGlobal  # on global time
                        image_11.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_11.stopped')
                        # update status
                        image_11.status = FINISHED
                        image_11.setAutoDraw(False)
                
                # *image_12* updates
                
                # if image_12 is starting this frame...
                if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_12.frameNStart = frameN  # exact frame index
                    image_12.tStart = t  # local t and not account for scr refresh
                    image_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.started')
                    # update status
                    image_12.status = STARTED
                    image_12.setAutoDraw(True)
                
                # if image_12 is active this frame...
                if image_12.status == STARTED:
                    # update params
                    pass
                
                # if image_12 is stopping this frame...
                if image_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_12.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_12.tStop = t  # not accounting for scr refresh
                        image_12.tStopRefresh = tThisFlipGlobal  # on global time
                        image_12.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_12.stopped')
                        # update status
                        image_12.status = FINISHED
                        image_12.setAutoDraw(False)
                
                # *polygon_7* updates
                
                # if polygon_7 is starting this frame...
                if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_7.frameNStart = frameN  # exact frame index
                    polygon_7.tStart = t  # local t and not account for scr refresh
                    polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_7.started')
                    # update status
                    polygon_7.status = STARTED
                    polygon_7.setAutoDraw(True)
                
                # if polygon_7 is active this frame...
                if polygon_7.status == STARTED:
                    # update params
                    pass
                
                # if polygon_7 is stopping this frame...
                if polygon_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_7.tStop = t  # not accounting for scr refresh
                        polygon_7.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                        # update status
                        polygon_7.status = FINISHED
                        polygon_7.setAutoDraw(False)
                
                # *key_resp_7* updates
                waitOnFlip = False
                
                # if key_resp_7 is starting this frame...
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_7.started')
                    # update status
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_7 is stopping this frame...
                if key_resp_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_7.tStop = t  # not accounting for scr refresh
                        key_resp_7.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
                        # update status
                        key_resp_7.status = FINISHED
                        key_resp_7.status = FINISHED
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = [key.name for key in _key_resp_7_allKeys]  # storing all keys
                        key_resp_7.rt = [key.rt for key in _key_resp_7_allKeys]
                        key_resp_7.duration = [key.duration for key in _key_resp_7_allKeys]
                
                # *text_6* updates
                
                # if text_6 is starting this frame...
                if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.tStart = t  # local t and not account for scr refresh
                    text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.started')
                    # update status
                    text_6.status = STARTED
                    text_6.setAutoDraw(True)
                
                # if text_6 is active this frame...
                if text_6.status == STARTED:
                    # update params
                    text_6.setText(globalClock.getTime()
                    , log=False)
                
                # if text_6 is stopping this frame...
                if text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_6.tStop = t  # not accounting for scr refresh
                        text_6.tStopRefresh = tThisFlipGlobal  # on global time
                        text_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_6.stopped')
                        # update status
                        text_6.status = FINISHED
                        text_6.setAutoDraw(False)
                # Run 'Each Frame' code from code_8
                
                if key_resp_7.keys:
                    dados.extend(zip(key_resp_7.keys, [globalClock.getTime()] * len(key_resp_7.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_6.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_6.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_6" ---
            for thisComponent in trial_6.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_6
            trial_6.tStop = globalClock.getTime(format='float')
            trial_6.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_6.stopped', trial_6.tStop)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
            loop_11.addData('key_resp_7.keys',key_resp_7.keys)
            if key_resp_7.keys != None:  # we had a response
                loop_11.addData('key_resp_7.rt', key_resp_7.rt)
                loop_11.addData('key_resp_7.duration', key_resp_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_6.maxDurationReached:
                routineTimer.addTime(-trial_6.maxDuration)
            elif trial_6.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep11 repeats of 'loop_11'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # set up handler to look after randomisation of conditions etc
        loop_12 = data.TrialHandler2(
            name='loop_12',
            nReps=rep12, 
            method='sequential', 
            extraInfo=expInfo, 
            originPath=-1, 
            trialList=data.importConditions('Incrementos_loop_4.xlsx'), 
            seed=None, 
        )
        thisExp.addLoop(loop_12)  # add the loop to the experiment
        thisLoop_12 = loop_12.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisLoop_12.rgb)
        if thisLoop_12 != None:
            for paramName in thisLoop_12:
                globals()[paramName] = thisLoop_12[paramName]
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        for thisLoop_12 in loop_12:
            currentLoop = loop_12
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
            # abbreviate parameter names if possible (e.g. rgb = thisLoop_12.rgb)
            if thisLoop_12 != None:
                for paramName in thisLoop_12:
                    globals()[paramName] = thisLoop_12[paramName]
            
            # --- Prepare to start Routine "trial_5" ---
            # create an object to store info about Routine trial_5
            trial_5 = data.Routine(
                name='trial_5',
                components=[image_9, polygon_6, image_10, key_resp_6, text_5],
            )
            trial_5.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_9.setPos((px1, py1))
            image_10.setPos((px2, py2))
            # create starting attributes for key_resp_6
            key_resp_6.keys = []
            key_resp_6.rt = []
            _key_resp_6_allKeys = []
            # store start times for trial_5
            trial_5.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_5.tStart = globalClock.getTime(format='float')
            trial_5.status = STARTED
            thisExp.addData('trial_5.started', trial_5.tStart)
            trial_5.maxDuration = None
            # keep track of which components have finished
            trial_5Components = trial_5.components
            for thisComponent in trial_5.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_5" ---
            # if trial has changed, end Routine now
            if isinstance(loop_12, data.TrialHandler2) and thisLoop_12.thisN != loop_12.thisTrial.thisN:
                continueRoutine = False
            trial_5.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_9* updates
                
                # if image_9 is starting this frame...
                if image_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_9.frameNStart = frameN  # exact frame index
                    image_9.tStart = t  # local t and not account for scr refresh
                    image_9.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_9.started')
                    # update status
                    image_9.status = STARTED
                    image_9.setAutoDraw(True)
                
                # if image_9 is active this frame...
                if image_9.status == STARTED:
                    # update params
                    pass
                
                # if image_9 is stopping this frame...
                if image_9.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_9.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_9.tStop = t  # not accounting for scr refresh
                        image_9.tStopRefresh = tThisFlipGlobal  # on global time
                        image_9.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_9.stopped')
                        # update status
                        image_9.status = FINISHED
                        image_9.setAutoDraw(False)
                
                # *polygon_6* updates
                
                # if polygon_6 is starting this frame...
                if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_6.frameNStart = frameN  # exact frame index
                    polygon_6.tStart = t  # local t and not account for scr refresh
                    polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_6.started')
                    # update status
                    polygon_6.status = STARTED
                    polygon_6.setAutoDraw(True)
                
                # if polygon_6 is active this frame...
                if polygon_6.status == STARTED:
                    # update params
                    pass
                
                # if polygon_6 is stopping this frame...
                if polygon_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_6.tStop = t  # not accounting for scr refresh
                        polygon_6.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_6.stopped')
                        # update status
                        polygon_6.status = FINISHED
                        polygon_6.setAutoDraw(False)
                
                # *image_10* updates
                
                # if image_10 is starting this frame...
                if image_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_10.frameNStart = frameN  # exact frame index
                    image_10.tStart = t  # local t and not account for scr refresh
                    image_10.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_10, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_10.started')
                    # update status
                    image_10.status = STARTED
                    image_10.setAutoDraw(True)
                
                # if image_10 is active this frame...
                if image_10.status == STARTED:
                    # update params
                    pass
                
                # if image_10 is stopping this frame...
                if image_10.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_10.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_10.tStop = t  # not accounting for scr refresh
                        image_10.tStopRefresh = tThisFlipGlobal  # on global time
                        image_10.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_10.stopped')
                        # update status
                        image_10.status = FINISHED
                        image_10.setAutoDraw(False)
                
                # *key_resp_6* updates
                waitOnFlip = False
                
                # if key_resp_6 is starting this frame...
                if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_6.frameNStart = frameN  # exact frame index
                    key_resp_6.tStart = t  # local t and not account for scr refresh
                    key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_6.started')
                    # update status
                    key_resp_6.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_6 is stopping this frame...
                if key_resp_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_6.tStop = t  # not accounting for scr refresh
                        key_resp_6.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_6.stopped')
                        # update status
                        key_resp_6.status = FINISHED
                        key_resp_6.status = FINISHED
                if key_resp_6.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_6.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_6_allKeys.extend(theseKeys)
                    if len(_key_resp_6_allKeys):
                        key_resp_6.keys = [key.name for key in _key_resp_6_allKeys]  # storing all keys
                        key_resp_6.rt = [key.rt for key in _key_resp_6_allKeys]
                        key_resp_6.duration = [key.duration for key in _key_resp_6_allKeys]
                
                # *text_5* updates
                
                # if text_5 is starting this frame...
                if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_5.frameNStart = frameN  # exact frame index
                    text_5.tStart = t  # local t and not account for scr refresh
                    text_5.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_5.started')
                    # update status
                    text_5.status = STARTED
                    text_5.setAutoDraw(True)
                
                # if text_5 is active this frame...
                if text_5.status == STARTED:
                    # update params
                    text_5.setText(globalClock.getTime()
                    , log=False)
                
                # if text_5 is stopping this frame...
                if text_5.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_5.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_5.tStop = t  # not accounting for scr refresh
                        text_5.tStopRefresh = tThisFlipGlobal  # on global time
                        text_5.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_5.stopped')
                        # update status
                        text_5.status = FINISHED
                        text_5.setAutoDraw(False)
                # Run 'Each Frame' code from code_7
                
                if key_resp_6.keys:
                    dados.extend(zip(key_resp_6.keys, [globalClock.getTime()] * len(key_resp_6.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_5.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_5.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_5" ---
            for thisComponent in trial_5.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_5
            trial_5.tStop = globalClock.getTime(format='float')
            trial_5.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_5.stopped', trial_5.tStop)
            # check responses
            if key_resp_6.keys in ['', [], None]:  # No response was made
                key_resp_6.keys = None
            loop_12.addData('key_resp_6.keys',key_resp_6.keys)
            if key_resp_6.keys != None:  # we had a response
                loop_12.addData('key_resp_6.rt', key_resp_6.rt)
                loop_12.addData('key_resp_6.duration', key_resp_6.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_5.maxDurationReached:
                routineTimer.addTime(-trial_5.maxDuration)
            elif trial_5.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            
            # --- Prepare to start Routine "trial_6" ---
            # create an object to store info about Routine trial_6
            trial_6 = data.Routine(
                name='trial_6',
                components=[image_11, image_12, polygon_7, key_resp_7, text_6],
            )
            trial_6.status = NOT_STARTED
            continueRoutine = True
            # update component parameters for each repeat
            image_11.setPos((px3, py3))
            image_12.setPos((px4, py4))
            # create starting attributes for key_resp_7
            key_resp_7.keys = []
            key_resp_7.rt = []
            _key_resp_7_allKeys = []
            # store start times for trial_6
            trial_6.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
            trial_6.tStart = globalClock.getTime(format='float')
            trial_6.status = STARTED
            thisExp.addData('trial_6.started', trial_6.tStart)
            trial_6.maxDuration = None
            # keep track of which components have finished
            trial_6Components = trial_6.components
            for thisComponent in trial_6.components:
                thisComponent.tStart = None
                thisComponent.tStop = None
                thisComponent.tStartRefresh = None
                thisComponent.tStopRefresh = None
                if hasattr(thisComponent, 'status'):
                    thisComponent.status = NOT_STARTED
            # reset timers
            t = 0
            _timeToFirstFrame = win.getFutureFlipTime(clock="now")
            frameN = -1
            
            # --- Run Routine "trial_6" ---
            # if trial has changed, end Routine now
            if isinstance(loop_12, data.TrialHandler2) and thisLoop_12.thisN != loop_12.thisTrial.thisN:
                continueRoutine = False
            trial_6.forceEnded = routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 0.3:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_11* updates
                
                # if image_11 is starting this frame...
                if image_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_11.frameNStart = frameN  # exact frame index
                    image_11.tStart = t  # local t and not account for scr refresh
                    image_11.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_11, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_11.started')
                    # update status
                    image_11.status = STARTED
                    image_11.setAutoDraw(True)
                
                # if image_11 is active this frame...
                if image_11.status == STARTED:
                    # update params
                    pass
                
                # if image_11 is stopping this frame...
                if image_11.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_11.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_11.tStop = t  # not accounting for scr refresh
                        image_11.tStopRefresh = tThisFlipGlobal  # on global time
                        image_11.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_11.stopped')
                        # update status
                        image_11.status = FINISHED
                        image_11.setAutoDraw(False)
                
                # *image_12* updates
                
                # if image_12 is starting this frame...
                if image_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_12.frameNStart = frameN  # exact frame index
                    image_12.tStart = t  # local t and not account for scr refresh
                    image_12.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_12, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'image_12.started')
                    # update status
                    image_12.status = STARTED
                    image_12.setAutoDraw(True)
                
                # if image_12 is active this frame...
                if image_12.status == STARTED:
                    # update params
                    pass
                
                # if image_12 is stopping this frame...
                if image_12.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > image_12.tStartRefresh + 0.25-frameTolerance:
                        # keep track of stop time/frame for later
                        image_12.tStop = t  # not accounting for scr refresh
                        image_12.tStopRefresh = tThisFlipGlobal  # on global time
                        image_12.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'image_12.stopped')
                        # update status
                        image_12.status = FINISHED
                        image_12.setAutoDraw(False)
                
                # *polygon_7* updates
                
                # if polygon_7 is starting this frame...
                if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_7.frameNStart = frameN  # exact frame index
                    polygon_7.tStart = t  # local t and not account for scr refresh
                    polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_7.started')
                    # update status
                    polygon_7.status = STARTED
                    polygon_7.setAutoDraw(True)
                
                # if polygon_7 is active this frame...
                if polygon_7.status == STARTED:
                    # update params
                    pass
                
                # if polygon_7 is stopping this frame...
                if polygon_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > polygon_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        polygon_7.tStop = t  # not accounting for scr refresh
                        polygon_7.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon_7.stopped')
                        # update status
                        polygon_7.status = FINISHED
                        polygon_7.setAutoDraw(False)
                
                # *key_resp_7* updates
                waitOnFlip = False
                
                # if key_resp_7 is starting this frame...
                if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    key_resp_7.frameNStart = frameN  # exact frame index
                    key_resp_7.tStart = t  # local t and not account for scr refresh
                    key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp_7.started')
                    # update status
                    key_resp_7.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
                
                # if key_resp_7 is stopping this frame...
                if key_resp_7.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > key_resp_7.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        key_resp_7.tStop = t  # not accounting for scr refresh
                        key_resp_7.tStopRefresh = tThisFlipGlobal  # on global time
                        key_resp_7.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'key_resp_7.stopped')
                        # update status
                        key_resp_7.status = FINISHED
                        key_resp_7.status = FINISHED
                if key_resp_7.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp_7.getKeys(keyList=['up','right'], ignoreKeys=["escape"], waitRelease=False)
                    _key_resp_7_allKeys.extend(theseKeys)
                    if len(_key_resp_7_allKeys):
                        key_resp_7.keys = [key.name for key in _key_resp_7_allKeys]  # storing all keys
                        key_resp_7.rt = [key.rt for key in _key_resp_7_allKeys]
                        key_resp_7.duration = [key.duration for key in _key_resp_7_allKeys]
                
                # *text_6* updates
                
                # if text_6 is starting this frame...
                if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_6.frameNStart = frameN  # exact frame index
                    text_6.tStart = t  # local t and not account for scr refresh
                    text_6.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_6.started')
                    # update status
                    text_6.status = STARTED
                    text_6.setAutoDraw(True)
                
                # if text_6 is active this frame...
                if text_6.status == STARTED:
                    # update params
                    text_6.setText(globalClock.getTime()
                    , log=False)
                
                # if text_6 is stopping this frame...
                if text_6.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > text_6.tStartRefresh + 0.3-frameTolerance:
                        # keep track of stop time/frame for later
                        text_6.tStop = t  # not accounting for scr refresh
                        text_6.tStopRefresh = tThisFlipGlobal  # on global time
                        text_6.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_6.stopped')
                        # update status
                        text_6.status = FINISHED
                        text_6.setAutoDraw(False)
                # Run 'Each Frame' code from code_8
                
                if key_resp_7.keys:
                    dados.extend(zip(key_resp_7.keys, [globalClock.getTime()] * len(key_resp_7.keys)))
                
                
                # check for quit (typically the Esc key)
                if defaultKeyboard.getKeys(keyList=["escape"]):
                    thisExp.status = FINISHED
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                # pause experiment here if requested
                if thisExp.status == PAUSED:
                    pauseExperiment(
                        thisExp=thisExp, 
                        win=win, 
                        timers=[routineTimer], 
                        playbackComponents=[]
                    )
                    # skip the frame we paused on
                    continue
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    trial_6.forceEnded = routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_6.components:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_6" ---
            for thisComponent in trial_6.components:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            # store stop times for trial_6
            trial_6.tStop = globalClock.getTime(format='float')
            trial_6.tStopRefresh = tThisFlipGlobal
            thisExp.addData('trial_6.stopped', trial_6.tStop)
            # check responses
            if key_resp_7.keys in ['', [], None]:  # No response was made
                key_resp_7.keys = None
            loop_12.addData('key_resp_7.keys',key_resp_7.keys)
            if key_resp_7.keys != None:  # we had a response
                loop_12.addData('key_resp_7.rt', key_resp_7.rt)
                loop_12.addData('key_resp_7.duration', key_resp_7.duration)
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if trial_6.maxDurationReached:
                routineTimer.addTime(-trial_6.maxDuration)
            elif trial_6.forceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-0.300000)
            thisExp.nextEntry()
            
        # completed rep12 repeats of 'loop_12'
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
        
        # --- Prepare to start Routine "_intertrial_interval_" ---
        # create an object to store info about Routine _intertrial_interval_
        _intertrial_interval_ = data.Routine(
            name='_intertrial_interval_',
            components=[polygon_5],
        )
        _intertrial_interval_.status = NOT_STARTED
        continueRoutine = True
        # update component parameters for each repeat
        # store start times for _intertrial_interval_
        _intertrial_interval_.tStartRefresh = win.getFutureFlipTime(clock=globalClock)
        _intertrial_interval_.tStart = globalClock.getTime(format='float')
        _intertrial_interval_.status = STARTED
        thisExp.addData('_intertrial_interval_.started', _intertrial_interval_.tStart)
        _intertrial_interval_.maxDuration = None
        # keep track of which components have finished
        _intertrial_interval_Components = _intertrial_interval_.components
        for thisComponent in _intertrial_interval_.components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "_intertrial_interval_" ---
        # if trial has changed, end Routine now
        if isinstance(MainLoop, data.TrialHandler2) and thisMainLoop.thisN != MainLoop.thisTrial.thisN:
            continueRoutine = False
        _intertrial_interval_.forceEnded = routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.5:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *polygon_5* updates
            
            # if polygon_5 is starting this frame...
            if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                polygon_5.frameNStart = frameN  # exact frame index
                polygon_5.tStart = t  # local t and not account for scr refresh
                polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_5.started')
                # update status
                polygon_5.status = STARTED
                polygon_5.setAutoDraw(True)
            
            # if polygon_5 is active this frame...
            if polygon_5.status == STARTED:
                # update params
                pass
            
            # if polygon_5 is stopping this frame...
            if polygon_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > polygon_5.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    polygon_5.tStop = t  # not accounting for scr refresh
                    polygon_5.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon_5.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_5.stopped')
                    # update status
                    polygon_5.status = FINISHED
                    polygon_5.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
                )
                # skip the frame we paused on
                continue
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                _intertrial_interval_.forceEnded = routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in _intertrial_interval_.components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "_intertrial_interval_" ---
        for thisComponent in _intertrial_interval_.components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # store stop times for _intertrial_interval_
        _intertrial_interval_.tStop = globalClock.getTime(format='float')
        _intertrial_interval_.tStopRefresh = tThisFlipGlobal
        thisExp.addData('_intertrial_interval_.stopped', _intertrial_interval_.tStop)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if _intertrial_interval_.maxDurationReached:
            routineTimer.addTime(-_intertrial_interval_.maxDuration)
        elif _intertrial_interval_.forceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.500000)
        thisExp.nextEntry()
        
    # completed 8.0 repeats of 'MainLoop'
    
    if thisSession is not None:
        # if running in a Session with a Liaison client, send data up to now
        thisSession.sendExperimentData()
    # Run 'End Experiment' code from code
    print("End routine!")
    import csv
    
    # Obtendo o diretório do Desktop (para Windows)
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    
    # Caminho completo para salvar o arquivo CSV no Desktop
    caminho_arquivo = os.path.join(desktop, 'dados_exp.csv')
    
    # Abrindo o arquivo para escrita
    with open(nome_arquivo, mode='w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        
        # Escrevendo as linhas da matriz no arquivo CSV
        escritor_csv.writerows(dados)
    
    print(f"Dados salvos em {nome_arquivo}")
    print("Experiment iniciado!")
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # return console logger level to WARNING
    logging.console.setLevel(logging.WARNING)
    # mark experiment handler as finished
    thisExp.status = FINISHED
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)

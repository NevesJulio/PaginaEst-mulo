/********************* 
 * Estimulo_Ice *
 *********************/


// store info about the experiment session:
let expName = 'Estimulo_ICE';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(salvarRoutineBegin());
flowScheduler.add(salvarRoutineEachFrame());
flowScheduler.add(salvarRoutineEnd());
const MainLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(MainLoopLoopBegin(MainLoopLoopScheduler));
flowScheduler.add(MainLoopLoopScheduler);
flowScheduler.add(MainLoopLoopEnd);



















































flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'Estimulos.csv', 'path': 'Estimulos.csv'},
    {'name': 'Incrementos.xlsx', 'path': 'Incrementos.xlsx'},
    {'name': 'incremento_loop2.xlsx', 'path': 'incremento_loop2.xlsx'},
    {'name': 'incremento_loop3.xlsx', 'path': 'incremento_loop3.xlsx'},
    {'name': 'Incrementos_loop_4.xlsx', 'path': 'Incrementos_loop_4.xlsx'},
    {'name': 'Incrementos.xlsx', 'path': 'Incrementos.xlsx'},
    {'name': 'incremento_loop2.xlsx', 'path': 'incremento_loop2.xlsx'},
    {'name': 'incremento_loop3.xlsx', 'path': 'incremento_loop3.xlsx'},
    {'name': 'Incrementos_loop_4.xlsx', 'path': 'Incrementos_loop_4.xlsx'},
    {'name': 'Incrementos.xlsx', 'path': 'Incrementos.xlsx'},
    {'name': 'incremento_loop2.xlsx', 'path': 'incremento_loop2.xlsx'},
    {'name': 'incremento_loop3.xlsx', 'path': 'incremento_loop3.xlsx'},
    {'name': 'Incrementos_loop_4.xlsx', 'path': 'Incrementos_loop_4.xlsx'},
    {'name': 'gaborVert.png', 'path': 'gaborVert.png'},
    {'name': 'gaborHoriz.png', 'path': 'gaborHoriz.png'},
    {'name': 'controle.jpeg', 'path': 'controle.jpeg'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);

async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = '\t';


  return Scheduler.Event.NEXT;
}

async function experimentInit() {
  // Initialize components for Routine "salvar"
  salvarClock = new util.Clock();
  // Initialize components for Routine "codigo"
  codigoClock = new util.Clock();
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image', units : 'cm', 
    image : 'gaborVert.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : 0.0 
  });
  image_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_2', units : 'cm', 
    image : 'gaborVert.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  polygon = new visual.Polygon({
    win: psychoJS.window, name: 'polygon', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    fillColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "trial_2"
  trial_2Clock = new util.Clock();
  image_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_3', units : 'cm', 
    image : 'gaborVert.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : 0.0 
  });
  image_4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_4', units : 'cm', 
    image : 'gaborVert.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  polygon_2 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_2', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    fillColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  key_resp_3 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "trial_3"
  trial_3Clock = new util.Clock();
  image_5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_5', units : 'cm', 
    image : 'gaborHoriz.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : 0.0 
  });
  image_6 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_6', units : 'cm', 
    image : 'gaborHoriz.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : true,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  polygon_3 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_3', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    fillColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  key_resp_4 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_3',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "trial_4"
  trial_4Clock = new util.Clock();
  image_7 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_7', units : 'cm', 
    image : 'gaborHoriz.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : 0.0 
  });
  image_8 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_8', units : 'cm', 
    image : 'gaborHoriz.png', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  polygon_4 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_4', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    fillColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  key_resp_5 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_4',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "trial_5"
  trial_5Clock = new util.Clock();
  image_9 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_9', units : 'cm', 
    image : 'controle.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : 0.0 
  });
  polygon_6 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_6', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    fillColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -1, 
    interpolate: true, 
  });
  
  image_10 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_10', units : 'cm', 
    image : 'controle.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : true,
    texRes : 128.0, interpolate : false, depth : -2.0 
  });
  key_resp_6 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_5',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "trial_6"
  trial_6Clock = new util.Clock();
  image_11 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_11', units : 'cm', 
    image : 'controle.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : 0.0 
  });
  image_12 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'image_12', units : 'cm', 
    image : 'controle.jpeg', mask : undefined,
    anchor : 'center',
    ori : 0.0, 
    pos : [0, 0], 
    draggable: false,
    size : [2, 2],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : false, depth : -1.0 
  });
  polygon_7 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_7', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    fillColor: new util.Color([(- 1.0), 1.0, (- 0.0039)]), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  key_resp_7 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  text_6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_6',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  // Initialize components for Routine "_intertrial_interval_"
  _intertrial_interval_Clock = new util.Clock();
  polygon_5 = new visual.Polygon({
    win: psychoJS.window, name: 'polygon_5', 
    edges: 100, size:[0.005, 0.005],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('red'), 
    fillColor: new util.Color('red'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

function salvarRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'salvar' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    salvarClock.reset();
    routineTimer.reset();
    salvarMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('salvar.started', globalClock.getTime());
    salvarMaxDuration = null
    // keep track of which components have finished
    salvarComponents = [];
    
    salvarComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function salvarRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'salvar' ---
    // get current time
    t = salvarClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code_2
    console.log(key_resp_2.keys);
    console.log(key_resp_3.keys);
    console.log(key_resp_4.keys);
    console.log(key_resp_5.keys);
    console.log(key_resp_6.keys);
    console.log(key_resp_7.keys);
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    salvarComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function salvarRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'salvar' ---
    salvarComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('salvar.stopped', globalClock.getTime());
    // the Routine "salvar" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function MainLoopLoopBegin(MainLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    MainLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 8, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Estimulos.csv',
      seed: undefined, name: 'MainLoop'
    });
    psychoJS.experiment.addLoop(MainLoop); // add the loop to the experiment
    currentLoop = MainLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    MainLoop.forEach(function() {
      snapshot = MainLoop.getSnapshot();
    
      MainLoopLoopScheduler.add(importConditions(snapshot));
      MainLoopLoopScheduler.add(codigoRoutineBegin(snapshot));
      MainLoopLoopScheduler.add(codigoRoutineEachFrame());
      MainLoopLoopScheduler.add(codigoRoutineEnd(snapshot));
      const loop_1LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_1LoopBegin(loop_1LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_1LoopScheduler);
      MainLoopLoopScheduler.add(loop_1LoopEnd);
      const loop_2LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_2LoopBegin(loop_2LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_2LoopScheduler);
      MainLoopLoopScheduler.add(loop_2LoopEnd);
      const loop_3LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_3LoopBegin(loop_3LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_3LoopScheduler);
      MainLoopLoopScheduler.add(loop_3LoopEnd);
      const loop_4LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_4LoopBegin(loop_4LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_4LoopScheduler);
      MainLoopLoopScheduler.add(loop_4LoopEnd);
      const loop_5LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_5LoopBegin(loop_5LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_5LoopScheduler);
      MainLoopLoopScheduler.add(loop_5LoopEnd);
      const loop_6LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_6LoopBegin(loop_6LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_6LoopScheduler);
      MainLoopLoopScheduler.add(loop_6LoopEnd);
      const loop_7LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_7LoopBegin(loop_7LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_7LoopScheduler);
      MainLoopLoopScheduler.add(loop_7LoopEnd);
      const loop_8LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_8LoopBegin(loop_8LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_8LoopScheduler);
      MainLoopLoopScheduler.add(loop_8LoopEnd);
      const loop_9LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_9LoopBegin(loop_9LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_9LoopScheduler);
      MainLoopLoopScheduler.add(loop_9LoopEnd);
      const loop_10LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_10LoopBegin(loop_10LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_10LoopScheduler);
      MainLoopLoopScheduler.add(loop_10LoopEnd);
      const loop_11LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_11LoopBegin(loop_11LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_11LoopScheduler);
      MainLoopLoopScheduler.add(loop_11LoopEnd);
      const loop_12LoopScheduler = new Scheduler(psychoJS);
      MainLoopLoopScheduler.add(loop_12LoopBegin(loop_12LoopScheduler, snapshot));
      MainLoopLoopScheduler.add(loop_12LoopScheduler);
      MainLoopLoopScheduler.add(loop_12LoopEnd);
      MainLoopLoopScheduler.add(_intertrial_interval_RoutineBegin(snapshot));
      MainLoopLoopScheduler.add(_intertrial_interval_RoutineEachFrame());
      MainLoopLoopScheduler.add(_intertrial_interval_RoutineEnd(snapshot));
      MainLoopLoopScheduler.add(MainLoopLoopEndIteration(MainLoopLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

function loop_1LoopBegin(loop_1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep1, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Incrementos.xlsx',
      seed: undefined, name: 'loop_1'
    });
    psychoJS.experiment.addLoop(loop_1); // add the loop to the experiment
    currentLoop = loop_1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_1.forEach(function() {
      snapshot = loop_1.getSnapshot();
    
      loop_1LoopScheduler.add(importConditions(snapshot));
      loop_1LoopScheduler.add(trialRoutineBegin(snapshot));
      loop_1LoopScheduler.add(trialRoutineEachFrame());
      loop_1LoopScheduler.add(trialRoutineEnd(snapshot));
      loop_1LoopScheduler.add(trial_2RoutineBegin(snapshot));
      loop_1LoopScheduler.add(trial_2RoutineEachFrame());
      loop_1LoopScheduler.add(trial_2RoutineEnd(snapshot));
      loop_1LoopScheduler.add(loop_1LoopEndIteration(loop_1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_2LoopBegin(loop_2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep2, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'incremento_loop2.xlsx',
      seed: undefined, name: 'loop_2'
    });
    psychoJS.experiment.addLoop(loop_2); // add the loop to the experiment
    currentLoop = loop_2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_2.forEach(function() {
      snapshot = loop_2.getSnapshot();
    
      loop_2LoopScheduler.add(importConditions(snapshot));
      loop_2LoopScheduler.add(trialRoutineBegin(snapshot));
      loop_2LoopScheduler.add(trialRoutineEachFrame());
      loop_2LoopScheduler.add(trialRoutineEnd(snapshot));
      loop_2LoopScheduler.add(trial_2RoutineBegin(snapshot));
      loop_2LoopScheduler.add(trial_2RoutineEachFrame());
      loop_2LoopScheduler.add(trial_2RoutineEnd(snapshot));
      loop_2LoopScheduler.add(loop_2LoopEndIteration(loop_2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_3LoopBegin(loop_3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep3, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'incremento_loop3.xlsx',
      seed: undefined, name: 'loop_3'
    });
    psychoJS.experiment.addLoop(loop_3); // add the loop to the experiment
    currentLoop = loop_3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_3.forEach(function() {
      snapshot = loop_3.getSnapshot();
    
      loop_3LoopScheduler.add(importConditions(snapshot));
      loop_3LoopScheduler.add(trialRoutineBegin(snapshot));
      loop_3LoopScheduler.add(trialRoutineEachFrame());
      loop_3LoopScheduler.add(trialRoutineEnd(snapshot));
      loop_3LoopScheduler.add(trial_2RoutineBegin(snapshot));
      loop_3LoopScheduler.add(trial_2RoutineEachFrame());
      loop_3LoopScheduler.add(trial_2RoutineEnd(snapshot));
      loop_3LoopScheduler.add(loop_3LoopEndIteration(loop_3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_4LoopBegin(loop_4LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_4 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep4, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Incrementos_loop_4.xlsx',
      seed: undefined, name: 'loop_4'
    });
    psychoJS.experiment.addLoop(loop_4); // add the loop to the experiment
    currentLoop = loop_4;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_4.forEach(function() {
      snapshot = loop_4.getSnapshot();
    
      loop_4LoopScheduler.add(importConditions(snapshot));
      loop_4LoopScheduler.add(trialRoutineBegin(snapshot));
      loop_4LoopScheduler.add(trialRoutineEachFrame());
      loop_4LoopScheduler.add(trialRoutineEnd(snapshot));
      loop_4LoopScheduler.add(trial_2RoutineBegin(snapshot));
      loop_4LoopScheduler.add(trial_2RoutineEachFrame());
      loop_4LoopScheduler.add(trial_2RoutineEnd(snapshot));
      loop_4LoopScheduler.add(loop_4LoopEndIteration(loop_4LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_4LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_4);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_4LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_5LoopBegin(loop_5LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_5 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep5, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Incrementos.xlsx',
      seed: undefined, name: 'loop_5'
    });
    psychoJS.experiment.addLoop(loop_5); // add the loop to the experiment
    currentLoop = loop_5;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_5.forEach(function() {
      snapshot = loop_5.getSnapshot();
    
      loop_5LoopScheduler.add(importConditions(snapshot));
      loop_5LoopScheduler.add(trial_3RoutineBegin(snapshot));
      loop_5LoopScheduler.add(trial_3RoutineEachFrame());
      loop_5LoopScheduler.add(trial_3RoutineEnd(snapshot));
      loop_5LoopScheduler.add(trial_4RoutineBegin(snapshot));
      loop_5LoopScheduler.add(trial_4RoutineEachFrame());
      loop_5LoopScheduler.add(trial_4RoutineEnd(snapshot));
      loop_5LoopScheduler.add(loop_5LoopEndIteration(loop_5LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_5LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_5);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_5LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_6LoopBegin(loop_6LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_6 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep6, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'incremento_loop2.xlsx',
      seed: undefined, name: 'loop_6'
    });
    psychoJS.experiment.addLoop(loop_6); // add the loop to the experiment
    currentLoop = loop_6;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_6.forEach(function() {
      snapshot = loop_6.getSnapshot();
    
      loop_6LoopScheduler.add(importConditions(snapshot));
      loop_6LoopScheduler.add(trial_3RoutineBegin(snapshot));
      loop_6LoopScheduler.add(trial_3RoutineEachFrame());
      loop_6LoopScheduler.add(trial_3RoutineEnd(snapshot));
      loop_6LoopScheduler.add(trial_4RoutineBegin(snapshot));
      loop_6LoopScheduler.add(trial_4RoutineEachFrame());
      loop_6LoopScheduler.add(trial_4RoutineEnd(snapshot));
      loop_6LoopScheduler.add(loop_6LoopEndIteration(loop_6LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_6LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_6);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_6LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_7LoopBegin(loop_7LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_7 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep7, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'incremento_loop3.xlsx',
      seed: undefined, name: 'loop_7'
    });
    psychoJS.experiment.addLoop(loop_7); // add the loop to the experiment
    currentLoop = loop_7;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_7.forEach(function() {
      snapshot = loop_7.getSnapshot();
    
      loop_7LoopScheduler.add(importConditions(snapshot));
      loop_7LoopScheduler.add(trial_3RoutineBegin(snapshot));
      loop_7LoopScheduler.add(trial_3RoutineEachFrame());
      loop_7LoopScheduler.add(trial_3RoutineEnd(snapshot));
      loop_7LoopScheduler.add(trial_4RoutineBegin(snapshot));
      loop_7LoopScheduler.add(trial_4RoutineEachFrame());
      loop_7LoopScheduler.add(trial_4RoutineEnd(snapshot));
      loop_7LoopScheduler.add(loop_7LoopEndIteration(loop_7LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_7LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_7);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_7LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_8LoopBegin(loop_8LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_8 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep8, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Incrementos_loop_4.xlsx',
      seed: undefined, name: 'loop_8'
    });
    psychoJS.experiment.addLoop(loop_8); // add the loop to the experiment
    currentLoop = loop_8;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_8.forEach(function() {
      snapshot = loop_8.getSnapshot();
    
      loop_8LoopScheduler.add(importConditions(snapshot));
      loop_8LoopScheduler.add(trial_3RoutineBegin(snapshot));
      loop_8LoopScheduler.add(trial_3RoutineEachFrame());
      loop_8LoopScheduler.add(trial_3RoutineEnd(snapshot));
      loop_8LoopScheduler.add(trial_4RoutineBegin(snapshot));
      loop_8LoopScheduler.add(trial_4RoutineEachFrame());
      loop_8LoopScheduler.add(trial_4RoutineEnd(snapshot));
      loop_8LoopScheduler.add(loop_8LoopEndIteration(loop_8LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_8LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_8);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_8LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_9LoopBegin(loop_9LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_9 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep9, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Incrementos.xlsx',
      seed: undefined, name: 'loop_9'
    });
    psychoJS.experiment.addLoop(loop_9); // add the loop to the experiment
    currentLoop = loop_9;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_9.forEach(function() {
      snapshot = loop_9.getSnapshot();
    
      loop_9LoopScheduler.add(importConditions(snapshot));
      loop_9LoopScheduler.add(trial_5RoutineBegin(snapshot));
      loop_9LoopScheduler.add(trial_5RoutineEachFrame());
      loop_9LoopScheduler.add(trial_5RoutineEnd(snapshot));
      loop_9LoopScheduler.add(trial_6RoutineBegin(snapshot));
      loop_9LoopScheduler.add(trial_6RoutineEachFrame());
      loop_9LoopScheduler.add(trial_6RoutineEnd(snapshot));
      loop_9LoopScheduler.add(loop_9LoopEndIteration(loop_9LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_9LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_9);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_9LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_10LoopBegin(loop_10LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_10 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep10, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'incremento_loop2.xlsx',
      seed: undefined, name: 'loop_10'
    });
    psychoJS.experiment.addLoop(loop_10); // add the loop to the experiment
    currentLoop = loop_10;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_10.forEach(function() {
      snapshot = loop_10.getSnapshot();
    
      loop_10LoopScheduler.add(importConditions(snapshot));
      loop_10LoopScheduler.add(trial_5RoutineBegin(snapshot));
      loop_10LoopScheduler.add(trial_5RoutineEachFrame());
      loop_10LoopScheduler.add(trial_5RoutineEnd(snapshot));
      loop_10LoopScheduler.add(trial_6RoutineBegin(snapshot));
      loop_10LoopScheduler.add(trial_6RoutineEachFrame());
      loop_10LoopScheduler.add(trial_6RoutineEnd(snapshot));
      loop_10LoopScheduler.add(loop_10LoopEndIteration(loop_10LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_10LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_10);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_10LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_11LoopBegin(loop_11LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_11 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep11, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'incremento_loop3.xlsx',
      seed: undefined, name: 'loop_11'
    });
    psychoJS.experiment.addLoop(loop_11); // add the loop to the experiment
    currentLoop = loop_11;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_11.forEach(function() {
      snapshot = loop_11.getSnapshot();
    
      loop_11LoopScheduler.add(importConditions(snapshot));
      loop_11LoopScheduler.add(trial_5RoutineBegin(snapshot));
      loop_11LoopScheduler.add(trial_5RoutineEachFrame());
      loop_11LoopScheduler.add(trial_5RoutineEnd(snapshot));
      loop_11LoopScheduler.add(trial_6RoutineBegin(snapshot));
      loop_11LoopScheduler.add(trial_6RoutineEachFrame());
      loop_11LoopScheduler.add(trial_6RoutineEnd(snapshot));
      loop_11LoopScheduler.add(loop_11LoopEndIteration(loop_11LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_11LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_11);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_11LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function loop_12LoopBegin(loop_12LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    loop_12 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: rep12, method: TrialHandler.Method.SEQUENTIAL,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'Incrementos_loop_4.xlsx',
      seed: undefined, name: 'loop_12'
    });
    psychoJS.experiment.addLoop(loop_12); // add the loop to the experiment
    currentLoop = loop_12;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    loop_12.forEach(function() {
      snapshot = loop_12.getSnapshot();
    
      loop_12LoopScheduler.add(importConditions(snapshot));
      loop_12LoopScheduler.add(trial_5RoutineBegin(snapshot));
      loop_12LoopScheduler.add(trial_5RoutineEachFrame());
      loop_12LoopScheduler.add(trial_5RoutineEnd(snapshot));
      loop_12LoopScheduler.add(trial_6RoutineBegin(snapshot));
      loop_12LoopScheduler.add(trial_6RoutineEachFrame());
      loop_12LoopScheduler.add(trial_6RoutineEnd(snapshot));
      loop_12LoopScheduler.add(loop_12LoopEndIteration(loop_12LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}

async function loop_12LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(loop_12);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function loop_12LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

async function MainLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(MainLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}

function MainLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}

function codigoRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'codigo' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    codigoClock.reset();
    routineTimer.reset();
    codigoMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('codigo.started', globalClock.getTime());
    codigoMaxDuration = null
    // keep track of which components have finished
    codigoComponents = [];
    
    codigoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function codigoRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'codigo' ---
    // get current time
    t = codigoClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from code
    /* Syntax Error: Fix Python code */
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    codigoComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function codigoRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'codigo' ---
    codigoComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('codigo.stopped', globalClock.getTime());
    // the Routine "codigo" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trialClock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    trialMaxDurationReached = false;
    // update component parameters for each repeat
    image.setPos([px1, py1]);
    image_2.setPos([px2, py2]);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    psychoJS.experiment.addData('trial.started', globalClock.getTime());
    trialMaxDuration = null
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(image);
    trialComponents.push(image_2);
    trialComponents.push(polygon);
    trialComponents.push(key_resp_2);
    trialComponents.push(text);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial' ---
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image* updates
    if (t >= 0.0 && image.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image.tStart = t;  // (not accounting for frame time here)
      image.frameNStart = frameN;  // exact frame index
      
      image.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image.setAutoDraw(false);
    }
    
    
    // *image_2* updates
    if (t >= 0.0 && image_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_2.tStart = t;  // (not accounting for frame time here)
      image_2.frameNStart = frameN;  // exact frame index
      
      image_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_2.setAutoDraw(false);
    }
    
    
    // *polygon* updates
    if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon.tStart = t;  // (not accounting for frame time here)
      polygon.frameNStart = frameN;  // exact frame index
      
      polygon.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon.setAutoDraw(false);
    }
    
    
    // *key_resp_2* updates
    if (t >= 0.0 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_2.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: [], waitRelease: true});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys.map((key) => key.name);  // storing all keys
        key_resp_2.rt = _key_resp_2_allKeys.map((key) => key.rt);
        key_resp_2.duration = _key_resp_2_allKeys.map((key) => key.duration);
      }
    }
    
    
    if (text.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text.setText(key_resp_2.keys, false);
    }
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_3
    import * as time from 'time';
    if (key_resp_2.keys) {
        dados.concat(zip(key_resp_2.keys, ([globalClock.getTime()] * key_resp_2.keys.length)));
        time.sleep(0.3);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial' ---
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_2.corr, level);
    }
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        psychoJS.experiment.addData('key_resp_2.duration', key_resp_2.duration);
        }
    
    key_resp_2.stop();
    if (trialMaxDurationReached) {
        trialClock.add(trialMaxDuration);
    } else {
        trialClock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trial_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_2' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trial_2Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    trial_2MaxDurationReached = false;
    // update component parameters for each repeat
    image_3.setPos([px3, py3]);
    image_4.setPos([px4, py4]);
    key_resp_3.keys = undefined;
    key_resp_3.rt = undefined;
    _key_resp_3_allKeys = [];
    psychoJS.experiment.addData('trial_2.started', globalClock.getTime());
    trial_2MaxDuration = null
    // keep track of which components have finished
    trial_2Components = [];
    trial_2Components.push(image_3);
    trial_2Components.push(image_4);
    trial_2Components.push(polygon_2);
    trial_2Components.push(key_resp_3);
    trial_2Components.push(text_2);
    
    trial_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trial_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_2' ---
    // get current time
    t = trial_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_3* updates
    if (t >= 0.0 && image_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_3.tStart = t;  // (not accounting for frame time here)
      image_3.frameNStart = frameN;  // exact frame index
      
      image_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_3.setAutoDraw(false);
    }
    
    
    // *image_4* updates
    if (t >= 0.0 && image_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_4.tStart = t;  // (not accounting for frame time here)
      image_4.frameNStart = frameN;  // exact frame index
      
      image_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_4.setAutoDraw(false);
    }
    
    
    // *polygon_2* updates
    if (t >= 0.0 && polygon_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_2.tStart = t;  // (not accounting for frame time here)
      polygon_2.frameNStart = frameN;  // exact frame index
      
      polygon_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_2.setAutoDraw(false);
    }
    
    
    // *key_resp_3* updates
    if (t >= 0.0 && key_resp_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_3.tStart = t;  // (not accounting for frame time here)
      key_resp_3.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_3.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_3.start(); }); // start on screen flip
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_3.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_3.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_3.getKeys({keyList: ['up', 'right'], waitRelease: true});
      _key_resp_3_allKeys = _key_resp_3_allKeys.concat(theseKeys);
      if (_key_resp_3_allKeys.length > 0) {
        key_resp_3.keys = _key_resp_3_allKeys.map((key) => key.name);  // storing all keys
        key_resp_3.rt = _key_resp_3_allKeys.map((key) => key.rt);
        key_resp_3.duration = _key_resp_3_allKeys.map((key) => key.duration);
      }
    }
    
    
    if (text_2.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_2.setText(key_resp_3.keys, false);
    }
    
    // *text_2* updates
    if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_2.tStart = t;  // (not accounting for frame time here)
      text_2.frameNStart = frameN;  // exact frame index
      
      text_2.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_2.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_4
    if (key_resp_3.keys) {
        dados.concat(zip(key_resp_3.keys, ([globalClock.getTime()] * key_resp_3.keys.length)));
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trial_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_2' ---
    trial_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_2.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_3.corr, level);
    }
    psychoJS.experiment.addData('key_resp_3.keys', key_resp_3.keys);
    if (typeof key_resp_3.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_3.rt', key_resp_3.rt);
        psychoJS.experiment.addData('key_resp_3.duration', key_resp_3.duration);
        }
    
    key_resp_3.stop();
    if (trial_2MaxDurationReached) {
        trial_2Clock.add(trial_2MaxDuration);
    } else {
        trial_2Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trial_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_3' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trial_3Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    trial_3MaxDurationReached = false;
    // update component parameters for each repeat
    image_5.setPos([px1, py1]);
    image_6.setPos([px2, py2]);
    key_resp_4.keys = undefined;
    key_resp_4.rt = undefined;
    _key_resp_4_allKeys = [];
    psychoJS.experiment.addData('trial_3.started', globalClock.getTime());
    trial_3MaxDuration = 0.3
    // keep track of which components have finished
    trial_3Components = [];
    trial_3Components.push(image_5);
    trial_3Components.push(image_6);
    trial_3Components.push(polygon_3);
    trial_3Components.push(key_resp_4);
    trial_3Components.push(text_3);
    
    trial_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trial_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_3' ---
    // get current time
    t = trial_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > trial_3MaxDuration) {
        trial_3MaxDurationReached = true
        continueRoutine = false
    }
    
    // *image_5* updates
    if (t >= 0.0 && image_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_5.tStart = t;  // (not accounting for frame time here)
      image_5.frameNStart = frameN;  // exact frame index
      
      image_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_5.setAutoDraw(false);
    }
    
    
    // *image_6* updates
    if (t >= 0.0 && image_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_6.tStart = t;  // (not accounting for frame time here)
      image_6.frameNStart = frameN;  // exact frame index
      
      image_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_6.setAutoDraw(false);
    }
    
    
    // *polygon_3* updates
    if (t >= 0.0 && polygon_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_3.tStart = t;  // (not accounting for frame time here)
      polygon_3.frameNStart = frameN;  // exact frame index
      
      polygon_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_3.setAutoDraw(false);
    }
    
    
    // *key_resp_4* updates
    if (t >= 0.0 && key_resp_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_4.tStart = t;  // (not accounting for frame time here)
      key_resp_4.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_4.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_4.start(); }); // start on screen flip
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_4.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_4.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_4.getKeys({keyList: ['up', 'right'], waitRelease: true});
      _key_resp_4_allKeys = _key_resp_4_allKeys.concat(theseKeys);
      if (_key_resp_4_allKeys.length > 0) {
        key_resp_4.keys = _key_resp_4_allKeys.map((key) => key.name);  // storing all keys
        key_resp_4.rt = _key_resp_4_allKeys.map((key) => key.rt);
        key_resp_4.duration = _key_resp_4_allKeys.map((key) => key.duration);
      }
    }
    
    
    if (text_3.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_3.setText(key_resp_4.keys, false);
    }
    
    // *text_3* updates
    if (t >= 0.0 && text_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_3.tStart = t;  // (not accounting for frame time here)
      text_3.frameNStart = frameN;  // exact frame index
      
      text_3.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_3.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_5
    if (key_resp_4.keys) {
        dados.concat(zip(key_resp_4.keys, ([globalClock.getTime()] * key_resp_4.keys.length)));
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trial_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_3' ---
    trial_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_3.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_4.corr, level);
    }
    psychoJS.experiment.addData('key_resp_4.keys', key_resp_4.keys);
    if (typeof key_resp_4.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_4.rt', key_resp_4.rt);
        psychoJS.experiment.addData('key_resp_4.duration', key_resp_4.duration);
        }
    
    key_resp_4.stop();
    if (trial_3MaxDurationReached) {
        trial_3Clock.add(trial_3MaxDuration);
    } else {
        trial_3Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trial_4RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_4' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trial_4Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    trial_4MaxDurationReached = false;
    // update component parameters for each repeat
    image_7.setPos([px3, py3]);
    image_8.setPos([px4, py4]);
    key_resp_5.keys = undefined;
    key_resp_5.rt = undefined;
    _key_resp_5_allKeys = [];
    psychoJS.experiment.addData('trial_4.started', globalClock.getTime());
    trial_4MaxDuration = 0.3
    // keep track of which components have finished
    trial_4Components = [];
    trial_4Components.push(image_7);
    trial_4Components.push(image_8);
    trial_4Components.push(polygon_4);
    trial_4Components.push(key_resp_5);
    trial_4Components.push(text_4);
    
    trial_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trial_4RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_4' ---
    // get current time
    t = trial_4Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // is it time to end the Routine? (based on local clock)
    if (t > trial_4MaxDuration) {
        trial_4MaxDurationReached = true
        continueRoutine = false
    }
    
    // *image_7* updates
    if (t >= 0.0 && image_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_7.tStart = t;  // (not accounting for frame time here)
      image_7.frameNStart = frameN;  // exact frame index
      
      image_7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_7.setAutoDraw(false);
    }
    
    
    // *image_8* updates
    if (t >= 0.0 && image_8.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_8.tStart = t;  // (not accounting for frame time here)
      image_8.frameNStart = frameN;  // exact frame index
      
      image_8.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_8.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_8.setAutoDraw(false);
    }
    
    
    // *polygon_4* updates
    if (t >= 0.0 && polygon_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_4.tStart = t;  // (not accounting for frame time here)
      polygon_4.frameNStart = frameN;  // exact frame index
      
      polygon_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_4.setAutoDraw(false);
    }
    
    
    // *key_resp_5* updates
    if (t >= 0.0 && key_resp_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_5.tStart = t;  // (not accounting for frame time here)
      key_resp_5.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_5.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_5.start(); }); // start on screen flip
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_5.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_5.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_5.getKeys({keyList: ['up', 'right'], waitRelease: true});
      _key_resp_5_allKeys = _key_resp_5_allKeys.concat(theseKeys);
      if (_key_resp_5_allKeys.length > 0) {
        key_resp_5.keys = _key_resp_5_allKeys.map((key) => key.name);  // storing all keys
        key_resp_5.rt = _key_resp_5_allKeys.map((key) => key.rt);
        key_resp_5.duration = _key_resp_5_allKeys.map((key) => key.duration);
      }
    }
    
    
    if (text_4.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_4.setText(key_resp_5.keys, false);
    }
    
    // *text_4* updates
    if (t >= 0.0 && text_4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_4.tStart = t;  // (not accounting for frame time here)
      text_4.frameNStart = frameN;  // exact frame index
      
      text_4.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_4.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_6
    if (key_resp_5.keys) {
        dados.concat(zip(key_resp_5.keys, ([globalClock.getTime()] * key_resp_5.keys.length)));
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_4Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trial_4RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_4' ---
    trial_4Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_4.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_5.corr, level);
    }
    psychoJS.experiment.addData('key_resp_5.keys', key_resp_5.keys);
    if (typeof key_resp_5.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_5.rt', key_resp_5.rt);
        psychoJS.experiment.addData('key_resp_5.duration', key_resp_5.duration);
        }
    
    key_resp_5.stop();
    if (trial_4MaxDurationReached) {
        trial_4Clock.add(trial_4MaxDuration);
    } else {
        trial_4Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trial_5RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_5' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trial_5Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    trial_5MaxDurationReached = false;
    // update component parameters for each repeat
    image_9.setPos([px1, py1]);
    image_10.setPos([px2, py2]);
    key_resp_6.keys = undefined;
    key_resp_6.rt = undefined;
    _key_resp_6_allKeys = [];
    psychoJS.experiment.addData('trial_5.started', globalClock.getTime());
    trial_5MaxDuration = null
    // keep track of which components have finished
    trial_5Components = [];
    trial_5Components.push(image_9);
    trial_5Components.push(polygon_6);
    trial_5Components.push(image_10);
    trial_5Components.push(key_resp_6);
    trial_5Components.push(text_5);
    
    trial_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trial_5RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_5' ---
    // get current time
    t = trial_5Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_9* updates
    if (t >= 0.0 && image_9.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_9.tStart = t;  // (not accounting for frame time here)
      image_9.frameNStart = frameN;  // exact frame index
      
      image_9.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_9.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_9.setAutoDraw(false);
    }
    
    
    // *polygon_6* updates
    if (t >= 0.0 && polygon_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_6.tStart = t;  // (not accounting for frame time here)
      polygon_6.frameNStart = frameN;  // exact frame index
      
      polygon_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_6.setAutoDraw(false);
    }
    
    
    // *image_10* updates
    if (t >= 0.0 && image_10.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_10.tStart = t;  // (not accounting for frame time here)
      image_10.frameNStart = frameN;  // exact frame index
      
      image_10.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_10.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_10.setAutoDraw(false);
    }
    
    
    // *key_resp_6* updates
    if (t >= 0.0 && key_resp_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_6.tStart = t;  // (not accounting for frame time here)
      key_resp_6.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_6.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_6.start(); }); // start on screen flip
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_6.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_6.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_6.getKeys({keyList: ['up', 'right'], waitRelease: true});
      _key_resp_6_allKeys = _key_resp_6_allKeys.concat(theseKeys);
      if (_key_resp_6_allKeys.length > 0) {
        key_resp_6.keys = _key_resp_6_allKeys.map((key) => key.name);  // storing all keys
        key_resp_6.rt = _key_resp_6_allKeys.map((key) => key.rt);
        key_resp_6.duration = _key_resp_6_allKeys.map((key) => key.duration);
      }
    }
    
    
    if (text_5.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_5.setText(key_resp_6.keys, false);
    }
    
    // *text_5* updates
    if (t >= 0.0 && text_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_5.tStart = t;  // (not accounting for frame time here)
      text_5.frameNStart = frameN;  // exact frame index
      
      text_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_5.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_7
    if (key_resp_6.keys) {
        dados.concat(zip(key_resp_6.keys, ([globalClock.getTime()] * key_resp_6.keys.length)));
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_5Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trial_5RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_5' ---
    trial_5Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_5.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_6.corr, level);
    }
    psychoJS.experiment.addData('key_resp_6.keys', key_resp_6.keys);
    if (typeof key_resp_6.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_6.rt', key_resp_6.rt);
        psychoJS.experiment.addData('key_resp_6.duration', key_resp_6.duration);
        }
    
    key_resp_6.stop();
    if (trial_5MaxDurationReached) {
        trial_5Clock.add(trial_5MaxDuration);
    } else {
        trial_5Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function trial_6RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'trial_6' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    trial_6Clock.reset(routineTimer.getTime());
    routineTimer.add(0.300000);
    trial_6MaxDurationReached = false;
    // update component parameters for each repeat
    image_11.setPos([px3, py3]);
    image_12.setPos([px4, py4]);
    key_resp_7.keys = undefined;
    key_resp_7.rt = undefined;
    _key_resp_7_allKeys = [];
    psychoJS.experiment.addData('trial_6.started', globalClock.getTime());
    trial_6MaxDuration = null
    // keep track of which components have finished
    trial_6Components = [];
    trial_6Components.push(image_11);
    trial_6Components.push(image_12);
    trial_6Components.push(polygon_7);
    trial_6Components.push(key_resp_7);
    trial_6Components.push(text_6);
    
    trial_6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function trial_6RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'trial_6' ---
    // get current time
    t = trial_6Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *image_11* updates
    if (t >= 0.0 && image_11.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_11.tStart = t;  // (not accounting for frame time here)
      image_11.frameNStart = frameN;  // exact frame index
      
      image_11.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_11.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_11.setAutoDraw(false);
    }
    
    
    // *image_12* updates
    if (t >= 0.0 && image_12.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      image_12.tStart = t;  // (not accounting for frame time here)
      image_12.frameNStart = frameN;  // exact frame index
      
      image_12.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (image_12.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      image_12.setAutoDraw(false);
    }
    
    
    // *polygon_7* updates
    if (t >= 0.0 && polygon_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_7.tStart = t;  // (not accounting for frame time here)
      polygon_7.frameNStart = frameN;  // exact frame index
      
      polygon_7.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_7.setAutoDraw(false);
    }
    
    
    // *key_resp_7* updates
    if (t >= 0.0 && key_resp_7.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_7.tStart = t;  // (not accounting for frame time here)
      key_resp_7.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_7.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_7.start(); }); // start on screen flip
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (key_resp_7.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp_7.status = PsychoJS.Status.FINISHED;
        }
      
    if (key_resp_7.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_7.getKeys({keyList: ['up', 'right'], waitRelease: true});
      _key_resp_7_allKeys = _key_resp_7_allKeys.concat(theseKeys);
      if (_key_resp_7_allKeys.length > 0) {
        key_resp_7.keys = _key_resp_7_allKeys.map((key) => key.name);  // storing all keys
        key_resp_7.rt = _key_resp_7_allKeys.map((key) => key.rt);
        key_resp_7.duration = _key_resp_7_allKeys.map((key) => key.duration);
      }
    }
    
    
    if (text_6.status === PsychoJS.Status.STARTED){ // only update if being drawn
      text_6.setText(key_resp_7.keys, false);
    }
    
    // *text_6* updates
    if (t >= 0.0 && text_6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text_6.tStart = t;  // (not accounting for frame time here)
      text_6.frameNStart = frameN;  // exact frame index
      
      text_6.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.3 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text_6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text_6.setAutoDraw(false);
    }
    
    // Run 'Each Frame' code from code_8
    if (key_resp_7.keys) {
        dados.concat(zip(key_resp_7.keys, ([globalClock.getTime()] * key_resp_7.keys.length)));
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trial_6Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function trial_6RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'trial_6' ---
    trial_6Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('trial_6.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp_7.corr, level);
    }
    psychoJS.experiment.addData('key_resp_7.keys', key_resp_7.keys);
    if (typeof key_resp_7.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_7.rt', key_resp_7.rt);
        psychoJS.experiment.addData('key_resp_7.duration', key_resp_7.duration);
        }
    
    key_resp_7.stop();
    if (trial_6MaxDurationReached) {
        trial_6Clock.add(trial_6MaxDuration);
    } else {
        trial_6Clock.add(0.300000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function _intertrial_interval_RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine '_intertrial_interval_' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    _intertrial_interval_Clock.reset(routineTimer.getTime());
    routineTimer.add(1.500000);
    _intertrial_interval_MaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('_intertrial_interval_.started', globalClock.getTime());
    _intertrial_interval_MaxDuration = null
    // keep track of which components have finished
    _intertrial_interval_Components = [];
    _intertrial_interval_Components.push(polygon_5);
    
    _intertrial_interval_Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}

function _intertrial_interval_RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine '_intertrial_interval_' ---
    // get current time
    t = _intertrial_interval_Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *polygon_5* updates
    if (t >= 0.0 && polygon_5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      polygon_5.tStart = t;  // (not accounting for frame time here)
      polygon_5.frameNStart = frameN;  // exact frame index
      
      polygon_5.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (polygon_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      polygon_5.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    _intertrial_interval_Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}

function _intertrial_interval_RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine '_intertrial_interval_' ---
    _intertrial_interval_Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('_intertrial_interval_.stopped', globalClock.getTime());
    if (_intertrial_interval_MaxDurationReached) {
        _intertrial_interval_Clock.add(_intertrial_interval_MaxDuration);
    } else {
        _intertrial_interval_Clock.add(1.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}

function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}

async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}

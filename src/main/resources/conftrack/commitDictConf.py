if context.getDeployedApplication() is None:
  app = context.getPreviousDeployedApplication()
else:
   app = context.getDeployedApplication()
if app.getEnvironment().TrackEnv:
              context.addStep(steps.jython(
                 description = "Commit dictionary to SVN",
                 order = 99,
                 script = "conftrack/retrieveAndCommitDictionary.py",
                 jython_context = {"env" : app.getEnvironment(),
                                   "dicts" : app.getEnvironment().getDictionaries()
                                   }
             ))



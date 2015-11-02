
def getHosts():
    print "======================================================================================="
    print "START: getHosts"
    # Get our deployed containers
    depHosts=[]
    for delta in deltas.deltas:
        delta_op = str(delta.operation)
        deployed = delta.previous if delta_op == "DESTROY" else delta.deployed
        container = deployed.container
        host = container.host
        depHosts.append(host)
    print "END  : getHosts"
    print "======================================================================================="
    return depHosts
# End def

def update_hosts(hosts, context):
    print "START: update_hosts1"
    print hosts
    if context.getDeployedApplication() is None:
      app = context.getPreviousDeployedApplication()
    else:
       app = context.getDeployedApplication()
    for host in hosts:
            print "Container = %s "  % (host)
            if host.TrackHost:
                      context.addStep(steps.os_script(
                         description = "Commit configuration files from host %s" % host,
                         order = 99,
                         target_host = host,
                         script = "conftrack/commit",
                         freemarker_context = {"env" : app.getEnvironment().getName(),
                                               "version": app.getVersion().getVersion(),
                                               "host": host,
                                               "app": app.getName()
                                              }
                     ))
            # End if
    print "END  : update_hosts1"
# End def

def getLdaps():
    print "======================================================================================="
    print "START: getLdaps"
    # Get our deployed containers
    depLdaps=[]
    for delta in deltas.deltas:
        delta_op = str(delta.operation)
        deployed = delta.previous if delta_op == "DESTROY" else delta.deployed
        container = deployed.container
        if container.TYPE_FIELD == "yotaConfig.Ldap:":
           depLdaps.append(container)
    print "END  : getLdaps"
    print "======================================================================================="
    return depLdaps
# End def

def update_hosts(hosts, context):
    print "START: update_hosts"
    print hosts
    if context.getDeployedApplication() is None:
      app = context.getPreviousDeployedApplication()
    else:
       app = context.getDeployedApplication()
    for host in hosts:
            print "Container = %s "  % (host)
            if host.TrackHost:
                      context.addStep(steps.os_script(
                         description = "Commit configuration files from host %s" % host,
                         order = 99,
                         target_host = host,
                         script = "conftrack/commit",
                         freemarker_context = {"env" : app.getEnvironment().getName(),
                                               "version": app.getVersion().getVersion(),
                                               "host": host,
                                               "app": app.getName()
                                              }
                     ))
            # End if
    print "END  : update_hosts"
# End def

def update_ldaps(containers, context):
    print "START: update_ldaps"
    print containers
    if context.getDeployedApplication() is None:
      app = context.getPreviousDeployedApplication()
    else:
       app = context.getDeployedApplication()
    for container in containers:
        if container.Track:
                      context.addStep(steps.os_script(
                         description = "Commit ldap configuration from host %s" % container.host,
                         order = 99,
                         target_host = container.host,
                         script = "conftrack/commitLdap",
                         freemarker_context = {"env" : app.getEnvironment().getName(),
                                               "version": app.getVersion().getVersion(),
                                               "host": container.host,
                                               "username": container.username,
                                               "password": container.password,
                                               "port": container.port,
                                               "app": app.getName()
                                              }
                     ))

    print "END: update_ldaps" 
# End def


update_hosts( getHosts(), context)
update_ldaps(getLdaps(), context)

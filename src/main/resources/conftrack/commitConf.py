def getDeploymentGroup():
    print "======================================================================================="
    print "START: getDeploymentGroup"
    # Get our deployed containers
    for delta in deltas.deltas:
        delta_op = str(delta.operation)
        deployed = delta.previous if delta_op == "DESTROY" else delta.deployed
        container = deployed.container
        host = container.host
        depGroup = host.deploymentGroup
        print "Deployment group for %s is %s" % (host, depGroup)
    print "depGroup = %s " % depGroup
    print "END  : getDeploymentGroup"
    print "======================================================================================="
    return depGroup
# End def

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


def getContainerListFromDeployedApplication():
    print "START: getContainerListFromDeployedApplication"
    containers = {}
    env = deployedApplication.getEnvironment()
    print "ENV = %s" % env.name
    members = env.getMembers()
    for container in members:
       print "Adding %s" % container.host
       containers[container.host] = container
    # End if
    print "END  : getContainerListFromDeployedApplication"
    return [containers[ke] for ke in containers.keys()]
# End def
    

def update_hosts(containers, context):
    print "START: update_hosts"
    deploymentGroup = getDeploymentGroup()
    print containers
    for container in containers:
            host = container.host
            dGrp = host.getProperty('deploymentGroup')
            print "Container = %s (%s/%s)"  % (host, dGrp, deploymentGroup)
            if dGrp == deploymentGroup and host.TrackHost:
                      context.addStep(steps.os_script(
                         description = "Commit configuration files from host %s" % host,
                         order = 99,
                         target_host = host,
                         script = "conftrack/commit",
                         freemarker_context = {"env" : deployedApplication.getEnvironment().getName(),
                                               "version": deployedApplication.getVersion().getVersion(),
                                               "host": host,
                                               "app": deployedApplication.getName()
                                              }
                     ))
            # End if
    print "END  : update_hosts"
# End def

def update_hosts1(hosts, context):
    print "START: update_hosts1"
    print hosts
    for host in hosts:
            print "Container = %s "  % (host)
            if host.TrackHost:
                      context.addStep(steps.os_script(
                         description = "Commit configuration files from host %s" % host,
                         order = 99,
                         target_host = host,
                         script = "conftrack/commit",
                         freemarker_context = {"env" : deployedApplication.getEnvironment().getName(),
                                               "version": deployedApplication.getVersion().getVersion(),
                                               "host": host,
                                               "app": deployedApplication.getName()
                                              }
                     ))
            # End if
    print "END  : update_hosts1"
# End def

#update_hosts( getContainerListFromDeployedApplication(), context )
update_hosts1( getHosts(), context )

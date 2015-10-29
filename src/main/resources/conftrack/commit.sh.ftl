set -x
cd ${host.WorkingDirectory}/${env}
svn up
mkdir -p ${host.WorkingDirectory}/${env}/${host.getName()}/file
cd ${host.WorkingDirectory}/${env}/
<#list host.filesToTrack as path>
  cp -r --parent ${path} ${host.WorkingDirectory}/${env}/${host.getName()}/file/
</#list>
svn add *
svn commit -m "${app} on ${env} version: ${version}"

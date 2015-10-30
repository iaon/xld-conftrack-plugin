set -x
cd ${host.WorkingDirectory}/${env}
svn up
mkdir -p ${host.WorkingDirectory}/${env}/${host.getName()}/ldap
cd ${host.WorkingDirectory}/${env}/ldap
${openDjPath}/export-ldif --port ${port}  --hostname localhost --bindDN "${username}" --bindPassword "${password}" --ldifFile ./ldap.ldif --trustAll
svn add *
svn commit -m "LDAP ${app} on ${env} version: ${version}"

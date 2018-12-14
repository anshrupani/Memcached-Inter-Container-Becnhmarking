import os
import stat

def prepare_exp(SSHHost, SSHPort, REMOTEROOT, optpt):
    f = open("run-experiment.sh", 'w')
    f.write("#!/bin/bash\n")
    f.write("set -x\n\n")
    
    f.write("ssh -i /home/ubuntu/.ssh/id_rsa ubuntu@server_container -o StrictHostKeyChecking=no \"memcached -P memcached.pid > memcached.out 2> memcached.err &\"\n") # adjust this line to properly start memcached

    f.write("sleep 5\n")

    f.write("RESULT=`ssh  -i /home/ubuntu/.ssh/id_rsa ubuntu@server_container -o StrictHostKeyChecking=no \"pgrep memcached\"`\n")

    f.write("if [[ -z \"${RESULT// }\" ]]; then echo \"memcached process not running\"; CODE=1; else CODE=0; fi\n")
        
    f.write("mcperf -N %d -R %d -n %d -s %s > stats.log 2>&1\n\n" % (optpt["noRequests"]*10 ,optpt["noRequests"], optpt["concurrency"], SSHHost)) #adjust this line to properly start the client

    f.write("REQPERSEC=`cat stats.log | grep 'Response rate' | sed 's/Response rate: //' | awk '{print $1}'`\n")
    f.write("LATENCY=`cat stats.log | grep 'Response time \[ms\]: avg ' | sed 's/Response time \[ms\]: avg //' | awk '{print $1}'`\n")
    
    f.write("ssh  -i /home/ubuntu/.ssh/id_rsa ubuntu@server_container -o StrictHostKeyChecking=no \"sudo kill -9 $RESULT\"\n")

    f.write("echo \"requests latency\" > stats.csv\n")
    f.write("echo \"$REQPERSEC $LATENCY\" >> stats.csv\n")
    
    f.write("scp  -i /home/ubuntu/.ssh/id_rsa ubuntu@server_container -o StrictHostKeyChecking=no:~/memcached.* .\n")

    f.write("if [[ $(wc -l <stats.csv) -le 1 ]]; then CODE=1; fi\n\n")
    
    f.write("exit $CODE\n")

    f.close()

    os.chmod("run-experiment.sh", stat.S_IRWXU) 

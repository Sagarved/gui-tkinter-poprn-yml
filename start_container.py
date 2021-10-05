import subprocess as sp
import time

def step_1():
        # Starting docker and VM services
        response=sp.run("echo 'Charter123'|sudo service docker restart", shell=True)
        wait = True
        while(wait):
             if response:
                wait = response.returncode
                print('Inside wait',wait)
             else:
               print('Waiting 10 secs')
               time.sleep(10)
        time.sleep(65)
        # Tuple not able to perform 'in' operation so, typecasted to string
        dls = str(sp.getstatusoutput(["echo 'Charter123'| sudo docker container ls"]))
        if '3000/tcp' not in dls:
            print('Not all containers have started')
            print(type(dls),dls)
            step_1()
        print('Containers are running properly')
        
def step_1a():
        time.sleep(20)
        vm = sp.Popen("sudo ./install_startup_service_for_vm.sh", shell=True)
        print('VM service')
        vm.wait()
        print("Completed step 1 and 1a")


def step_2():
        all_container = False
        #check container and service
        services = sp.check_output(["echo 'Charter123'|sudo docker service ls"], shell=True)
        #container = sp.run(["echo 'Charter123'| sudo docker container ls"], shell=True)
        #Working solution
        #container = sp.check_output(["echo 'Charter123'| sudo docker container ls"], shell=True)
        container = str(sp.getstatusoutput(["echo 'Charter123'| sudo docker container ls"]))
        return container
        """#GUI Readiness check
        if 'starting' in container:
                 return False
        else:
                 return True #print('Completed step 2')
        """

if __name__=="__main__":
        step_1()
        step_1a()
        i = 0
        while(i < 2):
                time.sleep(10)
                step_2()
                i += 1
        print('Done')

GUI README
Clone GUI repository and add to Home directory.
start_container file start and monitor container and dashboard process
device_api file used for querying api request to find devices connected to dashboard.
center_gui file is main file for rendering gui.

config file comprises of dashboard url and credential for orbiwise portal
Steps:
1a) pip install -r requirement.txt
1b) Update url, and credential in config.yml file
1) start container on boot time.
$ sudo vim ctontab -e
-> Enter start_container script in cronjob 
@reboot python3 /home/wrdlab/GUI/start_container.py  >> /home/wrdlab/GUI/sc.txt
-> Save and close the file
2) Start GUI on user Log In.
-> On centos 7 use 'gnome-session-properties' to edit this in the GUI. Go to terminal and type $gnome-session-properties
-> Add a center_gui script
3) Reboot the system to check system GUI is coming properly.
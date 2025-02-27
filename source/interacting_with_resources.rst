How to interact with lab resources
==================================

.. _using-ssh:

How to SSH into Wallace
-----------------------

The process for ssh'ing into Wallace is very similar between Mac/Windows users.

On Mac
^^^^^^

1. Open up the Terminal application; you can find this by typing <command+space> and searching for Terminal, which should have an icon with ``>_`` in the upper-right corner.
    - Unless you're using WashU wifi (wusm-secure), you'll need to be VPN'ed into WashU's network.
2. To SSH into Wallace for the first time, enter the following command::

    ssh <your-NIL-username>@wallace.neuroimage.wustl.edu -Y

3. You should then be prompted to enter your password. Type it in then press ``<Enter>``.

.. warning::

   There are no characters that will appear as you type in your password, so keep that in mind! If you think you made a typo, simply holding the <Backspace> key until you think all the characters are erased works.

On Windows
^^^^^^^^^^

The same instructions above, but perform them in either the Windows commmand prompt or Windows Powershell.

How to mount the Sylvester drive
--------------------------------

.. _mount-on-mac::

On Mac
^^^^^^

1. Ensure you are on WashU wifi, or are VPN'ed into their network.
2. Open the Finder application. At the top of your screen, click Go -> Connect To Server (near the bottom). 

   .. image:: images/finder-go.png
       :width: 150px
       :height: 350px


3. Type in the following IP address, above the section that says "Favorite Servers": ``smb://10.20.145.15``, then click "Connect".
   
    .. image:: images/connect-to-server.png
        :width: 400px

4. When prompted for your username and password, use your NIL username/password (NOT your Wustl key!)
5. When prompted to "Select the volumes you want to mount", choose "sylvester".
    
    .. image:: images/select-volumes-to-mount.png
        :width: 400px

6. You should now be able to access the Sylvester drive via Finder, it will appear in the sidebar under the IP address you entered earlier.

On Windows
^^^^^^^^^^

1. Ensure you are on WashU wifi, or are VPN'ed into their network.
2. Open the File Explorer.
3. Select *This PC* from the left pane. Then, on the File Explorer ribbon, select "More ..." > "Map network drive". 
    
    .. image:: images/windows-mount-network-drive.png

4. Specify this path to the Sylvester drive: ``\\neuroimage.wustl.edu\nil``
5. When prompted for your username, enter ``neuroimage\<your-NIL-username>``, and use your NIL password for your password.

.. _configuring-bash:

Configuring Bash
----------------

When using SSH, a default .bashrc file is provided at the following path: ``/data/sylvester/data1/LabOrientation/template_bashrc``. This file will configure Bash to include all the environment variables needed to use software on the system. To use this, you'll need to copy this over into your home directory (not your directory at ``/data/sylvester/data1/users``!), which can be done with this command::

    cp /data/sylvester/data1/LabOrientation/template_bashrc ~/.bashrc

.. hint::

   The ``~`` directory is shorthand for your Unix home directory at ``/home/usr/<your-NIL-username>/``.

.. _using-vnc:

Desktop access over VNC
-----------------------

Both Wallace and Gromit can be accessed via the Virtual Network Computing (VNC) protocol, which allow for a user-friendly desktop experience when running programs or accessing files on the server. Below are different procedures to do this on both MacOS and Windows.

Prerequisite for both MacOS and Windows
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you're starting a VNC server for the first time, or need to restart one (e.g. after a server reboot), follow these steps below:

1. First, :ref:`ssh into your preferred server <using-ssh>`.
2. Run the following command, which will start a new VNC server::

    /opt/TurboVNC/bin/vncserver -geometry 1920x1080

3. (FIRST-TIME USERS ONLY) The program will prompt you to create a password if this is your first time logging on, so simply type in a new password when prompted. Since this is a terminal application, keep in mind there won't be any feedback that you've typed a character in, unlike how passowrds appear when typed in on web pages (e.g. 'mypassword' looks like '***********' on a webpage). When you've typed your password, hit <Enter>. 

4. If there are any other prompts you receive, simply press <Enter> or type in the default option that appears.

You should now see some output similar to this::

    Desktop 'TurboVNC: gromit:X (<your-nil-username>)' started on display gromit:X
    
    Starting applications specified in /opt/TurboVNC/bin/xstartup.turbovnc
    Log file is /home/usr/<your-nil-username>/.vnc/gromit:X.log

The **X** placeholder here will be either a 1- or 2-digit number, which will be part of the port number used when accessing the VNC server.

.. hint::

    This command can also be used to view the status of any VNC servers you have running. To list all currently-registered servers, run the command ``/opt/TurboVNC/bin/vncserver -list``. If a server is not responding or needs to be killed for whatever reason, run ``/opt/TurboVNC/bin/vncserver -kill :X``, with X being a placeholder for the 1- or 2-digit server ID number (don't forget to add the colon before this number!). 

MacOS
^^^^^

MacOS has the ability to connect over VNC natively, without the need for downloading external software. 

1. Open Finder -> Go -> Connect to Server (this is the same window that appears when :ref:`mounting the network drive <mount-on-mac>`)
2. Depending on if you're connecting to Wallace or Gromit (I'll use Gromit in this example), enter ``vnc://gromit.neuroimage.wustl.edu:59XX`` into the top bar that appears. The 59 will alwasy come before the last two characters here, XX, which should be replaced with the ID number of your VNC server. If the ID number is 1 digit, make it 2 digits by prepending a 0 before (for example, if your server ID is 6, you would enter 5906 after the colon). If the ID is 2 digits, enter it as it appears (ID number 15 would be 5915 after the colon).
3. Click **Connect**. 
4. When prompted for a password, enter in the password you created when starting a VNC server for the first time. Keep in mind that this password gets truncated to 8 characters, so only enter the first 8 of your password if it's longer than that.

Windows
^^^^^^^

(Joey) At the time of making these docs, I don't have access to a Windows computer for creating detailed steps as above in the MacOS case, but they're very similar. 

We use a software called TigerVNC on our Windows computers to access VNC -- please contact NIL systems at nil-systems@npg.wustl.edu for questions about installing this on your system. 

The steps for connecting with TigerVNC here are largely the same as the MacOS instructions, as you'll need to enter the same ``vnc://...`` address and port number, and enter the same password as above. More detailed Windows instructions will be added soon!


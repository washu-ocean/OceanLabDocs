How to interact with lab resources
==================================

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

   The ``~`` directory is shorthand for your Unix home directory at ``/home/usr/<NIL-username/``.


